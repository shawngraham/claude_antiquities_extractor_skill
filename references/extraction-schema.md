# Extraction Schema

Complete JSON schema specification for antiquities trade data extraction.

## Entity Schema

### PERSON Entity

```json
{
  "canonical_id": "firstname_lastname",
  "type": "PERSON",
  "full_name": "Full Name",
  "mentions": ["name variant 1", "name variant 2", "alias"],
  "attributes": {
    "role": "dealer | collector | looter | archaeologist | customs_official | museum_director | restorer | auctioneer | authenticator | consultant",
    "nationality": "country name",
    "birth_date": "YYYY or YYYY-MM-DD if known",
    "death_date": "YYYY or YYYY-MM-DD if known",
    "known_aliases": ["alternate name 1", "alternate name 2"],
    "affiliation": "organization name or canonical_id",
    "specialization": "Greek pottery | Roman sculpture | Egyptian antiquities | etc.",
    "criminal_charges": "if prosecuted or investigated",
    "legal_status": "convicted | acquitted | investigated | under_indictment",
    "notes": "relevant biographical or contextual information"
  }
}
```

### ORGANIZATION Entity

```json
{
  "canonical_id": "abbreviated_organization_name",
  "type": "ORGANIZATION",
  "full_name": "Full Legal Name",
  "mentions": ["abbreviation", "alternative name"],
  "attributes": {
    "entity_type": "museum | gallery | auction_house | law_enforcement | university | customs | government | restoration_lab | insurance_company",
    "location": "city, country",
    "founded_date": "YYYY",
    "known_location": "address or general location",
    "specialization": "area of focus",
    "involvement": "description of role in trade (if any)",
    "country": "country of origin",
    "notes": "relevant institutional information"
  }
}
```

### ARTIFACT Entity

```json
{
  "canonical_id": "descriptive_name_identifier",
  "type": "ARTIFACT",
  "full_name": "Complete artifact description",
  "mentions": ["common name", "alternative reference"],
  "attributes": {
    "object_type": "pottery | sculpture | manuscript | coin | textile | tomb_goods | papyrus | bronze | stone | gemstone",
    "origin_location": "archaeological site or location",
    "origin_date": "YYYY BCE/CE or date range",
    "origin_culture": "Greek | Roman | Egyptian | Etruscan | etc.",
    "dimensions": "height x width x depth in cm, weight in kg",
    "material": "ceramic | stone | metal | organic | mixed",
    "condition": "description of current state",
    "legal_status": "looted | disputed | recovered | repatriated | uncertain_provenance | legitimately_acquired",
    "current_location": "museum or location name",
    "current_location_id": "canonical_id if organization",
    "excavation_details": "site name, date, excavator if known",
    "looted_date": "YYYY or approximate",
    "dealers_involved": ["canonical_id 1", "canonical_id 2"],
    "museums_held": ["canonical_id of museum 1", "canonical_id of museum 2"],
    "museum_accession_number": "if applicable",
    "documented_in": ["publication 1", "publication 2"],
    "notes": "key provenance details and unresolved questions"
  }
}
```

### LOCATION Entity

```json
{
  "canonical_id": "place_name_geographic_identifier",
  "type": "LOCATION",
  "full_name": "Complete location name",
  "mentions": ["alternate spelling", "historical name"],
  "attributes": {
    "location_type": "excavation_site | freeport | dealer_location | city | region | country | tomb | storage_facility",
    "country": "current country",
    "region": "province or region",
    "significance": "reason for inclusion in antiquities trade",
    "archaeological_importance": "description",
    "looting_history": "known looting activity",
    "freeport_type": "if applicable (Geneva, Singapore, etc.)",
    "coordinates": "latitude, longitude if known",
    "historical_context": "relevant background",
    "current_status": "active site | destroyed | inaccessible | preserved | etc."
  }
}
```

## Relationship Schema

```json
{
  "source_id": "canonical_id of source entity",
  "target_id": "canonical_id of target entity",
  "relation_type": "relationship type (see types below)",
  "attributes": {
    "date": "YYYY or YYYY-MM-DD when relationship occurred",
    "artifact": "canonical_id or name of artifact involved",
    "price": "sale price if monetary transaction",
    "context": "brief contextual description",
    "confidence": "high | medium | low (for uncertain relationships)",
    "source_text": "direct quote or page number from source",
    "notes": "additional details"
  }
}
```

