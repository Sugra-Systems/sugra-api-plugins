# Liquidity and financial conditions

## Central bank liquidity and money
Anchor: liquidity.cb_balance_sheet
Companions: liquidity.treasury_account, liquidity.reverse_repo, liquidity.net_liquidity, liquidity.regime, rates.reserve_rate, liquidity.money_supply, prices.cpi, liquidity.money_market_funds, liquidity.bank_credit, liquidity.consumer_credit, liquidity.consumer_credit_revolving
Why together: Liquidity reaching markets depends on what drains it (the Treasury's account, reverse repo) as much as on the balance sheet; money and credit show whether it reaches the economy.
Methods (the answer names the one it uses):
- Net liquidity = central bank assets minus the Treasury account minus reverse repo: a market heuristic, not an official measure; labelled computed.
- Change over 13 weeks rather than one week; weekly balance sheet data hold both Wednesday levels and week averages: use one kind.
- Net liquidity change over 13 weeks: the level now minus the level 13 weeks earlier, each from the same kind of weekly figure, in one unit.
- Overall direction: liquidity, credit conditions and the policy rate each vote by the sign of their 13-week change against a noise band; two votes the same way set the direction, otherwise neutral. A heuristic: give the label with each vote and its date.
- Real money: money supply deflated by CPI, beside the nominal.
- Consumer credit (Federal Reserve G.19): seasonally adjusted growth at an annual rate; the latest month is preliminary; the quarterly or 3-month rate beside it; revolving apart from nonrevolving (total minus revolving). Annualised monthly change from levels: ((L_t / L_t-1)^12 - 1) * 100, labelled computed. Fetch the anchor and only the companions the question names; a question on one measure does not need the others.
Traps:
- Consumer credit excludes loans secured by real estate.
- A methodology change, such as a new group of lenders added, makes a jump that is not new lending.
- Nominal money growth read without inflation.
Do not:
- Present net liquidity as an official statistic.

## Credit and financial conditions
Anchor: liquidity.financial_conditions
Companions: liquidity.financial_stress, liquidity.credit_spread_hy, liquidity.credit_spread_ig, rates.real_yield_10y, liquidity.bank_credit, liquidity.credit_gap
Why together: Conditions indexes summarise spreads, volatility, leverage and funding; spreads and real yields show which part is moving.
Methods (the answer names the one it uses):
- Index level against 0 (average conditions): above 0 is tighter or more stressed than average; the change in points.
- Several signals voting (conditions index, spreads, real yield, credit growth) rather than one.
- Spreads in bp against their own history (rank over 10-20 years).
Traps:
- Near-zero indexes: a percent change is meaningless.
- Some versions remove the influence of the business cycle and inflation: say which version.
Do not:
- Read one week's move as a change of regime.
