# Commodities

## Oil and gas
Anchor: prices.crude_oil
Companions: commodities.crude_stocks, commodities.futures_curve, commodities.futures_history, positioning.futures_positions, commodities.natgas_price, commodities.natgas_storage, commodities.product_stocks, commodities.crack_spread, prices.gasoline, commodities.energy_outlook, weather.degree_days, trade.strait_transits, industry.offshore_shut_in, expectations.release_consensus
Why together: Price against stocks and curve shape separates shortage from expectations; gas follows weather, oil logistics.
Methods (the answer names the one it uses):
- Stocks against the 5-year average for the same week (the usual convention); with too little history, the same week a year ago.
- Backwardation (near above far) = tight now, contango = surplus; first-to-second contract spread.
- 3-2-1 crack = (2 x gasoline + diesel - 3 x crude) / 3, dollars a barrel; products per gallon x 42.
- Gas: degree days against normal; a daily price for a daily event, not the monthly average.
- A weekly report against a named expectation; with none, against the seasonal norm, never "surprise".
Traps:
- Brent and the US benchmark are two prices; a contract names its delivery month (front against next, rolls).

## Farm goods and metals
Anchor: commodities.futures_curve
Companions: commodities.futures_history, positioning.futures_positions, crops.supply_demand, commodities.monthly_prices, commodities.farm_prices_annual, commodities.gold, rates.real_yield_10y, fx.effective
Why together: Harvest and price link through weather in growth phases and through stocks.
Methods (the answer names the one it uses):
- Price against weather in the crop's critical window (corn pollination, midsummer); outside it weather matters little.
- Stocks-to-use from the official balance; old crop against new crop on the curve.
- Gold against the real 10-year yield and the dollar's effective rate.
Traps:
- Annual farm prices or monthly world averages are not market quotes; contract units differ (cents a bushel, dollars a troy ounce).
