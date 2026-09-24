# Business Source Pack - 2026-09-24

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

## 4. Shippers’ coalition advances Class 8 electric battery truck adoption

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Wed, 23 Sep 2026 15:54:00 -0400
**URL:** https://www.supplychaindive.com/news/shippers-coalition-advances-class-8-electric-battery-truck-adoption/831160/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

Companies such as Microsoft and PepsiCo are aggregating demand to access sustainable transportation more affordably, recently placing an order for 2,500 trucks.

---

## 5. Old Dominion announces 4.9% general rate increase

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Wed, 23 Sep 2026 09:58:00 -0400
**URL:** https://www.supplychaindive.com/news/old-dominion-announces-49-general-rate-increase/830901/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The increase, which applies to a selection of services, is effective Oct. 5.

---

## 6. Amazon debuts direct rail service for Los Angeles-to-East Coast shipments

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Wed, 23 Sep 2026 09:43:00 -0400
**URL:** https://www.supplychaindive.com/news/amazon-debuts-direct-rail-service-for-los-angeles-to-east-coast-shipments/830836/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

Standard Ocean Express moves inventory cross-country faster than other options, the company said.

---

## 7. Plastics get pulled into tariff turmoil

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Wed, 23 Sep 2026 09:35:34 -0400
**URL:** https://www.supplychaindive.com/news/plastics-get-pulled-into-tariff-turmoil/830768/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

&ldquo;Depending on the size of the converter and your influence over the supply chain, there&rsquo;s probably a lot of confusion,&rdquo; said a Rabobank packaging and logistics analyst.

---

## 8. Ocean Spray names chief supply chain officer

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Wed, 23 Sep 2026 07:18:00 -0400
**URL:** https://www.supplychaindive.com/news/ocean-spray-names-chief-supply-chain-officer/830937/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

Brad Hartzell wades into the role leading operations for the company behind Craisins with 25 years of experience.

---

## 9. Webinar: Moving from reactive to preventative maintenance with Samsara

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Thu, 24 Sep 2026 07:35:24 +0000
**URL:** https://www.logisticsmanager.com/webinar-moving-from-reactive-to-preventative-maintenance-with-samsara/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Webinar: Moving from reactive to preventative maintenance with Samsara appeared first on Logistics Manager .

---

## 10. Hacis extends SuperLink China Direct service to Vietnam

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Wed, 23 Sep 2026 16:21:18 +0000
**URL:** https://www.logisticsmanager.com/hacis-extends-superlink-china-direct-service-to-vietnam/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Hacis extends SuperLink China Direct service to Vietnam appeared first on Logistics Manager .

---

## 11. Weather events delay Asian ocean freight, but port operations are recovering

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Wed, 23 Sep 2026 15:48:57 +0000
**URL:** https://www.logisticsmanager.com/weather-events-delay-asian-ocean-freight-but-port-operations-are-recovering/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Weather events delay Asian ocean freight, but port operations are recovering appeared first on Logistics Manager .

---

## 12. Penske Logistics automates bakery fulfilment operation in Illinois

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Wed, 23 Sep 2026 07:37:41 +0000
**URL:** https://www.logisticsmanager.com/penske-logistics-automates-bakery-fulfilment-operation-in-illinois/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Penske Logistics automates bakery fulfilment operation in Illinois appeared first on Logistics Manager .

---

## 13. Link Logistics adds 697,000ft² to US property portfolio

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Wed, 23 Sep 2026 07:17:54 +0000
**URL:** https://www.logisticsmanager.com/link-logistics-adds-697000ft%c2%b2-to-us-property-portfolio/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Link Logistics adds 697,000ft² to US property portfolio appeared first on Logistics Manager .

---

## 14. How B2B Marketers Misunderstand Their Customers

