# Crypto assets

## Coin prices and the crypto market
Anchor: crypto.price_history
Companions: crypto.price, crypto.market, crypto.stablecoin_supply, crypto.exchange_flows, crypto.hashrate, crypto.sentiment_index, crypto.derivatives, markets.indices
Why together: A coin moves with the whole crypto market and with liquidity; its move against the market separates the coin from the tide.
Methods (the answer names the one it uses):
- Windows in calendar days and UTC; name the quote currency (dollar or a stablecoin) and that prices differ by venue.
- Move in daily sigmas with sqrt(365), not 252.
- Against the market: change in total capitalisation and in bitcoin's share of it.
- Stablecoin supply growth as liquidity entering.
- Net exchange flows as a description only: no published link to later prices; an inflow is not selling.
- Hashrate as network health; a sentiment index as context only, a composite of others' inputs.
Traps:
- Market capitalisation = price x circulating supply, not money invested.
- Funding rates, open interest and liquidations are not in the data: leverage cannot be stated.
