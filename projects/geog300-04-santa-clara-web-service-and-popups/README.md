# Santa Clara County: Web Services, CSV Points, and Rich Pop-ups

**Course:** GEOG 300 · **Tool:** ArcGIS Online Map Viewer · **Live map:** https://arcg.is/0jn5CP0

<!-- ![Final map](images/final-map.png) -->

## Question
How do you combine a live county web service with your own point data and make the result useful to a visitor?

## Data
| Layer | Source |
|---|---|
| City limits (`SCCCityLimits`), added as a web service by URL | Santa Clara County GIS |
| Santa Clara sites: 15 landmarks with photo URLs and websites (CSV) | Course-provided |
| Traffic cameras: 12 intersections with live feed links (CSV) | Course-provided; feeds from the City of Santa Clara |

## Method
1. Found the city limits service in the county GIS server directory and added it to a map **by URL**. The layer stays hosted by the county, so it can be drawn but not restyled.
2. Uploaded the sites CSV as a hosted layer, located by its latitude and longitude columns.
3. Styled points, added **labels with halos**, and set pop-up titles from the place name.
4. Added an **image pop-up** whose picture comes from a field and which links to the site's website when clicked.
5. Repeated the CSV import for the traffic cameras, used a car symbol, and trimmed the pop-up to a single clickable image linked to the live camera.
6. Set the extent so the city limits and nearly all points are visible, and documented the map (summary, description, credits, terms of use).

## What I learned
- **Hosted vs. referenced layers.** A layer added by URL points back to its owner's server, which affects what you can edit and how fast it loads.
- **Pop-ups can carry media and links**, which turns a point map into a small visitor guide.
- **Check your CSV before import.** Reviewing the sites file, I found that 7 of its 15 records have stray whitespace or a malformed coordinate: five contain non-breaking spaces and one has latitude and longitude merged into a single cell. Values like these can turn a numeric column into text and cause points to silently fail to plot. I wrote a small script to clean them.

## Script: `scripts/clean_csv_coordinates.py`
Standard-library Python that repairs coordinate columns and reports anything it cannot fix:

```bash
python3 scripts/clean_csv_coordinates.py sites.csv sites_clean.csv --lat lat --lon long
# 15 rows read, 7 coordinate pairs repaired, 0 unusable
```

It strips non-breaking spaces and whitespace, splits a merged "lat, long" cell, and flags rows with non-numeric or out-of-range coordinates.

## Skills shown
Web services, CSV import and geocoding by coordinates, symbology, labeling, media pop-ups, data quality checks, scripting.
