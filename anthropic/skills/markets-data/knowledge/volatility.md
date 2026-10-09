# Volatility and options

## Options on one security
Anchor: volatility.iv_surface
Companions: volatility.option_chain, volatility.iv_rank, volatility.skew, volatility.implied_move, volatility.put_call, volatility.unusual_volume, markets.realized_vol, equities.earnings_calendar
Why together: Implied against realized shows whether protection is dear; skew shows demand for downside cover; short-dated above long-dated shows an event or stress.
Methods (the answer names the one it uses):
- Implied minus realized over matching windows (30 days each), in volatility points.
- IV rank or percentile over the history held; its number of observations is part of the figure. Above 80 or below 20 is the usual threshold, a convention.
- Skew = 25-delta put IV minus 25-delta call IV; positive = downside cover dearer.
- One-sigma move = price x IV x sqrt(days / 365), labelled computed; not the straddle price.
- Put/call against its own history; volume and open interest apart.
Traps:
- Unusual volume does not say who bought or sold.
- IV is annualised, high before a scheduled event and falls after it.

## Market volatility
Anchor: volatility.market_implied
Companions: volatility.term_structure, markets.realized_vol, markets.indices, liquidity.financial_stress, liquidity.credit_spread_hy
Why together: Implied prices the expected move; realized volatility and spreads show whether stress spreads.
Methods (the answer names the one it uses):
- The large-cap US index's 30-day implied volatility in points (annualised percent); daily equivalent = level / sqrt(252); changes in points.
- Implied above realized is normal (index variance about 2.2 times realized: Bollerslev, Tauchen and Zhou 2009, 1990-2007); a narrowing or reversed gap is the reading.
- Term structure: short horizons below 3-6 months is normal; short above long marks stress or a near event.
- Level as a percentile over 10-20 years, dates named; never a crash forecast.
