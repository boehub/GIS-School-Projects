# GIS School Projects

**Ryan Boe**: coursework portfolio in Geographic Information Systems (GIS) and geography, built at Old Dominion University.

Each project is written up as a short case study: the question being asked, the data and tools used, the method, what the map or analysis showed, and what I would do differently. The goal is to show how I work with spatial data, not just to host assignment files.

## Skills demonstrated

| Area | What I did |
|---|---|
| **Cartography and design** | Thematic and multivariate maps, colorblind-safe palettes (ColorBrewer, diverging ramps), proportional symbols, labels with halos, basemap blending |
| **Coordinate systems and projections** | Public Land Survey System (PLSS) vs. latitude/longitude, Web Mercator vs. polar projection |
| **Spatial analysis** | Overlay (intersect), data enrichment, Getis-Ord Gi\* hot spot analysis |
| **Data handling** | Joining tables to geography, loading CSVs and web services, cleaning coordinate data, filtering, field aliases and formatting |
| **Interactive web mapping** | Configured pop-ups (images, links, curated fields), saved and shared web maps |
| **Dashboards** | Tableau Public dashboard of world population |
| **Scripting** | Python (standard library) script for cleaning coordinate columns in point CSVs |

**Tools:** ArcGIS Online (Map Viewer), Tableau Public, Python

## Projects

| # | Project | Focus | Live map |
|---|---|---|---|
| 1 | [Principal Meridians and the PLSS](projects/geog300-01-principal-meridians-plss/) | Survey systems vs. latitude/longitude | [Open](https://arcg.is/0reGni0) |
| 2 | [Magnetic North in Two Projections](projects/geog300-02-magnetic-north-polar-projection/) | Projection choice and interpretation | [Open](https://arcg.is/1Cy1vG2) |
| 3 | [Income and Poverty by State](projects/geog300-03-income-and-poverty-by-state/) | Two-variable map, pop-ups, field formatting | [Open](https://arcg.is/0ejy8j) |
| 4 | [Santa Clara Sites and Traffic Cameras](projects/geog300-04-santa-clara-web-service-and-popups/) | Web services, CSV import, image pop-ups | [Open](https://arcg.is/0jn5CP0) |
| 5 | [Afghanistan: Hydrology and Regions](projects/geog300-05-afghanistan-hydrology-and-regions/) | Qualitative regions, custom color, blending | [Open](https://arcg.is/yKXHu1) |
| 6 | [Hot Spot Analysis in Norfolk](projects/geog300-06-norfolk-hot-spot-analysis/) | Overlay, enrichment, Gi\* hot spots | [Open](https://arcg.is/yuPLL) |
| 7 | [US Housing: Multivariate Mapping](projects/geog300-07-us-housing-multivariate-mapping/) | Compare A to B, predominance, color + size | [Open](https://arcg.is/188vi13) |
| 8 | [Chesapeake Bay Wetlands and Flood Hazard](projects/geog101s-ex2-chesapeake-wetlands-flood-hazard/) | Wetlands and flood-risk context | [Open](https://arcg.is/0z1zjC0) |
| 9 | [World Population Dashboard](dashboards/world-population-tableau/) | Tableau dashboard | [Open](https://public.tableau.com/app/profile/ryan.boe1040/viz/worldpop_final_Ryan_Boe/Dashboard1) |

Projects 1-7 are from GEOG 300 (Maps and Geographic Information Systems), fall 2025. Project 8 is from GEOG 101S, fall 2025.

## Repository layout

```
gis-school-projects/
├── README.md
├── projects/
│   ├── geog300-01-principal-meridians-plss/
│   ├── ...
│   └── geog101s-ex2-chesapeake-wetlands-flood-hazard/
│       ├── README.md      # the case study
│       └── images/        # map screenshots
└── dashboards/
    └── world-population-tableau/
```

Project 4 also includes a small [Python script](projects/geog300-04-santa-clara-web-service-and-popups/scripts/clean_csv_coordinates.py) for cleaning coordinate columns.

## Notes on data and sources

- Every project README lists where its data came from and who gets credit. Most layers come from Esri's Living Atlas, the BLM, NOAA, DataUSA, and local government GIS services.
- Course-provided files and assignment instructions are not republished here. The case studies describe the work in my own words.
- These are class exercises. Where I had to substitute a layer or ran into a limitation, the case study says so.
