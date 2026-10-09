# Weather

## Forecast, conditions and normal
Anchor: weather.forecast
Companions: weather.observation, weather.official_forecast, hazards.official_warnings, weather.history, climate.annual_series, weather.degree_days, weather.degree_day_normals, weather.model_run
Why together: A forecast is read against what is observed now, what the official service says, and the normal of the same window.
Methods (the answer names the one it uses):
- Computed normal: the same calendar window in each of the past 10 or 30 years at the point, labelled "computed, N years"; the anomaly against it.
- Degree days: cooling = sum of max(0, Tmean - base), heating = sum of max(0, base - Tmean), base named; a region weights its largest cities by population; against the same window of past years.
- Forecast change: two fetches at stated times; their gap is the revision.
Traps:
- The gridded history back to the 1940s is a reanalysis: close to stations on average, off at one station on one day.
- A daily mean hides the evening peak; a UTC-day maximum is not the local afternoon maximum.
- Degree days from the latest analysis are a one-day snapshot, not a forecast or a history.
Do not:
- Call a value hot, dry or extreme without the normal and its base period.