**Source:** MIT Sloan Management Review
**Type:** professional_insight
**Published:** Tue, 15 Sep 2026 11:00:37 +0000
**URL:** https://sloanreview.mit.edu/article/how-b2b-marketers-misunderstand-their-customers/
**Relevance score:** 5/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Nick Lowndes/Ikon Images Businesses are striving to adapt ever faster to keep pace with rapid change, and yet B2B marketing practices have remained surprisingly static. Sure, the tactics have shifted to digital executions, and the use of data has made targeting B2B buyers more precise, but marketers remain rooted in fundamentally flawed assumptions about the [&#8230;]

---

## 15. Air IT launches AI services for SMEs lacking plans - IT Brief UK

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Thu, 24 Sep 2026 07:15:00 GMT
**URL:** https://news.google.com/rss/articles/CBMihAFBVV95cUxPWFVHS0x0ZWxQX2xpcmRuU0xEanVtYTVuUm4tR0tJLWN4T1lJVEgzSHJFamphenl2Z0pqZF9mUmp3bFdwT1hIaWhWWkdaYnRVQnVGOHJsWnY3TkhvaDdGQkNZX1lYMng3SnN2cXpUbWVsOUZNVVBXQl81UzNWc1NPWjM0Tmw?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Air IT launches AI services for SMEs lacking plans IT Brief UK

---

## 16. Air IT Group launches new suite of AI services to close the SME AI decision gap - Edinburgh Chamber of Commerce

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Mon, 21 Sep 2026 11:21:36 GMT
**URL:** https://news.google.com/rss/articles/CBMitgFBVV95cUxQVEZPbUNJSzhDNHk5Zm5Gc0pHelY4azdsRjZ3cGx4cHYyYzRlamtfcjN1LVh2NmFLMGE3c1Nuc1hvam90TmVzVlF0TFE5d1BwQ1ZoamhUcDhWWHUyMEZuaXdDQ3VGRnV3Zl9BVU8wX1gxbVVtUkVQMXJ0YmoydmdncWl4NjJ5WVp6RnAxbVNqSUVFV1RDMksydGlLaFFrVGFDcTVjOXp3OS1IejNrbUtHdGRsYlBFdw?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Air IT Group launches new suite of AI services to close the SME AI decision gap Edinburgh Chamber of Commerce

---

## 17. Anthropic Dominates UK SME AI Spending as Adoption Surges 1,000% Since 2023 - FF News

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Mon, 14 Sep 2026 07:00:00 GMT
**URL:** https://news.google.com/rss/articles/CBMisgFBVV95cUxNelREUTY5VzJNcFFKbHR2UmQ5TEFMcFYyQkdrcGpwdEE1UERZNTkxM29NSzRqSng5WER5Q2lDSVlnTWdXc1JIVjJQSHNpbTY3MGc0V0xBak5ablR0SGJMWnhjb1h4V2t3LUZseU83MHZRd0Y4d3ptbU9kS0hjUmp6RklnU0EtV3E1NTdMS0tiMGdpdHNzTUFBM3BmWl9UT19DNUE0N1FFYmFnZ2RCSEpHa3lB?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Anthropic Dominates UK SME AI Spending as Adoption Surges 1,000% Since 2023 FF News

---

## 18. UK business leaders sceptical about use of AI in recruitment - Personnel Today

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Fri, 18 Sep 2026 10:41:49 GMT
**URL:** https://news.google.com/rss/articles/CBMimwFBVV95cUxQY0FHNTA0R2pDekF4ZFJSV0wzY09tMTJKdFRmXzdMVl9mZDdiYjBfU1pjQ19DSUhBZDJrTXBNZi1haC1PaUlTWC1SazNfRm50S292X0ZCTXZJbWJrMzNkVk9xZDgyYkh4SmhmSjBxd2tyUzlmSF9PdWE5OTRsX2JsUVMyeHRYdDVBTkVFMVhSTXRPSnBRcEJZZzB2RQ?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

UK business leaders sceptical about use of AI in recruitment Personnel Today

---

## 19. Why small businesses could be the big winners from AI - UKTN

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Wed, 16 Sep 2026 11:11:59 GMT
**URL:** https://news.google.com/rss/articles/CBMikwFBVV95cUxPQzA4OGJsazhjekFQZlRyMFNXbWZtQUo2Tlp2a0FNMTloX3VFZ2pvTkVWb2Vjdi1abjBscG92U2kwTUgyTkpSRlAzR19nd204M0d4MkViNXRabFRGck5GMkJ0QVc2bmRfakRPa0JnM0R4S2stLU40NVg5V3dET0twVTNJeVVuSDVia3Y2RHJEUTlldlU?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Why small businesses could be the big winners from AI UKTN

---

## 20. How AI Is Transforming India's FMCG Supply Chain, Distribution & Demand Forecasting - logisticsinsider.in

**Source:** Google News - FMCG AI supply chain UK
**Type:** news_search
**Published:** Mon, 27 Jul 2026 07:00:00 GMT
**URL:** https://news.google.com/rss/articles/CBMisgFBVV95cUxOUU1Nd0QzTTU0YUJYQ2hiVHc0c3pCSmQzOXhhZDBvTnlkZHJjVmZUTDZlenN6VzhFSlFoTHlaQkNXTEJ3MkFpQUJ4amJuVllFWEsxS0VUNk9HeEk3bXNybTJNLVRIbGMyT2N5b3FoY0M1MEdoOHZhOWlaT3NOWk9CLWtFeHd3VWZnZHNESEt3V0w2cGxBWGxDYUpOUjZCVUI4M2xTeHdKY1pNLUtWbE1JcGFB?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

How AI Is Transforming India's FMCG Supply Chain, Distribution & Demand Forecasting logisticsinsider.in

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
**Published:** Sun, 20 Sep 2026 13:19:21 GMT
**URL:** https://news.google.com/rss/articles/CBMivgFBVV95cUxPMlZzS2pwSTBleTJObnZFYVhnby1wSzhfaWdUS243aW5udEVFOEhIeVVxUlBoUlBLdW5BSFUzUURLWENVMWxidDNBZ1hPVXptM2VRRHdGU0p3NzZrNFBBbFlzVnE2UDM1MEZSRzd2bXdteHRaVkZqZW05WjdQemdkbHI3XzNUOEZ4WUIxcGlKSzZJYU5WdFowYmN0SjJDRGtzM3dZb01nVllmM3NSWEFvZ0VSVXlRN2hzcDNFdG1R?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Building Enterprise AI Workflow Automation Systems: Key Architectures and Best Practices Nasscom

---

## 23. AI Automation Market Size, Share, Growth Forecast, 2034 - Fortune Business Insights

**Source:** Google News - business intelligence AI workflow
**Type:** news_search
**Published:** Mon, 17 Aug 2026 07:00:00 GMT
**URL:** https://news.google.com/rss/articles/CBMidkFVX3lxTE9vdUdZcjJRc1VBTWZvOS1aazE3MzVvQjVwXzA0bmNnaTlSUWhZcXYwZW1USnVobmxWVUNETXZwT1hPLU5JM2UzVElWdXpnLXRsdklGZkNyaEVMeWpLZWVQNUNqdWFvOGF0cEpza1JBU25pWWYteEE?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

AI Automation Market Size, Share, Growth Forecast, 2034 Fortune Business Insights

---

## 24. Parakeet Health lands major AI partnership with national dermatology group Qualderm - Fierce Healthcare

**Source:** Google News - business intelligence AI workflow
**Type:** news_search
**Published:** Tue, 08 Sep 2026 07:00:00 GMT
**URL:** https://news.google.com/rss/articles/CBMixAFBVV95cUxNTWw3VFNsODVPcnY2SWE0V3FHTUp2NnRySnh1azVjUkRmTmRnQjBUWXRhWXpjeWhBYWs3MWI0bTFzek1DUWZLN0Zid1dGOVlLY1NNZHFYVXRiRWZsaUdwWE1xdEtnemJuVmtpVU8welNBdzNGSzY5RVpFaTJjQnBlOVl3ZHlweUE0b3cyWjVON0k2Z2F0cW0tOHBJWGUwUlM5Z2xILVliNjJ5MmhlaWZ2T2JMdmtPMTJpMGQ3dVcxSGw5eFBI?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Parakeet Health lands major AI partnership with national dermatology group Qualderm Fierce Healthcare

---

## 25. Moody's: retail P&C distribution faces the fastest AI disruption of any financial services segment - Insurance Business

**Source:** Google News - retail distribution AI UK
**Type:** news_search
**Published:** Tue, 04 Aug 2026 07:00:00 GMT
**URL:** https://news.google.com/rss/articles/CBMi-gFBVV95cUxQVTNEVXBSOXJHMFFfcmpESWpJZEw2MEE3UHR5X1FGOUpkSVFrX2x2Z0RheXJYX0VQcUpxVFRQckRfOE1LM1NhSkhiaXJKWmxIUUpmd2dEdHRVcy05dGdHaEF1OXZpRWpBWTI5YXdxOUxUclpOZTRsM2tGMnRNd3pQdlA1NHUtMzBLMEtGYzBTTVpmNmtTbnQzcDhXOGcyczl4MUtlMmlWbGxuYkVQU0pqSDRkVzZZN3JwRnNYUXl5X3hJaGZGNGhrVHQ2bUktbHlYVGk2RUg4MThjTUFOYmxvMGx2dnB4ZXR6YVZwbFNnVlNfa2VXbXBULU9B?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Moody's: retail P&C distribution faces the fastest AI disruption of any financial services segment Insurance Business

---

## 26. ONS business, economy and technology statistics

**Source:** ONS
**Type:** official_watchlist
**Published:** 2026-09-24
**URL:** https://www.ons.gov.uk/
**Relevance score:** 5/5
**Quality note:** Official source: credible context, but may be broad or slow-moving.
**Manual check:** Yes - this source is included as a watchlist item.

**Summary:**

Official UK statistics source for business conditions, productivity, retail, labour market and economic context.

---

## 27. OECD AI, SMEs, productivity and digital adoption

**Source:** OECD
**Type:** official_watchlist
**Published:** 2026-09-24
**URL:** https://www.oecd.org/
**Relevance score:** 5/5
**Quality note:** Official source: credible context, but may be broad or slow-moving.
**Manual check:** Yes - this source is included as a watchlist item.

**Summary:**

Useful for international context on SME digital adoption, productivity, AI diffusion and policy.

---

## 28. The Grocer - UK FMCG and grocery sector

**Source:** The Grocer
**Type:** fmcg_watchlist
**Published:** 2026-09-24
**URL:** https://www.thegrocer.co.uk/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.
**Manual check:** Yes - this source is included as a watchlist item.

**Summary:**

Specialist UK FMCG and grocery source. Useful for suppliers, wholesalers, pricing, retail pressure and distribution signals.

---

## 29. IGD grocery, retail and supply-chain insight

**Source:** IGD
**Type:** fmcg_watchlist
**Published:** 2026-09-24
**URL:** https://www.igd.com/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.
**Manual check:** Yes - this source is included as a watchlist item.

**Summary:**

Useful for grocery, retail, wholesale and supply-chain context.

---

## 30. Kantar retail and FMCG insights

**Source:** Kantar
**Type:** fmcg_watchlist
**Published:** 2026-09-24
**URL:** https://www.kantar.com/uki/industries/retail
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.
**Manual check:** Yes - this source is included as a watchlist item.

**Summary:**

Professional insight source for FMCG, retail, consumers and brand performance.

---

## 31. NielsenIQ retail and FMCG insights

**Source:** NielsenIQ
**Type:** fmcg_watchlist
**Published:** 2026-09-24
**URL:** https://nielseniq.com/global/en/insights/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.
**Manual check:** Yes - this source is included as a watchlist item.

**Summary:**

Professional retail and FMCG data source for market trends, consumer behaviour and category performance.

---

## 32. From portal-hopping to instant answers: HEMA’s journey with MCP and Amazon Bedrock

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Wed, 23 Sep 2026 18:41:09 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/from-portal-hopping-to-instant-answers-hemas-journey-with-mcp-and-amazon-bedrock/
**Relevance score:** 4/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

HEMA, a 100-year-old Dutch retailer, turned developer portal-hopping into instant answers by building HAL, an internal AI assistant on Amazon Bedrock AgentCore. Using Model Context Protocol (MCP), HAL delivers governed knowledge inside the tools teams already use, with no AWS credentials on the client and security anchored in Microsoft Entra ID.

---

## 33. Use open weight models as your AI coding agent with Amazon Bedrock

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Wed, 23 Sep 2026 18:17:44 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/use-open-weight-models-as-your-ai-coding-agent-with-amazon-bedrock/
**Relevance score:** 4/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Pair OpenCode, an open-source terminal-native AI coding agent, with open weight models on Amazon Bedrock to get a secure, flexible, pay-per-use coding assistant. Learn how to configure multi-model workflows, match the right model to each task, and keep your data in your own AWS account with no infrastructure to manage.

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

## 35. Harnessing AI to make mining safer

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Wed, 23 Sep 2026
**URL:** https://www.mckinsey.com/industries/metals-and-mining/our-insights/harnessing-ai-to-make-mining-safer
**Relevance score:** 4/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

AI could improve both safety and productivity by anticipating problems before they arise, detecting worker fatigue and automating dangerous tasks.

---

## 36. India’s new insurance track: The marathon becomes an AI-led decathlon

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Wed, 23 Sep 2026
**URL:** https://www.mckinsey.com/industries/financial-services/our-insights/indias-new-insurance-track-the-marathon-becomes-an-ai-led-decathlon
**Relevance score:** 4/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

As India’s economy continues to ramp up, insurers have an opportunity to capture value by improving productivity, modernizing operating models, and scaling technology and AI across the enterprise.

---

## 37. Alarm bells sound in Brussels as EU sales of Chinese hybrid cars rocket

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Thu, 24 Sep 2026 08:34:46 GMT
**URL:** https://www.theguardian.com/business/2026/sep/24/eu-sales-chinese-hybrid-cars-rocket
**Relevance score:** 4/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Explosive growth in imported vehicles omitted from EV tariffs fuels concern for future of European carmakers EU imports three times more from China than bloc exports there Business news – live updates Sales of Chinese hybrid cars have rocketed in the EU in the past four and a half years, new data shows, underlining growing concerns in Brussels over the future of the European car industry. In 2022, just 659 Chinese-made fully hybrid cars (vehicles in which the petrol or diesel engine charge the motor and battery) were sold in the EU. However, after Brussels imposed anti-subsidy tariffs on fully electric cars from China in 2024 , sales of hybrids have shot up to 160,662 in the first seven months of this year. Continue reading...

---

## 38. Housebuilder Vistry slashes profit forecasts as losses balloon

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Thu, 24 Sep 2026 09:00:52 GMT
**URL:** https://www.theguardian.com/business/2026/sep/24/housebuilder-vistry-slashes-profit-forecasts-as-losses-balloon
**Relevance score:** 4/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Firm unveils further cost-cutting plan including job losses blaming poor summer sales of private homes Business live – latest updates Vistry Group, one of Britain’s biggest housebuilders, has slashed its annual profit expectations after half-year losses ballooned as it grappled with a £600m pile of unsold homes. Adam Daniel, the new chief executive of the Bovis Homes and Countryside owner, insisted that “the issues can be fixed”, as he set out a detailed turnaround plan that involves pulling out of private sales in south-east England and slimming operations to turn Vistry into a more focused, 12,000-homes-a-year builder. Continue reading...

---

## 39. Bring more intelligence to everyday work with GPT-6 Sol and GPT-6 Luna on Amazon Bedrock

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Tue, 22 Sep 2026 18:10:22 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/bring-more-intelligence-to-everyday-work-with-gpt-6-sol-and-gpt-6-luna-on-amazon-bedrock/
**Relevance score:** 3/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

GPT-6 Sol and GPT-6 Luna are now generally available on Amazon Bedrock, giving you more options to match intelligence and efficiency to each workload.

---

## 40. Claude Opus 5.5 is now available on AWS

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Tue, 22 Sep 2026 17:28:01 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/claude-opus-5-5-is-now-available-on-aws/
**Relevance score:** 3/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Claude Opus 5.5, Anthropic's most capable Opus model for agentic coding, knowledge work, and long-running tasks, is now available on Amazon Bedrock and Claude Platform on AWS. This post covers what's new in Opus 5.5, practical guidance, and how to start building with the model on Amazon Bedrock.

---

## 41. Power BI sample reports, refreshed with modern visual defaults

**Source:** Microsoft Power BI Blog
**Type:** bi_tooling
**Published:** Wed, 02 Sep 2026 16:00:00 GMT
**URL:** https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Power-BI-sample-reports-refreshed-with-modern-visual-defaults/ba-p/5363807
**Relevance score:** 3/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Microsoft has refreshed its Power BI sample reports with modern visual defaults, stronger semantic models, mobile-optimized layouts, and newer authoring features to help creators build clearer, more effective reports.

---

## 42. Five Urgent Priorities for CMOs in 2027

**Source:** MIT Sloan Management Review
**Type:** professional_insight
**Published:** Tue, 22 Sep 2026 11:00:03 +0000
**URL:** https://sloanreview.mit.edu/article/five-urgent-priorities-for-cmos-in-2027/
**Relevance score:** 3/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Matt Harrison Clough/Ikon Images In an unpredictable economy and fractured media landscape, marketing leaders are navigating a period of profound transformation and disruption — and as AI technologies evolve, the pace of change will only increase. In response, the highest priorities of chief marketing officers today are shifting, and understanding their concerns is essential to [&#8230;]

---

## 43. Maintenance meets AI: A proven approach for asset-heavy industries

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Wed, 23 Sep 2026
**URL:** https://www.mckinsey.com/capabilities/operations/our-insights/maintenance-meets-ai-a-proven-approach-for-asset-heavy-industries
**Relevance score:** 3/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Embedding the latest AI and technology within day-to-day operations is transforming maintenance from a cost center into a significant driver of value.

---

## 44. Untitled

**Source:** GOV.UK SMEs digital adoption
**Type:** official_policy
**Published:** 
**URL:** https://www.gov.uk/api/search.json?q=SME%20digital%20adoption%20artificial%20intelligence&count=5&order=updated-newest
**Relevance score:** 3/5
**Quality note:** Official source: credible context, but may be broad or slow-moving.
**Fetch error:** HTTP Error 422: Unknown Error

**Summary:**



---

## 45. Untitled

**Source:** GOV.UK business productivity technology
**Type:** official_policy
**Published:** 
**URL:** https://www.gov.uk/api/search.json?q=business%20productivity%20technology%20SME&count=5&order=updated-newest
**Relevance score:** 3/5
**Quality note:** Official source: credible context, but may be broad or slow-moving.
**Fetch error:** HTTP Error 422: Unknown Error

**Summary:**



---

## 46. Agentic conversational video intelligence built on AWS

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Wed, 23 Sep 2026 18:21:54 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/agentic-conversational-video-intelligence-built-on-aws/
**Relevance score:** 2/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Learn how to build a conversational video intelligence solution on AWS using an agentic architecture. A single Strands Agents SDK agent orchestrates Amazon Bedrock, Amazon Rekognition, and Amazon Transcribe at runtime, deciding which service to call so you can ask natural language questions about your videos and get answers in seconds.

---

## 47. Why Design Thinking Needs a Responsibility Reboot

**Source:** MIT Sloan Management Review
**Type:** professional_insight
**Published:** Wed, 23 Sep 2026 11:00:47 +0000
**URL:** https://sloanreview.mit.edu/article/why-design-thinking-needs-a-responsibility-reboot/
**Relevance score:** 2/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Marie Montocchio/Ikon Images For years, social media companies have come under fire for promoting divisive, false, and dangerous content in order to monetize user engagement. But in March, when a jury in Los Angeles Superior Court found Meta and Google liable for causing harm to users due to the addictive nature of their products, the [&#8230;]

---

## 48. How Sustainability Transformations Quietly Lose Their Edge

**Source:** MIT Sloan Management Review
**Type:** professional_insight
**Published:** Mon, 21 Sep 2026 11:00:43 +0000
**URL:** https://sloanreview.mit.edu/article/how-sustainability-transformations-quietly-lose-their-edge/
**Relevance score:** 2/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Gillian Blease/Ikon Images Corporate sustainability is facing headwinds. Net-zero pledges are being quietly walked back. Regulatory pressure is loosening in some parts of the world. Shareholders are demanding stronger business cases. Inside companies, sustainability leaders sometimes spend more time defending their function than expanding it. The familiar question “Where is the value?” has returned with [&#8230;]

---

## 49. How AI Creates a Capability Mirage

**Source:** MIT Sloan Management Review
**Type:** professional_insight
**Published:** Mon, 14 Sep 2026 11:00:15 +0000
**URL:** https://sloanreview.mit.edu/article/how-ai-creates-a-capability-mirage/
**Relevance score:** 2/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

PPaint/Ikon Images Dry rot. A Potemkin village. The Wizard of Oz. What do those things have in common? In each case, they may look good on the surface, but it’s only an illusion. Wood afflicted with dry rot looks just fine until the tree it’s in topples down. Grigory Potemkin is said to have tried [&#8230;]

---

## 50. Author Talks: The business of owning a sports team

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Wed, 23 Sep 2026
**URL:** https://www.mckinsey.com/featured-insights/mckinsey-on-books/author-talks-the-business-of-owning-a-sports-team
**Relevance score:** 2/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

How does business ownership compare with owning a sports team? Baltimore Orioles owner David M. Rubenstein explains the leadership mindset, culture building, and long-term thinking that team ownership requires.

---

## 51. Rewiring procurement in resources: Making judgment an enduring asset

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Wed, 23 Sep 2026
**URL:** https://www.mckinsey.com/capabilities/operations/our-insights/rewiring-procurement-in-resources-making-judgment-an-enduring-asset
**Relevance score:** 2/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

For procurement leaders in the resources sector, using AI to codify the function’s category expertise does not just capture more value—it turns hard-won judgment into a compounded, durable advantage.

---

## 52. UK interest rates ‘increasingly likely to rise’ if energy prices remain high, Bank of England’s Lombardelli warns – business live

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Thu, 24 Sep 2026 09:13:31 GMT
**URL:** https://www.theguardian.com/business/live/2026/sep/24/global-bond-sell-off-us-economy-fears-stock-markets-ftse-dollar-pound-latest-news-updates
**Relevance score:** 2/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Rolling coverage of the latest economic and financial news Newsflash: A Bank of England deputy governor is warning that interest rates will be raised, if necessary, to combat the risk of persistent inflationary pressures from higher oil prices. Clare Lombardelli is telling the Sixth Biennial Conference on Macroeconomic Policy in Warsaw that the energy shock due to the conflict in the Middle East is likely to keep pushing UK inflation higher in the coming months. Strong demand for AI components is already pushing up global export prices and weather-related shocks add upside risks. On the other hand, trade diversion is reducing inflation. The longer higher energy prices persist, the greater the risk that indirect effects build and that inflation expectations, wage bargaining and price-setting behaviour begin to adjust in response. On that basis, policy is increasingly likely to need to tighten if elevated energy prices persist, absent clear evidence of disinflation or weaker activity. But this is by no means suggesting that monetary policy should respond mechanically to movements in energy prices. The key issue is not the spot price of energy itself but the interaction of the underly

---

## 53. Two years of OpenAI Academy

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Wed, 23 Sep 2026 16:00:00 GMT
**URL:** https://openai.com/index/two-years-of-openai-academy
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Marking two years of OpenAI Academy and bringing AI skills to even more communities.

---

## 54. OpenAI extends cyber access to Ukraine for civilian defense

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Wed, 23 Sep 2026 13:00:00 GMT
**URL:** https://openai.com/index/openai-extends-cyber-access-to-ukraine-for-civilian-defense
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

OpenAI is extending access to its Daybreak program to the Government of Ukraine to support the cyber defense of civilian infrastructure.

---

## 55. Sam Altman’s remarks at the United Nations Security Council

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Wed, 23 Sep 2026 12:00:00 GMT
**URL:** https://openai.com/index/sam-altman-un-security-council-remarks
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

OpenAI CEO Sam Altman discusses AI safety, human control, and international cooperation in remarks to the United Nations Security Council.

---

## 56. Harvey turns legal context into stronger drafts with GPT-6 Astra

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Wed, 23 Sep 2026 12:00:00 GMT
**URL:** https://openai.com/index/harvey-from-context-to-confidence-with-astra
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

GPT-6 Astra produces more structured, context-aware legal documents, freeing lawyers to focus on strategy.

---

## 57. How invideo improves color grading 3x with GPT‑6 Astra

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Wed, 23 Sep 2026 12:00:00 GMT
**URL:** https://openai.com/index/invideo-builds-with-gpt-6-astra
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

With GPT‑6 Astra, invideo plans edits with greater precision, improves color correction and grading threefold, and produces 50 custom effects in one day.

---

## 58. Advancing Private AI Compute with secure, server-side memory

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Wed, 23 Sep 2026 16:00:57 +0000
**URL:** https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Introducing private, server-side memory to Private AI Compute for personal AI.

---

## 59. Gemini 3.8 text-to-speech says hello

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Wed, 23 Sep 2026 15:25:14 +0000
**URL:** https://deepmind.google/blog/say-hello-to-gemini-38-text-to-speech/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**



---

## 60. Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Tue, 15 Sep 2026 17:05:57 +0000
**URL:** https://deepmind.google/blog/introducing-gemini-3-8-live-and-3-8-live-extended-thinking/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**



---

## 61. AlphaGenome Atlas: A predictive map of every possible DNA letter change in the human genome

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Tue, 08 Sep 2026 14:00:15 +0000
**URL:** https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

AlphaGenome Atlas maps the molecular effects of 9 billion single-letter DNA variants across the human genome.

---

## 62. Introducing WeatherNext 3, our most advanced and accurate global weather AI model

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Thu, 03 Sep 2026 15:02:08 +0000
**URL:** https://deepmind.google/blog/introducing-weathernext-3-our-most-advanced-and-accurate-global-weather-ai-model/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**



---

## 63. £170 a bag? Protein users squeezed as prices soar

**Source:** BBC Business
**Type:** independent_news
**Published:** Wed, 23 Sep 2026 23:12:01 GMT
**URL:** https://www.bbc.co.uk/news/articles/cm93e2gz8y41o?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Consumers are feeling the pinch from the rising cost of protein.

---

## 64. They were labelled 'pervert glasses'. Will a camera-free version transform their image?

**Source:** BBC Business
**Type:** independent_news
**Published:** Thu, 24 Sep 2026 00:50:24 GMT
**URL:** https://www.bbc.co.uk/news/articles/cwp80l0my1x2o?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Meta has unveiled audio-only smart glasses, with some questioning whether it is a response to the backlash over privacy.

---

## 65. Lidl banned from selling copycat Birkenstock sandals, Dutch court rules

**Source:** BBC Business
**Type:** independent_news
**Published:** Wed, 23 Sep 2026 21:25:01 GMT
**URL:** https://www.bbc.co.uk/news/articles/cqrm90m2g1dzo?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Lidl must also compensate Birkenstock and pay its legal fees, according to the court ruling

---

## 66. Trump and Xi come face-to-face as US and China jostle for dominance over AI

**Source:** BBC Business
**Type:** independent_news
**Published:** Wed, 23 Sep 2026 22:01:17 GMT
**URL:** https://www.bbc.co.uk/news/articles/c6gqdgg8w59xo?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

The US and China are vying for AI supremacy while seeking to keep it under human control.

---

## 67. How the oil capital of the US welcomed a solar power boom

**Source:** BBC Business
**Type:** independent_news
**Published:** Wed, 23 Sep 2026 23:12:22 GMT
**URL:** https://www.bbc.co.uk/news/articles/cmx2zxv6936zo?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Texas is now the country's biggest producer of solar-farmed electricity.

---

## 68. UK ‘losing up to £6.5bn a year in EU trade’ without post-Brexit product deal

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Thu, 24 Sep 2026 08:48:11 GMT
**URL:** https://www.theguardian.com/politics/2026/sep/24/uk-losing-billions-in-eu-trade-due-to-mismatched-product-rules
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

IPPR finds failure to align testing standards has forced companies to abandon exporting to EU and is costing costing 0.18% of national income The UK is losing out on annual exports to the EU that could be worth as much as £6.5bn without a deal with Brussels that allows manufacturers to jettison duplicate product testing. In the latest attempt to calculate the loss of trade with the EU after Brexit, the IPPR thinktank said many companies have given up selling goods to the EU or set up subsidiaries inside the trade bloc after successive governments failed to secure a mutual recognition agreement that would avoid the extra administration costs. Motor vehicle and part exports would have been between £2.48bn and £3.42bn higher each year. Electronic exports could have been between £1.17bn and £1.67bn higher. Pharmaceutical exports would have had an estimated annual uplift of between £740m and £820m. Continue reading...

---

## 69. UK defence contractors to offer 40,000 apprenticeships, placements and jobs

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Wed, 23 Sep 2026 21:00:00 GMT
**URL:** https://www.theguardian.com/education/2026/sep/23/uk-defence-contractors-40000-apprenticeships-work-placements-jobs-wes-streeting
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Wes Streeting says he leads a ‘ministry for growth’ as Labour seeks to show more defence spending will create UK jobs Defence contractors have promised to create 40,000 apprenticeships, work experience placements and jobs for young people each year, as Wes Streeting claimed to be overseeing a “ministry for growth”. Labour is keen to demonstrate that the rapid increase in defence spending planned for the coming years, which may necessitate tax rises, will result in jobs in the UK. Continue reading...

---

## 70. Untitled

**Source:** GOV.UK AI business adoption
**Type:** official_policy
**Published:** 
**URL:** https://www.gov.uk/api/search.json?q=artificial%20intelligence%20business%20adoption&count=5&order=updated-newest
**Relevance score:** 1/5
**Quality note:** Official source: credible context, but may be broad or slow-moving.
**Fetch error:** HTTP Error 422: Unknown Error

**Summary:**



---
