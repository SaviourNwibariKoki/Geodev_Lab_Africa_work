# Month 1 Summary

## Question

Which parts of Port Harcourt Local Government Area, Rivers State, Nigeria, are furthest from a mapped waste-related point?

## Operation and why I ran it

I ran a **100-metre buffer** around every mapped OpenStreetMap road feature in the analysis-ready projected dataset. This operation answers a useful supporting part of the question: it identifies the areas within a short distance of the mapped road network, which is relevant to future waste-collection route accessibility. I used EPSG:32632 (WGS 84 / UTM zone 32N), where the buffer distance is correctly interpreted in metres.

The input layer was `roads_osm` in `port_harcourt_waste_accessibility_analysis_ready.gpkg`. The output is one buffer polygon for each road feature, with no dissolve, in `week4_roads_100m_buffer.gpkg` under the layer `roads_100m_buffer`.

## Expectation before running

The input contained 4,994 road features. I expected approximately **4,994 output buffer features**, one for each road feature, and expected the buffer distance to be 100 metres. Because the road network contains many connected and overlapping roads, I expected the buffers to overlap in places but to remain separate features because I did not dissolve them. I expected no empty geometries for non-empty road inputs.

## Result and four checks

The operation produced **4,994 buffer features**, exactly matching the input road count. Every output feature has `buffer_m = 100`.

1. **Look at the map:** I inspected the exported map, `week4_100m_road_access_buffer.png`. The blue buffer areas follow the mapped road network across the LGA, the LGA boundary is visible, settlement boundaries are shown, and the map includes a title, legend, and 5 km scale bar.
2. **Check the row count:** The result has 4,994 rows, matching the expected one-buffer-per-road result of approximately 4,994.
3. **Verify one feature by hand:** The first road is about 139.4 m long. Its generated buffer has an area of approximately 59,250 m², close to the simple straight-line estimate of about 59,300 m² for a 100 m buffer around a 139.4 m line. This is a reasonable result, allowing for the road's actual shape and rounded buffer ends.
4. **Look for empty geometry:** The result has **0 empty geometries** and **0 null geometries**.

## What surprised me

The output count stayed exactly the same as the road count, even though the map looks visually dense. This is because overlapping buffers were intentionally not dissolved: each road feature keeps its own buffer polygon. The map also shows that mapped roads cover many parts of the LGA, but this does not tell me whether waste facilities are present or whether collection routes are actually accessible.

## What data I still need

The current OpenStreetMap extraction contains **zero mapped waste-related points inside the Port-Harcourt LGA**. I still need a verified waste-facility or collection-point dataset from the relevant Rivers State or Port Harcourt environmental authority. With that dataset, I can calculate settlement-to-nearest-facility distances and assess which areas are underserved. I also need to distinguish mapped road proximity from actual route accessibility, which may require a validated road network with travel restrictions, road condition, and route-cost information.

## Outputs

- Analysis result: [week4_roads_100m_buffer.gpkg](week4_roads_100m_buffer.gpkg)
- Map image: [week4_100m_road_access_buffer.png](week4_100m_road_access_buffer.png)
- Reproducible script: [run_week4_analysis.py](run_week4_analysis.py)
