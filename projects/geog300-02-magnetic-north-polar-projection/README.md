# Magnetic North in Two Projections

**Course:** GEOG 300 · **Tool:** ArcGIS Online Map Viewer · **Live map:** https://arcg.is/1Cy1vG2

<!-- ![Polar map](images/final-map.png) -->

## Question
How does the choice of map projection change what we can see in the movement of Earth's north magnetic pole over time?

## Data
- Historical north magnetic pole positions, from NOAA's National Centers for Environmental Information (geomagnetic poles dataset)
- Arctic Ocean basemap, a geogrid layer (Arctic Circle), and World Countries (Generalized), all from Esri

## Method
**Part 1: Web Mercator.** Explored a prepared web map of magnetic north positions, read the attribute table, and used the locate tool to get coordinates.

**Part 2: Build a polar map.**
1. Set the Arctic Ocean basemap (polar projection) and zoomed to the pole.
2. Filtered the geogrid to the Arctic Circle (styled black) and filtered countries to those touching the circle.
3. Gave each Arctic country its own color with transparency and reordered the legend.
4. Styled the magnetic pole points by year with **equal interval** classes (4 classes), a color ramp where earlier years are lighter, and years formatted without thousands separators.
5. Documented the map in the item details and tagged it.

## What I found
- The earliest observation in the data is **1590**.
- Between **2015 and 2019** the pole moved from about **160.03° W to 175.35° E**. That is a shift of roughly 25° of longitude, and it crosses the 180° meridian, which is exactly the kind of movement that a flat Mercator map handles badly.
- The path **wanders irregularly**; it is not a clean spiral.
- In Web Mercator the poles stretch to infinity, so the area that matters most for this question cannot even be displayed. The polar projection keeps the pole in view and shows direction and distance of travel without that distortion.
- Map layout also shapes interpretation: the legend order and the lightest-to-darkest year ramp (earliest lightest) make time easy to read.

## Takeaway
A projection is an analytical choice. For polar data, a polar projection is the right tool; Mercator misleads.

## Skills shown
Projection selection, filtering by geography, classification methods (equal interval), legend and symbol design, map documentation.
