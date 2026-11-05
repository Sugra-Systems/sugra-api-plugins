# Crops

## Drought and harvest
Anchor: crops.condition
Companions: weather.growing_regions, weather.water_balance, weather.area_rainfall, hazards.drought_category, crops.soil_moisture, crops.vegetation_index, water.flow_percentile, crops.supply_demand, crops.export_sales, crops.yield_annual, commodities.futures_curve, trade.strait_transits, calendar.release_dates
Why together: Drought reaches prices through expected yield, where weather in flowering and grain fill outweighs the season average, and through transport (low rivers, canal transits).
Methods (the answer names the one it uses):
- Moisture deficit = precipitation minus reference evapotranspiration over the window, against the same sum in past years.
- Days above a named temperature in the critical window (US corn late June to late July, soybeans late July to late August).
- Drought categories are percentile bands, D2 (5th-10th) and worse the usual market threshold.
- Good-plus-excellent share against last week, last year and the five-year average for the same week; it explains about 85 percent of detrended US corn yield variation at the final rating but 8 at the first (farmdoc daily, University of Illinois, 1986-2016 sample).
- Report hours (ET): crop condition Monday 16:00, after the day session; balances 12:00, inside it; export sales Thursday 08:30.
Traps:
- One station for a district; drought outside the growth phase; a rating without its week number, revised the next week.
- A low river does not raise freight when exports are weak: demand decides.
- Annual yield by country is a trend, not a weekly rating.
