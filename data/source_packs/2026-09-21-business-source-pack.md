# Business Source Pack - 2026-09-21

Purpose: source material for practical AI business adoption and market intelligence briefs.

Use this file as input for `prompts/business_insight_prompt.md`.

## Source selection reminder

- Prefer implementation evidence over hype.
- Treat vendor/company sources as biased primary signals.
- Separate fact, meaning, risk and application.
- Look for BI/workflow, FMCG/distribution, SME and market intelligence relevance.

---

## 1. Power BI Q&A retirement reminder: February 2027 timeline update

**Source:** Microsoft Power BI Blog
**Type:** bi_tooling
**Published:** Thu, 10 Sep 2026 16:00:00 GMT
**URL:** https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Power-BI-Q-A-retirement-reminder-February-2027-timeline-update/ba-p/5365841
**Relevance score:** 5/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

In December, we announced the retirement of Power BI Q&A , our legacy natural-language querying experience, with retirement planned for December 2026. To give current Q&A user's additional time to assess their dependencies and transition to newer Copilot-powered solutions, we’re extending the retirement date to February 2027. This post recaps the affected experiences and provides updates on Copilot capacity availability, embedded scenarios, and sovereign clouds. Recap of the January announcement What is being deprecated? The retirement applies to both the end-user Q&A experiences, and the associated Q&A configuration tools. Retiring experience Recommended alternative Q&A in reports Copilot with Power BI reports Q&A on a dashboard Copilot standalone experience Q&A virtual analyst in mobile app Copilot in Power BI Mobile Q&A in Power BI embedded analytics Copilot for SaaS scenarios . For embedded PaaS scenarios, refer to the updates later in this post. Q&A Setup Prep Data for AI What happens at retirement? Beginning in February 2027, Q&A will no longer work in Power BI. The Q&A visual will be removed, and existing reports that contain Q&A visuals will display an error in place of the

---

## 2. Modern Power BI architecture choices for reporting on Azure Databricks: A performance benchmark for Power BI storage modes

**Source:** Microsoft Power BI Blog
**Type:** bi_tooling
**Published:** Thu, 03 Sep 2026 11:30:43 GMT
**URL:** https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Modern-Power-BI-architecture-choices-for-reporting-on-Azure/ba-p/5364286
**Relevance score:** 5/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Many enterprise Power BI semantic models use Azure Databricks as a data source. When building these models, developers and architects face an early and consequential decision: which storage mode to use. Cost, security, and ease of development and tuning all factor in — but report performance is probably the most important of them, because reports that are slow to load are one of the most common causes of end-user dissatisfaction. In practice, that decision is often made on intuition rather than evidence. To help change that, we've published a new white paper, Modern Power BI Architecture Choices for Reporting on Azure Databricks , benchmarking four ways of serving the same Delta tables to a Power BI report: Direct Lake on OneLake — over Delta tables in a Fabric lakehouse or warehouse Direct Lake on mirrored Unity Catalog tables — shortcuts, no copy DirectQuery — on a Databricks SQL warehouse Composite Model on Databricks — DirectQuery combined with Import-mode aggregations Figure: The four Power BI storage modes benchmarked to evaluate their impact on report performance and scalability. What the results suggest: there's no universal winner — but there are clear patterns. Direct Lak

---

## 3. Upgrade Power BI Dataflows Gen1 to Fabric Dataflows Gen2 with the Upgrade Wizard (Preview)

**Source:** Microsoft Power BI Blog
**Type:** bi_tooling
**Published:** Mon, 24 Aug 2026 15:00:00 GMT
**URL:** https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Upgrade-Power-BI-Dataflows-Gen1-to-Fabric-Dataflows-Gen2-with/ba-p/5360422
**Relevance score:** 5/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Upgrading Power BI Dataflows Gen1 is now easier with the Dataflows Upgrade Wizard. Now in preview for eligible workspaces assigned to Fabric capacity, the wizard provides a guided experience to upgrade Power BI Dataflows Gen1 items to Fabric Dataflows Gen2 (CI/CD). The wizard preserves key properties of the existing dataflow and assesses each item before you begin, helping you understand the upgrade scope and expected follow-up actions. Modernize at your own pace Power BI Dataflows Gen1 remains supported in a legacy state, while new feature investment focuses on Fabric Dataflows Gen2 (CI/CD), as shared in a previous post about the future of Dataflows . The Upgrade Wizard gives dataflow owners a guided self-service path to start that modernization without rebuilding their Power Query logic. You don't need to upgrade your full estate at once. Start with a representative set of dataflows, validate the results, and expand at a pace that works for your organization. For detailed migration planning and inventory guidance, review Migrate from Dataflow Gen1 to Dataflow Gen2 . Build on the benefits of Dataflows Gen2 Fabric Dataflows Gen2 (CI/CD) builds on the Power Query authoring experienc

---

## 4. The hidden cost of operating two shipping systems

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Mon, 21 Sep 2026 05:00:00 -0400
**URL:** https://www.supplychaindive.com/spons/the-hidden-cost-of-operating-two-shipping-systems/830822/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

