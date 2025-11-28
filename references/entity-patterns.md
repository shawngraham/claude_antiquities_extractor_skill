# Entity Recognition Patterns

Common linguistic patterns and context clues for identifying antiquities trade entities and relationships.

## Person Recognition Patterns

### Dealer Indicators
- "X, an antiquities dealer"
- "X specialized in Greek pottery"
- "X sold to collectors"
- "X was a dealer in looted artifacts"
- "X's warehouse contained illicit artifacts"
- References to running a gallery or shop
- Involvement in auction houses or sales
- Known to facilitate transactions

### Collector Indicators
- "X, an American collector"
- "X assembled a collection of"
- "X purchased artifacts from"
- References to owning or acquiring artworks
- Museum donations or bequests by X
- Private collection disparities

### Looter/Tomb Raider Indicators
- "X excavated without permission"
- "X removed artifacts from the site"
- "Local diggers employed by X"
- "X participated in clandestine digs"
- "Night digging at the site"

### Official/Law Enforcement Indicators
- "X, Egyptian customs official"
- "X led the investigation"
- "Interpol agent X"
- "X ordered the seizure"
- "X from the Ministry of"

### Authenticator/Restorer Indicators
- "Expert X authenticated"
- "Restorer X worked on"
- "Conservator X cleaned"
- "X examined the provenance"

## Organization Recognition Patterns

### Museum Indicators
- Organization name + "Museum"
- "The Getty", "The Louvre", "The Met"
- References to "collection", "holdings", "acquisitions"
- "on display at X"
- "acquired by X in [year]"
- Specific accession numbers

### Auction House Indicators
- "Christie's", "Sotheby's", "Bonhams"
- "sold at auction"
- "lot number X at Y auction house"
- "Estimate: price range"

### Law Enforcement/Customs Indicators
- "Interpol"
- "Italian Ministry of Culture"
- "US Customs and Border Protection"
- "the investigation by [agency]"
- "seized by [organization]"

### University/Research Indicators
- "X University"
- "Department of Archaeology"
- "Research Institute"

## Location Recognition Patterns

### Excavation Site Patterns
- Named with "near [city]" or "Valley of Kings"
- References to "tomb KV[number]"
- "Ancient [civilization] site"
- Archaeological context clues
- "Looted from the site of"
- "Clandestine excavations at"

### Freeport Indicators
- "Geneva Freeport"
- "Singapore Freeport"
- "Stored in a freeport"
- "Temporarily placed in X freeport"

### Geographic Location Patterns
- Country names (Egypt, Italy, Greece, etc.)
- Region names (Tuscany, Upper Egypt, Aegean)
- City names (Rome, Cairo, London)
- Warehouse or storage locations
- Border crossings or transit points

### Dealer Location Patterns
- References to "his gallery in X"
- "Located in Switzerland"
- "Operating out of Y city"
- Business registration locations

## Artifact Recognition Patterns

### Named Artifacts
- "The Euphronios Sarpedon Krater"
- "The Siphnian Treasury sculptures"
- Specific museum accession numbers (e.g., "Louvre E 14384")
- Common historical names (e.g., "The Parthenon Marbles")

### Descriptive Artifacts
- "A Greek red-figure kylix"
- "Egyptian canopic jars from Thebes"
- "Roman marble sculpture depicting"
- "Bronze statue of Hellenistic origin"

### Archaeological Classification Patterns
- Object type + cultural origin
- "Lekythos" (Greek funeral vessel)
- "Funerary equipment from tomb"
- Material descriptions (marble, terracotta, bronze)

### Condition and Status Clues
- "Restored by X"
- "Missing [parts]"
- "Fragmented but complete"
- "Heavily damaged"
- "In pristine condition"

### Provenance Clues
- "Previously in the collection of X"
- "Looted from the temple of"
- "Allegedly found near"
- "Disputed provenance"
- "Documentation missing for 1970-1985"

## Relationship Recognition Patterns

### Sale/Transaction Verbs
- "sold to", "acquired by", "purchased from"
- "transferred to", "passed to"
- "sold at auction", "sold privately"
- "consigned to"
- Specific prices or valuations
- Dates of transactions

### Looting/Theft Verbs
- "looted from", "stolen from", "removed from"
- "excavated without permission"
- "illicitly obtained"
- "removed during the night"
- "smuggled across"

### Possession/Location Verbs
- "held by", "stored at", "kept in"
- "housed in", "remains in"
- "currently located at"
- "on display at"

### Professional Relationships
- "Worked for", "employed by"
- "Collaborated with", "partnered with"
- "Consulted by"
- "Authenticated by"
- "Restored by"

### Recovery/Repatriation Verbs
- "recovered by", "seized by"
- "confiscated from"
- "returned to"
- "repatriated to"
- "recovered in a raid"

### Temporal Indicators
- "In [year]", "On [date]"
- "During the 1970s"
- "After 1970" (often regarding documentation gaps)
- "By [year]"
- "From [year] to [year]"

## Common Contextual Clues

### Gap Indicators
- "Whereabouts unknown between X and Y"
- "History unclear for period"
- "No documentation available"
- "Private collection [dates]"
- "Subsequently acquired by unknown party"
- *These gaps are significant—often hide illegal activity*

### Red Flags in Text
- "Allegedly found"
- "Unknown origin"
- "Sold without provenance"
- "Hastily deaccessioned"
- "Smuggling route"
- "Swiss warehouse"
- "Customs seizure"

### Authority and Expertise
- Academic credentials or museum affiliation
- Publication history
- Expert testimony
- Governmental or institutional authority
- Museum director status

### Corruption Indicators
- "Bribed officials"
- "Customs officials allegedly involved"
- "Government complicity"
- "With official knowledge"
- "Permit irregularities"

## Disambiguation Guide

### Handling Name Variants
- "Giovanni Medici", "G. Medici", "Medici the dealer" → canonicalize as `giovanni_medici`
- Include all variants in `mentions` array
- Track aliases separately in attributes

### Multiple People with Same Name
- Use birth dates or additional context for disambiguation
- Canonical ID: `firstname_lastname_1` and `firstname_lastname_2` if necessary
- Include distinguishing attributes (birth date, nationality, specialization)

### Organization Name Changes
- "Metropolitan Museum" vs "The Met" vs "The Metropolitan Museum of Art"
- Canonicalize to most complete form
- Include abbreviations in `mentions`

### Location Name Evolution
- Historical vs. modern place names
- "Thebes" vs. "Luxor", "Constantinople" vs. "Istanbul"
- Use modern names in canonical_id, historical names in mentions

## Pattern Application Strategy

1. **Pre-read** the document once for context
2. **Identify entity type** using indicators above
3. **Look for relationships** using verb patterns
4. **Capture temporal context** for all transactions/movements
5. **Note gaps** in provenance or documentation
6. **Check for disambiguation needs** (same names, location variants)
7. **Cross-reference** against known figures (see known-figures.md if available)
