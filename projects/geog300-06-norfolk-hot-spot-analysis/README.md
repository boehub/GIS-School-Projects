# Hot Spot Analysis in Norfolk, VA: Where Should Health Assistance Go?

**Course:** GEOG 300 · **Tool:** ArcGIS Online (Map Viewer Classic analysis tools) · **Live map:** https://arcg.is/yuPLL

<!-- ![Final map](images/final-map.png) -->

## Question
Given a study area in Norfolk, which ZIP codes combine **low household income** with **heavy exposure to carcinogen-producing toxic sites**, making them the strongest candidates for a government health assistance program?

## Data
Course-provided layers: Virginia cancer mortality (1970-1994) and toxic waste (carcinogen) sites, a Norfolk study area polygon, Southside Virginia ZIP codes, and a ZIP-level layer enriched with Esri household demographics.

## Method
1. **Overlay (Intersect)** the carcinogen sites with the study area to keep only the sites inside it, then counted them from the attribute table (about 0.6 credits of analysis).
2. **Overlay (Intersect)** the ZIP codes with the study area to clip them to the area of interest.
3. Added an **enriched** layer of ZIP-level household data (median household income).
4. Ran **Find Hot Spots** (Getis-Ord Gi\*) on **median household income**.
5. Ran Find Hot Spots on the **number of carcinogen sites** in each ZIP code.
6. Combined the two results to rank ZIP codes by need and kept only the layers needed to show the solution.

## How to read a hot spot result
These were the points I had to correct and understand properly:

- A **hot spot** is a statistically significant cluster of *high values*; a **cold spot** is a significant cluster of *low values*. Hot/cold refers to the analyzed variable, not to cancer rates (unless that is the variable).
- The **confidence level** (90%, 95%, 99%) says how unlikely it is that the clustering arose by chance. It is **not** the size of the value. A 99% cold spot is a very strong cluster of low values.
- Areas that are not significant (neutral color) show no clustering, which does not mean low values.
- For **income**, cold spots (low-income clusters) are the ones that matter for assistance. For **carcinogen counts**, hot spots (many sites) are the ones that matter.
- Median household income is a typical value for each area, not a count, so it works for hot spot analysis without normalizing.

## What I found
<!-- Fill in from the final map: how many sites are in the study area; which ZIP codes are low-income cold spots; which are carcinogen hot spots; which ZIP code overlaps both. -->
Overlaying the low-income cold spots with the carcinogen hot spots narrows the candidates to the ZIP code(s) where both conditions coincide. A ZIP code that is both a low-income cold spot and a carcinogen hot spot is the strongest case for assistance.

## Caveats
- ZIP-code polygons are arbitrary units (the modifiable areal unit problem); results can change with different boundaries.
- Cancer mortality data (1970-1994) is old, and carcinogen sites do not prove exposure or cause. This analysis identifies where to look, not why.
- There were too few values to run hot spot analysis on high school graduation rates or households in poverty.

## Skills shown
Vector overlay, data enrichment, spatial statistics (Gi\*), interpreting significance and confidence, multi-criteria prioritization, using analysis credits responsibly.
