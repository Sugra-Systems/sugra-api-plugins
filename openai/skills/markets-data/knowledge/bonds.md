# Bonds and credit as markets

## Yields, curve and credit spreads
Anchor: rates.treasury_10y
Companions: rates.treasury_2y, rates.spread_10y_2y, rates.real_yield_10y, expectations.inflation_market_5y, bonds.term_premium_10y, bonds.real_curve, fiscal.auction_results, liquidity.credit_spread_ig, bonds.credit_spread_bbb, bonds.credit_spread_baa, liquidity.credit_spread_hy, bonds.corporate_curve, rates.treasury_3m, rates.spread_10y_3m, rates.futures_path
Why together: Level, slope and the real part show what moves a yield; spreads show the price of risk; a weak auction can explain a rise better than news.
Methods (the answer names the one it uses):
- Nominal = real + breakeven; 10-year = expected average short rate over 10 years + term premium, a model estimate, not a quote.
- A day's change in bp against the usual daily change of that yield (standard deviation of daily changes over a year).
- Auction demand (bid-to-cover, accepted yield against the yield just before) against past auctions of the same maturity.
- A spread against its own history as a percentile, in bp.
- Price change of a bond is about minus duration x yield change: prices fall when yields rise.
Traps:
- A spread change in percent instead of bp; the real curve comes weekly, not daily.
- Investment grade, BBB and high yield are different spreads: name the one quoted.
