# Who Gets to Decide?

### AI, the Public Ledger, and the Problem of Legitimacy

> *If AI can make society richer, smarter, and more capable while consuming enormous public resources and making some people economically disposable, who gets to decide whether that trade is worth it?*

**Draft for paper development — assembled from talking points, four research briefs (Gemini/agy), and two Perplexity deep-research reports. 2026-10-28.**

---

## 1. The Question

Every technological wave asks two questions. The first — *does it work?* — gets answered by engineers and markets. The second — *who pays, who gains, and who got asked?* — gets answered by politics, usually late and usually after a generation has already absorbed the cost. The AI wave is asking both at once, and the second question is being answered by actors who never stood for election.

The premise of the trade is generous: AI will make us richer, smarter, and more capable. The price is equally concrete: enormous public resources consumed — electricity, water, grid capital, publicly underwritten research — and a class of people whose economic contribution is priced out of the market. The open question is not whether the ledger balances in aggregate. It is who holds the pen.

This paper argues that the trade may well be worth it, but that its legitimacy is unsettled: the decision is currently being made by a narrow set of private actors whose incentives run toward acceleration, while the costs land on a diffuse public that has neither representation nor compensation. History suggests this gap gets closed — but only after political conflict, and only if the closure comes before the capital is locked in.

## 2. The Promised Ledger: Richer, Smarter, More Capable

**"Richer."** The macro projections are enormous and mutually inconsistent. Goldman Sachs (Briggs & Kodnani, 2023) projects a ~7% global GDP uplift (~$7 trillion) over ten years; McKinsey (2023) puts generative AI at $2.6–4.4 trillion annually across 63 use cases; PwC's older forecast claims a 14% global GDP uplift by 2030 ($15.7 trillion). Against these, Acemoglu (2024, NBER WP 32429) offers the sober counterestimate: if generative AI cost-effectively covers only ~4.6% of tasks over a decade, the ten-year GDP uplift is 0.93–1.56% — roughly 0.06% per year. Meanwhile the measured statistics still resemble a modern Solow paradox: through 2025–2026, U.S. nonfarm labor productivity remains within its post-2000 trendline of ~1.5–2.0%, with no statistically significant AI inflection in aggregate TFP. Brynjolfsson, Rock, and Syverson's (2021) J-curve explains the lag — general-purpose technologies require years of unmeasured complementary investment before measured productivity turns up — but the J-curve is a promise, not a receipt.

**"Smarter."** The micro evidence is genuinely strong, with caveats. In the largest field deployment to date, Brynjolfsson, Li, and Raymond (2023/2025) found a generative AI assistant raised resolved issues per hour by 14% across 5,179 customer-support agents — with gains concentrated in novices (bottom quintile: +34%, reaching top-quintile performance in two months instead of six) and near-zero for veterans. Noy and Zhang (2023, *Science*) found ChatGPT cut professional writing time 37% while raising quality 0.45 standard deviations. But Dell'Acqua et al.'s (2023) "jagged technological frontier" experiment shows the flip side: inside AI's competence, consultants were 25% faster and 40% better; outside it, AI users were 19 percentage points *less* likely to be correct than unassisted peers, seduced by fluent hallucinations. And Doshi and Hauser (2024, *Science*) document a collective-level cost: AI assistance lifts individual output while compressing the diversity of ideas the group draws from — everyone gets smarter, the pool gets shallower.

