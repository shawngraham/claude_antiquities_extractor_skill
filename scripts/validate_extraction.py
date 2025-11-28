#!/usr/bin/env python3
"""
Validation script for antiquities trade data extraction JSON.
Ensures structural integrity and referential consistency.

Usage:
    python validate_extraction.py <path_to_json_file>
    python validate_extraction.py <path_to_json_file> --strict
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple


class AntiquitiesDataValidator:
    """Validates extracted antiquities trade data against schema requirements."""

    VALID_ENTITY_TYPES = {"PERSON", "ORGANIZATION", "ARTIFACT", "LOCATION"}
    
    VALID_RELATIONSHIP_TYPES = {
        "looted_from", "sold_to", "handled_by", "located_in",
        "employed_by", "collaborated_with", "recovered_by",
        "displayed_at", "authenticated_by", "repatriated_to",
        "investigated_by", "prosecuted_by"
    }
    
    PERSON_ROLES = {
        "dealer", "collector", "looter", "archaeologist",
        "customs_official", "museum_director", "restorer",
        "auctioneer", "authenticator", "consultant", "official",
        "tomb_raider", "smuggler", "law_enforcement"
    }
    
    ORGANIZATION_TYPES = {
        "museum", "gallery", "auction_house", "law_enforcement",
        "university", "customs", "government", "restoration_lab",
        "insurance_company", "research_institute"
    }
    
    ARTIFACT_TYPES = {
        "pottery", "sculpture", "manuscript", "coin", "textile",
        "tomb_goods", "papyrus", "bronze", "stone", "gemstone",
        "fresco", "mosaic", "jewelry", "furniture", "vessel"
    }
    
    LOCATION_TYPES = {
        "excavation_site", "freeport", "dealer_location", "city",
        "region", "country", "tomb", "storage_facility", "museum",
        "auction_house", "warehouse", "border_crossing"
    }

    def __init__(self, strict: bool = False):
        self.strict = strict
        self.errors: List[str] = []
        self.warnings: List[str] = []

    def validate_file(self, filepath: str) -> bool:
        """Load and validate JSON file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return self.validate_data(data)
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON: {e}")
            return False
        except FileNotFoundError:
            self.errors.append(f"File not found: {filepath}")
            return False

    def validate_data(self, data: Dict) -> bool:
        """Validate the extraction data structure."""
        
        # Check top-level structure
        if not isinstance(data, dict):
            self.errors.append("Root must be a JSON object")
            return False

        entities = data.get("entities", [])
        relationships = data.get("relationships", [])
        metadata = data.get("metadata", {})

        if not isinstance(entities, list):
            self.errors.append("'entities' must be an array")
            return False

        if not isinstance(relationships, list):
            self.errors.append("'relationships' must be an array")
            return False

        # Validate entities
        canonical_ids: Set[str] = set()
        for i, entity in enumerate(entities):
            entity_errors = self.validate_entity(entity, i)
            self.errors.extend(entity_errors)
            
            if "canonical_id" in entity:
                canonical_ids.add(entity["canonical_id"])

        # Validate relationships
        for i, rel in enumerate(relationships):
            rel_errors = self.validate_relationship(rel, i, canonical_ids)
            self.errors.extend(rel_errors)

        # Validate metadata if present
        if metadata:
            self.validate_metadata(metadata)

        return len(self.errors) == 0

    def validate_entity(self, entity: Dict, index: int) -> List[str]:
        """Validate individual entity."""
        errors = []
        
        # Required fields
        if "canonical_id" not in entity:
            errors.append(f"Entity {index}: missing 'canonical_id'")
        elif not isinstance(entity["canonical_id"], str) or not entity["canonical_id"]:
            errors.append(f"Entity {index}: 'canonical_id' must be non-empty string")
        elif not self._is_valid_canonical_id(entity["canonical_id"]):
            errors.append(f"Entity {index}: canonical_id '{entity['canonical_id']}' format invalid (should be lowercase with underscores)")

        if "type" not in entity:
            errors.append(f"Entity {index}: missing 'type'")
        elif entity["type"] not in self.VALID_ENTITY_TYPES:
            errors.append(f"Entity {index}: invalid type '{entity['type']}'")

        # PERSON entities should have full_name
        if entity.get("type") == "PERSON" and "full_name" not in entity:
            if self.strict:
                errors.append(f"Entity {index}: PERSON entity missing 'full_name'")
            else:
                self.warnings.append(f"Entity {index}: PERSON entity missing 'full_name'")

        # Validate mentions array
        if "mentions" in entity:
            if not isinstance(entity["mentions"], list):
                errors.append(f"Entity {index}: 'mentions' must be an array")
            elif not all(isinstance(m, str) for m in entity["mentions"]):
                errors.append(f"Entity {index}: 'mentions' must contain only strings")

        # Validate attributes
        if "attributes" in entity:
            if not isinstance(entity["attributes"], dict):
                errors.append(f"Entity {index}: 'attributes' must be an object")
            else:
                self._validate_attributes(entity, index, errors)

        return errors

    def _is_valid_canonical_id(self, cid: str) -> bool:
        """Check canonical_id format."""
        # Basic format check: lowercase, alphanumeric and underscores
        if not all(c.islower() or c.isdigit() or c == '_' for c in cid):
            return False
        if cid.startswith('_') or cid.endswith('_'):
            return False
        return True

    def _validate_attributes(self, entity: Dict, index: int, errors: List[str]):
        """Validate type-specific attributes."""
        entity_type = entity.get("type")
        attributes = entity.get("attributes", {})

        if entity_type == "PERSON":
            if "role" in attributes:
                role = attributes["role"]
                if isinstance(role, str):
                    if role not in self.PERSON_ROLES and self.strict:
                        self.warnings.append(
                            f"Entity {index}: role '{role}' not in standard list"
                        )
                elif isinstance(role, list):
                    for r in role:
                        if r not in self.PERSON_ROLES and self.strict:
                            self.warnings.append(
                                f"Entity {index}: role '{r}' not in standard list"
                            )

        elif entity_type == "ORGANIZATION":
            if "entity_type" in attributes:
                etype = attributes["entity_type"]
                if etype not in self.ORGANIZATION_TYPES and self.strict:
                    self.warnings.append(
                        f"Entity {index}: entity_type '{etype}' not in standard list"
                    )

        elif entity_type == "ARTIFACT":
            if "object_type" in attributes:
                otype = attributes["object_type"]
                if otype not in self.ARTIFACT_TYPES and self.strict:
                    self.warnings.append(
                        f"Entity {index}: object_type '{otype}' not in standard list"
                    )

        elif entity_type == "LOCATION":
            if "location_type" in attributes:
                ltype = attributes["location_type"]
                if ltype not in self.LOCATION_TYPES and self.strict:
                    self.warnings.append(
                        f"Entity {index}: location_type '{ltype}' not in standard list"
                    )

    def validate_relationship(self, rel: Dict, index: int, 
                            canonical_ids: Set[str]) -> List[str]:
        """Validate individual relationship."""
        errors = []

        # Required fields
        if "source_id" not in rel:
            errors.append(f"Relationship {index}: missing 'source_id'")
        elif rel["source_id"] not in canonical_ids:
            errors.append(
                f"Relationship {index}: source_id '{rel['source_id']}' not found in entities"
            )

        if "target_id" not in rel:
            errors.append(f"Relationship {index}: missing 'target_id'")
        elif rel["target_id"] not in canonical_ids:
            errors.append(
                f"Relationship {index}: target_id '{rel['target_id']}' not found in entities"
            )

        if "relation_type" not in rel:
            errors.append(f"Relationship {index}: missing 'relation_type'")
        elif rel["relation_type"] not in self.VALID_RELATIONSHIP_TYPES:
            errors.append(
                f"Relationship {index}: invalid relation_type '{rel['relation_type']}'"
            )

        # Validate attributes if present
        if "attributes" in rel:
            if not isinstance(rel["attributes"], dict):
                errors.append(f"Relationship {index}: 'attributes' must be an object")

        return errors

    def validate_metadata(self, metadata: Dict):
        """Validate metadata section."""
        if not isinstance(metadata, dict):
            self.errors.append("'metadata' must be an object")

    def report(self):
        """Print validation report."""
        print("\n" + "="*60)
        print("EXTRACTION VALIDATION REPORT")
        print("="*60)

        if not self.errors and not self.warnings:
            print("✓ Validation passed with no issues")
            return 0

        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for error in self.errors:
                print(f"  • {error}")

        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for warning in self.warnings:
                print(f"  • {warning}")

        print("="*60)
        return 1 if self.errors else 0


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_extraction.py <json_file> [--strict]")
        sys.exit(1)

    filepath = sys.argv[1]
    strict = "--strict" in sys.argv

    validator = AntiquitiesDataValidator(strict=strict)
    
    if validator.validate_file(filepath):
        exit_code = validator.report()
    else:
        exit_code = validator.report()

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
