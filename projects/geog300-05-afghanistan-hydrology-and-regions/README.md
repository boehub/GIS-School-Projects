# Afghanistan: Hydrology, Flood Risk, and Qualitative Regions

**Course:** GEOG 300 · **Tool:** ArcGIS Online Map Viewer · **Live map:** https://arcg.is/yKXHu1

<!-- ![Final map](images/final-map.png) -->

## Question
How do you style qualitative regions and hydrology so a reader can separate permanent water from seasonal water and see the terrain underneath?

## Data
Course-provided Afghanistan layers: water lines (rivers and streams), water areas, and UN regions of Afghanistan. Colors chosen with ColorBrewer 2.0; basemap is Esri's Firefly Imagery Hybrid.

## Method
1. Opened an existing Afghanistan web map and saved a working copy.
2. **Rivers and streams:** styled by the stream-type field (perennial vs. non-perennial) as unique values. Picked colorblind-friendly blues from ColorBrewer and entered them as **hex codes**, with a dark, thick line for perennial streams and a lighter, thinner line for non-perennial ones.
3. Renamed the cryptic field to **Type of Stream** with a field alias, and trimmed the pop-up to that one field.
4. **Water areas:** styled by feature type (inland water vs. land subject to inundation), then filtered to show only the higher-risk "land subject to inundation" as a **Flood Risk** layer.
5. **Regions:** styled the UN region field by unique values, turned pop-ups off, and renamed the layer.
6. **Basemap blending:** switched to Firefly Imagery Hybrid and tuned blend modes so the terrain shows through the symbols.

## Concepts demonstrated
- **Qualitative vs. quantitative data.** The UN region field is qualitative: it names categories with no inherent order, so unique-value (categorical) colors are the right choice, not a graduated ramp.
- **Discrete vs. continuous.** Regions are discrete areas with hard borders.
- **Why regions?** Geographers group places by shared traits to organize space, compare places, and see patterns in culture, climate, population, and environment.
- **Styling options for regions:** color, shading and transparency, labels, and patterns. These tell readers which areas are alike and different, and each choice trades clarity against clutter.
- **Accessible color.** Custom hex colors from a colorblind-safe palette keep the two stream types distinguishable by value and line width, not hue alone.

## Limitations
In the original assignment, a layer author's account no longer existed, so I used a substitute copy of the same map from another author. I noted this to the instructor. It is a reminder that web-map workflows depend on layers staying available, so documenting sources matters.

## Skills shown
Unique-value symbology, hex-color control, line-width design, filters, field aliases, pop-up configuration, basemap blending, accessible color choices.
