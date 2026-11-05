# Prices

## Inflation
Anchor: prices.cpi
Companions: prices.cpi_core, prices.pce, prices.pce_core, prices.cpi_median, prices.cpi_trimmed_mean, prices.cpi_sticky, prices.cpi_shelter, prices.cpi_ex_shelter, prices.cpi_rent, prices.cpi_oer, housing.market_rent, prices.cpi_food, prices.cpi_energy, prices.cpi_goods, prices.cpi_services, prices.ppi, prices.import_prices, prices.crude_oil, prices.gasoline, prices.unit_labour_costs, prices.cpi_nsa, expectations.inflation_household, expectations.inflation_market_5y, expectations.inflation_model, rates.policy_rate, rates.real_yield_10y
Why together: Headline against core separates food and energy noise; median, trimmed mean and sticky prices show whether price rises are broad; shelter lags market rents. Expectations show whether inflation stays anchored, and the real policy rate whether policy is tight.
Reading order: Euro area (ECB): headline, energy and food, core, goods and services, wages, unit labour costs and profits, expectations, projections. Australia (ABS): annual headline, trimmed mean, monthly unadjusted and adjusted, excluding volatile items, contributions in pp.
Methods (the answer names the one it uses):
- Side by side: from the previous month, from a year ago, and 3- and 6-month annualised; name a base effect when the month a year earlier was unusual.
- Contributions: in pp with signs; the three largest plus one core measure.
- Breadth: median, trimmed mean and sticky prices against headline.
- Target: each central bank on its own index (Federal Reserve: PCE; ECB: HICP; Bank of England: CPI); the gap to target in pp.
- Real policy rate: ex post = policy rate minus inflation from a year ago; ex ante = policy rate minus expected inflation of the same horizon, or the inflation-indexed yield. Labelled computed, both series named.
- Expectations side by side, each named by kind: household survey, model, market.
- 12-month rate from an index: I_t / I_t-12 - 1. From 12 monthly rates: the product of (1 + r) over the 12 months, minus 1, labelled computed; the sum of the monthly rates is not it.
- Average of a rate over a few months: the mean of those monthly figures, over the matching months of the other measure when they are compared.
- Indexation and contracts use the unadjusted index; US seasonal factors are revised for five years each February.
Traps:
- Core differs by country: US excludes food and energy, with median and trimmed mean beside it; euro area excludes energy, food, alcohol and tobacco; UK reports CPI and CPIH (with owner-occupier housing costs); Japan excludes fresh food, and fresh food and energy; Canada prefers trim (20 percent cut from each tail) and median (common is heavily revised); Australia the trimmed mean. Levels across countries need that caveat.
- One month annualised is not a rate from a year ago; a 3-month annualised rate of a monthly index is not quarterly growth.
- Market-implied inflation includes risk and liquidity premia; household expectations follow gasoline prices.
- CPI shelter covers all existing leases, so it lags new-lease rents.
- Tokyo CPI comes out before the national index: a leading measure, not national data. The euro area flash gives the headline and main aggregates; full detail comes mid-month.
- A monthly change is not the 12-month rate; a measure that includes owner-occupier housing is not the plain consumer price index. Name which was read.
Do not:
- Quote more decimals than the publisher (CPI is published to one decimal).
- Treat PCE and CPI inflation as one measure: weights and coverage differ.
