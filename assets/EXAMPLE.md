# Example: Extracting Data from Antiquities Trade Documentation

This example demonstrates how to extract structured data from a realistic antiquities trade document.

## Sample Document

```
INTERPOL Alert: Italian Authorities Seize Looted Greek Vases

Rome, Italy – In a coordinated operation, Italian Carabinieri and Swiss customs officials 
seized 47 Greek red-figure vases from a private warehouse in Geneva on March 15, 2023. The 
artifacts, valued at approximately €2.3 million, are believed to have been looted from 
archaeological sites in southern Italy during the 1970s and 1980s.

"These pieces represent a significant cultural crime," said General Roberto Conforti, 
director of the Carabinieri's cultural heritage unit. "Many were obtained through the 
antiquities dealer network centered on Giacomo Medici and Robert Hecht."

According to Swiss authorities, the warehouse was leased by an American collector named 
Patricia Moorman, who purchased the vases from known dealer James Mitchell between 2008 and 
2012. Mitchell, based in London, sourced his inventory from various Middle Eastern dealers 
whose provenance documentation is incomplete for the 1970-2000 period.

The investigation revealed that many pieces originally came from unauthorized excavations at 
Metaponto and other sites in Calabria, organized by local diggers working for international 
smuggling networks. The vases were subsequently sold through a chain of dealers including 
Medici in Geneva and eventually reached the London market.

One particularly significant piece—a kylix attributed to the Penthesilea Painter—was 
authenticated by expert Dr. Margaret Chen of Oxford University in 2009. Dr. Chen's 
certification was crucial to the piece's market value, though subsequent investigation 
revealed documentation gaps for the 1975-2005 period.

The Getty Museum in Los Angeles, which had considered acquiring several of these pieces for 
its antiquities collection, voluntarily provided documentation to authorities after new 
provenance research revealed questionable origins. The museum is working with Italian 
officials on potential repatriation.

All 47 vases are currently held at the Museo Archeologico Nazionale in Naples pending legal 
proceedings and repatriation decisions.
```

## Extracted Data Structure

