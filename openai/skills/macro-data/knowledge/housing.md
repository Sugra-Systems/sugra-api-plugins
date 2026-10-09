# Housing

## Construction
Anchor: housing.starts
Companions: housing.permits, housing.mortgage_rate, housing.months_supply
Why together: Permits lead starts; the mortgage rate drives demand; months' supply shows whether builders will add or cut.
Methods (the answer names the one it uses):
- Monthly figures are seasonally adjusted annual rates: compare them with the same series, never with an annual count.
- Use the publisher's interval: a change whose interval includes zero is not significant.
- Read the trend over the publisher's window: 3 months for permits, longer for starts.
- Single-family apart from multifamily, which is lumpy.
Traps:
- Starts swing with storms and harsh winters and are noisier than permits.
Do not:
- Call one month's change a trend when its interval includes zero.

## Prices, sales and affordability
Anchor: housing.repeat_sales_index
Companions: housing.median_price, housing.existing_sales, housing.months_supply, housing.affordability, housing.mortgage_rate, housing.market_rent, prices.cpi_shelter, housing.property_prices_intl
Why together: The mortgage rate drives affordability, then sales, and prices with a lag; months' supply shows the balance between buyers and sellers.
Methods (the answer names the one it uses):
- Price change from the repeat-sales index (the same homes over time); the median price for what buyers paid.
- Months' supply: about six months is balance, by industry convention for existing homes.
- Affordability index: 100 means a median income just qualifies for a median-priced home; higher is more affordable.
- Mortgage rate: weekly change in bp, and its spread over the 10-year yield.
- Rents: new-lease (market) rents lead CPI shelter.
- Across countries: harmonised residential property price indexes, real (deflated by CPI) or nominal, named.
Traps:
- The median price moves with the mix of homes sold (season, region, size); the repeat-sales index does not.
- New-home supply counts homes not yet built or not finished; existing-home supply does not.
- Sales and prices are seasonal: compare with a year ago or use adjusted series.
- The repeat-sales index comes about two months after its reference month.
Do not:
- Read a fall in the median price as a price decline without the repeat-sales index.