Freight sat out the shipping consolidation trend. Here's what closing that gap actually looks like.

---

## 5. When demand won’t sit still: Building a more flexible warehouse network

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Mon, 21 Sep 2026 05:00:00 -0400
**URL:** https://www.supplychaindive.com/spons/when-demand-wont-sit-still-building-a-more-flexible-warehouse-network/830243/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

See how flexible warehousing can help supply chains adapt as demand, inventory and markets shift.

---

## 6. When budget cuts fail: The stranded costs and complexity hiding in your supply chain

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Mon, 21 Sep 2026 05:00:00 -0400
**URL:** https://www.supplychaindive.com/spons/when-budget-cuts-fail-the-stranded-costs-and-complexity-hiding-in-your-sup/830621/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

Cost programs fail for two reasons: stranded costs and complexity. Learn which complexity protects your margins and which costs quietly erode them.

---

## 7. FedEx levies fees on US imports from Canada, Europe and others

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Fri, 18 Sep 2026 15:26:00 -0400
**URL:** https://www.supplychaindive.com/news/fedex-levies-fees-on-us-imports-from-canada-europe-and-others/830797/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The demand surcharges, which also include higher fees for China-to-U.S. volume, will take effect as parcel shippers gear up for peak season.

---

## 8. TJX CEO: Distribution model will help weather El Niño

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Fri, 18 Sep 2026 10:53:00 -0400
**URL:** https://www.supplychaindive.com/news/tjx-ceo-distribution-model-will-help-weather-el-nino/830665/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The off-price retailer&rsquo;s supply chain strategy allows it to hold inventory instead of going straight to stores, according to a Q2 earnings call.

---

## 9. Untitled

**Source:** Retail Gazette
**Type:** retail_fmcg_news
**Published:** 
**URL:** https://www.retailgazette.co.uk/blog/feed/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.
**Fetch error:** HTTP Error 403: Forbidden

**Summary:**



---

## 10. Mileway expands German logistics base

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Mon, 21 Sep 2026 09:44:56 +0000
**URL:** https://www.logisticsmanager.com/mileway-expands-german-logistics-base/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Mileway expands German logistics base appeared first on Logistics Manager .

---

## 11. Kuehne+Nagel agrees strategic collaboration with Amazon

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Mon, 21 Sep 2026 09:06:56 +0000
**URL:** https://www.logisticsmanager.com/kuehnenagel-agrees-strategic-collaboration-with-amazon/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Kuehne+Nagel agrees strategic collaboration with Amazon appeared first on Logistics Manager .

---

## 12. Raphael Capital sells 29,585ft² industrial unit

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Mon, 21 Sep 2026 08:10:18 +0000
**URL:** https://www.logisticsmanager.com/raphael-capital-sells-29585ft%c2%b2-industrial-unit/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Raphael Capital sells 29,585ft² industrial unit appeared first on Logistics Manager .

---

## 13. Autonomous tech trialled at Port of Antwerp-Bruges

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Mon, 21 Sep 2026 07:53:37 +0000
**URL:** https://www.logisticsmanager.com/autonomous-tech-trialled-at-port-of-antwerp-bruges/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Autonomous tech trialled at Port of Antwerp-Bruges appeared first on Logistics Manager .

---

## 14. On-Demand: Building supply chain resilience – navigating uncertainty, disruption and change

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Fri, 18 Sep 2026 13:00:18 +0000
**URL:** https://www.logisticsmanager.com/webinar-building-supply-chain-resilience-navigating-uncertainty-disruption-and-change/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post On-Demand: Building supply chain resilience – navigating uncertainty, disruption and change appeared first on Logistics Manager .

---

## 15. How B2B Marketers Misunderstand Their Customers