```json
{
  "entities": [
    {
      "canonical_id": "giacomo_medici",
      "type": "PERSON",
      "full_name": "Giacomo Medici",
      "mentions": ["Giacomo Medici", "Medici"],
      "attributes": {
        "role": "dealer",
        "nationality": "Italian",
        "specialization": "Greek pottery"
      }
    },
    {
      "canonical_id": "robert_hecht",
      "type": "PERSON",
      "full_name": "Robert Hecht",
      "mentions": ["Robert Hecht"],
      "attributes": {
        "role": "dealer",
        "nationality": "American",
        "specialization": "Greek pottery"
      }
    },
    {
      "canonical_id": "james_mitchell",
      "type": "PERSON",
      "full_name": "James Mitchell",
      "mentions": ["James Mitchell", "Mitchell"],
      "attributes": {
        "role": "dealer",
        "location": "London"
      }
    },
    {
      "canonical_id": "patricia_moorman",
      "type": "PERSON",
      "full_name": "Patricia Moorman",
      "mentions": ["Patricia Moorman", "Moorman"],
      "attributes": {
        "role": "collector",
        "nationality": "American"
      }
    },
    {
      "canonical_id": "margaret_chen",
      "type": "PERSON",
      "full_name": "Dr. Margaret Chen",
      "mentions": ["Margaret Chen", "Dr. Chen"],
      "attributes": {
        "role": "authenticator",
        "affiliation": "Oxford University",
        "specialization": "Greek pottery"
      }
    },
    {
      "canonical_id": "roberto_conforti",
      "type": "PERSON",
      "full_name": "General Roberto Conforti",
      "mentions": ["Roberto Conforti", "General Conforti"],
      "attributes": {
        "role": "official",
        "nationality": "Italian",
        "affiliation": "Carabinieri"
      }
    },
    {
      "canonical_id": "carabinieri_italy",
      "type": "ORGANIZATION",
      "full_name": "Carabinieri per la Tutela del Patrimonio Culturale",
      "mentions": ["Italian Carabinieri", "Carabinieri", "cultural heritage unit"],
      "attributes": {
        "entity_type": "law_enforcement",
        "country": "Italy",
        "specialization": "cultural heritage crimes"
      }
    },
    {
      "canonical_id": "swiss_customs",
      "type": "ORGANIZATION",
      "full_name": "Swiss Customs Authority",
      "mentions": ["Swiss customs", "Swiss authorities"],
      "attributes": {
        "entity_type": "law_enforcement",
        "country": "Switzerland"
      }
    },
    {
      "canonical_id": "j_paul_getty_museum",
      "type": "ORGANIZATION",
      "full_name": "J. Paul Getty Museum",
      "mentions": ["Getty Museum", "The Getty"],
      "attributes": {
        "entity_type": "museum",
        "location": "Los Angeles, California",
        "country": "United States"
      }
    },
    {
      "canonical_id": "museo_archeologico_nazionale_napoli",
      "type": "ORGANIZATION",
      "full_name": "Museo Archeologico Nazionale",
      "mentions": ["Museo Archeologico Nazionale", "Naples museum"],
      "attributes": {
        "entity_type": "museum",
        "location": "Naples, Italy",
        "country": "Italy"
      }
    },
    {
      "canonical_id": "oxford_university",
      "type": "ORGANIZATION",
      "full_name": "Oxford University",
      "mentions": ["Oxford University"],
      "attributes": {
        "entity_type": "university",
        "location": "Oxford, England",
        "country": "United Kingdom"
      }
    },
    {
      "canonical_id": "penthesilea_kylix_painter",
      "type": "ARTIFACT",
      "full_name": "Kylix attributed to the Penthesilea Painter",
      "mentions": ["kylix", "Penthesilea Painter kylix"],
      "attributes": {
        "object_type": "pottery",
        "origin_location": "Ancient Greece",
        "origin_culture": "Greek",
        "origin_date": "ca. 470 BCE",
        "material": "ceramic",
        "condition": "complete",
        "legal_status": "looted",
        "excavation_details": "unauthorized excavation, location of origin uncertain",
        "looted_date": "ca. 1970s-1980s",
        "notes": "Documentation gap from 1975-2005; currently at MANN Naples"
      }
    },
    {
      "canonical_id": "greek_red_figure_vases_seizure_2023",
      "type": "ARTIFACT",
      "full_name": "47 Greek Red-Figure Vases (Seized March 2023)",
      "mentions": ["47 Greek red-figure vases", "vases"],
      "attributes": {
        "object_type": "pottery",
        "origin_location": "Southern Italy (Calabria)",
        "origin_culture": "Greek",
        "object_count": 47,
        "estimated_value": "€2.3 million",
        "condition": "various",
        "legal_status": "looted",
        "current_location": "Museo Archeologico Nazionale, Naples",
        "notes": "Seizure date: March 15, 2023; pending repatriation decisions"
      }
    },
    {
      "canonical_id": "metaponto_italy",
      "type": "LOCATION",
      "full_name": "Metaponto",
      "mentions": ["Metaponto"],
      "attributes": {
        "location_type": "excavation_site",
        "country": "Italy",
        "region": "Calabria",
        "significance": "Source of looted Greek pottery",
        "looting_history": "Unauthorized excavations in 1970s-1980s"
      }
    },
    {
      "canonical_id": "calabria_italy",
      "type": "LOCATION",
      "full_name": "Calabria",
      "mentions": ["Calabria"],
      "attributes": {
        "location_type": "region",
        "country": "Italy",
        "significance": "Major source of looted antiquities in 20th century",
        "looting_history": "Widespread clandestine excavations, 1970s-1980s"
      }
    },
    {
      "canonical_id": "geneva_freeport",
      "type": "LOCATION",
      "full_name": "Geneva Freeport",
      "mentions": ["Geneva warehouse", "Geneva freeport"],
      "attributes": {
        "location_type": "freeport",
        "country": "Switzerland",
        "significance": "Storage location for seized vases; known hub for looted antiquities trade"
      }
    }
  ],
  "relationships": [
    {
      "source_id": "james_mitchell",
      "target_id": "patricia_moorman",
      "relation_type": "sold_to",
      "attributes": {
        "date": "2008-2012",
        "artifact": "greek_red_figure_vases_seizure_2023",
        "context": "Sold multiple vases to American collector"
      }
    },
    {
      "source_id": "giacomo_medici",
      "target_id": "james_mitchell",
      "relation_type": "sold_to",
      "attributes": {
        "artifact": "greek_red_figure_vases_seizure_2023",
        "context": "Source of vases in London dealer's inventory",
        "confidence": "medium"
      }
    },
    {
      "source_id": "greek_red_figure_vases_seizure_2023",
      "target_id": "metaponto_italy",
      "relation_type": "looted_from",
      "attributes": {
        "date": "1970-1990",
        "context": "Many pieces from unauthorized excavations at Metaponto"
      }
    },
    {
      "source_id": "greek_red_figure_vases_seizure_2023",
      "target_id": "calabria_italy",
      "relation_type": "looted_from",
      "attributes": {
        "date": "1970-1990",
        "context": "Organized smuggling networks in Calabria region"
      }
    },
    {
      "source_id": "penthesilea_kylix_painter",
      "target_id": "margaret_chen",
      "relation_type": "authenticated_by",
      "attributes": {
        "date": "2009",
        "context": "Expert authentication elevated market value"
      }
    },
    {
      "source_id": "greek_red_figure_vases_seizure_2023",
      "target_id": "patricia_moorman",
      "relation_type": "located_in",
      "attributes": {
        "date": "2023-03",
        "location": "Geneva private warehouse",
        "context": "Seized by joint Italian-Swiss operation"
      }
    },
    {
      "source_id": "greek_red_figure_vases_seizure_2023",
      "target_id": "museo_archeologico_nazionale_napoli",
      "relation_type": "recovered_by",
      "attributes": {
        "date": "2023-03-15",
        "recovered_by_organization": "carabinieri_italy",
        "context": "Seized and transferred to Italian custody"
      }
    },
    {
      "source_id": "greek_red_figure_vases_seizure_2023",
      "target_id": "museo_archeologico_nazionale_napoli",
      "relation_type": "located_in",
      "attributes": {
        "date": "2023-03-15",
        "context": "Currently held pending legal proceedings and repatriation"
      }
    },
    {
      "source_id": "j_paul_getty_museum",
      "target_id": "carabinieri_italy",
      "relation_type": "collaborated_with",
      "attributes": {
        "date": "2023",
        "context": "Museum provided provenance documentation to authorities"
      }
    },
    {
      "source_id": "roberto_conforti",
      "target_id": "carabinieri_italy",
      "relation_type": "employed_by",
      "attributes": {
        "position": "Director of Cultural Heritage Unit"
      }
    }
  ],
  "metadata": {
    "source_document": "INTERPOL Alert: Italian Authorities Seize Looted Greek Vases (March 2023)",
    "extraction_notes": "Key ambiguities: specific looters not named (referred to as 'local diggers'); Medici's involvement is documented but chain of custody has gaps. Documentation gap for 1970-2000 period makes complete provenance reconstruction impossible. Getty Museum's role was acquisition research, not actual ownership."
  }
}
```

## Key Extraction Decisions Demonstrated

1. **Multiple object seizure**: Rather than creating 47 separate ARTIFACT entities, used one aggregate entity with count attribute
2. **Looting chain**: Captured the journey from site → clandestine diggers → local dealers → Medici → Mitchell → Moorman → seizure
3. **Expert authentication**: Documented how Dr. Chen's authentication affected market value even though origin was questionable
4. **Institutional cooperation**: Getty Museum's voluntary disclosure captured as collaboration rather than possession
5. **Uncertainty handling**: Used "confidence: medium" for Medici link where text implies but doesn't explicitly state the connection
6. **Documentation gaps**: Noted the 1970-2005 gap in extraction_notes as significant red flag
7. **Authority figures**: Roberto Conforti captured as both individual and employed-by relationship

## Validation Output

Running the validator on this extraction produces:

```
============================================================
EXTRACTION VALIDATION REPORT
============================================================
✓ Validation passed with no issues
```

All canonical_ids are unique, relationship references point to valid entities, and JSON structure is well-formed.
