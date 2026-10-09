# Fiscal

## Budget, debt and auctions
Anchor: fiscal.budget_balance
Companions: fiscal.debt, fiscal.debt_to_gdp, fiscal.deficit_to_gdp, fiscal.interest_outlays, fiscal.auction_results, rates.treasury_10y
Why together: A deficit is read against the size of the economy and the cost of financing it; auctions show how easily the debt is absorbed.
Methods (the answer names the one it uses):
- Fiscal year to date against the same months a year earlier (US fiscal year: October to September), never one month alone.
- Adjust for payments shifted by weekends and holidays, naming who made the adjustment (the Congressional Budget Office publishes one for the US).
- Debt and deficit as a percent of GDP, with interest outlays beside them as a share of revenue or GDP.
- Auctions: bid-to-cover, the gap between the high and median accepted yields, and the shares of bidder classes, each against recent auctions of the same maturity.
- For a rolling deficit, name the window (fiscal year, 12 months) and the source.
Traps:
- The monthly balance is not seasonally adjusted and swings with tax dates.
- A series that changes sign takes a difference in currency units, not a percent change.
- Gross debt includes debt held by government accounts; debt held by the public does not. Name which.
Do not:
- Compare one month's deficit with the month before.
