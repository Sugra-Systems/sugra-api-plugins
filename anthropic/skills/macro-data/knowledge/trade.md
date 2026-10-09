# Trade

## Trade and tariffs
Anchor: trade.trade_balance
Companions: trade.exports, trade.imports, trade.bilateral_flows, trade.tariff_rates, trade.trade_measures, prices.import_prices, trade.strait_transits
Why together: A balance moves with exports, imports and prices; tariffs are checked through rates and flows, not statements.
Methods (the answer names the one it uses):
- The change in a balance is a difference in currency units, never a percent: a balance can change sign.
- Volume against value: deflate by trade prices before calling a change real.
- Tariffs: the applied rate by product line, then the flows of those lines before and after the date it took effect.
- Bilateral: a partner's exports to a country and that country's imports from the partner differ (valuation, timing, re-exports); name whose record.
- Shipping: strait and canal transits against the same weeks a year earlier.
Traps:
- Imports jump ahead of a tariff date and fall back after: read several months.
- Monthly trade is revised; balance-of-payments and customs bases differ.
Do not:
- Read an announcement as a tariff in force.
