# Waste Collection Accessibility in Port Harcourt

This repository contains a place-based GIS study of access to **mapped waste-related points** in Port Harcourt Local Government Area, Rivers State, Nigeria. The proposed analysis combines GRID3 administrative and settlement data with OpenStreetMap roads and waste-related amenities.

Read the complete project brief here: [project-brief.md](project-brief.md).

## Completed QGIS-style extraction

The extraction follows the QuickOSM workflow described in the brief. The same Overpass query logic can be run from QGIS QuickOSM using the following keys and values:

- `highway=*` for road ways;
- `amenity=waste_disposal`;
- `amenity=recycling`;
- `amenity=waste_transfer_station`.

The GRID3 LGA boundary and settlement extent data were downloaded from their official ArcGIS feature services, and the settlement extract was clipped locally to the exact `Port-Harcourt` LGA boundary.

## Extraction results

The extraction was run on **8 September 2026** using the Port Harcourt bounding box and then clipped to the Port-Harcourt LGA boundary.

| Layer | Result |
|---|---:|
| Port-Harcourt LGA boundary | 1 feature |
| GRID3 settlement blocks after clipping | 130 features |
| OpenStreetMap road features in the extraction area | 47,609 ways |
| OSM waste-related features in the extraction area | 1 feature |
| OSM waste-related features inside Port-Harcourt LGA | 0 features |
| Nearest-waste distance layer | Not created because there were no in-LGA points |

The one waste-related feature found in the wider extraction area was an OSM `amenity=recycling` way named **Recycline Plant**, tagged as a recycling centre. It was outside the exact Port-Harcourt LGA boundary, so it was not used as a nearest facility for the LGA analysis.

### Interpretation and limitation

There are currently **no mapped OSM waste-disposal, recycling, or waste-transfer points inside the extracted Port-Harcourt LGA boundary**. Therefore, it would be misleading to calculate or map distance to the nearest waste point from these data alone. This is a limitation of current OSM coverage, not evidence that Port Harcourt has no waste facilities.

The project should now either obtain a verified municipal or environmental-agency waste-facility dataset, or narrow the question to the wider Port Harcourt extraction area and clearly label the result as distance to the nearest **mapped** OSM waste-related point.

## GeoPackage output

The extracted and clipped layers are packaged in [port_harcourt_waste_accessibility.gpkg](port_harcourt_waste_accessibility.gpkg):

- `lga_boundary` — GRID3 Port-Harcourt LGA boundary;
- `settlements` — GRID3 settlement blocks clipped to the LGA;
- `roads_osm` — OpenStreetMap road ways clipped to the LGA;
- `waste_points_osm` — OSM waste-related points after clipping; empty in this run.

A nearest-distance layer was intentionally not generated because the in-LGA waste layer is empty.

## Planned next step

Obtain a verified waste-facility dataset from the relevant Rivers State or Port Harcourt environmental authority, document its source and date, add it to the GeoPackage, and then calculate settlement-to-nearest-facility distances in a projected CRS. If no authoritative dataset is available, retain the documented zero-point limitation rather than treating missing OSM features as missing facilities.

## Data sources

- [GRID3 NGA Operational LGA Boundaries](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about)
- [GRID3 NGA Settlement Extents v4.1](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about)
- [OpenStreetMap](https://www.openstreetmap.org/)
- [QuickOSM documentation](https://docs.3liz.org/QuickOSM/)
- [OSM `amenity=waste_disposal` tagging](https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dwaste_disposal)
- [OSM `amenity=recycling` tagging](https://wiki.openstreetmap.org/wiki/Tag:amenity%3Drecycling)
- [Overpass API](https://overpass-api.de/)

## Important data note

OpenStreetMap coverage is community-maintained and may be incomplete. This project reports distance from **mapped waste-related points**, not distance from every formal waste facility.
