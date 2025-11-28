# Red Flags and Suspicious Patterns

Guide for recognizing common indicators of looted artifacts and illicit antiquities trafficking when extracting from documents.

## Provenance Red Flags

### Documentation Gaps
- **Post-1970 gaps**: Most suspicious period for Mediterranean antiquities (Egyptian law 1970, UNESCO Convention)
- **"1970–present" missing**: Precise documentation ends at 1970 and resumes decades later
- **"Private collection"**: Often code for unknown and potentially looted origin
- **"From European collection"**: Vague geographic attribution suggests effort to obscure origin
- **"Recently surfaced"**: Recent discovery often indicates recent looting or long concealment
- **No excavation documentation**: Legitimate antiquities typically have dig records, site photos, field notes

### Suspicious Selling Patterns
- **Rapid price escalation**: Significant value increase between sales suggests authentication/documentation manipulation
- **Multiple sales in short period**: Rapid "flipping" to launder provenance through market
- **Swiss involvement**: Geneva particularly associated with looted artifacts storage and sales
- **Use of middlemen**: Each dealer is a "layer" obscuring original source
- **Public vs. private sales**: Same artifact sold privately after failed public auction (authentication concerns)
- **Auction house withdrawal**: Piece withdrawn from sale after provenance questions (common flag)

## Source and Documentation Indicators

### Suspicious Documentation
- **Minimal paperwork**: Legitimate antiquities have export permits, import records, museum communications
- **Photocopies only**: Originals "unavailable", "in storage", "lost"
- **Undated photographs**: Photos without provenance or dating context
- **Recent photography**: High-quality modern photos of ancient piece with no historical documentation
- **Laboratory testing absence**: No thermoluminescence dating, material analysis, or conservation records
- **Expert authentication lacking**: Major pieces typically have published authentication; absence is red flag

### Suspicious Dealer Claims
- **"Long-time collection"**: Conveniently before 1970 but undocumented
- **"Inherited from estate"**: Vague familial history without supporting records
- **"Acquisition at European auction"**: Specific auction details mysteriously unavailable
- **"From Swiss collector"**: Geneva freeports used to warehouse and disguise origins
- **Multiple contradictory stories**: Different provenance narratives for same object

## Entity Red Flags

### Known Problem Dealers
- Giacomo Medici (Italian dealer, convicted)
- Robert Hecht (American dealer, indicted)
- Robin Symes (London-based dealer)
- Christos Michaelides (Cyprus-based smuggler)
- Julian Ludwig (German looter)
- Any dealer with conviction or indictment

### Suspicious Institutional Behavior
- **Deaccessioning without transparency**: Removing object from public collection without explanation
- **Rushed donation**: High-value artifact donated without standard vetting
- **Unofficial acquisition**: Object appears in collection without formal accession documentation
- **Sudden provenance revision**: Museum changes acquisition narrative (often post-scandal)
- **Refusing repatriation discussions**: Institution resists inquiry about contested origin
- **Stonewalling**: Institution refuses to release provenance files or correspondence

### Problem Locations
- **Geneva freeports**: Known storage for looted goods in transit
- **Sicilian/Calabrese dealers**: Region historically associated with clandestine excavation networks
- **Middle Eastern markets**: Looted items often pass through Lebanon, Dubai, London en route to US/Europe
- **Cyprus**: Historically major looting and smuggling hub for Mediterranean antiquities

## Relationship and Activity Red Flags

### Looting Operations
- **Organized nighttime digging**: Systematic excavation of sites during darkness
- **"Antiquity hunters"**: Local men hired for clandestine excavation without archaeological training
- **Tomb breaking**: Evidence of deliberate destruction to access contents
- **Mass removal**: Multiple artifacts from single site within short timeframe
- **Fragment scattering**: Archaeological site left with scattered broken pieces (looters seeking specific items)

### Trafficking Methods
- **Multiple jurisdictions**: Artifact moves through multiple countries (complicates legal claims)
- **Freeport usage**: Stored in international airport bonded zones (avoids customs/import laws)
- **Documentation fabrication**: Provenance papers created to match authentication narrative
- **Expert complicity**: Scholars or conservators knowingly certify questionable provenance
- **Auction house coordination**: Multiple pieces by same looters appear at different houses

### Relationship Red Flags
- **Dealer-to-dealer chains**: Series of sales between known dealers (layering supply)
- **Looter-to-dealer pipeline**: Local excavators consistently supply single dealer
- **Museum-dealer axis**: Specific museum repeatedly acquires from specific dealer
- **Customs complicity**: Border officers involved in moving pieces across frontiers
- **Expert-dealer connection**: Authenticator consistently works with same dealer (potential conflict)

## Language and Narrative Red Flags

### Suspicious Phrasing
- **"Appeared in the market"**: Vague origin, often looted
- **"Thesaurus antiquities"**: Collection liquidated, possibly looted goods being sold off
- **"Museum deaccession"**: Object removed from public ownership, sometimes questionably
- **"Restitution candidate"**: Euphemism for "stolen goods"
- **"Contested ownership"**: Legal dispute over rightful owner (implies prior wrongful possession)
- **"Without prejudice to ownership"**: Seller claims no knowledge of true origin or claimants

### Narrative Inconsistencies
- **Contradictory accounts**: Different dates or prior ownership in various sources
- **Selective transparency**: Full provenance listed for some artifacts, gaps in others
- **Changing stories**: Article revisions between early and later reporting
- **Anonymous sources**: Key information attributed to unnamed dealers or collectors
- **Reputation defense**: Excessive positive statements about reputation suggest prior accusations

## Extraction Guidance for Red Flags

1. **Document all red flags** in the `extraction_notes` metadata
2. **Note documentation gaps** with approximate dates (e.g., "1970-1990 undocumented")
3. **Mark uncertain relationships** with `"confidence": "low"` when red flags suggest unverified claims
4. **Include suspicious phrases** in `source_text` attributes
5. **Cross-reference known problem figures** against `known-figures.md` reference
6. **Highlight freeport involvement** as significant relationship attribute
7. **Note authentication details** particularly expert involvement and timing
8. **Track institutional behavior** including documentation refusals or reversals

## Example Red Flag Extraction

```json
{
  "canonical_id": "suspicious_artifact",
  "type": "ARTIFACT",
  "full_name": "Greek Vessel of Unknown Origin",
  "attributes": {
    "origin_location": "Greece (unspecified)",
    "legal_status": "disputed",
    "documentation_status": "incomplete",
    "known_issues": [
      "No provenance documentation before 1990",
      "Recently authenticated after decades in private collection",
      "Passed through Geneva freeport before sale"
    ]
  }
}
```

```json
{
  "source_id": "dealer",
  "target_id": "suspicious_artifact",
  "relation_type": "handled_by",
  "attributes": {
    "confidence": "low",
    "context": "Dealer claims item from European estate; full estate details unavailable",
    "red_flags": [
      "Vague acquisition narrative",
      "No estate documentation provided",
      "Rapid price increase over 10 years",
      "Authentication immediately after acquisition"
    ]
  }
}
```

## Assessment Framework

Rate overall artifact/transaction risk:

- **HIGH RISK**: Multiple simultaneous red flags, documentation gaps around 1970, freeport involvement, known problem dealer
- **MEDIUM RISK**: One or two red flags, later acquisition period, questionable but not definitively looted
- **LOW RISK**: Complete documentation, clear excavation records, legitimate institutional provenance, published scholarship

Always include risk assessment in extraction_notes when multiple red flags are identified.
