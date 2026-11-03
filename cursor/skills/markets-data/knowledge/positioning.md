# Positioning: holders, shorts, flows

Each figure names its as-of date and its publication date (the usual lags are in the concept registry).

## Insiders and holders
Anchor: positioning.insider_transactions
Companions: positioning.insider_net_buying, positioning.insider_history_3y, positioning.blockholders, positioning.institutional_holdings, positioning.holders_summary, positioning.congress_trades
Why together: Open-market buys say more than sales, opportunistic trades more than routine, several insiders more than one.
Methods (the answer names the one it uses):
- Open-market purchases (P) and sales (S) only; exercises, grants and tax withholding (M, A, F) are pay.
- Routine = same month in each of the 3 prior years, else opportunistic; with less history, unclassified, say why.
- Cluster: 3 or more insiders buying within 30 days (a convention); size against the prior holding.
- Net buying = 100 x (buys - sells) / (buys + sells), open market.
- The 10b5-1 plan flag (required since April 2023) is a fact, not a reason to drop a trade.
Traps:
- 13F as current holdings: a quarter-end, long-only book, 45-135 days old.
- Congressional trades come weeks late; an empty history does not prove no trades.
- Record: opportunistic buys and clusters preceded excess returns; routine trades and sales little (Cohen, Malloy and Pomorski 2012, sample 1986-2007).

## Short positions
Anchor: positioning.short_interest
Companions: positioning.days_to_cover, positioning.short_pct_float, equities.float_shares, markets.price_history, positioning.short_volume, positioning.fails_to_deliver, positioning.borrow_fee, positioning.uk_short_disclosures
Why together: Days to cover joins the position to liquidity; share of float shows crowding.
Methods (the answer names the one it uses):
- Share of float = short interest / float shares; float shares = float value / price on its date, approximate.
- Days to cover = short interest / 20-session average volume, a rank among peers or in its history, not a threshold; more days = harder to close.
- Change between two reports; a jump in fails to deliver hints at borrowing trouble.
Traps:
- Daily short volume is not short interest: off-exchange only, market-maker sales included, so above half is normal.
- Borrow cost is not in the data: say so.

## Fund flows and futures positions
Anchor: positioning.etf_flows
Companions: positioning.market_fund_flows, positioning.etf_holdings, positioning.futures_positions, positioning.futures_percentile
Why together: Who buys, and how crowded one side is.
Methods (the answer names the one it uses):
- Flow = change in shares outstanding x net asset value: an estimate between filings.
- 4-13 weeks against one week; beyond 2 standard deviations of 12 periods is large, by convention.
- Speculators' net futures position as a 3-5 year percentile describes, it does not signal reversal; open interest growth has the better record (Hong and Yogo 2012, commodity futures 1965-2008).
- Commercial traders hedge: their position is not a view.
