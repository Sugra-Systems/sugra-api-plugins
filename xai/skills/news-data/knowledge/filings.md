# Filings and disclosures

## Company disclosures
Anchor: filings.material_events
Companions: filings.press_releases, filings.filing_history, filings.filing_search, filings.disclosure_change, filings.earnings_transcript, filings.japan_filings, news.company_coverage
Why together: The filing is the primary record of what a company says happened; coverage tells who noticed, the press release what the company chose to stress.
Methods (the answer names the one it uses):
- A US current report declares item numbers, and the item is the event type: 1.01 material agreement, 1.03 bankruptcy or receivership, 1.05 material cybersecurity incident, 2.01 acquisition or disposal completed, 2.02 results, 5.02 officer or director change, 7.01 fair-disclosure statement, 8.01 other events. Name the item types searched; a type not searched is not absent. With the type unknown, search all items.
- Two dates: the event date the report states and the filing date, up to four business days later. Day 0 is the first session after the filing's acceptance time; an after-close filing moves it to the next session.
- An amendment (form with /A) revises an earlier filing: read both, count one event.
- A press release is the company's own words: primary for what the company said, not an independent check of it.
- Full-text search matches words: a hit in boilerplate, a risk factor or an exhibit list is not an event; read the passage.
- Disclosure change: a low year-over-year similarity of an annual-report section flags rewritten text, not its direction; read the changed section before calling it news.
- Japan files under its own system with dates in JST; convert to UTC.
Traps:
- A source holds a limited history; an older filing not returned is not absent.
- A transcript is what management said on the call, not audited figures.
Do not:
- Present a claim from a press release or a call as verified fact.
- Count an amendment or an exhibit refiled as a new event.
