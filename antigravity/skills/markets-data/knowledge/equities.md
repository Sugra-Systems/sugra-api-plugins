# Equities

## Earnings
Anchor: equities.earnings_surprise
Companions: equities.earnings_calendar, equities.estimates, equities.model_estimate, equities.income_statement, equities.ratios, equities.sector_percentile, equities.earnings_quality, volatility.implied_move, equities.earnings_event_study, equities.earnings_drift, filings.disclosure_change, filings.earnings_transcript
Why together: A report is judged against expectations, not zero; quality and peers separate a one-off from a trend.
Methods (the answer names the one it uses):
- Surprise = actual minus estimate, in percent of the absolute estimate; name whose estimate (analysts' mean or a model) and its date.
- Reaction = cumulative abnormal return over the report window, market model estimated before it; a report after the close moves the next session (day 0 and day +1).
- Actual move against the options-implied move for the first expiry after the report.
- Seasonal businesses: against the same quarter a year ago.
- Quality: published scores (F-score 0-9, accruals, M-score) as defined; a rewritten risk or discussion section is a flag, not a direction.
- Name N events; an interval that includes zero is "not distinguishable from zero on N events".
Traps:
- Reported (GAAP) against adjusted EPS unnamed; announcement date against fiscal quarter end.
- No P/E with losses, no EV/EBITDA for banks; trailing = the last four reported quarters.
- Post-earnings drift is gone in large stocks (Martineau 2022, sample 1984-2019): history, not a signal.

## Valuation and market regime
Anchor: equities.valuation_multiples
Companions: rates.real_yield_10y, volatility.market_implied, volatility.term_structure, equities.factor_returns, equities.sector_strength, markets.breadth, liquidity.financial_conditions, liquidity.credit_spread_hy
Why together: Valuation, volatility, factors and breadth describe a regime better than one number.
Methods (the answer names the one it uses):
- A multiple against its own history as a rank, period named.
- Rough equity risk premium = earnings yield minus real 10-year yield, labelled computed.
- Sector strength over a named window is a fact; "cycle phase -> sector" is a hypothesis (little gain even with perfect phase knowledge: Jacobsen, Stangl and Visaltanachoti 2007).
- Families vote: trend, momentum, volatility, volume each read alone, then "3 of 4 agree"; no weights.
Traps:
- The cyclically adjusted P/E (10 years of real earnings) is not trailing P/E; a multiple is not a timer.