### Relationship Types

| Type | From | To | Example |
|------|------|-----|---------|
| `looted_from` | PERSON/ORG | ARTIFACT | Looter removed artifact |
| `looted_from` | ARTIFACT | LOCATION | Artifact taken from excavation site |
| `sold_to` | PERSON/ORG | PERSON/ORG | Dealer sold to collector/museum |
| `handled_by` | ARTIFACT | PERSON | Restorer worked on artifact |
| `handled_by` | ARTIFACT | ORG | Gallery displayed artifact |
| `located_in` | ARTIFACT | LOCATION | Artifact currently stored at location |
| `located_in` | ORG | LOCATION | Organization operates at location |
| `employed_by` | PERSON | ORG | Staff or contractor relationship |
| `collaborated_with` | PERSON | PERSON | Joint business operations |
| `recovered_by` | ARTIFACT | PERSON | Law enforcement official recovered |
| `recovered_by` | ARTIFACT | ORG | Police or customs authority recovered |
| `displayed_at` | ARTIFACT | ORG | Museum exhibition or acquisition |
| `authenticated_by` | ARTIFACT | PERSON | Expert certified provenance |
| `repatriated_to` | ARTIFACT | ORG | Returned to country/museum |
| `repatriated_to` | ARTIFACT | LOCATION | Returned to origin location |
| `investigated_by` | PERSON | ORG | Law enforcement inquiry |
| `prosecuted_by` | PERSON | ORG | Legal action taken |

## Extraction Rules

1. **Canonical ID Consistency**: Once you assign a canonical_id to an entity, use that same ID in all relationships where that entity appears
2. **No Orphan Relationships**: Every `source_id` and `target_id` must correspond to an entity in the entities array
3. **Multiple Roles**: If a person has multiple roles (e.g., "dealer and collector"), include both in the role attribute as an array
4. **Temporal Precision**: Use full dates (YYYY-MM-DD) when available, years (YYYY) when specific date unknown, approximate notation (ca. 1500) for uncertain dates
5. **Uncertain Information**: If information is implied but not explicit, either include it with a `confidence: "low"` attribute or note it in extraction_notes
6. **Source Attribution**: Include `source_text` in relationships when possible for verification purposes
7. **Location Names**: Use modern names primarily but note historical names in the mentions array

## Common Extraction Patterns

### Simple Sale
```json
{
  "source_id": "dealer_name",
  "target_id": "collector_name",
  "relation_type": "sold_to",
  "attributes": {
    "artifact": "artifact_canonical_id",
    "date": "1967",
    "price": "if mentioned",
    "context": "Sold at auction house or private deal"
  }
}
```

### Artifact Looting Chain
```json
[
  {"source_id": "looter", "target_id": "artifact", "relation_type": "looted_from"},
  {"source_id": "artifact", "target_id": "excavation_site", "relation_type": "looted_from"},
  {"source_id": "dealer_1", "target_id": "dealer_2", "relation_type": "sold_to", "attributes": {"artifact": "artifact_id"}},
  {"source_id": "dealer_2", "target_id": "museum", "relation_type": "sold_to", "attributes": {"artifact": "artifact_id", "legal_context": "sold without disclosure of provenance"}}
]
```

### Multi-Stage Recovery
```json
[
  {"source_id": "artifact", "target_id": "storage_location", "relation_type": "located_in"},
  {"source_id": "artifact", "target_id": "law_enforcement_agency", "relation_type": "recovered_by", "attributes": {"date": "2008"}},
  {"source_id": "artifact", "target_id": "origin_country_museum", "relation_type": "repatriated_to", "attributes": {"date": "2010"}}
]
```

## Validation Checklist

- [ ] All `source_id` and `target_id` values exist as `canonical_id` in entities array
- [ ] All `canonical_id` values are unique within the document
- [ ] Person canonical_id follows `firstname_lastname` format (lowercase, underscores)
- [ ] Organization canonical_id is abbreviated and meaningful
- [ ] Artifact canonical_id is descriptive and unique
- [ ] Location canonical_id includes geographic qualifiers for disambiguation
- [ ] All relationship types are from the approved list
- [ ] Dates follow ISO format (YYYY, YYYY-MM-DD, or approximate notation)
- [ ] No required fields are missing from entities or relationships
- [ ] Confidence levels marked for uncertain information
