# From concept to call

Each `<area>.yaml` maps a concept id to countries (`us`, `ez`, `gb`, `jp`, `cn`, `de`, `ca`, other ISO codes; `other` = only a country the concept does not list: a listed country always takes its own entry, never `other`). Fill placeholders from the question: `<ISO2>`, `<iso2>`, `<ISO3>`, `<year>`, `<bank>`.

## 1. Read the entry
- `op`: the operation id. `key` is a macro series `country/section`: call `macro_country_section` with params `country` and `section`, the two halves of the key (`us/unrate` is `country: us, section: unrate`), or pass the key as one series of `macro_multi`. `key` is never a parameter name. `series_id` goes to `fred_series_series_id`. `params` are fixed; add the window (section 3).
- `unit`: the unit of the value the call returns. `note`: how to read it.
- `gap` + `substitute`: the data are not in the catalog. Say so, then give the substitute, named as a substitute.
- `compute`: derive it from the concepts named, by the method in the knowledge file; label the result computed.

## 2. Batch and transform
- Fetch the anchor and companions in as few calls as possible: `macro_multi` takes up to 5 keys of one kind (all rates, all indexes or money, all counts). Split mixed kinds into separate calls; a failed series comes back under `errors` and the rest stands.
- One call per series: the level and every transform come back together, so ask all you need in one call, with the window of the longest need.
- Request only the transforms listed for the key (`transform`, comma-separated). By kind: `mom_pct`, `yoy_pct` for indexes, money and levels; `mom_pp`, `yoy_pp` for monthly rates; `dod_bps`, `wow_bps` for daily and weekly rates and spreads; `mom_abs`, `yoy_abs` for counts; `qoq_ann_pct` only on `us/gdp`, `us/real-gdp`, `eu/gdp`, `gb/gdp`, `jp/gdp`. The macro ops take these transforms only (not `lin`, `chg`, `pch` or `3m_ann`); a 3-month annualised rate of a monthly series is computed from levels (section 3).
- `mom_*` and `dod_bps` compare with the previous observation: the previous week on weekly data, the previous quarter on quarterly data. `wow_bps` spans 5 observations, so on weekly data the week change is `dod_bps`. `yoy_*` compare with a year earlier.
- Transform units: `*_pct` and `qoq_ann_pct` in pct, `*_pp` in pp, `*_bps` in bp, `*_abs` in the unit of the level.
- `fred_series_series_id`: `transforms` lists values of its `units` parameter, one call each: `pch` (on the previous observation), `pc1` (on a year earlier) and `pca` (annualised) return pct; `chg` and `ch1` return the change in the unit of the level. The level is the call without `units`.
- No transform listed: read the levels and compute the change yourself. This covers rates typed as levels, ratios, indexes centred on zero and balances that change sign.

## 3. Window
- Call every bound entry by its `op` through the generic operation call; never through a by-series shortcut tool (the keys here do not match its names). Parameters, all you need (do not describe these ops): `macro_country_section` `country`, `section`, `transform`, `last_n`, `start`, `end`, `order`; `macro_multi` `series`, `transform`, `last_n`, `start`, `end`, `order`; `fred_series_series_id` `series_id`, `units`, `limit`, `sort_order`, `observation_start`, `observation_end`, `frequency`, `aggregation_method`; `macro_releases` `release`, `upcoming`, `limit`, `start`, `end` (no country); `macro_cb_calendar_bank` `bank`. `macro_country_profile` takes `country` and a `latest` flag: keep `latest` at its default (`latest: false` asks for every indicator's whole history, more than one response holds).
- `macro_country_section` and `macro_multi`: `last_n` for the latest observations, `start` and `end` (YYYY-MM-DD) for a fixed period, `order`. `macro_multi` has `series` (comma list, up to 5), `transform`, those window parameters and nothing else: no `fields`.
- `fred_series_series_id` has no `last_n`. Latest points: `limit` with `sort_order: desc` (newest first). A history: `observation_start` and `observation_end`. A change: `units`.
- Size the window to the method, not the maximum: monthly 14 to 26 points, quarterly 8, daily or weekly 60 to 90 days (a year of daily points is 20k+ characters; for one rate over a long span prefer `fred_series_series_id` with `limit`). A long window is a larger answer, not a better one.
- Weekly data: ask `yoy_*` with `start` one year and 8 weeks back, not with `last_n`.
- A count or streak over a window (days below zero, months above a threshold) comes from ONE call that covers the whole window, never counts added from two calls: name the column counted and the first and last date, label it computed. Many rows to count by eye: take a coarser frequency (fred_series_series_id `frequency`) and say so.
- A 3- or 6-month annualised change needs at least 7 monthly observations; a year-on-year change needs 13.

## 4. Units
- `macro_country_profile`, `macro_indicators` and `ecb_yield_curve` return fractions (0.05 = 5 pct): multiply by 100 and say so.
- Convert every term to one unit before adding or subtracting (USD mn and USD bn mix in net liquidity).
- Money outside the US is `lcu`, `lcu_mn` or `lcu_bn`, currency in the note. Convert only with a named exchange rate and date.
- A unit or label in the response wins over the binding; report a mismatch.
- Licensed series (note says licensed): attribute to the rights holder named in the response, link, never reprint tables.

## 5. When a call fails
1. Retry once with the same parameters. An unknown-parameter error is not a transient fault: fix the parameter from section 3, do not retry as is. A response-too-large error means the window or list asked for exceeds what one response holds (the response cap the notes name): narrow the window or the limit, never retry as is.
2. Call the entry's `fallback`, if it has one.
3. Discover: `search_endpoints` with the concept name and country, `describe_endpoint` for the parameters, then call. If what it returns measures something else, name it a substitute.
4. Still nothing: report it (section 6).

## 6. Name the outcome
- "Not in the catalog": the entry is a gap; give the substitute.
- "Call failed": the call errored after the retry, the fallback and discovery; name the concept and the date asked.
- "Source stale": the latest observation is older than the concept's frequency plus its usual lag; give its date.
- Never fill a missing number with a default, a remembered figure or another country's series.

## 7. Known gaps - do not search for them
- Central-bank meeting dates cover the Fed, ECB, Bank of England, Bank of Japan, SNB and Riksbank only. Any other bank is a gap (the calendar bindings); never call the calendar with another bank.
- No first-print or vintage history of a US release, no consensus forecast for a US release. News and event search do not hold them either: do not search for them, say it is not in the catalog and give the substitute from the entry.
- A forecast edition is not guessed: use the latest edition, or the ones the entry names. A missing edition is a gap, not a reason to try other labels.