**Source:** MIT Sloan Management Review
**Type:** professional_insight
**Published:** Tue, 15 Sep 2026 11:00:37 +0000
**URL:** https://sloanreview.mit.edu/article/how-b2b-marketers-misunderstand-their-customers/
**Relevance score:** 5/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Nick Lowndes/Ikon Images Businesses are striving to adapt ever faster to keep pace with rapid change, and yet B2B marketing practices have remained surprisingly static. Sure, the tactics have shifted to digital executions, and the use of data has made targeting B2B buyers more precise, but marketers remain rooted in fundamentally flawed assumptions about the [&#8230;]

---

## 16. UK Entrepreneurs Lag Behind Europe in AI Adoption Despite Heavy Admin Burden, bunq Research Reveals - FF News

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Thu, 17 Sep 2026 16:15:34 GMT
**URL:** https://news.google.com/rss/articles/CBMifEFVX3lxTE1jQjNfOVNQcElabGQ0VjBaVWJ6YkJSbWxDZ21QZ1hHWU9icjFlaXg3OGduMFNkZ3N4WS1ESkJ0WUg1anRxUGU0dlNsa3Zocmd3eHd1TGVRR1UzbXloelFnRDhTMjkxQTluTWhjbzltYVl4emFmejlLR3VSUGI?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

UK Entrepreneurs Lag Behind Europe in AI Adoption Despite Heavy Admin Burden, bunq Research Reveals FF News

---

## 17. Why small businesses could be the big winners from AI - UKTN

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Wed, 16 Sep 2026 11:11:59 GMT
**URL:** https://news.google.com/rss/articles/CBMikwFBVV95cUxPQzA4OGJsazhjekFQZlRyMFNXbWZtQUo2Tlp2a0FNMTloX3VFZ2pvTkVWb2Vjdi1abjBscG92U2kwTUgyTkpSRlAzR19nd204M0d4MkViNXRabFRGck5GMkJ0QVc2bmRfakRPa0JnM0R4S2stLU40NVg5V3dET0twVTNJeVVuSDVia3Y2RHJEUTlldlU?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Why small businesses could be the big winners from AI UKTN

---

## 18. Air IT launches AI agent marketplace for UK SMEs - IT Europa

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Thu, 17 Sep 2026 10:42:11 GMT
**URL:** https://news.google.com/rss/articles/CBMif0FVX3lxTE44aU1DMWJmQVU4MEZYNmdJUEF2TG1iaFN4THU3b2taUkdjUHlJejR1RG5JZDgxUUZ2S2dGS3BfaHFURTlOQlcyemFLMG1weW14UlBKMnRDeTZSNW1CdFZDN295UEdla3h6REV1ZGRrb2ZKNWxUd0M1M0dUSUlHcmM?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Air IT launches AI agent marketplace for UK SMEs IT Europa

---

## 19. UK business leaders sceptical about use of AI in recruitment - Personnel Today

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Fri, 18 Sep 2026 10:41:49 GMT
**URL:** https://news.google.com/rss/articles/CBMimwFBVV95cUxQY0FHNTA0R2pDekF4ZFJSV0wzY09tMTJKdFRmXzdMVl9mZDdiYjBfU1pjQ19DSUhBZDJrTXBNZi1haC1PaUlTWC1SazNfRm50S292X0ZCTXZJbWJrMzNkVk9xZDgyYkh4SmhmSjBxd2tyUzlmSF9PdWE5OTRsX2JsUVMyeHRYdDVBTkVFMVhSTXRPSnBRcEJZZzB2RQ?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

UK business leaders sceptical about use of AI in recruitment Personnel Today

---

## 20. UK small businesses want AI to win back time, not just write copy - channelx.world

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Fri, 18 Sep 2026 08:49:13 GMT
**URL:** https://news.google.com/rss/articles/CBMinAFBVV95cUxOb1RTWWZjZWtsM0RoaUFxQnJKamx3TnFjWjZTX2NjVEhLV2hUaHk5Z0dURTZ4RHQ1NzZBTm1ha25KTlJqeDFuUnFuMEExTThwNnpKeERjb09GY29QWVVxYmwxVFo2MF85S0p0cTktNHUwMkVPamlfWlBKM0UyTmZSQVoxQm9rTEtLbkJSZVl4b3hkTUY1OExRbVBxWEw?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

UK small businesses want AI to win back time, not just write copy channelx.world

---

## 21. Innowise joins Creatio partner ecosystem to deploy AI workflows - Portal ERP

**Source:** Google News - business intelligence AI workflow
**Type:** news_search
**Published:** Tue, 15 Sep 2026 09:29:08 GMT
**URL:** https://news.google.com/rss/articles/CBMinAFBVV95cUxPSFFXRzhfOE45RzJuN2VGRFZpYkdqOGpxSi1NWDZyQktla0hvaGJNcUFHWFZQaExfRXZLTEJwaUlINGFoZWhmUk84eHRqRlk4RzJGN0RqLUNISVlsNTcxSnJJa1d4OVd0TkRYMk5XYzFSMGVhVUVtSDVkUUNUY3ludTc4MFZoY0FiblJROG5HQ3h3ekp4cU5BN01UQUU?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Innowise joins Creatio partner ecosystem to deploy AI workflows Portal ERP

---

## 22. Building Enterprise AI Workflow Automation Systems: Key Architectures and Best Practices - Nasscom

**Source:** Google News - business intelligence AI workflow
**Type:** news_search
**Published:** Fri, 18 Sep 2026 09:53:32 GMT
**URL:** https://news.google.com/rss/articles/CBMivgFBVV95cUxPMlZzS2pwSTBleTJObnZFYVhnby1wSzhfaWdUS243aW5udEVFOEhIeVVxUlBoUlBLdW5BSFUzUURLWENVMWxidDNBZ1hPVXptM2VRRHdGU0p3NzZrNFBBbFlzVnE2UDM1MEZSRzd2bXdteHRaVkZqZW05WjdQemdkbHI3XzNUOEZ4WUIxcGlKSzZJYU5WdFowYmN0SjJDRGtzM3dZb01nVllmM3NSWEFvZ0VSVXlRN2hzcDNFdG1R?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Building Enterprise AI Workflow Automation Systems: Key Architectures and Best Practices Nasscom

---

## 23. Parakeet Health lands major AI partnership with national dermatology group Qualderm - Fierce Healthcare

**Source:** Google News - business intelligence AI workflow
**Type:** news_search
**Published:** Tue, 08 Sep 2026 07:00:00 GMT
**URL:** https://news.google.com/rss/articles/CBMixAFBVV95cUxNTWw3VFNsODVPcnY2SWE0V3FHTUp2NnRySnh1azVjUkRmTmRnQjBUWXRhWXpjeWhBYWs3MWI0bTFzek1DUWZLN0Zid1dGOVlLY1NNZHFYVXRiRWZsaUdwWE1xdEtnemJuVmtpVU8welNBdzNGSzY5RVpFaTJjQnBlOVl3ZHlweUE0b3cyWjVON0k2Z2F0cW0tOHBJWGUwUlM5Z2xILVliNjJ5MmhlaWZ2T2JMdmtPMTJpMGQ3dVcxSGw5eFBI?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Parakeet Health lands major AI partnership with national dermatology group Qualderm Fierce Healthcare

---

## 24. Chartwell Mortgage Services adopts JammJar AI platform - The Intermediary

**Source:** Google News - business intelligence AI workflow
**Type:** news_search
**Published:** Fri, 24 Jul 2026 07:00:00 GMT
**URL:** https://news.google.com/rss/articles/CBMimAFBVV95cUxOdjNwN2FHQUIzMmlJT193LUQwY0ZYdGZpM0RFaVJHRURSdUZnUUVmd19yQTVZQW8tX1BYZGJVNDZMY3JfWjhELVNrQ2dYMy1MSTBtS0FhSFBzeHF4bGptWWhEX20xNlZweVd0NlZUb0owWnAtX2JnSVFnQkJrUmJocVpXaVljYUFxQWNIUGszTXhRdXRoaG0wMg?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Chartwell Mortgage Services adopts JammJar AI platform The Intermediary

---

## 25. AI Automation Market Size, Share, Growth Forecast, 2034 - Fortune Business Insights

**Source:** Google News - business intelligence AI workflow
**Type:** news_search
**Published:** Mon, 17 Aug 2026 07:00:00 GMT
**URL:** https://news.google.com/rss/articles/CBMidkFVX3lxTE9vdUdZcjJRc1VBTWZvOS1aazE3MzVvQjVwXzA0bmNnaTlSUWhZcXYwZW1USnVobmxWVUNETXZwT1hPLU5JM2UzVElWdXpnLXRsdklGZkNyaEVMeWpLZWVQNUNqdWFvOGF0cEpza1JBU25pWWYteEE?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

AI Automation Market Size, Share, Growth Forecast, 2034 Fortune Business Insights

---

## 26. Moody's: retail P&C distribution faces the fastest AI disruption of any financial services segment - Insurance Business

**Source:** Google News - retail distribution AI UK
**Type:** news_search
**Published:** Tue, 04 Aug 2026 07:00:00 GMT
**URL:** https://news.google.com/rss/articles/CBMi-gFBVV95cUxQVTNEVXBSOXJHMFFfcmpESWpJZEw2MEE3UHR5X1FGOUpkSVFrX2x2Z0RheXJYX0VQcUpxVFRQckRfOE1LM1NhSkhiaXJKWmxIUUpmd2dEdHRVcy05dGdHaEF1OXZpRWpBWTI5YXdxOUxUclpOZTRsM2tGMnRNd3pQdlA1NHUtMzBLMEtGYzBTTVpmNmtTbnQzcDhXOGcyczl4MUtlMmlWbGxuYkVQU0pqSDRkVzZZN3JwRnNYUXl5X3hJaGZGNGhrVHQ2bUktbHlYVGk2RUg4MThjTUFOYmxvMGx2dnB4ZXR6YVZwbFNnVlNfa2VXbXBULU9B?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Moody's: retail P&C distribution faces the fastest AI disruption of any financial services segment Insurance Business

---

## 27. ONS business, economy and technology statistics

**Source:** ONS
**Type:** official_watchlist
**Published:** 2026-09-21
**URL:** https://www.ons.gov.uk/
**Relevance score:** 5/5
**Quality note:** Official source: credible context, but may be broad or slow-moving.
**Manual check:** Yes - this source is included as a watchlist item.

**Summary:**

Official UK statistics source for business conditions, productivity, retail, labour market and economic context.

---

## 28. OECD AI, SMEs, productivity and digital adoption

**Source:** OECD
**Type:** official_watchlist
**Published:** 2026-09-21
**URL:** https://www.oecd.org/
**Relevance score:** 5/5
**Quality note:** Official source: credible context, but may be broad or slow-moving.
**Manual check:** Yes - this source is included as a watchlist item.

**Summary:**

Useful for international context on SME digital adoption, productivity, AI diffusion and policy.

---

## 29. The Grocer - UK FMCG and grocery sector

**Source:** The Grocer
**Type:** fmcg_watchlist
**Published:** 2026-09-21
**URL:** https://www.thegrocer.co.uk/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.
**Manual check:** Yes - this source is included as a watchlist item.

**Summary:**

Specialist UK FMCG and grocery source. Useful for suppliers, wholesalers, pricing, retail pressure and distribution signals.

---

## 30. IGD grocery, retail and supply-chain insight

**Source:** IGD
**Type:** fmcg_watchlist
**Published:** 2026-09-21
**URL:** https://www.igd.com/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.
**Manual check:** Yes - this source is included as a watchlist item.

**Summary:**

Useful for grocery, retail, wholesale and supply-chain context.

---

## 31. Kantar retail and FMCG insights

**Source:** Kantar
**Type:** fmcg_watchlist
**Published:** 2026-09-21
**URL:** https://www.kantar.com/uki/industries/retail
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.
**Manual check:** Yes - this source is included as a watchlist item.

**Summary:**

Professional insight source for FMCG, retail, consumers and brand performance.

---

## 32. NielsenIQ retail and FMCG insights

**Source:** NielsenIQ
**Type:** fmcg_watchlist
**Published:** 2026-09-21
**URL:** https://nielseniq.com/global/en/insights/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.
**Manual check:** Yes - this source is included as a watchlist item.

**Summary:**

Professional retail and FMCG data source for market trends, consumer behaviour and category performance.

---

## 33. Introducing Astra for Law

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Thu, 17 Sep 2026 00:00:00 GMT
**URL:** https://openai.com/index/astra-for-law
**Relevance score:** 4/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

OpenAI for Law brings frontier intelligence for law, custom firm workflows, connected legal data sources, and legal-grade controls for confidential client work.

---

## 34. Manage semantic model settings in context with the default settings pane (Preview)

**Source:** Microsoft Power BI Blog
**Type:** bi_tooling
**Published:** Thu, 17 Sep 2026 16:00:00 GMT
**URL:** https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Manage-semantic-model-settings-in-context-with-the-default/ba-p/5366792
**Relevance score:** 4/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

The semantic model settings pane is becoming the default way to configure semantic models in the Power BI service. The pane opens alongside your workspace, so you can review and change settings without leaving the current page. It provides the same settings as the full semantic model settings page while keeping the surrounding context visible. The classic settings page remains available during this transition, but it no longer opens first. This change builds on the settings pane preview and provides a more focused experience for managing semantic models. Why it matters The pane helps you stay in context while you manage a semantic model. It opens on the right side of the browser window and keeps your workspace visible. Settings are organized into expandable sections and tabs, including refresh, data access, performance, and OneDrive and SharePoint. You can use the search box at the top of the pane to find a setting across all sections and tabs. For example, enter "re" and select View refresh history to go directly to refresh history instead of opening sections one at a time. This organization is especially useful for semantic models with several connection, refresh, or performance 

---

## 35. When AI Disruption Never Ends

**Source:** MIT Sloan Management Review
**Type:** professional_insight
**Published:** Thu, 10 Sep 2026 11:00:26 +0000
**URL:** https://sloanreview.mit.edu/article/when-ai-disruption-never-ends/
**Relevance score:** 4/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Phil Bliss/theispot.com A vice president of product opens her laptop on a Monday morning to find that the AI model her team had worked with for the past six weeks to build a customer workflow has been leapfrogged by a cheaper, faster alternative. Again. Her Slack feed is blowing up with links to the announcement. [&#8230;]

---

## 36. Responsible AI Means Knowing the Limits of Agent Autonomy

**Source:** MIT Sloan Management Review
**Type:** professional_insight
**Published:** Tue, 08 Sep 2026 11:00:36 +0000
**URL:** https://sloanreview.mit.edu/article/responsible-ai-means-knowing-the-limits-of-agent-autonomy/
**Relevance score:** 4/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

For the fifth year in a row, MIT Sloan Management Review and Boston Consulting Group (BCG) have assembled an international panel of AI experts that includes academics and practitioners to help us understand how responsible artificial intelligence is being implemented across organizations worldwide. In previous posts this year, we have explored artificial intelligence’s impact on [&#8230;]

---

## 37. The transformer supercycle: Why demand is outrunning supply

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Fri, 18 Sep 2026
**URL:** https://www.mckinsey.com/industries/electric-power-and-natural-gas/our-insights/the-transformer-supercycle-why-demand-is-outrunning-supply
**Relevance score:** 4/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

A new era of increased demand and constrained supply is fundamentally changing the global transformer market and reshaping decision-making across the value chain.

---

## 38. The new AgentCore runtime: Elastic, optimized, and consistently fast starts

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Fri, 18 Sep 2026 15:31:34 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/the-new-agentcore-runtime-elastic-optimized-and-consistently-fast-starts/
**Relevance score:** 3/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Today we are announcing the new AgentCore runtime, a capability of Amazon Bedrock AgentCore built for the speed, flexibility, and cost efficiency that production agents demand. It reclaims memory as sessions release it and delivers consistent cold starts regardless of image size or concurrency.

---

## 39. Power BI sample reports, refreshed with modern visual defaults

**Source:** Microsoft Power BI Blog
**Type:** bi_tooling
**Published:** Wed, 02 Sep 2026 16:00:00 GMT
**URL:** https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Power-BI-sample-reports-refreshed-with-modern-visual-defaults/ba-p/5363807
**Relevance score:** 3/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Microsoft has refreshed its Power BI sample reports with modern visual defaults, stronger semantic models, mobile-optimized layouts, and newer authoring features to help creators build clearer, more effective reports.

---

## 40. How to Reinvent Your Company Without Starting Over

**Source:** MIT Sloan Management Review
**Type:** professional_insight
**Published:** Wed, 09 Sep 2026 11:00:37 +0000
**URL:** https://sloanreview.mit.edu/article/how-to-reinvent-your-company-without-starting-over/
**Relevance score:** 3/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Grundini/Ikon Images How does a fossil fuel company become the world’s largest developer of offshore wind? How does a software company written off for missing the mobile revolution become one of the world’s most valuable companies in the age of AI? Ørsted and Microsoft have faced a puzzle familiar to many leaders: When technological, regulatory, [&#8230;]

---

## 41. WIRED: The AI playbook top companies use

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Mon, 21 Sep 2026
**URL:** https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/wired-the-ai-playbook-top-companies-use
**Relevance score:** 3/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

McKinsey’s Dan Swan explains why capturing AI’s full potential requires companies to move beyond experimentation and fundamentally rewire their businesses across technology, processes, people, and leadership.

---

## 42. UK urged to strengthen financial muscle of national wealth fund to aid economy

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Mon, 21 Sep 2026 04:00:35 GMT
**URL:** https://www.theguardian.com/business/2026/sep/21/uk-urged-to-strengthen-financial-muscle-of-national-wealth-fund-to-aid-economy
**Relevance score:** 3/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Unions, thinktanks and others say overhaul could provide investment Britain needs Unions, thinktanks, environmental groups and charities have come together to call on ministers to boost the financial firepower of the national wealth fund to empower it to invest more in Britain and rebalance the country’s economy. Lower energy bills, the revitalisation of the UK’s industrial heartlands and the provision of more high-quality jobs could all be unlocked by scaling up the NWF, according to a statement from organisations including the TUC, Greenpeace, WWF and the New Economics Foundation. Turbocharging the retrofitting of homes and buildings. Giving the public a bigger stake in critical infrastructure through taking part-ownership stakes in key projects. Launching a targeted investment programme to bring new green industries to communities hit hardest by deindustrialisation. Supporting a network of regional banks to funnel money into the small businesses that hold up local economies. Continue reading...

---

## 43. Untitled

**Source:** GOV.UK SMEs digital adoption
**Type:** official_policy
**Published:** 
**URL:** https://www.gov.uk/api/search.json?q=SME%20digital%20adoption%20artificial%20intelligence&count=5&order=updated-newest
**Relevance score:** 3/5
**Quality note:** Official source: credible context, but may be broad or slow-moving.
**Fetch error:** HTTP Error 422: Unknown Error

**Summary:**



---

## 44. Untitled

**Source:** GOV.UK business productivity technology
**Type:** official_policy
**Published:** 
**URL:** https://www.gov.uk/api/search.json?q=business%20productivity%20technology%20SME&count=5&order=updated-newest
**Relevance score:** 3/5
**Quality note:** Official source: credible context, but may be broad or slow-moving.
**Fetch error:** HTTP Error 422: Unknown Error

**Summary:**



---

## 45. How Cooley is accelerating IPO work with ChatGPT

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Thu, 17 Sep 2026 12:00:00 GMT
**URL:** https://openai.com/index/cooley-gopublic
**Relevance score:** 2/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Cooley built GO Public with ChatGPT Work to bring intelligence to the IPO process, helping lawyers surface issues earlier and focus judgment where it matters most.

---

## 46. Reimagining advertising with AI

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Wed, 16 Sep 2026 13:00:00 GMT
**URL:** https://openai.com/index/reimagining-advertising-with-ai
**Relevance score:** 2/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Explore new AI-powered advertising experiences from OpenAI, including Sponsored Agents, tools for marketers, and integrations with HubSpot and Shopify.

---

## 47. Amazon SageMaker Inference: 2026 year-to-date launches in review

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Fri, 18 Sep 2026 20:52:14 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-inference-2026-year-to-date-launches-in-review/
**Relevance score:** 2/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Amazon SageMaker AI shipped 13 inference launches in year-to-date across two deployment paths: fully managed endpoints and Amazon SageMaker HyperPod Inference. This post reviews each launch, from inference recommendations and capacity-aware instance pools to tiered KV caching and disaggregated prefill and decode.

---

## 48. Introducing Kimi K3 on Amazon Bedrock

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Fri, 18 Sep 2026 16:52:01 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/introducing-kimi-k3-on-amazon-bedrock/
**Relevance score:** 2/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Kimi K3 from Moonshot AI is now available on Amazon Bedrock, giving you a powerful new open-weight option for coding and knowledge work. It offers native vision, a 1-million-token context window, and explicit prompt caching to reduce latency and input costs.

---

## 49. Migrating multi-model AI agents to Amazon Bedrock AgentCore runtime

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Fri, 18 Sep 2026 15:38:53 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/migrating-multi-model-ai-agents-to-amazon-bedrock-agentcore-runtime/
**Relevance score:** 2/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Migrate a multi-model healthcare AI agent from self-managed Amazon ECS with AWS Fargate to Amazon Bedrock AgentCore runtime, preserving triple-model orchestration and vector-enhanced knowledge retrieval while reducing infrastructure management. The framework-agnostic pattern applies across healthcare, financial services, and manufacturing.

---

## 50. Deploy Hugging Face models on Amazon SageMaker AI with coding agents

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Fri, 18 Sep 2026 15:25:23 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/deploy-hugging-face-models-on-amazon-sagemaker-ai-with-coding-agents/
**Relevance score:** 2/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Deploy production-ready Hugging Face models on Amazon SageMaker AI using six open-source agent skills. Point a coding agent at a model and get back a real-time endpoint with the right serving container, autoscaling, Amazon CloudWatch alarms, and a verified teardown path.

---

## 51. How AI Creates a Capability Mirage

**Source:** MIT Sloan Management Review
**Type:** professional_insight
**Published:** Mon, 14 Sep 2026 11:00:15 +0000
**URL:** https://sloanreview.mit.edu/article/how-ai-creates-a-capability-mirage/
**Relevance score:** 2/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

PPaint/Ikon Images Dry rot. A Potemkin village. The Wizard of Oz. What do those things have in common? In each case, they may look good on the surface, but it’s only an illusion. Wood afflicted with dry rot looks just fine until the tree it’s in topples down. Grigory Potemkin is said to have tried [&#8230;]

---

## 52. Author Talks: How to turn hope into action

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Fri, 18 Sep 2026
**URL:** https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-how-to-turn-hope-into-action
**Relevance score:** 2/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

What compels us to act when we see a problem? Draper Richards Kaplan Foundation CEO Jim Bildner reflects on social entrepreneurship, personal loss, and how hope can move us to act.

---

## 53. Social care referral networks: Improving health in rural communities

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Fri, 18 Sep 2026
**URL:** https://www.mckinsey.com/industries/public-sector/our-insights/social-care-referral-networks-improving-health-in-rural-communities
**Relevance score:** 2/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Six design dimensions can help states stand up social care referral networks that meaningfully improve health outcomes for Medicaid members in rural and underserved communities.

---

## 54. The $2.3 trillion horizon: How AI is rewriting the semiconductor story

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Fri, 18 Sep 2026
**URL:** https://www.mckinsey.com/industries/semiconductors/our-insights/the-2-point-3-trillion-dollar-horizon-how-ai-is-rewriting-the-semiconductor-story
**Relevance score:** 2/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

AI is fueling unprecedented semiconductor growth while upending long-standing industry dynamics and shifting the sources of value.

---

## 55. Only 160 apprenticeship starts in eight months on Labour’s flagship scheme

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Mon, 21 Sep 2026 04:00:36 GMT
**URL:** https://www.theguardian.com/education/2026/sep/21/apprenticeship-starts-labour-scheme-skills-revolution
**Relevance score:** 2/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Exclusive: Government warned ‘skills revolution’ at risk amid slow start to project with target of 30,000 starts by end of parliament Labour has been warned its “skills revolution” to tackle youth unemployment risks failure, after its flagship apprenticeship scheme enrolled only 160 young people in its first eight months. The shortfall, highlighted in a report by the Fabian Society, leaves the government well off track of achieving its ambition of 30,000 “foundation apprenticeship” starts by the end of this parliament. Continue reading...

---

## 56. Introducing the Australian Youth Safety Blueprint

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Fri, 18 Sep 2026 12:00:00 GMT
**URL:** https://openai.com/index/australian-youth-safety-blueprint
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

OpenAI introduces the Australian Youth Safety Blueprint, a six-pillar roadmap for safer AI experiences that protect and empower young people.

---

## 57. Helping older adults use AI in everyday life

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Wed, 16 Sep 2026 16:00:00 GMT
**URL:** https://openai.com/index/helping-older-adults-use-ai-in-everyday-life
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

OpenAI and AARP are bringing free, hands-on ChatGPT workshops to 1,000 older adults across 10 U.S. cities to build practical AI skills safely.

---

## 58. Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Tue, 15 Sep 2026 17:05:57 +0000
**URL:** https://deepmind.google/blog/introducing-gemini-3-8-live-and-3-8-live-extended-thinking/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**



---

## 59. AlphaGenome Atlas: A predictive map of every possible DNA letter change in the human genome

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Tue, 08 Sep 2026 14:00:15 +0000
**URL:** https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

AlphaGenome Atlas maps the molecular effects of 9 billion single-letter DNA variants across the human genome.

---

## 60. Introducing WeatherNext 3, our most advanced and accurate global weather AI model

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Thu, 03 Sep 2026 15:02:08 +0000
**URL:** https://deepmind.google/blog/introducing-weathernext-3-our-most-advanced-and-accurate-global-weather-ai-model/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**



---

## 61. Proactive cyber defense for governments and enterprises

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Wed, 02 Sep 2026 16:24:24 +0000
**URL:** https://deepmind.google/blog/proactive-cyber-defense-for-governments-and-enterprises/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**



---

## 62. Introducing Gemini 3.8 Flash and 3.8 Flash Cyber

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Wed, 02 Sep 2026 16:18:31 +0000
**URL:** https://deepmind.google/blog/introducing-gemini-3-8-flash-and-38-flash-cyber/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**



---

## 63. UK should 'team up' with Canada in new Europe alliance, Canadian minister tells BBC

**Source:** BBC Business
**Type:** independent_news
**Published:** Mon, 21 Sep 2026 04:00:38 GMT
**URL:** https://www.bbc.co.uk/news/articles/cmed7p06epxjo?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

It comes after European Commission President proposed "opening the door" for Canada to become an associate member of the EU.

---

## 64. US and China discuss AI safety plan ahead of Trump-Xi summit

**Source:** BBC Business
**Type:** independent_news
**Published:** Mon, 21 Sep 2026 05:50:56 GMT
**URL:** https://www.bbc.co.uk/news/articles/c8vgyzn2d31yo?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Top US and Chinese officials held talks in New York on Sunday ahead of a Trump-Xi summit this week.

---

## 65. Nvidia boss rejects AI extinction fears as 'doomsday narratives'

**Source:** BBC Business
**Type:** independent_news
**Published:** Mon, 21 Sep 2026 06:25:43 GMT
**URL:** https://www.bbc.co.uk/news/articles/cr5ye7p13jg7o?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Jensen Huang's comments come after warnings from AI researchers that the technology could lead to human extinction.

---

## 66. Will you get £13,000 a year when you stop working? Here's how to check

**Source:** BBC Business
**Type:** independent_news
**Published:** Mon, 21 Sep 2026 08:49:45 GMT
**URL:** https://www.bbc.co.uk/news/articles/crq5x74yv6dxo?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

How to find out how much state pension you're likely to receive - and what you can do about it now.

---

## 67. Billionaire Man United owner loses moral high ground after tax exile, Labour chair says

**Source:** BBC Business
**Type:** independent_news
**Published:** Sun, 20 Sep 2026 11:22:21 GMT
**URL:** https://www.bbc.co.uk/news/articles/cm0rexrwjj1vo?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

The billionaire businessman told the BBC he has lost confidence in the UK due to a combination of high taxes and high immigration.

---

## 68. Air traffic control failure ‘fixed’ after flight disruption in Scotland, Northern Ireland and northern England – business live

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Mon, 21 Sep 2026 09:57:33 GMT
**URL:** https://www.theguardian.com/business/live/2026/sep/21/asian-shares-rise-optimism-us-chinese-talks-trade-ai-oil-falls-live-updates
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

UK transport secretary Heidi Alexander warns ‘there may be some delays as things reset’ The UK transport secretary, Heidi Alexander , has just said that the technical issue at Prestwick Centre has been fixed – but warned there could be “some delays as things reset”. She said on X: There has been a further IT issue affecting @NATS. Engineers have fixed the problem and systems are resuming. Continue reading...

---

## 69. Nvidia boss says there is ‘0% chance’ AI destroys the world by 2030

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Mon, 21 Sep 2026 08:27:17 GMT
**URL:** https://www.theguardian.com/technology/2026/sep/21/nvidia-boss-jensen-huang-dismisses-warnings-ai-destroys-world-anthropic
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Jensen Huang dismisses warnings from former Anthropic researcher and others as ‘doomsday narratives’ Business live – latest updates The boss of the chipmaker Nvidia has said AI will not develop to a point that will lead to the extinction of the human race within a few years, rejecting such assertions as overblown “doomsday narratives”. Jensen Huang, the co-founder and chief executive of the $5tn AI chipmaker, said the claims made on social media by the former Anthropic researcher Jacob Coxon that AI could become “superhuman” and kill off humanity within the decade was “irresponsible”. Continue reading...

---

## 70. ‘It’s unrecognisable’: How being a tax haven has changed Jersey

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Mon, 21 Sep 2026 04:00:35 GMT
**URL:** https://www.theguardian.com/uk-news/2026/sep/21/its-unrecognisable-how-being-a-tax-haven-has-changed-jersey
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

While global billionaires and multinational companies have been lured to its shores, many islanders feel left behind and priced out, with food bank use increasing On a late Friday afternoon on the Channel Island of Jersey, tourists and locals are flocking to St Helier’s waterfront where the town’s sprawling beach has emerged at low tide. In one direction, they face the calm waters of St Aubin’s Bay, ringed by a seaside promenade and punctuated with a tidal island hosting the 16th century Elizabeth Castle. Continue reading...

---

## 71. Untitled

**Source:** GOV.UK AI business adoption
**Type:** official_policy
**Published:** 
**URL:** https://www.gov.uk/api/search.json?q=artificial%20intelligence%20business%20adoption&count=5&order=updated-newest
**Relevance score:** 1/5
**Quality note:** Official source: credible context, but may be broad or slow-moving.
**Fetch error:** HTTP Error 422: Unknown Error

**Summary:**



---
