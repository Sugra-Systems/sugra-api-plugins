# Currencies

## Exchange rates
Anchor: fx.spot
Companions: fx.reference_rate, fx.effective, fx.rate_differential, rates.treasury_2y, rates.policy_rate, calendar.cb_meetings, positioning.futures_positions, fx.implied_vol, trade.trade_balance
Why together: Rate gaps and expected policy move a currency; the effective rate separates a currency's strength from one pair.
Methods (the answer names the one it uses):
- Quote direction first: EUR/USD 1.10 = 1.10 dollars per euro, a rise is a stronger euro. The inverse is 1/x; its percent change is not the negative of the original.
- Cross rate = two rates against one base, divided, same date and fixing, labelled computed.
- The pair's change against the change in the 2-year yield gap over the same window.
- Carry = rate gap / realized volatility of the pair, beside speculators' positions; carry is prone to sudden unwinds (Brunnermeier, Nagel and Pedersen 2008, 8 currencies to 2006).
- Effective (trade-weighted) against bilateral; the real effective rate deflates by relative prices.
- Central bank decision day: the move against the usual daily move.
Traps:
- A reference rate is a once-a-day fixing (the euro reference near 16:00 Central European Time), not a market close; holidays are missing days.
- Implied currency volatility missing: name realized volatility as realized.
Do not:
- Read one pair as "the dollar's strength".
