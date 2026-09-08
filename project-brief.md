# Waste Collection Accessibility in Port Harcourt

## Part 1: The question

Which parts of **Port Harcourt Local Government Area, Rivers State, Nigeria**, are furthest from a mapped waste-related point?

## Part 2: Why it matters

This question matters because local environmental agencies and city planners need to understand which settlement areas may be underserved by mapped waste infrastructure. The result could help identify locations for improved collection routes or additional facilities, while also showing where better data is needed. The analysis will not treat missing OpenStreetMap features as proof that no formal facility exists.

## Part 3: The data I need

- Port Harcourt Local Government Area boundary.
- Settlement extents or built-up areas within the study area.
- Road network for accessibility and route-distance analysis.
- Mapped waste-disposal, recycling, or waste-transfer points.

## Part 4: Where each dataset comes from

- **Port Harcourt Local Government Area boundary** — [GRID3 NGA Operational LGA Boundaries](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about) — downloaded from the official GRID3 feature service and filtered to `Port-Harcourt`.
- **Settlement extents / built-up areas** — [GRID3 NGA Settlement Extents v4.1](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about) — downloaded from the official GRID3 feature service and clipped to the LGA.
- **Road network** — [OpenStreetMap](https://www.openstreetmap.org/) using the [QuickOSM plugin](https://docs.3liz.org/QuickOSM/) — extracted with `highway=*` and clipped to the LGA.
- **Mapped waste-related points** — [OpenStreetMap waste-disposal tagging](https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dwaste_disposal), [recycling tagging](https://wiki.openstreetmap.org/wiki/Tag:amenity%3Drecycling), and [Overpass API](https://overpass-api.de/) — extracted with `amenity=waste_disposal`, `amenity=recycling`, and `amenity=waste_transfer_station`, then clipped to the LGA.

The data check found 130 settlement blocks and 47,609 road features, but no mapped waste-related points inside Port-Harcourt LGA. One recycling-centre feature was found in the wider extraction area but fell outside the LGA. This limitation is documented rather than treated as evidence that Port Harcourt has no waste facilities.

## Part 5: What I would build

I would build a reproducible QGIS map showing settlement areas symbolised by their distance to the nearest mapped waste-related point. Where enough waste points are available, I would calculate network distance using the road layer and produce a ranked table of underserved settlement areas. For the current extraction, I would first obtain a verified municipal waste-facility dataset or narrow the question before calculating distances.

**Author: Saviour Nwibari Koki**
