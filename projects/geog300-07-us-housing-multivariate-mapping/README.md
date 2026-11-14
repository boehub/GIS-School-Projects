# US Housing: Multivariate Mapping with Esri Demographics

**Course:** GEOG 300 · **Tool:** ArcGIS Online Map Viewer · **Live map:** https://arcg.is/188vi13

<!-- ![Final map](images/final-map.png) -->

## Question
How do different map styles change the story you can tell about the same county-level housing data?

## Data
Esri Updated Demographics, US Variables, 2023 (Living Atlas), county level: owner-occupied, renter-occupied, and vacant housing units, total housing units, median household income, and median home value. Used for educational purposes.

## Method
One dataset was duplicated into three layers, each styled by a different method:

| Layer | Style | Why |
|---|---|---|
| **2023 Owner and Renter Population** | **Compare A to B** with a colorblind-friendly diverging ramp | Shows the ratio of owner to renter units |
| **2023 Housing Units** | **Predominant category** (owner, renter, vacant) | Shows which category leads in each county |
| **Home Income & Home Value** | **Color and size**, high to low, white outlines, dark-gray basemap | Shows two quantitative variables at once |

Pop-ups were configured for each layer to show only the fields needed to check the map (for the predominance layer, the three categories plus total units, so they can be summed and verified).

## Reading the maps
- **Message of the Compare A to B map:** where homeowners dominate and where renters dominate, county by county.
- **How Compare A to B works:** it divides one variable by the other and uses a diverging ramp: one color family where owners exceed renters, another where renters exceed owners, and the middle where the two are about equal.
- **A percent-of-total variant** (A as a share of A+B) gives a more intuitive reading than raw counts, and keeps a very large county from drowning out smaller ones.
- **Why predominance:** it answers "what is the main housing situation here?" at a glance. Checking pop-ups against the total confirms the categories add up.

## County comparison (qualitative)
| County | Home ownership | Median income | Home values |
|---|---|---|---|
| Routt, CO | Mostly owner-occupied; above the national average | High | Very high, resort-driven market |
| Grand Forks, ND | About half owner-occupied; below the national average | Moderate | Moderate |
| Teton, WY | Mostly owner-occupied; slightly below the national average | Extremely high, with strong inequality | Exceptionally high, luxury and second-home market |

## Skills shown
Living Atlas data, layer duplication, three complementary symbology methods, diverging colorblind-safe ramps, legend interpretation, pop-up design for verifying a map, dark-basemap design.
