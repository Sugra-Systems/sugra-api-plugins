# Reading macro data

Companions are listed most useful first: fetch the anchor and only those your method needs; add a call only for a named gap.

## Rules
1. Name the kind of change: level, from the previous period, from a year ago, or annualised over 3 or 6 months, computed from levels: ((I_t / I_t-3)^4 - 1) * 100 and ((I_t / I_t-6)^2 - 1) * 100, labelled computed. The previous period shows momentum, a year ago the level of the rate; 3 and 6 months smooth noise and turn sooner than a year.
2. Seasonality: change from the previous month only on seasonally adjusted (SA) data; read unadjusted (NSA) data against a year ago.
3. A real figure names its deflator.
4. Give the reference period and the release date, plus the next release (calendar.release_dates, calendar.cb_meetings). Quarterly data arrive weeks after the quarter, annual data months after; a release date inferred from past dates is labelled estimated.
5. First estimates are provisional; a revised series is not what was known on release day (expectations.data_vintages). Name the status: flash, advance, second, third, revised; unknown is "unknown", never "final".
6. Compare three ways: with trend (3-6 months), with expectations (named, whose), with history (rank over 10-20 years).
7. A date in a series is the first day of its period: a quarterly date in October is the fourth quarter. The latest period is the latest the source holds; report it as is with its lag, and do not chase other series to find a newer one.
8. A change, an average or a window names its last observation and the base it is measured from.
9. Quote the series the question names, with its look-alike labelled as such if you add it: the broad and the narrow unemployment rate, total and regular pay, the monthly change and the 12-month rate, the real and the nominal yield, the survey and the model expectation, the target and the effective rate. A neighbour in the answer is never given as the figure asked.
10. A change inside the publisher's sampling error is not a move: say "within sampling error" and give the 3-month trend.

## Presenting
- Each figure: reference month or quarter (not the release date), SA or NSA, kind of change, real or nominal, estimate status, and for non-daily data the usual frequency and lag, even when not stale.
- Changes in rates and spreads in pp or bp, never percent. No monthly against quarterly without aggregating. No more decimals than the publisher.
- Dated anchors (month and year), never "last month". A release time (publisher's zone and UTC) only when set against news or prices.
- No "high" or "weak" without a number and a base; a threshold that is a convention says so.
- Fact, inference and assumption apart; timing alone is "coincided with", not "because of".
- A missing number is named for what it is: not published, stale, or a failed call; never a neutral default.
- Conflicting sources side by side with dates, never averaged. "Within normal range" is a result too: show value and threshold.
- Order: conclusion, figures, comparison, companions that confirm or contradict (name a contradiction), limits (revisions, sampling error, dates differing by country). Length follows the question. A directional answer ends with what to watch next and the strongest counter-reading.

## Expectations, consensus and revisions
Anchor: expectations.release_consensus
Companions: expectations.professional_survey, expectations.inflation_household, expectations.inflation_market_5y, expectations.inflation_model, expectations.cb_projections, international.official_forecasts, expectations.data_vintages
Why together: "Above or below expectations" and "how it was revised" say more than a bare number, but each comparator is a different kind of expectation.
Methods (the answer names the one it uses):
- Name the comparator's kind: professional survey, household survey, market, model, official forecast, or the series' own trend. None is a consensus without grounds; with no comparator say "against trend", not "surprise".
- Surprise = actual minus the named comparator; standardised, divided by the standard deviation of past surprises.
- Forecast revision between editions; first estimate against the latest.
- A model or official forecast carries the average historical error for its horizon, called that, not an interval; a gap smaller than that error is no disagreement.
Traps:
- A consensus without whose.
- Market-implied expectations carry risk and liquidity premia; a prediction-market price is not a consensus of economists.
- The market's reaction to a surprise depends on the cycle phase, known only in hindsight.
Do not:
- Average forecasts from different sources into one number.
