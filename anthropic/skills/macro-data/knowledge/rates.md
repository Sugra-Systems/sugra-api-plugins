# Rates

## Policy rate and yield curve
Anchor: rates.policy_rate
Companions: calendar.cb_meetings, rates.effective_rate, rates.futures_path, expectations.cb_projections, rates.treasury_2y, rates.treasury_10y, rates.spread_10y_2y, rates.spread_10y_3m, rates.treasury_3m, rates.real_yield_10y, expectations.inflation_market_5y, rates.reserve_rate, rates.money_market_rate, rates.decision_odds
Why together: The 2-year yield tracks expected policy; the 10-year adds growth, inflation and the term premium. The futures path against the central bank's own projection shows where market and bank disagree.
Methods (the answer names the one it uses):
- Policy rate with the date of its last change and the next meeting; a target range is quoted with both bounds, and the effective rate shows where trading sits inside it.
- Futures-implied rate = 100 minus the futures price; read the path meeting by meeting against the bank's own projected path where it publishes one (Federal Reserve: the median of its participants' projections).
- Nominal 10-year = real 10-year + breakeven; breakeven = nominal minus real (computed).
- A decision-day move in bp against the usual daily move of the same yield.
- A change in a yield or rate over a day, a month or a year is the difference of the two levels in bp or pp, dated by the last day; read it from levels when the window is short.
- Slopes: 10-year minus 2-year, and 10-year minus 3-month (the input to recession models). Calling the curve inverted when the slope is below zero is a convention.
- Transmission: policy expectations, then the slope, real yields, credit spreads and financial conditions.
Traps:
- Name the one asked: the real yield is not the nominal one; the target is not the effective rate; a futures-implied rate is not the policy rate.
- Inversion is not a timer: the lag to recession is long and variable.
- A prediction-market price is not a consensus of economists; a futures price can carry a risk premium.
- Central banks set different instruments: a target range (Federal Reserve), the deposit facility rate (ECB), Bank Rate (Bank of England).
Do not:
- Give a percent change of a rate: changes in yields and spreads are in bp.
- Present a market-implied path as the central bank's plan.
