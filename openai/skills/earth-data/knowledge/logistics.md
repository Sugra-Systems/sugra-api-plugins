# Logistics

## Shipping, ports and straits
Anchor: logistics.port_calls_deviation
Companions: trade.strait_transits, logistics.port_activity, logistics.port_disruptions, water.waves, hazards.tropical_cyclones, logistics.freight_rates
Why together: A delay or a drop in calls is checked for weather first, then for an event, then for demand.
Methods (the answer names the one it uses):
- Transits over a week against the same weeks of past years; port calls in units of the port's own spread.
Traps:
- Vessel counts without tonnage; one week as a trend.

## Aviation
Anchor: logistics.airport_weather
Companions: logistics.aviation_delays, logistics.aviation_advisories, logistics.disruption_risk, hazards.volcanic_ash
Why together: Observed weather, the aerodrome forecast and delay programmes in force answer "will there be delays".
Methods (the answer names the one it uses):
- Visibility and cloud base below minimums at peak departure hours; crosswind; thunderstorms nearby; destination and connecting airports too.
Traps:
- Airport reports are in UTC; delay programmes are not run in every country; a computed risk index is not an official notice.
