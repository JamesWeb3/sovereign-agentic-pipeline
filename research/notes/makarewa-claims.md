# Makarewa data centre — reading notes

Working notes on the Southland/Makarewa controversy: one section per source read, then
the cross-source contradictions, then the analysis layer. Sources themselves live in
`../sources/`; these are the distillation, not the record.

**Contents**

- Reading notes, one section per source, in the order they were read
- [Contradiction table](#contradiction-table) — the cross-source conflicts and their status
- [Analysis layer](#analysis-layer) — which objections survive the documents
- [Source analysis](#source-analysis) — per-source findings keyed by source id, moved out of
  `../sources/` so those files hold only frontmatter, verbatim quotes and claim IDs

## Datagrid Makarewa fast-track application

Source: `growth-first/datagrid-fasttrack-application-2024-05` · camp: growth-first · 2 May 2024

- Applicant's self-interested framing.
- This is an application from someone who wishes to implement a data centre in Southland and states the intention, details, resources and constraints involved in building it.
- Intention of the Data Centre is to attract hyperscale and other data centre developers to carry out work in Southland.
- The capacity of the Data Centre Park could reach over 240MW of IT load (application).
- NZ power generation is 82% renewable whilst transitioning to a low carbon economy. Checked against MBIE: the Jan–Mar 2024 quarter sat at 85.7%, so the application's figure is ~3.7 points lower. Not necessarily wrong — most likely a different basis (an annual figure rather than a quarterly one, or an older year). Establish the basis and period before this enters the graph. See contradiction table.
- Timing: the MBIE Jan–Mar 2024 figure was published ~June 2024, a month *after* this application was filed (2 May 2024), so the applicant could not have used it. The most recent quarterly available at filing was the December 2023 quarter (released ~March 2024), reported as 90.3% — **not yet verified against the source PDF**. 82% is lower than both candidates, so there is no figure it matches. Open question: verify the December 2023 number, then check MBIE's *annual* figures for 2021–2023, where low-80s values are plausible and would explain it without anything untoward.
- Water Use was not stated directly in the source, will have to look further if he actually said anything
- 49 hectares of land area are proposed for data centre development.

## RNZ, post-approval coverage

Source: `neutral/rnz-second-largest-drain-2026-03` · camp: neutral · 17 March 2026

- Almost a 2 year gap between the proposition/application compared to the opinions being given out
- 'It will apparently be the country's second biggest user of electricity after the Tiwai Point aluminium smelter.'
- 84 Emergency generators, each containing a 10,000 litre diesel tank and a 15m high exhaust stack.
- 550 workers are expected on site
- 50 staff are only required to keep it going
- Given a large contact energy wind farm just 50 kilometres away
- Personally supported by the Southland Mayor (Rob Scott)
- Mayor and political figures are likely to support more due to the potential growth it will bring to the economy whilst certain groups of civilians attached to the land are to disapprove of the idea and create massive rallies of disapproval.

## 1News, community questions

Source: `neutral/1news-community-questions-2026-07` · camp: neutral · 23 July 2026

- 'I don't know if we've got the amount of available electricity that they want' - Invercargill Citizen on an Interview
- Claims that it would use southland's colder climate for cooling rather than groundwater.
- Rob Scott proposes it's worth it to challenge rules and regulations due to the pace/growth of AI
- Mercury bought a 12% stake for $53m and signed a 140MW (Mercury) long-term PPA in March
- The data centre would open at 2028
- Material would be a climate-first source if cited direct material from Kelly Blomfield, Southland Sustainable Resource Coalition.
- From RNZ: 12m-high noise barriers over 9.5ha on a 48-ha property, and the mayor's actual consultation quotes.

## Environment Southland consent documents

Source: `official/es-consent-water-2026` · camp: official · 13 March 2026
- Consent was granted WITHOUT public notification
- Was not publicly notified as it was argued that it was assessed as having no more than 'minor environmental effects'
- Directly affected parties were consulted and gave written approval: tāngata tiaki of the
  Ōreti Mātaitai, Invercargill City Council, the Department of Conservation, and landowners
  with potentially affected bores
- Nine consents were granted, AUTH-20252550-01 to -09. The list below was previously
  incomplete here: it omitted the operational groundwater take (03) and the wetland
  removal (05), which are the two that matter most.
  - (01) Discharge treated wastewater to land from an amenities block
  - (02) Discharge contaminants to air from diesel generators
  - **(03) Take and use groundwater** — the operational take, for cooling and potable supply
  - (04) Take groundwater to dewater a construction area
  - **(05) Remove a wetland**
  - (06) Occupy the coastal marine area with a datacable
  - (07) Install a datacable in the coastal marine area
  - (08) Discharge water from dewatering of a site
  - (09) Earthworks in proximity of a wetland
- The tenth authorisation people sometimes count is Southland District Council's land use
  consent, a different authority. See `official/sdc-s104-decision-2026-03`.


## Contradiction table

Conflicting values — figures where two sources give different numbers for the same fact.

| Claim | Value A | Value B | Notes |
| --- | --- | --- | --- |
| Construction jobs | "up to 550" (RNZ, Mar) | 1,200 (1News, Jul) | **Closed. Three different quantities, all correct.** `abley-transport-assessment-2025-08`: "Up to 550 staff may be present on the site during the peak construction period" - concurrent on-site headcount, sized for 400 car parks. Datagrid's release claims "Over 1,200 skilled and technical jobs" - total roles over the build. `insight-economics-makarewa-2025-07`: 5,751 annual jobs / 5,387 FTEs - national, direct plus indirect, onsite and offsite. Nobody contradicted anybody; three sources answered three questions. |
| Permanent staff | ~50 (RNZ) | 80 (1News) | **Closed, and my earlier "resolved in favour of 80" was wrong.** `abley-transport-assessment-2025-08` gives three figures: the park "will employ between 60 - 100 staff", with "Up to 45 staff on site at any one time" (5 admin, 10 security, 5 ops management, up to 26 ops). RNZ's ~50 tracks the 45 concurrent; 1News's 80 tracks Alfatech's "average daily workforce of 80" via `insight-economics-makarewa-2025-07`. Both are right about different quantities - concurrent on site vs total employed. |
| Site footprint | 49 ha = 43 owned + ~6 in OIO (application) | "48-ha property" (RNZ) | **Both may undercount.** `sdc-s104-decision-2026-03` consents six titles across *three* addresses — 342 and 370 Flora Road East plus 63 Taylor Road, Lorneville. Every other source describes a two-address site. Component areas given: 9.5ha datahalls, ~4ha GXP substation, 18.66ha planting. Establish whether the 48/49ha figures cover the Taylor Road title at all. |
| National electricity share | Datagrid alone "about six per cent of our country's total electricity supply" (Greens, 26 Jul 2026) | ALL data centres 0.6% now, ~3% by 2030 (Energy Minister Simeon Brown, 9 Aug 2026) | **The Greens' arithmetic checks out; the conflict is real and is about *when*.** Against `mbie-energy-in-nz-2025` (40,002 GWh consumed in 2024, the most recent annual), 280 MW running flat out is 2,453 GWh = **6.1% of national consumption**. So "about six per cent" is sound for a fully built, fully loaded Makarewa. Brown's 0.6% is data centres *operating now*, when Makarewa is not built. His 3% by 2030 is the number that cannot stand beside the Greens' 6%, unless it excludes Makarewa or assumes it is far from full load. That is the question to put to MBIE or the minister's office. |
| Renewable share | 82% (application) | 85.7% (MBIE, Jan–Mar 2024) | **Closed. 82% is MBIE's calendar-2021 annual figure, one edition stale at filing.** `mbie-energy-in-nz-2022`: "Electricity generated from renewable sources this year was 82.1 per cent of total generation". At filing on 2 May 2024 the latest annual was Energy in New Zealand 2023 (August 2023), covering 2022 at 87%; the 2024 edition (88.0% for 2023) was not published until September 2024. So the applicant quoted a real MBIE figure that was one edition out of date. Note it *understates* the renewable share — a conservative error, not a flattering one. |

Disputed characterisations — competing accounts of the same events, not competing measurements.

| Question | Applicant / council | Opposing party | Notes |
| --- | --- | --- | --- |
| Was consultation adequate? | Mayor: "done it right" | Coalition: meeting alone, applicant absent | Resolvable on the record — who attended, and when. |

What each row still needs:

- **Construction jobs** — closed. `abley-transport-assessment-2025-08` supplied the missing basis.
- **Permanent staff** — closed, by the same source.
- **Site footprint** — reconcile the Taylor Road title against the 48/49ha figures. The LINZ
  OIO decision records 42.8167ha acquired at 370 Flora Road East, which should settle the
  "43 owned" half. Not yet read.
- **National electricity share** — open, and the sharpest row in the table. Needs MBIE
  generation data.
- **Renewable share** — closed by `mbie-energy-in-nz-2022`.
- **Consultation** — needs an attendance record.

MBIE's annual series is now in the corpus (`mbie-energy-in-nz-2022`,
`mbie-energy-in-nz-2024`), which closed the renewable-share row and supplies the national
denominator for the electricity-share row.

A new row belongs here once someone reads the Marshall Day noise assessment: the s104
consents a datacentre that "will breach a nighttime noise limit", and low-frequency noise is
one of the two grounds for the consent review now before Southland District Council.

## Analysis layer

Each entry names the source it comes from and, where technical, the document that settles it.
The point of the layer is to separate objections that survive contact with the consent
documents from those that do not. Written against 18 sources as at 2026-09-04; entries move
between sections as evidence arrives, and several below are explicitly provisional.

### Technically sound objections

**1. The public was excluded by design, not by oversight.**
Both consents were non-notified. `sdc-s104-decision-2026-03` disposes of the question in one
sentence: "No matters have arisen in the assessment of this application which would indicate
that the application ought to have been notified." `es-consent-water-2026` assessed effects as
"no more than minor" and consulted only directly affected parties. There was no public
submission process at any point. This is not a characterisation — it is what both decisions
say, and it is why `sources/climate-first/` was empty until a political party spoke.

**2. Two independent experts could not find the consent documents.**
`smc-expert-reaction-2026-03`, published two days after the grant. Dr Helen Rutter, senior
hydrogeologist: "I haven't been able to find the Environment Southland resource consent."
Dr Daniel Collins, hydrologist: "It is not apparent to me how much water would be abstracted
and discharged." If qualified specialists asked for public comment could not locate the
documents, "the process was opaque in practice" is established fact rather than grievance.

**3. A policy threshold was exceeded and then set aside.**
`es-consent-water-2026`: drawdown on bores E46/0002, E46/0960 and E46/0342 exceeds the 20%
allowed by Policy 31 RWP and Policy 22 pSWLP. The commissioner grants it anyway, conceding
that "written approval does not necessarily overcome a policy exceedance" before deciding the
effect "can be disregarded". A fourth bore at about 27% drawdown is set aside because the
owners say they do not use it. An objection that effects thresholds were waived is supported
by the decision's own reasoning.

**4. The cold-climate cooling claim is false as stated.**
Three regulator statements say water-based cooling. `sdc-s104-decision-2026-03`: "Cooling plant
will utilise adiabatic cooling." `es-consent-water-2026` decision: the system "is designed to
reduce heat through evaporation of water." AUTH-20252550-03 is granted for "cooling water and
potable supply", capped at 220,752,000 litres a year. Any claim that Southland's climate
removes the need for groundwater is contradicted by the consents.

**5. There is a second, larger water take that nobody reports.**
AUTH-20252550-04: 321,408,000 litres in total for construction dewatering at 60 L/s over about
two months, against 220,752,000 L/year for operations. Every news story covers the operational
figure and none covers this one.

**6. The consent authorises a nighttime noise breach.**
`sdc-s104-decision-2026-03` lists among the consents sought "Operation of datacentre which will
breach a nighttime noise limit". Whether the acoustic assessment behind it was adequate is what
the s128 review will decide, but the SSRC's objection has a documentary basis: the council
consented a breach. Provisional pending the Marshall Day assessment, which nobody has read.

**7. Coolant-laden wastewater is unaccounted for.**
Rutter flags "coolant laden" wastewater from the fast-track application, with "no information
as to treatment or discharge". The only wastewater consent in the corpus is AUTH-20252550-01,
up to 5 m3/day from an amenities block, likened in the decision to 2-3 large households.
Either it is dealt with in a document nobody has read, or the adiabatic system does not
produce it, or it is unconsented. Open.

### Not technically sound objections

**1. "The jobs numbers are inconsistent, so someone is lying."**
They are three different quantities, all correct. `abley-transport-assessment-2025-08`: "Up to
550 staff may be present on the site during the peak construction period" - concurrent
headcount. `datagrid-resource-consent-pr-2026-03`: "Over 1,200 skilled and technical jobs" -
total roles over the build. `insight-economics-makarewa-2025-07`: 5,751 annual jobs including
indirect, national. A category error, not deceit.

**2. "The permanent staffing figures contradict each other."**
Same pattern. Abley: 60-100 employed, "up to 45 staff on site at any one time". Insight, via
Alfatech: an average daily workforce of 80. RNZ's ~50 tracks the concurrent figure and 1News's
80 the total.

**3. "The applicant understated renewables at 82% to flatter its case."**
`mbie-electricity-tables-2026` gives 82.15% for calendar 2021 - a real MBIE figure. It was one
annual edition out of date at filing, when the current figure was 87%. Note the direction: 82%
*understates* the renewable share. An applicant shading the numbers would have used the higher
one. Staleness, not spin.

**4. "The take will drain Southland's groundwater."**
`es-consent-water-2026`: allocation from the zone including this take is "less than 9 % of the
allocation limit", and under 10% even if the dewatering and operational takes fell in the same
water year. `smc-expert-reaction-2026-03`, Collins, independent: "Southland is relatively
water-rich, has lower water resource demand... this places Southland among the better locations
for a data centre in Aotearoa." The objection does not survive its own best expert.

**5. "It will raise household power bills."**
Not sound *or* unsound on this evidence - the corpus contains no analysis either way. Speidel
notes international experience of data centres "driving power and land prices up"; Brown
frames policy around avoiding bill increases. Both are assertions. Listed here so it is not
mistaken for an established objection.

### Growth-first arguments

**1. Economic scale, from the applicant's own modelling.**
`insight-economics-makarewa-2025-07`: over a three-year build, $2.53b to national GDP, $1.48b
in wages, 5,751 annual jobs, $380m one-off GST. Operationally $36m GDP a year, $12m wages,
about $5.5m GST. These are input-output multiplier estimates, national and including indirect
effects - a modelled projection, not a measurement.

**2. The consented figures are worst-case caps, not expected operation.**
`rnz-datagrid-pledges-2026-08`, Benjamin Black: "initially we have to come up with what's
called the maximum set of effects, assuming the worst case for everything... That's how you end
up with some pretty terrifying numbers." Datagrid now expects under 66 million litres a year
against 220 million consented, and fewer than 34 generators against 84 permitted. The mechanism
is real and it explains several apparent contradictions. It is also unenforceable: a consent
ceiling binds, an expectation does not.

**3. Southland is genuinely well suited, on independent evidence.**
Collins again, who is not connected to the applicant: relatively water-rich, low competing
demand, significant local generation at Manapouri.

**4. Strategic and competitive case.**
`smc-expert-reaction-2026-03`, Professor Albert Bifet: "If New Zealand wants to stay competitive
in AI, we will need more infrastructure like this." Professor Nirmal Nair: New Zealand "is still
an attractive place to build AI loads supported by our current and growing electricity
generation". Minister James Meager, in `teaomaori-makarewa-wai-2026-07`: "the exact sort of
infrastructure the South Island should be competing for".

**5. The applicant says it chose the harder consenting route.**
`rnz-datagrid-pledges-2026-08`, Galasso: "They proposed to me the Fast-track process... I said,
'thank you, but no thank you.'" Weakened by `datagrid-fasttrack-application-2024-05`, which is
Datagrid's own fast-track application. Reconcilable - apply in 2024, take the standard route in
2026 - but unresolved, and it is the applicant contradicting his own filing.

### Climate-first arguments

**1. The scale of the electricity draw is real and now verified.**
280 MW at full load is 2,453 GWh a year. Against `mbie-electricity-tables-2026`, that is 6.13%
of 2023 national consumption and 6.04% of 2025 - so the Green Party's "about six per cent"
holds against every year in MBIE's series. One consented site, six per cent of a country's
electricity.

**2. The renewable share is not a fixed property of Southland.**
MBIE's series: 88.13% in 2023, 85.50% in 2024, 88.46% in 2025. It moves several points on
hydrology alone. "Green power" without a year attached is not a claim that can be checked, and
a large new load on a hydro-dependent grid interacts with what Collins calls "Aotearoa's
electricity generation dry-winter problem".

**3. Displacement, not direct emissions, is the climate mechanism.**
Speidel puts it precisely: hydro use here contributes to warming "indirectly, perhaps, if the
hydro power used by the data centre displaces power that would have headed north and then needs
to be generated elsewhere using fossil fuels". This is the strongest version of the emissions
argument and the corpus cannot yet settle it - it needs generation dispatch modelling, not a
consent document.

**4. The benefits may not land where the costs do.**
Dowell: "local communities may provide the land, energy and enabling infrastructure, while much
of the strategic control and commercial value remains concentrated elsewhere." Speidel from the
network side: the Tasman Ring cable "tells us that the main market for the new Data Centre is
likely to be Australia." Set against Insight's $2.53b national GDP figure, this is a real
disagreement about what the project is for, not about what it measures.

**5. The jobs asymmetry is structural.**
Thousands during construction, up to 45 on site at any one time thereafter. Both Speidel and
Dowell make the same point independently: "the long-term workforce is typically small once
construction is complete". Not an objection to the figures, an objection to which figure the
public debate has been conducted in.

**6. There is no national framework, and there was none when this was consented.**
`1news-brown-underwrite-generation-2026-08`: the Energy Minister is "getting some policy advice
around what that looks like". No cabinet paper, discussion document or consultation exists.
`es-consent-water-2026` states the regulator's own limits: "Environment Southland is not a
construction or energy regulator and does not have any regional rules relating to the use of
generated electricity." Nobody assessed the electricity question because no one had the job.
This is the Greens' actual argument and it is the hardest to answer.

### What would change these classifications

- The **Marshall Day noise assessment** would move objection 6 from provisional to settled
  either way, and is the evidentiary heart of the s128 review.
- The **SSRC request as lodged** would let the objectors' case be assessed on its own terms
  rather than through the council's summary of it.
- **Generation dispatch modelling** is the only thing that can resolve climate-first argument 3.
  Nothing in the current corpus can.
- A **household price analysis** would decide whether the price objection belongs in either list.



## Figures from the Datagrid consent release not yet captured verbatim
Source: `datagrid-resource-consent-pr-2026-03` - https://www.datagrid.nz/pr1-rc/resourceconsent

Moved out of the source file: these are paraphrase, and paraphrase belongs here. Each needs
the release's own sentence captured before it can back a Claim.

- Power draw of 280MW, described as making Datagrid the country's second-largest electricity
  user after the Tiwai Point aluminium smelter. Most urgent of the three: it contradicts
  "over 240MW of IT load" in the 2024 fast-track application, and nobody has recorded how the
  release actually words it.
- Approval for the Tasman Ring Network landing at Oreti Beach, described as the first
  international subsea cable to the South Island. The 2024 application calls the cable
  Te Waipounamu - renamed, or a different component, unresolved.
- Consent granted 11 March 2026 by three councils - Southland District Council, Environment
  Southland, and Invercargill City Council - covering the Makarewa campus and the subsea
  cable landing at Oreti Beach.


## Source analysis

Moved out of `research/sources/` on 2026-09-03: source files hold frontmatter, a summary,
verbatim quotes and claim IDs only. All analysis, flags and follow-ups live here, keyed by
source id.


### `1news-community-questions-2026-07`

#### The contested claim worth modelling

`claim-makarewa-consultation-adequate` is directly disputed between sources. In
`rnz-second-largest-drain-2026-03` the same mayor says the community was consulted and
listened to. Here, a residents' group is holding its own meetings because it feels it
was not, and the applicant did not attend. Same Claim, two Sources, opposite positions.
A spreadsheet loses this. The graph is what makes it queryable.


### `datagrid-fasttrack-application-2024-05`

#### Two things worth flagging

**The capex is withheld.** Both cost figures in the application are redacted as
`s 9(2)(b)(ii)` (commercially sensitive, Official Information Act). So every dollar figure
in the media coverage comes from somewhere other than this document, and should be traced
to whoever actually said it. Do not attribute a cost to the application.

**"240MW of IT load" is not the same quantity as the 280MW reported in coverage.** IT load
is the compute draw, excluding cooling and overheads; a facility's grid draw is higher.
Before either number goes in the graph as `claim-makarewa-power-draw`, establish which
quantity each source is measuring. This is exactly the kind of thing the graph is for.


### `datagrid-resource-consent-pr-2026-03`

#### Four things worth flagging

**280MW is Datagrid's own figure, not a media invention.** The 2024 fast-track application
says "over 240MW of IT load"; this says 280MW. Both are the applicant's own numbers, two
years apart. They are probably different quantities (IT load excludes cooling and overheads)
*and* different vintages. Establish which is which before either enters
`claim-makarewa-power-draw`.

**The 1,200 jobs figure predates RNZ's 550.** This release is 11 March 2026;
`rnz-second-largest-drain-2026-03` reports "up to 550 workers" on 17 March 2026. The larger
number came *first*, so the discrepancy is not a scale-up over time. The surviving
explanation is a difference in basis — total jobs created over the build versus peak
concurrent headcount on site.

**The CEO named here is Remi Galasso.** The 2024 application
(`datagrid-fasttrack-application-2024-05`) names Perrine Dhalluin as CEO. Either leadership
changed between 2024 and 2026, or the two hold different roles. Do not merge them into one
`:Person` node until this is resolved.

**The cable has a different name.** "Tasman Ring Network" here; "Te Waipounamu" in the 2024
application. Same cable renamed, or a different component — unresolved.


### `es-consent-water-2026`

#### Documents not yet read

- `Redacted - s95-95G Recommending Report APP-20252550.pdf` (26.5 MB) — the notification decision
- `Datagrid NZ Partnership Ltd - PDP Groundwater Take_Rev3.pdf` (33 MB) — the applicant's take assessment
- `Datagrid_Makarewa_Review of Groundwater Assessment.pdf` (282 KB) — ES review of the above
- `Data NZ Limited Partnership - Cultural impact Assessment.pdf` (1.6 MB)

The reported figure that Datagrid **expects to use ~66 million litres a year, 70% less than
consented**, does not appear anywhere in the decision or in the permits. It is an operator
statement made at a public meeting five months after these consents were granted, and it is
not traceable to this source. It has its own file: `rnz-datagrid-pledges-2026-08`.


### `rnz-datagrid-pledges-2026-08`

#### Five things worth flagging

**The 66m figure is weaker evidence than the 220m it is set against.** 220,752,000 L/year is a
binding condition in a signed permit (`es-consent-water-2026`, AUTH-20252550-03). 66 million is
RNZ paraphrasing a spoken remark at a chamber meeting. Both belong on
`claim-makarewa-water-take` — James is explicit that neither should be deleted — but the graph
should record *what kind* of quantity each is. A consent ceiling and an operator's forecast are
different promises: one is enforceable, the other is not.

**66 million is almost exactly 30% of the consent limit.** 220,752,000 x 0.30 = 66,225,600.
The figure appears to be derived from the consent ceiling rather than measured or modelled
independently, which is consistent with "70% less than consented" being the actual claim and
"66 million" being its arithmetic restatement.

**Black's worst-case framing may resolve several contradiction-table rows at once.** If
consented conditions are "the maximum set of effects, assuming the worst case", then the same
mechanism may explain the 84 vs 34 generators, and possibly the jobs and footprint conflicts.
Worth testing against those rows rather than treating each as a separate discrepancy.

**Galasso says he refused fast-track, but the corpus holds his fast-track application.**
`datagrid-fasttrack-application-2024-05` is a fast-track approval application filed by Datagrid
in May 2024. Probably reconcilable — applied for fast-track listing in 2024, then took the
standard RMA route for the consents actually granted in 2026 — but as stated the two conflict,
and it is the applicant contradicting his own filing. Do not let either stand unqualified.

**Capex has moved again: $5b here, $3.5b in `1news-community-questions-2026-07` (July 2026).**
One month apart. Same pattern as the power draw (240MW / 280MW) and the jobs figures.

#### Not verified — do not use

Search-engine summaries attributed a stronger claim to Datagrid — that it would use **no**
groundwater, relying entirely on free air cooling with rainwater harvesting for "occasional
evaporative adiabatic assist". That wording does **not** appear in this RNZ article, which says
only that the company "had pledged to rely primarily on rainwater". If that stronger claim is
wanted, find where it actually came from first. Note it would also sit against the commissioner's
decision, which says the cooling system "is designed to reduce heat through evaporation of water".


### `rnz-second-largest-drain-2026-03`

#### Note on the jobs figures

This source says "up to 550 workers" on site during construction and "about 50 staff" to
run it. `1news-community-questions-2026-07` reports 1200 and 80 for what appear to be the
same two quantities, four months later. Both are in the graph; neither is deleted. Load
them as two Numbers evidencing the same Claim and let the contradiction be visible, then
find out which is right and why it changed.


### `teaomaori-makarewa-wai-2026-07`

#### Three things worth flagging

**The consent was non-notified, and that reframes the consultation dispute.** The argument
between the mayor and the residents' coalition in `rnz-second-largest-drain-2026-03` and
`1news-community-questions-2026-07` is not about whether consultation was thorough — it is
that there was no statutory public submission process at all. The mayor's "they've consulted
the community" describes voluntary engagement. `claim-makarewa-consultation-adequate` should
be modelled with this underneath it.

**Consultation splits into two different questions.** Iwi *were* notified; the public was
not. Those are separate facts with separate answers, and collapsing them loses the finding.

**Groundwater is used, not avoided.** Any note that the site relies on Southland's cold
climate *instead of* groundwater is wrong: it draws 220m litres a year and recirculates it.
Cold-climate cooling and groundwater use are not alternatives here.

#### Still missing behind this

This is coverage, not the consent. The 220m litre figure traces to a reporter reading the
consents, not to the consents themselves — `businessdesk.co.nz` reported the same figure and
is paywalled. The authoritative source is Environment Southland's water take consent, which
was not published because the application was non-notified. LGOIMA request pending.

#### Leads this opens

The three rūnanga named above, Minister James Meager, and Dr Karaitiana Taiuru all have
their own material, which would be primary rather than reported. The rūnanga in particular
are a dimension this corpus currently lacks entirely.


### `insight-economics-makarewa-2025-07`

#### What this settles, and what it does not

**It is the origin of the jobs numbers, and it disowns both reported ones.** Its construction
figures are multiplier estimates of national employment - 5,751 annual jobs, 3,050 of them
direct - and section 6.2 is explicit that even "direct" spans onsite and offsite work. Nothing
in it is a count of people at Makarewa. 550 and 1,200 are therefore not rival estimates of
this quantity; they answer a different question, from a document nobody has found yet.

**The permanent-staff row is closed.** 80 jobs / 72.3 FTEs at full build-out, sourced from
Alfatech. Written July 2025, so it predates RNZ's ~50 by eight months and 1News's 80 by a
year.

> **Superseded.** The conclusion originally drawn here — that 1News was right and RNZ's ~50
> unsupported — was wrong. `abley-transport-assessment-2025-08` gives 60–100 employed and
> "up to 45 staff on site at any one time". Both figures were right about different
> quantities. See the Abley section below.

**It is the applicant's consultant, and should be read as such.** Prepared for Datagrid,
by Insight Economics, and lodged in support of the consent application. `camp: growth-first`.
The disclaimer accepts no liability for actions arising from its contents.

### `sdc-s104-decision-2026-03`

#### Three findings

**The site is larger than any other source says.** Six titles, three addresses - 342 and 370
Flora Road East *and* 63 Taylor Road, Lorneville. The entire corpus, including Datagrid's own
release, describes a two-address site of 48-49ha.

**The cooling is adiabatic, which is the third regulator statement against the cold-climate
framing.** SDC: "Cooling plant will utilise adiabatic cooling to provide efficiencies in water
supply and power usage". ES decision: "designed to reduce heat through evaporation of water".
ES permit AUTH-20252550-03: granted for "cooling water and potable supply".

**But potable water is rainwater by condition, not groundwater.** Condition OP7 requires
onsite rainwater collection with 150m3 of tank storage for potable supply. That sits against
the ES groundwater permit, whose stated purpose includes potable supply. Two regulators, two
different accounts of where drinking water comes from - worth resolving before either backs a
Claim.

**Timing correction.** SDC decided 5 March 2026; ES granted 11 March 2026. Datagrid's release
(`datagrid-resource-consent-pr-2026-03`, 11 March) presents consent from three councils as a
single event. It was not.


### `abley-transport-assessment-2025-08`

#### It is the origin of every workforce number, and it dissolves both jobs rows

Because a transport assessment has to size car parks and model peak-hour flows, it states
on-site headcount directly - the one thing neither the economic assessment nor any council
document does. "Up to 550 staff may be present on the site during the peak construction
period" is where RNZ's 550 comes from. It is concurrent headcount, not total roles.

Set the three construction figures side by side and the contradiction disappears: 550
concurrent on site (Abley), "over 1,200 skilled and technical jobs" over the build
(Datagrid's release), 5,751 annual jobs nationally including indirect (Insight Economics).
Three questions, three answers.

**Correction to my earlier note.** I recorded the permanent-staff row as resolved in favour
of 80 and RNZ's ~50 as unsupported. Abley shows otherwise: "Up to 45 staff on site at any one
time", against 60-100 employed in total. RNZ's ~50 is the concurrent figure; 1News's 80 is
the total. Neither was wrong.

### `sdc-review-request-2026-08`

#### The live challenge, and who is making it

The objector has a name and a legal route: the **Southland Sustainable Resources Coalition**
lodged a s128 review request on 27 July 2026, relying on Condition GEN4. The grounds are
entirely acoustic - methodology, low-frequency noise and infrasound, noise source
identification, baseline monitoring, the unspecified ground factor for sound propagation, and
whether the existing conditions suffice.

**This does not fill the climate-first folder.** The report is SDC's, summarising SSRC's case
rather than reproducing it. The SSRC request as lodged is the document that would, and it is
not on the council's page. Worth asking for.

**The council had its own dates wrong.** The report body says the consent was granted 11 March
2026 with the review period expiring 11 September; a post-meeting note corrects both to 5
March and 5 September, explaining that the 11 March dates belong to the Environment Southland
consents. That confirms the 5 March 2026 decision date read off the s104 signature block, and
it means the decision on whether to review is due **5 September 2026**.

**A noise row belongs in the contradiction table** once someone reads Marshall Day: the s104
consents a datacentre that "will breach a nighttime noise limit", and SSRC's case is that the
assessment underpinning that was inadequate.


### `smc-expert-reaction-2026-03`

#### The experts could not find the documents

The most consequential thing in this source is not an opinion but an admission of fact, twice
over, from people qualified to read the consents. Dr Helen Rutter, a senior hydrogeologist:
"I haven't been able to find the Environment Southland resource consent which might contain
some of the above details." Dr Daniel Collins, hydrologist: "It is not apparent to me how much
water would be abstracted and discharged."

Both were commenting on 13 March 2026, two days after the consents were granted. The permits
carrying those numbers - 7 L/s, 604,800 L/day, 220,752,000 L/year - were published by
Environment Southland on 13 March, the same day. Two subject-matter experts asked for public
comment could not locate what a search now returns in minutes.

That is the sharpest available evidence of what non-notification meant in practice, and it is
worth more than any campaigner's characterisation of the same thing. It also justifies the
premise of this repository better than anything else in the corpus.

#### A discharge nobody has accounted for

Rutter flags "coolant laden" wastewater from the fast-track application, with "no information
as to treatment or discharge". The corpus holds AUTH-20252550-01, which consents up to 5 m3/day
of *treated wastewater from an amenities block* - sinks, showers and toilets, described in the
decision as equivalent to 2-3 large households. Nothing in the nine Environment Southland
consents obviously covers coolant-laden process water.

Either it is dealt with somewhere unread - the PDP air discharge or environmental management
plan documents - or the adiabatic system does not produce it, or it is genuinely unconsented.
Worth resolving: it is a discharge question raised by a hydrogeologist and not visibly answered
in any decision document.

#### Two independent voices on the jobs question

Speidel: "There's a few jobs during construction but generally very few thereafter because most
of the operation is automated and remote controlled from places with a larger pool of IT staff."
Dowell: "the long-term workforce is typically small once construction is complete". Neither
gives a number, so neither contradicts Abley's 60-100 employed or Insight's 80 - but both frame
the operational figure as the one that matters, against a public debate conducted almost
entirely in construction numbers.

#### Where the value lands - the repository's own question

Dowell puts the sovereignty argument in its sharpest form: "local communities may provide the
land, energy and enabling infrastructure, while much of the strategic control and commercial
value remains concentrated elsewhere." Speidel reaches the same place from the network side:
the Tasman Ring cable "tells us that the main market for the new Data Centre is likely to be
Australia." Set against Insight Economics' $2.53b national GDP contribution, that is a genuine
disagreement about what the project is for, not about what it measures.


### `1news-brown-underwrite-generation-2026-08`

#### There is no government data centre policy to cite

> **Correction, 2026-09-15.** This conclusion was right as at 9 August and is now out of date. `greens-national-policy-response-2026-08` shows Prime Minister Christopher Luxon announced a data centre proposal on **14 August 2026**, including a requirement for new "firmed energy". The Greens say it is silent on whether that firming must be renewable, on community engagement in consenting, and on water standards. The announcement itself is not yet in the corpus and should be: a beehive.govt.nz release from 14 August would be the primary source, and would test the Greens' characterisation of it.

Chased on 2026-09-03 and it does not exist as a document. What exists: the Prime Minister on
27 July 2026 directing Nicola Willis and DPMC to develop principles ("I want to be able to get
all the interests that are in that space to come back with some sensible, common-sense rules"),
and Simeon Brown on 9 August saying "we're getting some policy advice around what that looks
like". No cabinet paper, no discussion document, no consultation, nothing on beehive.govt.nz,
DPMC or MBIE that a search surfaces.

That is itself the finding. Datagrid is consented, built and under construction; the Greens
want a moratorium; SSRC is seeking a s128 review - and the national framework all of them are
arguing about has not been written. The two concepts the government has named are
"additionality" (large centres must bring new generation rather than draw on the existing grid)
and a "compact" setting the terms of entry. Both are aspirations, not rules.

#### The 6% question

The Greens say Makarewa alone will use "about six per cent of our country's total electricity
supply". Brown says data centres in total are 0.6% now and head for about 3% by 2030. Those
cannot both be true as stated, and both are on the record within a fortnight of each other.
This is a better test of the graph than the water figures, because unlike 220m vs 66m there is
no "different quantity" reading that obviously rescues both. Resolving it needs MBIE generation
statistics, which the corpus still lacks entirely.


### `mbie-energy-in-nz-2022` and `mbie-energy-in-nz-2024`

#### The 82% is real, and it is three years old

MBIE's annual publication for calendar 2021 records the renewable share of electricity
generation as 82.1 per cent. That is the only published New Zealand figure matching the
fast-track application's "82%", and it settles a question this file has carried open since the
first reading note.

The timing matters. The application was filed 2 May 2024. Energy in New Zealand 2023, published
August 2023 and covering calendar 2022, put the share at 87 per cent — that was the current
edition at filing. The 88.0 per cent figure for 2023 was not published until September 2024,
four months after filing.

So the applicant used a genuine MBIE figure one edition out of date. Worth being fair about the
direction of the error: 82.1% *understates* New Zealand's renewable share against both the
then-current 87% and the later 88%. An applicant shading the numbers in its own favour would
have used the higher figure. This looks like staleness, not spin, and the source file should
say so.

#### The national denominator, and what it does to the 6% claim

Energy in New Zealand 2024 gives 2023 totals: **43,488 GWh generated**, **39,130 GWh consumed**,
88.0 per cent renewable, with industrial consumption at 12,903 GWh.

Run the Greens' claim against it. 280 MW × 8,760 hours = 2,453 GWh a year at full utilisation —
5.6% of generation, 6.3% of consumption. At 240 MW of IT load the figures are 4.8% and 5.4%.
"About six per cent of our country's total electricity supply" is therefore arithmetically
sound for a completed Makarewa running hard, measured against consumption.

That sharpens rather than dissolves the conflict with the Energy Minister. Brown's 0.6% is
plainly today's operating fleet, which does not include an unbuilt Makarewa. His **3% by 2030**
is the figure that cannot sit beside the Greens' 6% for one site, unless it excludes Makarewa
or assumes a low load factor. Both numbers are also projections rather than measurements, and
the graph should record them as such.

#### A caveat on these two sources

Both are `type: report`, not `type: dataset`. Energy in New Zealand is a statistical publication,
and the honest label for a PDF of commentary and charts is a report. MBIE does publish the
underlying data tables as spreadsheets, and those would be the genuine `dataset` source — worth
adding when someone needs a full time series rather than the handful of figures quoted here.

Also note MBIE sits behind Imperva bot protection: the HTML pages and `/dmsdocument/` links
refuse automated fetches, while direct `/assets/*.pdf` links work. Anyone re-checking these
should expect the landing pages to fail and go to the PDFs.

#### The 2025 edition, and a tighter check on the 6%

`mbie-energy-in-nz-2025` (published August 2025, covering calendar 2024) is the current annual
and the denominator to use. National consumption was **40,002 GWh** in 2024.

280 MW x 8,760 hours = 2,453 GWh, which is **6.13 per cent** of that. The Greens' "about six
per cent of our country's total electricity supply" is not a rhetorical flourish; it is what
the arithmetic gives for a completed Makarewa running at full load, against the most recent
published national figure. Record it as a projection all the same - the site does not open
until 2028.

The same edition weakens a different argument. The renewable share **fell to 85.5 per cent in
2024, down 2.6 points from 88.1 per cent in 2023**, on low hydro. Southland's renewable
electricity is the applicant's central environmental claim, and MBIE's own series shows the
national share moving several points on hydrology alone. Any "green power" claim needs a year
attached to it.

One inconsistency worth noting: `mbie-energy-in-nz-2024` gives the 2023 renewable share as
88.0 per cent in its summary and 88.1 per cent in the body; `mbie-energy-in-nz-2025` reports it
as 88.1. A tenth of a point, but the graph should carry one value with its source, not both.

#### The spreadsheet tables — retrieved 2026-09-04

Karl downloaded them by hand; they are in `data/raw/` (gitignored) and registered in
`data/README.md`. `mbie-electricity-tables-2026` is now the corpus's first `type: dataset`
source, and it is the authoritative version of figures that until now came from PDFs
describing them.

Three things came out of it:

**The application's 82% is 2021, at 82.15 per cent** — confirmed to two decimals from the
series itself rather than inferred from a publication's prose.

**The 88.0 / 88.1 discrepancy resolves to 88.1.** The table gives 88.13 for 2023, so the 2024
publication's body was right and its summary rounded down.

**A figure this corpus already cites has since been revised.** `mbie-energy-in-nz-2024` gives
2023 national consumption as 39,130 GWh; the current table gives 40,004 GWh (estimated sales)
or 40,067.6 GWh (actual sales). Generation for 2023 also moved, 43,488 to 43,592 GWh. The
workbook's Revisions sheet attributes it to methodology improvements for residential and
transport consumption. Worth carrying into the graph design: a Number needs a vintage as well
as a value, because the same official figure for the same year changes between publications.

The Makarewa share holds against the corrected denominators — 280 MW at full load is 2,453
GWh, which is 6.14% of 2022 consumption, 6.13% of 2023, 6.12% of 2024 and 6.04% of 2025. The
Greens' "about six per cent" survives every year in the series.

#### The original blocked-retrieval note, kept for the record

MBIE publishes quarterly XLSX data tables on its electricity statistics and renewables
statistics pages, which would be a genuine `type: dataset` source rather than these `report`
PDFs. They could not be fetched: MBIE's HTML sits behind Imperva bot protection and refuses
automated requests, including with a cookie jar and a browser user agent. Only direct
`/assets/*.pdf` links pass, and guessing XLSX asset paths returned 404s.

Retrieving them needs a human with a browser. The pages are:

- Electricity statistics: https://www.mbie.govt.nz/building-and-energy/energy-and-natural-resources/energy-statistics-and-modelling/energy-statistics/electricity-statistics
- Renewables statistics: https://www.mbie.govt.nz/building-and-energy/energy-and-natural-resources/energy-statistics-and-modelling/energy-statistics/renewables-statistics

MBIE also lists `energyinfo@mbie.govt.nz` for data queries. That is now also the address for
**licence terms**: neither workbook states any, and `data/README.md` requires redistribution
rights to be confirmed before any derived table is committed to a public repo.

