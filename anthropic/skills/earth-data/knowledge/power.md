# Power

## Heat and the grid
Anchor: power.load
Companions: power.load_forecast, weather.forecast, weather.degree_days, power.fuel_mix, power.interchange, power.wholesale_price, power.solar_observed, hazards.official_warnings, water.gauge_observed, commodities.natgas_price, commodities.natgas_storage
Why together: Peak load comes from heat in population centres at the evening hour, when solar fades; gas covers the peak; warm rivers limit plant cooling.
Methods (the answer names the one it uses):
- Load and its forecast as percent of the region's historical peak, in local hours.
- Net load = load minus wind and solar at the evening hour.
- Flows into the region as a sign of shortage, after checking the publisher's sign convention.
Traps:
- Degree days are not load; one city is not the region; retail is not wholesale price.
- Heat alone is not a gas price: a record warm month can bring lower gas when solar and wind grow and storage is above its five-year average.

## Cold and the grid
Anchor: power.load_forecast
Companions: power.load, weather.forecast, weather.degree_days, power.fuel_mix, power.generator_outages, power.plants, power.outages, power.scarcity_notices, commodities.natgas_price, commodities.futures_curve
Why together: Cold raises gas and power demand while it cuts gas output, and gas plants cover the peak, so gas and power fail together.
Methods (the answer names the one it uses):
- Day-ahead error = (actual - forecast) / forecast, against the usual 2-3 percent (Winter Storm Elliott, December 2022, eastern US, from the FERC and NERC inquiry: 6.8 at one day, 8.8 at two).
- Outages in MW and as a share of expected capacity, against past events (the same inquiry: 90,500 MW, 13 percent; freezing 31 percent, fuel 24, mechanical and electrical 41; gas output down 16 percent in three days).
- Forecast minimum against plant and well design limits, not only the normal: in that inquiry about 80 percent of freeze failures came above the design minimum.
Traps:
- A firm gas contract does not guarantee gas; a cold record says nothing about outages, whose causes come from operator reports.
