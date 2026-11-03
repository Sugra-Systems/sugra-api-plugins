# Reading market prices

For every quoted instrument: stocks, funds, indexes, futures, currencies, coins. Fetch the anchor and only the companions the method needs; add a call only for a named gap.

## Rules
1. A price carries its as-of time: the session close (exchange time zone, session date) or an intraday time, and any delay. Outside the session the latest price is the last close: say so. Older than the last session is stale: give its time, never call it current.
2. Window returns use prices adjusted for dividends and splits (total return); levels, highs and lows are unadjusted. A split is a fall in an unadjusted series, not a move. Index levels are usually price return: name the kind.
3. Windows count trading days: about 21 a month, 252 a year (currencies about 260); coins trade daily, so their windows are calendar days in UTC. Name the first and last date.
4. Daily sigma = annualised volatility / sqrt(252); move in sigmas = return / daily sigma, labelled computed. Above 2 is unusual by convention, below 1 ordinary.
5. Abnormal return = return minus beta x market return (or minus the sector fund's return) over the same window, labelled approximate. Relative volume = volume / 20-day average: above 2 heavy, below 1 light, by convention; 1.0 is the average.
6. Yields, spreads and implied volatility change by differences (bp, pp, volatility points); prices and index levels in percent.
7. A price is in its quote currency. Return in another currency = (1 + local return) x (1 + currency return) - 1, rate and date named. Real return deflates by consumer prices over the same window, labelled computed.
8. Comparing instruments: one window, one base date, one kind of return, one currency; a missing one shows "no data".
9. A cause is named only for an event found inside the window before the move; otherwise list what was checked (market, sector, flows) and say no event was found. Coinciding is not causing.
10. A position (short interest, holdings, futures positions) is a stock on a date; a flow (short volume, fund flows, trades) covers a period. Never one for the other.
11. A disclosed figure has two dates, as of and made public; what was known on a day follows the second.

## Cannot know
- No price forecast, target, or buy, sell or hold. A directional question gets the evidence both ways and what to watch.
- An estimate (model, flow estimate, implied move) is called one and names its method. A published effect is a historical average with its sample end, not a prediction for one security.
- Stale, not published, missing and failed call are four different statements; never fill a gap with a remembered price.

## Price move of one security
Anchor: markets.price_history
Companions: markets.returns, markets.relative_volume, markets.realized_vol, markets.beta, markets.indices, equities.sector_strength, news.abnormal_return, filings.material_events, news.company_sentiment, equities.analyst_actions, volatility.implied_move, markets.corporate_actions, markets.trading_calendar, markets.price
Why together: "Up 3 percent" says nothing without the normal range, the market, the sector and volume.
Methods (the answer names the one it uses):
- Sigmas (rule 4), abnormal return and relative volume (rule 5).
- Actual move against the options-implied move for that date.
- Events in the window: filings, news, analyst actions; news after the close moves the next session (day 0 and day +1).
- Whole market: index levels and breadth (markets.breadth); without breadth, equal-weight against cap-weighted fund.
Traps:
- A return across an ex-dividend or split date on unadjusted prices.
- A renamed or reused ticker: resolve the company first.
- A holiday or half day is not a quiet day.
