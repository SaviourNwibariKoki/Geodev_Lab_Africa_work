# Week 2 Data Note

**Project:** Waste Collection Accessibility in Port Harcourt  
**Study area:** Port-Harcourt Local Government Area, Rivers State, Nigeria  
**Author:** Saviour Nwibari Koki  
**Data checked:** 8 September 2026  
**Package:** `port_harcourt_waste_accessibility.gpkg`

This note describes the four datasets used for the proposed GIS analysis. The layers are stored together in the GeoPackage committed to this repository and can be opened in QGIS using **Layer > Add Layer > Add Vector Layer**.

| Dataset / GeoPackage layer | Source and source link | Features in packaged layer | Geometry and CRS | Key columns | Gaps, missing values, or other observations |
|---|---|---:|---|---|---|
| Port-Harcourt LGA boundary (`lga_boundary`) | GRID3 NGA Operational LGA Boundaries, official GRID3 feature service: [data.grid3.org](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about) | 1 | Polygon; EPSG:4326 | `lganame`, `lgacode`, `statename`, `statecode`, `source`, `Shape__Area`, `Shape__Length` | The layer contains the selected Port-Harcourt boundary. The boundary is used to clip the other datasets to the study area. |
| Settlement extents (`settlements`) | GRID3 NGA Settlement Extents v4.1, official GRID3 feature service: [data.grid3.org](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about) | 130 | MultiPolygon; EPSG:32632 | `block_id`, `block_area_sqm`, `building_count`, `building_area_percentage`, `extent_type`, `composite_class`, `Shape__Area`, `Shape__Length` | The data contains 130 settlement blocks after clipping to the LGA. Several descriptive GRID3 attributes can be empty for individual blocks; these should be checked before using them for a detailed settlement ranking. |
| OpenStreetMap roads (`roads_osm`) | OpenStreetMap, extracted in QGIS with the [QuickOSM plugin](https://docs.3liz.org/QuickOSM/) using `highway=*`: [openstreetmap.org](https://www.openstreetmap.org/) | 4,994 | MultiLineString; EPSG:4326 | `osm_id`, `highway`, `name` | The packaged count is the clipped in-LGA layer. The wider bounding-box extraction contained 47,609 road ways before clipping. `name` is often missing because many OSM roads are unnamed. Road coverage and classification depend on community mapping and may be incomplete. |
| Mapped waste-related features (`waste_points_osm`) | OpenStreetMap/Overpass extraction using `amenity=waste_disposal`, `amenity=recycling`, and `amenity=waste_transfer_station`; references: [waste disposal tagging](https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dwaste_disposal), [recycling tagging](https://wiki.openstreetmap.org/wiki/Tag:amenity%3Drecycling), [Overpass API](https://overpass-api.de/) | 0 inside the LGA | Geometry column is `GEOMETRY`; EPSG:32632 | `osm_id`, `osm_type`, `amenity`, `name` | No mapped waste-related feature fell inside the exact Port-Harcourt LGA boundary. One `amenity=recycling` feature named “Recycline Plant” was found in the wider extraction area but fell outside the LGA. The empty layer is therefore a documented OpenStreetMap coverage limitation, not evidence that Port Harcourt has no formal waste facilities. `name` would also be incomplete even if features were present. |

## Summary of the check

The GeoPackage opens as a spatial SQLite/GeoPackage file and contains the LGA boundary, 130 settlement blocks, 4,994 clipped road features, and an empty in-LGA waste-related layer. The wider extraction statistics in the project README are retained for transparency, but the counts in this table refer specifically to the layers delivered in the GeoPackage.

Because there are currently no mapped waste-related points inside the LGA, a nearest-waste distance layer was **not** calculated. The next analytical step should be to obtain a verified municipal or environmental-agency waste-facility dataset, or to revise the study area and label any result explicitly as distance to the nearest **mapped** OSM waste-related point.

## Reproducibility note

The roads and waste-related features were obtained from OpenStreetMap through the QuickOSM/Overpass workflow. OpenStreetMap is community-maintained, so the results should be interpreted as an analysis of mapped features rather than a complete inventory of waste infrastructure.
