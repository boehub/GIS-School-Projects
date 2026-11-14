# Principal Meridians and the Public Land Survey System

**Course:** GEOG 300, Maps and Geographic Information Systems · **Tool:** ArcGIS Online Map Viewer · **Live map:** https://arcg.is/0reGni0

<!-- ![Final map](images/final-map.png) -->

## Question
The Public Land Survey System (PLSS) divides most of the US west of Ohio into townships, ranges, and sections measured from a set of *principal meridians*. How do those survey reference points relate to the global latitude/longitude grid?

## Data
| Layer | Source |
|---|---|
| Principal meridian initial points (with year adopted) | Course-provided point layer |
| World Latitude and Longitude Grids (1° grid) | Esri |
| USA States Generalized Boundaries | Esri |
| Public Land Survey System (townships, sections) | Bureau of Land Management (BLM) |

## Method
1. Loaded the principal meridian points and inspected the attribute table (year each meridian was adopted).
2. Added the 1° latitude/longitude grid and removed the coarser grids so only the 1° layer remained.
3. Styled the state layer as black outlines with no fill and pop-ups off, so it works as context only.
4. Added the BLM PLSS layer and created map bookmarks for places where the survey system begins or breaks down:
   - Ohio/Pennsylvania border, where the PLSS survey begins
   - South Louisiana, the French long-lot system
   - Texas panhandle area, a region not surveyed with the PLSS (Spanish land-grant legacy)
   - San Rafael, California, where the PLSS is superimposed on the earlier Spanish survey
5. Saved a final view at one point where a principal meridian meets the 1° grid, and shared the map.

## What I found
- **Adoption dates:** the principal meridians in the layer were adopted between **1803 and 1956**.
- **Meridians are survey references, not graticule lines.** The meridian points are sited for the convenience and history of each regional survey, so only a few land close to a whole-degree grid intersection. The grid is a global reference; the PLSS is a local one.
- **Projection changes how the grid looks, not where it is.** A latitude/longitude coordinate stays the same in any projection; only its drawn spacing and shape change.
- **Alaska has several principal meridians** (Fairbanks, Copper River, Seward, and Umiat) because it is huge, was surveyed in separate regions over many decades, and each meridian only works well for the area near it. Meridians converge toward the pole, so a single grid cannot cover that much territory without growing distorted.
- **The PLSS is not universal.** The bookmarks show areas where earlier French and Spanish land systems shaped the pattern of parcels instead.

## Skills shown
Layer search and styling, graticules, working with several reference systems at once, bookmarks, map sharing.

## What I'd do next
Measure how far each principal meridian's initial point sits from the nearest 1° intersection (a quick distance calculation) to put numbers on how closely the two systems line up.
