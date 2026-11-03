# Labour

## Unemployment, jobs and pay
Anchor: labour.unemployment_rate
Companions: labour.payrolls, labour.payrolls_first_print, labour.wage_growth_regular, labour.participation_rate, labour.participation_prime_age, labour.employment_population_prime_age, labour.average_pay, labour.job_openings, labour.quits_rate, labour.unemployed_level, labour.underemployment_rate, labour.employment_cost_index, labour.wage_growth_tracker, labour.conditions_index
Why together: Unemployment falls both when jobs grow and when people leave the labour force; only participation and employment tell which, and the 25-54 measures are free of population ageing. Openings and quits show labour demand and workers' confidence.
Reading order: UK (ONS): payrolled employees from tax data, the Labour Force Survey, vacancies, pay, claimant count; the latest three months against the previous three and a year earlier.
Methods (the answer names the one it uses):
- Payrolls: the headline is the monthly change in thousands, with the revisions to the two months before; the 3-month average change smooths noise. Computed from levels: (P_t - P_t-3) / 3, dated by the last month.
- A change in a rate over 1 or 12 months is the difference of the two levels in pp, not a percent change.
- Regular pay (UK) is pay excluding bonuses and is not the total pay series, whose growth the source reports directly. Regular pay growth is computed: the mean of the latest 3 months over the mean of the same 3 months a year earlier, minus 1; label it computed.
- Openings per unemployed: job openings over the number unemployed for the same reference month; above 1 means more openings than unemployed people.
- Real pay: pay growth minus inflation over the same 3 months or the same year, deflator named (UK real pay differs on CPIH and CPI; use the CPI that matches the question and say which).
- Name the pay measure: average hourly pay (moves with the mix of jobs), the employment cost index (fixed mix, quarterly), or the median change for the same people (Atlanta Fed tracker: the 3-month moving average, its headline, beside the 12-month moving average; job stayers and switchers apart).
- Conditions index (Kansas City Fed): level and momentum are two readings and can diverge.
- Underemployment: broad unemployment rate minus the headline rate. The broad rate (with involuntary part-time and marginally attached) is not the headline rate: name which one.
- Noise: a monthly change inside the publisher's 90 percent interval is within sampling error (US, per the BLS technical note: payrolls about 120 thousand, unemployment rate about 0.2 pp; the release states the current interval).
Traps:
- The household and payroll surveys are independent and can diverge for months: name the survey behind each figure. Openings and hires are aligned to the payroll survey, so their agreement confirms nothing.
- Payrolls are revised in the next two releases and again once a year.
- Average pay rises when low-paid jobs are lost (composition).
- Openings are a stock on the last business day of the month; hires and quits are flows over it. Openings arrive about a month after payrolls for the same month.
- The same-people tracker matches about 2,000 pairs a month and has no value for a month the survey was not run.
Do not:
- Explain a rise or fall in the unemployment rate without participation. A question for the rate and its change needs the anchor alone: the broad rate and the other companions only when slack is asked.
- Call a change within sampling error a rise or a fall.

## Jobless claims
Anchor: labour.initial_claims
Companions: labour.continuing_claims, labour.unemployment_rate, labour.payrolls
Why together: Claims are weekly and early; continuing claims show whether the laid-off find work; the monthly surveys confirm or not.
Reading order: US (DOL): initial claims with last week's revision, the 4-week average, then insured unemployment (continuing claims), one week behind.
Methods (the answer names the one it uses):
- Trend: the 4-week average against the same four weeks a year earlier.
- Continuing claims rising while initial claims are flat point to slower hiring, not more layoffs.
Traps:
- Holidays, storms and seasonal plant shutdowns distort single weeks.
- Last week's figure is revised: quote the revised number.
Do not:
- Read one week as a trend.

## Sahm rule
Anchor: labour.sahm_rule
Companions: labour.unemployment_rate, labour.unemployed_job_losers, labour.unemployed_entrants, labour.initial_claims, growth.real_consumption, growth.recession_dates
Why together: The rule uses one series and cannot say why unemployment rose; job losers against new entrants, claims and spending tell which.
Methods (the answer names the one it uses):
- Definition: the 3-month average unemployment rate minus the lowest 3-month average of the previous 12 months; threshold 0.50 pp.
- Name the version: first-release (each month as published then) or revised (recomputed on today's data). They can disagree at the threshold: 1976 crossed only as first published, 2003 only in the revised version.
- Give the value and its distance to 0.50 pp, not a flag; 0.49 and 0.51 are the same signal.
- Coincident, not leading: first readings of 0.50 came 2-4 months after the NBER peaks of 2001, 2007 and 2020.
- Before "recession", check causes: job losers and temporary layoffs against entrants and a growing labour force.
Traps:
- An empirical regularity, not a law; false alarms in 1959 and 1976.
- Temporary layoffs after a storm, an undercount of new immigrants in the household survey, or a missing survey month can move it.
Do not:
- Date or forecast a recession with it.
