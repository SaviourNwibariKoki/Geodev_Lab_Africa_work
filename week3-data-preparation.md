# Week 3 Data Preparation and Quality Checks

**Project:** Waste Collection Accessibility in Port Harcourt  
**Study area:** Port-Harcourt Local Government Area, Rivers State, Nigeria  
**Author:** Saviour Nwibari Koki  
**Preparation date:** 19 September 2026

## Analysis-ready coordinate system

I chose **EPSG:32632 — WGS 84 / UTM zone 32N** because Port Harcourt is in longitude zone 32N, and this projected coordinate reference system uses **metres**. It is therefore suitable for measuring distances, calculating areas, and carrying out future network-accessibility analysis. The original layers were mixed between EPSG:4326 and EPSG:32632; all layers were reprojected into EPSG:32632 so that the analysis-ready file has one consistent CRS.

## What was reprojected and clipped

The following layers were processed from `port_harcourt_waste_accessibility.gpkg`:

| Layer | Processing | Final features | Final geometry |
|---|---|---:|---|
| `lga_boundary` | Reprojected to EPSG:32632; retained as the study-area boundary | 1 | Polygon |
| `settlements` | Reprojected to EPSG:32632 and clipped to the LGA boundary | 130 | Polygon/MultiPolygon |
| `roads_osm` | Reprojected to EPSG:32632 and clipped to the LGA boundary | 4,994 | LineString/MultiLineString |
| `waste_points_osm` | Reprojected to EPSG:32632; checked against the LGA boundary | 0 | Empty layer |

The layers were clipped using the Port-Harcourt LGA boundary. The packaged roads and settlement features have no features outside that boundary after processing. The waste layer remains empty because no mapped OSM waste-related feature was found inside the LGA in the Week 2 extraction.

## Five quality checks and findings

### 1. CRS consistency and suitability

**Check:** Confirm that every layer has a defined CRS and that the CRS is appropriate for measurement.  
**Finding:** All four output layers use EPSG:32632.  
**Decision:** The original mixed CRS situation was fixed by reprojecting the layers into UTM 32N. Coordinates are now in metres and the data is ready for projected distance and area operations.

### 2. Geometry validity

**Check:** Test for null geometries and invalid geometries, including self-crossing polygon shapes.  
**Finding:** The LGA boundary, settlement layer, and road layer each contain zero invalid geometries and zero null geometries. The waste layer is empty, so there are no waste geometries to validate.  
**Decision:** No geometry repair was required. The empty waste layer was flagged as a data-coverage limitation.

### 3. Duplicate features

**Check:** Test for duplicate rows using the non-geometry attributes of each layer.  
**Finding:** No duplicate attribute rows were found in the boundary, settlement, roads, or waste layers.  
**Decision:** No duplicate features were removed.

### 4. Missing and incomplete attributes

**Check:** Inspect non-geometry columns for null values and assess whether missing values affect the planned analysis.  
**Finding:** The settlement layer has 11 missing `building_area_stdev` values. The road layer has 4,609 missing `name` values, meaning many roads are unnamed in OpenStreetMap. The boundary layer has no missing attribute values. The waste layer has no rows.  
**Decision:** Missing values were not filled with invented values. The settlement standard-deviation gaps are flagged for any future analysis that uses that field, while missing road names do not prevent network analysis because the road geometry and `highway` class remain available.

### 5. Spatial coverage and study-area extent

**Check:** Confirm that the required layers cover the intended study area and that features outside the LGA have been removed.  
**Finding:** The boundary contains one Port-Harcourt LGA feature. All 130 settlement features and all 4,994 road features intersect the boundary after clipping; no outside features remain. The waste layer has zero in-LGA features.  
**Decision:** The boundary, settlements, and roads passed the extent check. The zero waste-point result is flagged as incomplete OpenStreetMap coverage and must not be interpreted as proof that no formal waste facilities exist.

## Problems found and decisions

The main preparation problem was the mixed source CRS: the boundary and roads were in geographic EPSG:4326 while the settlement and waste layers were already in EPSG:32632. This was fixed by transforming every layer to EPSG:32632. The layers also contained expected attribute gaps, which were documented and left as missing rather than imputed. The empty waste layer was retained so that the limitation is transparent and reproducible.

## Analysis-ready output

The prepared file is:

`port_harcourt_waste_accessibility_analysis_ready.gpkg`

It is stored in the repository root and contains the four consistently projected layers: `lga_boundary`, `settlements`, `roads_osm`, and `waste_points_osm`. The reproducible preparation script is [prepare_week3.py](prepare_week3.py), and the validation script is [check_week3_quality.py](check_week3_quality.py).
