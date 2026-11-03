# Prediction markets

## Event probabilities
Anchor: predictions.contract_price
Companions: predictions.price_history, predictions.open_interest, predictions.orderbook, rates.decision_odds, rates.futures_path
Why together: A probability is read with volume, open interest and spread: a thin market is noise.
Methods (the answer names the one it uses):
- Probability = price as a share of the payout, at the bid-ask midpoint; a wide spread is a range, not a point.
- Quote only after checking depth (volume, open interest, spread); an empty result is a valid answer.
- Change after an event; venues side by side, never averaged, each with its resolution rules.
- A base rate first where one exists.
Traps:
- A contract price is not a consensus of economists; resolution rules differ by venue.
