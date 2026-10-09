# Hazards

## Tropical cyclone
Anchor: hazards.tropical_cyclones
Companions: hazards.official_warnings, hazards.cyclone_forecast_track, hazards.impact_alerts, water.surge_observed, industry.offshore_shut_in, industry.refineries, power.plants, power.load, logistics.port_calls_deviation, logistics.aviation_delays, prices.crude_oil, prices.gasoline, labour.initial_claims
Why together: A storm hits production, refining, exports and demand at once, each market in its own direction; water (surge, rain) does more harm than wind.
Methods (the answer names the one it uses):
- Order: storm and warnings, exposure (industry file), disruption, prices.
- Category is 1-minute sustained wind; basins using 10-minute wind read about 10 percent lower.
- The cone holds about two thirds of past centre-track errors (NHC; its radii are reset each season, lately about 25 nautical miles at 12 h to 200 at 120 h in the Atlantic); beyond 72 h the track is a direction.
- US warnings: hurricane warning = 64 kt expected, 36 h before 34 kt winds arrive; watch = possible, 48 h; surge the same.
- Output: initial claims in the hit states rise for weeks; output and payrolls dip and rebound, one episode.
Traps:
- Category describes wind only; the cone shows the centre only, not the wind or water zone.
- A forecast landfall is not the landfall; early damage estimates are revised hard.

## Earthquake, tsunami, volcano
Anchor: hazards.earthquakes
Companions: hazards.earthquake_losses, hazards.impact_alerts, hazards.tsunami, hazards.shaking_at_point, hazards.volcanoes, hazards.volcanic_ash, hazards.volcano_alert_level, power.plants
Why together: Magnitude alone does not say damage; depth, distance to cities and population exposed do.
Methods (the answer names the one it uses):
- Loss alert level as the main damage gauge: the higher of the death and loss bands (red: 1,000 deaths or 1 billion USD and more); it is reissued as data arrive.
- Analogues: past events in the same zone with magnitude, depth and losses.
- Volcano: the ground alert level and the aviation colour code are separate.
Traps:
- First magnitudes are revised; early deaths and damage are undercounted.
- A tsunami threat is decided by the warning centre, not by the magnitude.

## Wildfire and smoke
Anchor: hazards.wildfires
Companions: hazards.official_warnings, weather.forecast, hazards.lightning, hazards.air_quality, hazards.air_quality_forecast, hazards.air_columns_satellite, hazards.wildfire_perimeters, power.grid_assets
Why together: Spread needs wind and humidity; damage depends on what is near; smoke spoils air far away.
Methods (the answer names the one it uses):
- Distance from detections to assets and wind toward them; detection count and radiative power day to day.
- Surface PM2.5 against the place's usual level and the WHO 24-hour guideline (15 ug/m3).
Traps:
- A detection is a thermal anomaly at a pixel centre, not a fire area: flares and industry trigger it, clouds hide fires, satellites pass a few times a day.
- A satellite gas column is not surface air; US and European air indexes use different scales.

## Space weather
Anchor: hazards.space_weather_scales
Companions: hazards.kp_index, hazards.flare_probabilities, logistics.aviation_advisories
Why together: Each scale maps to different systems: G to high-latitude grids, satellites and navigation; R to daylit radio and polar flights; S to radiation on polar routes and satellites.
Methods (the answer names the one it uses):
- Kp 5 is G1, up to Kp 9 at G5; about 1,700 G1 and 4 G5 events per 11-year cycle (NOAA SWPC scales).
Traps:
- A flare is not a storm: a storm follows in 1-3 days only after an Earth-directed mass ejection.

## Losses and insurance
Anchor: hazards.disaster_costs
Companions: hazards.insured_losses, hazards.impact_alerts, hazards.earthquake_losses, hazards.volcanoes
Why together: Economic loss, insured loss and deaths rank events differently.
Methods (the answer names the one it uses):
- Loss = intensity at each asset x exposure x vulnerability; insured loss after policy terms, separately.
- Parametric cover pays on an index trigger in about two weeks without assessing the loss; payout minus loss is basis risk.
Traps:
- An automatic alert level is not a loss in money; a loss total needs its publisher and date.
