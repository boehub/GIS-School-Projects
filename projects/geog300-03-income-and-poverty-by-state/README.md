# Income and Poverty by State: A Two-Variable Map

**Course:** GEOG 300 · **Tool:** ArcGIS Online Map Viewer · **Live map:** https://arcg.is/0ejy8j

<!-- ![Final map](images/final-map.png) -->

## Question
How are average income and poverty rate related across US states, and how can a single map show both?

## Data
DataUSA state-level data (2019) joined to a US states layer: average income, wage GINI coefficient, child poverty percentage, and poverty rate for 50 states plus DC.

## Method
1. Joined the DataUSA table to a state geography layer and added it to the map.
2. **Poverty rate** was styled as a color-graduated choropleth (darkest = highest).
3. A second copy of the layer showed **average income** as graduated symbol size with outlines, so both variables are visible together.
4. Configured pop-ups to show only the key fields, in a sensible order, with a clean title.
5. Set field aliases and number formatting so users see readable labels and rounded values (no cents on income).
6. Wrote the reflection in the item description and shared the map.

## What I found
I checked the visual impression against the data (51 rows):

| Relationship | Pearson r |
|---|---|
| Average income vs. poverty rate | **-0.57** |
| Average income vs. child poverty | -0.37 |
| Poverty rate vs. child poverty | 0.93 |
| Average income vs. wage GINI | 0.23 |

- **Higher-income states tend to have lower poverty, but the link is moderate, not strict.** Mississippi has the lowest average income (about $25,100) and the highest poverty rate (19.6%); New Hampshire has the lowest poverty rate (7.27%). But Utah has a low poverty rate (8.91%) with below-median average income, and DC has the highest average income (about $59,500) with a mid-range poverty rate (13.45%).
- **Population is not the explanation on its own.** North Dakota (small population) has above-median average income (about $36,800) while New Jersey (about 9 million people) is higher (about $45,000). Population helps readers judge how many people stand behind a rate, but it does not predict income.
- **Pop-ups change interpretation.** They connect the symbols to exact values and context (population, inequality) that the colors alone cannot carry, and they spare readers a spreadsheet.
- **Useful filters** for exploring the joined layer: poverty rate above a threshold, income above/below the national median, GINI above a threshold, or a region of states.

## Skills shown
Table-to-geography joins, choropleth vs. proportional symbols, multi-layer maps from one dataset, pop-up configuration, field formatting, checking a map's impression with quick statistics.

## Limitations
Correlation across states hides large differences inside states, and the two measures describe different things (average income vs. share below the poverty line). With more time I would map the residuals, the states that are richer or poorer than their poverty rate predicts.
