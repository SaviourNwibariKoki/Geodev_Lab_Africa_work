# Waste Collection Accessibility in Port Harcourt

## 1. The question

**Which parts of Port Harcourt Local Government Area are furthest from a mapped waste-related point?**

The analysis will measure network or straight-line proximity from settlement areas to the nearest mapped waste-related point, then identify the most underserved settlement areas within Port Harcourt LGA. It will not treat missing OpenStreetMap features as proof that no formal facility exists.

## 2. Why it matters

Understanding spatial gaps in municipal waste management can help local environmental agencies allocate resources more efficiently. Identifying specific neighbourhoods that are underserved can support better collection routes and the strategic placement of new waste infrastructure, reducing illegal dumping and improving community health.

## 3. The data I need

1. Port Harcourt Local Government Area boundary.
2. Settlement extents or built-up areas within the study area.
3. Road network for accessibility and route-distance analysis.
4. Mapped waste collection, waste-disposal, recycling, or waste-transfer points.

## 4. Where each dataset comes from

| Dataset | Source link | Format / extraction |
|---|---|---|
| Local Government Area boundaries | [GRID3 NGA Operational LGA Boundaries](https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about) | Download the Nigeria LGA boundary layer and filter to Port Harcourt LGA; GeoPackage or GIS-compatible feature layer. |
| Settlement extents / built-up areas | [GRID3 NGA Settlement Extents](https://data.grid3.org/datasets/GRID3::grid3-nga-settlement-extents-v4-1/about) | Download the Nigeria settlement-extents layer and clip to Port Harcourt LGA; GeoPackage or GIS-compatible feature layer. |
| Road network | [OpenStreetMap](https://www.openstreetmap.org/) via [QuickOSM](https://docs.3liz.org/QuickOSM/) | Extract roads within Port Harcourt LGA using QuickOSM; GeoPackage layer. |
| Waste collection / disposal points | [OpenStreetMap waste-disposal tag](https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dwaste_disposal), [recycling tag](https://wiki.openstreetmap.org/wiki/Tag:amenity%3Drecycling), and [Overpass API](https://overpass-api.de/) | Extract mapped `amenity=waste_disposal`, `amenity=recycling`, and `amenity=waste_transfer_station` points within Port Harcourt LGA using QuickOSM or Overpass; GeoPackage layer. |

### Data check and limitation

GRID3 provides public Nigeria settlement and LGA boundary datasets. OpenStreetMap provides documented waste-related amenity tags and an Overpass extraction route. The number of mapped waste points must be checked at extraction time because OSM coverage changes and may be sparse; if no usable waste points are returned for Port Harcourt LGA, the question will be narrowed or the waste-point source will be supplemented with a verified municipal dataset before analysis.

## 5. What I would build

I would build a reproducible QGIS workflow and a map showing settlement areas symbolised by distance to the nearest mapped waste point. A companion table would rank the most underserved neighbourhoods, while the road network would support a more realistic network-distance or service-area calculation where the data quality allows it.