**"More capable."** AlphaFold's 200+ million predicted protein structures (Jumper, Hassabis, Baker — 2024 Nobel Prize in Chemistry) collapsed a years-long experimental pipeline into minutes, and Sweden's MASAI randomized trial (Lång et al., 2023, *Lancet Oncology*) showed AI-supported mammography catching 20% more cancers while cutting radiologist reading time 44%. The caveats are translational: Phase II/III clinical failure rates persist at 85–90% regardless of how fast we fold proteins (Eroom's law), diagnostic models degrade on out-of-distribution scanners and populations, and higher sensitivity without clinical context risks a downstream cascade of overdiagnosis and defensive biopsies that inflates spending without moving mortality.

**The aggregation problem.** Even granting every projection above, the gains are aggregate and the losses are particular. Kaldor-Hicks efficiency (Kaldor 1939; Hicks 1939) calls a change an improvement if the winners *could* compensate the losers and still win. The word doing the political work is *could*. Nothing in the arithmetic requires that they *do*.

## 3. The Public Ledger I: What Society Is Consuming

**Energy.** Global data centers consumed ~460 TWh in 2022, ~2% of world electricity (IEA, 2024), projected to reach 945–1,050 TWh (~3%) by 2030; U.S. data centers took ~4% of national electricity in 2023, and EPRI (2024) projects 4.6–9.1% of U.S. generation by 2030. At the human scale: a classic search query costs ~0.3 Wh; an LLM query ~2.9 Wh (de Vries, *Joule*, 2023); an image generation ~10–12 Wh. Training GPT-3 took ~1,287 MWh (Patterson et al., 2021); Llama 3 405B logged 39.3 million GPU hours and an estimated 30–50 GWh (Meta, 2024). Inference, not training, is 60–80%+ of a deployed model's lifetime energy.

**Water.** Training GPT-3 consumed an estimated 700,000 liters of freshwater directly (Li et al., UC Riverside, 2023); 10–50 chat prompts evaporate about a bottle's worth. AI-driven global freshwater withdrawals are projected at 4.2–6.6 billion m³ annually by 2027. The locality matters more than the global total: over 20% of U.S. data centers sit in moderately to highly stressed watersheds (Siddik et al., *ERL*, 2021); Google's facilities in The Dalles, Oregon consumed 29% of the municipality's potable supply in 2021; desert-Southwest campuses compete with agriculture over the over-allocated Colorado River.

**Who pays the grid bill.** In Northern Virginia, Dominion Energy forecasts data-center peak load growing from ~3 GW (2023) to over 13 GW by 2039; transmission interconnection queues now run 4–5 years (LBNL, 2024). Under standard cost-of-service ratemaking, the new lines and substations roll into the aggregate rate base — meaning residential ratepayers help underwrite industrial-scale load. The FERC dispute over AWS co-location at Talen's Susquehanna nuclear plant (Docket EL24-148, 2024) is the argument in miniature: should retail ratepayers absorb the standby and reliability costs of a hyperscaler's private bargain?

**The public paid for the science too.** DARPA's Strategic Computing Initiative (~$1B, 1983–1993) and the $150M CALO project that became Siri; NSF funding behind PageRank and through the AI winters behind Hinton, LeCun, and Bengio; DOE national labs that built the parallel-computing substrate. Mariana Mazzucato's *Entrepreneurial State* (2013) names the pattern: socialized risk, privatized reward. The public sector was the patient venture capitalist of four decades of basic science; the hyperscalers now enclose the returns.

**Capital and materials.** Combined hyperscaler capex grew from ~$410B (2025) to a projected $720–745B (2026) — a sum negotiated in fewer than ten corporate boards — heading toward cumulative global AI infrastructure spend of $0.8–1.0 trillion by 2026 (Goldman Sachs/Morgan Stanley, 2024). High-voltage transformer backlogs run 3–4 years; China processes >90% of rare earths (USGS, 2024). The opportunity cost is quiet but real: the same transformers, engineers, and clean generation could serve heat pumps, transit, and grid modernization.

**The honest counterweights.** Data centers remain ~2–3% of global electricity — modest next to air conditioning (~2,000 TWh). Efficiency has historically decoupled compute from power: 2010–2018, global data-center compute grew 550% while electricity rose only 6% (Masanet et al., *Science*, 2020). Hyperscalers are the largest corporate buyers of clean-power PPAs — Microsoft's 835 MW Three Mile Island restart deal, Google's 500 MW Kairos SMR order. And Jevons cuts both ways: cheaper tokens may simply summon more of them.

## 4. The Public Ledger II: Disposability

**The measured baseline.** Acemoglu and Restrepo (2020, *JPE*) found each additional robot per 1,000 U.S. workers (1990–2007) cut the employment-to-population ratio ~0.2 points — about 3.3 displaced workers per robot — and depressed wages 0.42%; their (2022, *Econometrica*) account attributes 50–70% of U.S. wage-structure change since 1980 to relative declines for routine-task workers. Generative AI moves the exposure up the skill ladder: Eloundou et al. (2023) estimate 80% of the U.S. workforce has at least 10% of tasks exposed to LLMs; the IMF (Cazzaniga et al., 2024) puts exposure at 40% of global and 60% of advanced-economy employment, with roughly half of exposed jobs at risk of wage erosion or displacement.

**Unemployment is not disposability.** The theoretical stake, in Harari's (*Homo Deus*, 2016; *21 Lessons*, 2018) phrase, is a "useless class" — not people between jobs but people without a market. The distinction is economic, not rhetorical: cyclical unemployment clears when demand recovers; structural disposability means marginal revenue product has fallen permanently below the cost of retraining or social reproduction, and the displaced do not re-equilibrate — they detach, transfer, or get warehoused on disability rolls.

**History's warning labels.** During the British Industrial Revolution's "Engels' Pause," output per worker rose ~46% (1790–1840) while real wages rose only ~12% and the capital share doubled (Allen, 2009); ~250,000 handloom weavers were displaced 1800–1835, their real wages collapsing over 70% — an entire generation paid the transition bill and never re-cleared. In the American deindustrialization, Autor, Dorn, and Hanson show exposed local labor markets still depressed 10–15+ years later, and Davis and von Wachter (2011, *AER*) put displaced workers' lifetime earnings losses at 15–20% (~$112,000 discounted). Case and Deaton's "deaths of despair" are the demographic scar tissue of a reabsorption that never came.

**The distributional scoreboard.** Between 1979 and 2022, U.S. net productivity grew 64.7% while median real hourly compensation grew 14.8% (EPI/BLS, 2024). Karabarbounis and Neiman (2014, *QJE*) document a ~5-point global decline in corporate labor share across 59 countries; Autor et al. (2020, *QJE*) locate the cause in reallocation toward superstar firms with low labor-to-revenue ratios and high markups. AI's extreme capital intensity — GPU clusters, gigawatt campuses, foundation-model IP — is the superstar structure with the volume turned up: the surplus is structurally positioned to accrue to compute owners and model owners, not to labor.

**The counter-thesis.** Reabsorption has never failed to come — yet. Autor et al. (2024) show 60% of 2018 U.S. employment sat in occupational categories that didn't exist in 1940; the reinstatement effect keeps inventing tasks. Aging cuts the same way: 61 countries will have shrinking working-age populations by 2050 (UN WPP, 2024), so automation may plug holes rather than create surpluses. Generative AI's skill-leveling (the novice +34% result) is genuinely egalitarian within firms. And Baumol's cost disease guarantees that the relational, physical, non-automatable services will absorb the released labor, at prices the rich — and eventually everyone — pay. The disposability thesis is a hypothesis about *this* wave's speed and breadth, not a law.

## 5. The Tail That Haunts the Ledger

The original talking points remain the tail-risk appendix to this argument. The extinction scenario is not terminators but control: misalignment, instrumental convergence (Bostrom), fast takeoff (I.J. Good), and coordination failure in the race. Expert p(doom) clusters at 10–20% — the AI Impacts ESPAI 2024 survey of 1,580 researchers averages ~18% for extinction or permanent severe disempowerment; Hinton 10–20%; Bengio ~20%; Christiano 20% — with the honest spread running from LeCun's near-zero to Yampolskiy's 99%. Even among pessimists this is a tail risk, not a forecast; 53% of Americans (Yougov/Yahoo, 2025) nonetheless already price it in.

The relevance to the trade question is structural. Extinction is disposability taken to its limit: a system competent enough to run our infrastructure could make *everyone* economically disposable at once, and it is the one cost the winners cannot compensate after the fact. It is also the one cost the current decision-makers are least accountable for — their fiduciary horizon is the next funding round, not the next century.

## 6. Who Has Been Deciding

Frontier direction is set by an oligopoly of four American labs (OpenAI, Anthropic, Google DeepMind, Meta) and a handful of Chinese state-linked champions, with compute pipelines controlled by four hyperscalers and an accelerator vendor holding >80% of data-center GPU sales (Nvidia). The 2026 capex figure — $720–745B across four firms — is a public investment decision of infrastructure-republic scale, made by private boards with fiduciary duties to shareholders. Nobody elected Sam Altman; as one critic has it, the executive's willingness to accept "some bad things happening for the benefits of this technology" is not the same as public authorization for the trade (Tech Policy Press, 2025).

**Alignment is a political question wearing a technical costume.** RLHF collapses plural, non-commensurable human values into a scalar reward — and the reward is fit by annotators in Nairobi, Manila, and Lagos working to guidelines drafted in San Francisco. Santurkar et al. (ICML 2023) show the tuned models systematically mirror the preferences of left-leaning, educated, urban U.S. demographics and diverge from the old, the poor, and the non-Western. Arrow's impossibility theorem (1951) and Sen's liberal paradox (1970) then guarantee that no non-dictatorial aggregation is clean: *someone's* function is being optimized, which means someone is doing the optimizing.

**The regimes and their gaps.** The EU AI Act (Regulation 2024/1689, in force August 2024) regulates by compute threshold (>10²⁵ FLOPs) but its Brussels effect is blunted where hyperscalers can geofence features (Meta and Apple, 2024–2025). The U.S. relied on Executive Order 14110 (October 2023) — Defense Production Act reporting at 10²⁶ FLOPs, a NIST-hosted Safety Institute — an administrative commitment with no statutory base, reversible with every administration. China's CAC Generative AI Measures (August 2023) require alignment with "Socialist Core Values" before release — legitimacy claimed from state doctrine rather than plural consent. Industry self-regulation (White House voluntary commitments 2023, Frontier Model Forum, corporate scaling policies) carries the classic moral hazard: the policed write their own beat descriptions.

**The opinion gap.** Pew (August 2023): 52% of U.S. adults more concerned than excited about AI; 10% more excited. AIPI tracking (2023–2024): 72% of American voters favor slowing AI development versus 8% favoring acceleration; 82% distrust tech executives to self-regulate; 86% support independent safety standards even at the cost of slower development. The elites race; the public brakes. That is the democratic deficit stated as a crosstab.

## 7. What History Teaches: Who Decided the Last Transitions

The deep-research synthesis across the historical record is a single pattern with a moral: **the terms of a technological transition are set first by whoever owns the scarce infrastructure, and renegotiated later — if at all — through political conflict, regulation, public investment, and compensation.**

- **Railroads (1860s–1910s).** The first high-speed network behaved like the frontier labs: local monopolies charging what the traffic would bear, with farmers — the displaced class of that era — discovering their economic fate was priced by distant boards. Decades of agrarian conflict produced the first federal regulator (the ICC's rate authority, early 1900s) and the antitrust stack: Sherman Act (1890), Clayton and FTC Acts (1914). The Pacific Telegraph Act of 1860 — non-discriminatory carriage, in order received — is the 19th century's net-neutrality clause, and a reminder that "common carrier" is a solution this country has built before.
- **Electrification (1880s–1930s).** The productivity payoff arrived only after decades of complementary reorganization — shop floors rebuilt around the unit motor (UN DESA, 2019) — and the private utility monopolies that built the grids were eventually disciplined, extended, and in places socialized: TVA (1933), the Rural Electrification Act (1936), which took farm electrification from ~10% to ~90% in fifteen years. The lesson: the grid was built private, and made public when the distribution of its benefits became a political question.
- **The New Deal and GI Bill (1933–1944).** The mid-century answer to the productivity-sharing problem of the first machine age: mass secondary and higher education, social insurance, collective bargaining, and a veterans' dividend that functioned as a technology-transition payment on an industrial scale. Broad sharing followed organization and policy — it did not follow from the machines themselves.
- **Deindustrialization (1970–2010).** The counter-example: the Rust Belt shows what happens when the renegotiation *doesn't* come. Displaced manufacturing workers received trade-adjustment assistance sized for a recession and suffered for a structural shock — the persistent local scarring (Autor, Dorn, Hanson) and deaths of despair (Case & Deaton) are the empirical content of "just transition failed."
- **The political response is the mechanism.** Across every episode, the dispossessed did not wait for efficiency arguments: machine-breaking, Chartism, the Factory Acts, minimum wages, the rise of labour parties (Springer, *Lessons from History*, 2025). Deep shifts in labor demand are inherently political, and the institutions of the Western social contract — public education, progressive taxation, social insurance — are the fossil record of previous AI debates, settled in favor of compensation.

The uncomfortable corollary for the present: in every prior wave, the compensation arrived *after* a generation of concentrated pain, and arrived because the losers organized. Whether AI's losers — including the globally dispersed annotators and ratepayers — can organize faster than capital locks in is the open question. Engels' Pause is the null hypothesis.

## 8. The Counterarguments, Honestly

A paper that survives contact with a skeptical audience states its opposition at full strength.

1. **The epistocratic defense (Brennan, 2016).** Lay publics are rationally ignorant of transformer architectures and dual-use biosecurity; 72% "slow down" may measure anxiety, not judgment. Complex risk may not be adjudicable by plebiscite.
2. **The pacing problem (Marchant et al., 2011).** Capability scales faster than deliberation. A citizens' assembly convened in 2026 ratifies 2024's frontier; every deliberation carries a tax, and in an anarchic international system the democratizing nation may simply lose the race to a state that skips the debate.
3. **The meta-governance regress.** Who decides who decides? Assemblies need convened agendas, curated testimony, stratified samples, aggregation rules — all upstream technocratic choices. The conveners are a new elite with better manners.
4. **The aggregate really is enormous.** Even Acemoglu's pessimism concedes positive gains; the Stanford AI Index (2026) pegs U.S. consumer surplus from generative AI at ~$172B annually while most tools remain nearly free — a transfer to households that no one voted for and no one is taxing. Private AI investment rose 127.5% in 2025. The trade might be worth it even if nobody authorized it.
5. **The counterfactual is worse.** The alternative to concentrated private acceleration may not be democratic deliberation; historically it has often been no transition at all — or Bengal's, where the terms were set by a power that did not even pretend to consent.

## 9. Toward a Legitimate Trade

The question "who gets to decide?" has a descriptive and a normative answer, and the gap between them is the paper's thesis.

**Descriptively:** today, the trade is being decided by fewer than ten corporate boards, a handful of regulators operating on executive authority and voluntary commitments, and a race dynamic that punishes unilateral restraint. The public's role is consumption, employment, and electricity rates.

**Normatively**, the historical record and the legitimacy literature converge on a reciprocity principle: *when the public socializes the risk, it acquires a proportionate claim on the reward and on the rules* (Mazzucato, 2013; "No Public Money Without Public Power," 2026). Concretely, that claim has four cashable forms, each with precedent:

1. **Compensation that is actual, not potential** — the Kaldor-Hicks gap closed by real transfers: a data dividend or sovereign wealth stake (public warrants or royalties against public compute and research support), transition insurance for displaced workers sized to the shock rather than to a recession.
2. **Utility-style governance of the bottleneck** — frontier compute and models treated as common carriers or licensed infrastructure, with the non-discrimination principle the ICC and the Pacific Telegraph Act pioneered, and public-interest directors or clawbacks attached to public support.
3. **Representation in the room** — deliberative mini-publics and citizens' assemblies with actual standing (the Collective Intelligence Project's constitutional pilots; NAIRR/EuroHPC as a "CERN for AI" public compute option), because representation, transparency, and accountability are the minimum legitimacy bar (Tech Policy Press, 2025; HDSR, 2025).
4. **Speed recognized** — a constitutional-moment framing (Ackerman): the window in which the rules can be written before capital lock-in makes them ex-post ratification is narrow, and every gigawatt campus poured narrows it further.

**The conclusion the evidence supports** is neither techno-optimist nor doomist: the AI trade is plausibly net-positive in aggregate — richer by any serious estimate, smarter in the RCTs, more capable in the labs — but an uncompensated aggregate gain is a political choice disguised as an economic one. The deciding class today is self-selected, unaccountable, and structurally biased toward acceleration; the paying class is diffuse, under-organized, and unrepresented. Every prior transition in which the trade ended up being worth it got there the same way: the losers organized, the public bought itself a seat, and the surplus was shared because sharing was made a condition. The answer to "who gets to decide whether the trade is worth it?" is therefore not a fact but a pending decision — and like the last ones, it will be settled by whoever shows up to make it.

---

## Sources

**Original talking points (extinction/p(doom) spine)**
- AI Impacts, Expert Survey on Progress in AI (ESPAI 2023/2024) — https://aiimpacts.org/wp-content/uploads/2026/09/ESPAI2024.pdf
- "Why do Experts Disagree on Existential Risk and P(doom)?" (arXiv, Feb 2025) — https://arxiv.org/html/2502.14870v1
- "Does AI pose an existential risk? We asked 5 experts" (The Conversation, 2025) — https://theconversation.com/does-ai-pose-an-existential-risk-we-asked-5-experts-266345
- AI Experts on Catastrophe Scenarios — https://ifanyonebuildsit.com/intro/ai-experts-on-catastrophe-scenarios
- Polls & Surveys (PauseAI) — https://pauseai.info/polls-and-surveys
- "MIT Explains the 12 Possible Endings for AI" (Species | Documenting AGI, 2026) — https://www.youtube.com/watch?v=FLcrvMfHUJM

**Economics of the upside and of disposability**
- Acemoglu & Restrepo (2020), "Robots and Jobs," *JPE*; (2022), "Tasks vs. Skills," *Econometrica*; Acemoglu (2024), "The Simple Macroeconomics of AI," NBER WP 32429
- Eloundou et al. (2023), "GPTs are GPTs"; IMF (Cazzaniga et al., 2024), Gen-AI and the Future of Work; WEF *Future of Jobs* 2023
- Allen (2009), "Engels' Pause" (Explorations in Economic History); Autor, Dorn & Hanson (2013, 2016), China shock; Davis & von Wachter (2011, *AER*); Case & Deaton (2020)
- Karabarbounis & Neiman (2014, *QJE*); Autor, Dorn, Katz, Patterson & Van Reenen (2020, *QJE*), superstar firms; Autor et al. (2024, NBER WP 32389), new work
- Brynjolfsson, Li & Raymond (2023/2025), "Generative AI at Work"; Noy & Zhang (2023, *Science*); Dell'Acqua et al. (2023), jagged frontier; Doshi & Hauser (2024, *Science*); Brynjolfsson, Rock & Syverson (2021), productivity J-curve
- Briggs & Kodnani (2023, Goldman Sachs); Chui et al. (2023, McKinsey); Rao et al. (PwC); EPI/BLS productivity-pay gap (2024)
- Lång et al. (2023, *Lancet Oncology*), MASAI trial; Jumper/Hassabis/Baker, AlphaFold, 2024 Nobel

**Public resources**
- IEA (2024), *Energy and AI*; EPRI (2024) U.S. data-center projections; de Vries (*Joule*, 2023); Patterson et al. (2021); Meta (2024), Llama 3
- Li et al. (2023, UC Riverside), GPT-3 water footprint; Siddik et al. (*ERL*, 2021); City of The Dalles records (2022)
- Dominion IRP (2024); LBNL interconnection queues (2024); FERC Docket EL24-148 (2024); Reason Foundation (2024)
- Mazzucato (2013), *The Entrepreneurial State*; Masanet et al. (*Science*, 2020); Alcott (2005), Jevons; Constellation/Microsoft TMI PPA (2024); USGS (2024)

**Governance and legitimacy**
- Gabriel (2020), "Artificial Intelligence, Values, and Alignment"; Santurkar et al. (ICML 2023); Casper et al. (2023); Henrich, Heine & Norenzayan (2010); Arrow (1951); Sen (1970)
- EU Regulation 2024/1689; U.S. EO 14110 (2023); CAC Generative AI Measures (2023); Bradford (2020), Brussels Effect
- Pew Research (Aug 2023); AIPI tracking (2023–2024); Tech Policy Press (2025), "AI Governance Is Being Decided Now" — https://www.techpolicy.press/ai-governance-is-being-decided-now-and-the-public-isnt-in-the-room/
- HDSR (MIT Press), "Frontier AI, Power, and the Public Interest" — https://hdsr.mitpress.mit.edu/pub/xdukxlpp
- Common Wealth, "Take Back the Future: Democratising Power over AI" — https://www.common-wealth.org/publications/take-back-the-future-democratising-power-over-ai
- "No Public Money Without Public Power" (2026) — https://www.linkedin.com/pulse/public-money-without-power-pierre-jean-duvivier-dit-sage-cfqie
- Brennan (2016), *Against Democracy*; Marchant et al. (2011), pacing problem; Ackerman (1991), *We the People*

**Historical transitions**
- UN DESA WP 158 (2019), "Lessons for Today from Past Periods of Rapid Technological Change" — https://www.un.org/esa/desa/papers/2019/wp158_2019.pdf
- History News Network, "Old Concepts for New Concerns: the Railroad, the Internet, and Government Regulation" — https://www.historynewsnetwork.org/article/old-concepts-for-new-concerns-the-railroad-the-int
- Toloui, "Titans, Swarms, or Human Renaissance?" (Digitalist Papers) — https://www.digitalistpapers.com/vol2/toloui
- "Lessons from History: The Societal Impacts of Technological Change" (Springer, 2025) — https://link.springer.com/10.1007/978-3-032-11814-1_21
