# Growth and cycle

## GDP and the current quarter
Anchor: growth.real_gdp
Companions: growth.gdp_contributions, growth.final_sales_private, growth.gdp_nowcast, growth.gdi, growth.real_consumption, growth.real_disposable_income, growth.saving_rate, growth.industrial_production, growth.manufacturing_output, growth.manufacturing_pmi, growth.capacity_utilisation, growth.retail_sales, growth.business_survey, growth.consumer_sentiment, growth.durable_goods_orders, growth.inventories_to_sales
Why together: GDP is quarterly, late and revised, so monthly data and nowcasts carry the current quarter. GDP and income measure output from two sides and are partly independent.
Methods (the answer names the one it uses):
- Name the growth basis: quarter on quarter annualised (as the US publishes), not annualised (euro area, UK), or from a year ago. Convert before comparing: annualised = ((1 + q/100)^4 - 1) * 100.
- Contributions in pp with signs (imports subtract); real final sales to private domestic purchasers as underlying demand; the three largest contributions.
- Nowcasts side by side; their spread is the uncertainty. Each comes with its date, next update, the release that moved it (it changes only when data come out) and its historical error against the first GDP estimate (Atlanta Fed model: mean absolute error under 1 pp, root mean square a little over 1 pp).
- Revision size: the mean absolute revision of US real growth is about 0.5 pp from the advance to the second estimate and 1.2 pp to the latest (BEA, 1999-2024).
- GDP against GDI: show the gap; their average is a third estimate only when labelled so.
- Business surveys: diffusion indexes and balances move in points; 50 (0 for a balance) is the no-change line. A purchasing managers' index above 50 is expansion; without it, manufacturing output over 3 and 12 months is the hard-data reading, named as a substitute.
- Whether a monthly change in sales or orders is a move depends on its sampling error.
Traps:
- US annualised growth set against unannualised euro area growth.
- A nowcast is a model without judgement, not data, and is not shown to beat professional forecasters.
- Nominal retail sales rise with prices: deflate before calling it volume. Earlier months are revised: quote the revised figures.
Do not:
- Call an estimate final: the US status runs advance, second, third, then annual revisions.

## Recession signals
Anchor: growth.recession_signals
Companions: labour.sahm_rule, rates.spread_10y_3m, growth.curve_recession_probability, growth.gdp_recession_index, growth.activity_index, growth.recession_probability, labour.initial_claims, liquidity.financial_conditions, liquidity.credit_spread_hy, growth.leading_index, liquidity.credit_gap, growth.recession_dates
Why together: No signal is reliable alone and each has its own lag; agreement across independent groups (labour, curve, activity, GDP, finance) weighs more than any one.
Methods (the answer names the one it uses):
- Count the signals firing, each with its threshold and group; indicators sharing inputs count once.
- Curve: 10-year minus 3-month below zero for three months or more, on monthly averages. The New York Fed model turns the spread into a 12-month-ahead recession probability: quote its published value, do not refit it.
- GDP-based recession index: above 67 signals a start, below 33 an end; published a quarter late and not revised.
- Chicago Fed activity index: 0 is trend growth; a 3-month average below -0.70 after an expansion signals recession.
- Sahm rule: version named (labour file).
- Composite leading indicator: above 100 and rising is expansion, falling is downturn; below 100 and falling is slowdown, rising is recovery.
- Credit-to-GDP gap: above 2 pp starts the countercyclical buffer, 10 pp sets its maximum (BIS guide).
- Lags to NBER peaks are measured, not assumed; NBER dates turning points months after the fact.
Traps:
- Curve inversion is not a timer: the lead has been long and variable.
- Financial conditions and stress indexes centre on zero: a percent change is meaningless; read the level and the change in points.
- Model probabilities and composites built on overlapping inputs do not confirm each other.
Do not:
- Give a dated recession forecast; report signals, thresholds and lags.
