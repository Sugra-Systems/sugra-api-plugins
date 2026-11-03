# Water

## Flood and rivers
Anchor: water.river_forecast
Companions: water.river_ensemble, water.gauge_observed, water.annual_peaks, water.flow_percentile, hazards.official_warnings, weather.forecast, logistics.road_events
Why together: High water means something only against the flood threshold and the river's past peaks; an ensemble shows what one line hides.
Methods (the answer names the one it uses):
- Rank of the current peak among annual peaks; return period T = (years + 1) / rank; chance of at least one T-year flood in n years = 1 - (1 - 1/T)^n.
- Flow percentile on the date: below the 10th much below normal, below the 25th below normal.
Traps:
- A model cell discharge is not a gauge reading; a peak series under 30 years gives a rough return period.
- Stage (height) and discharge (flow) are different quantities.

## Coastal water level and surge
Anchor: water.surge_observed
Companions: water.coastal_level_observed, water.tide_predicted, water.sea_level_model, water.waves, hazards.official_warnings
Why together: Surge is the part of the level the tide does not explain; the danger is surge on top of the tide.
Methods (the answer names the one it uses):
- Surge = observed level minus predicted tide at one station, one window, one datum; peak surge timed against high tide.
Traps:
- A tide prediction is astronomy, no weather; modelled sea level with its pressure part leaves out wind setup.
- Mixed datums shift levels by up to metres.
