# Business Source Pack - 2026-09-25

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

## 4. Companies channel IEEPA tariff refunds into their coffers, Atlanta Fed says

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Thu, 24 Sep 2026 12:47:00 -0400
**URL:** https://www.supplychaindive.com/news/companies-channel-ieepa-tariff-refunds-into-their-coffers-atlanta-fed-says/831169/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

While most firms are keeping the returned cash, the institution said &ldquo;a nontrivial portion&rdquo; of refunds is being used to benefit customers and employees.

---

## 5. US, China to extend trade war truce by 2 months

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Thu, 24 Sep 2026 10:55:00 -0400
**URL:** https://www.supplychaindive.com/news/us-china-to-extend-trade-war-truce-by-2-months/831251/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The pact reached last year to lower tariffs and suspend other trade actions will stay in effect until Jan. 10, Treasury Secretary Scott Bessent told Fox News.

---

## 6. Amazon: AI supply chain agents among seller upgrades

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Thu, 24 Sep 2026 09:00:00 -0400
**URL:** https://www.supplychaindive.com/news/amazon-ai-supply-chain-agents-among-seller-upgrades/831164/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The company will offer inbound planning and aged inventory agents as part of a larger push to help sellers grow internationally.

---

## 7. Lowe’s debuts drone delivery pilot with Wing, DoorDash

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Thu, 24 Sep 2026 08:00:00 -0400
**URL:** https://www.supplychaindive.com/news/lowes-debuts-drone-delivery-pilot-with-wing-doordash/831162/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The initial rollout at a North Carolina store involves over 100 SKUs and could later expand to other locations.

---

## 8. Want a smart tariff strategy? Lawyer tells CFOs to go back to basics

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Thu, 24 Sep 2026 07:30:00 -0400
**URL:** https://www.supplychaindive.com/news/want-a-smart-tariff-strategy-lawyer-tells-cfos-to-go-back-to-basics/831204/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

Executives should be mindful that earnings calls are effectively a &ldquo;voluntary deposition,&rdquo; Terence Lau, dean of Syracuse University&rsquo;s College of Law, said.

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

## 10. Waitrose commits to responsible cocoa sourcing in expanded Tony’s Open Chain partnership

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Thu, 24 Sep 2026 11:17:34 +0000
**URL:** https://www.logisticsmanager.com/waitrose-commits-to-responsible-cocoa-sourcing-in-expanded-tonys-open-chain-partnership/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Waitrose commits to responsible cocoa sourcing in expanded Tony&#8217;s Open Chain partnership appeared first on Logistics Manager .

---

## 11. Webinar: Moving from reactive to preventative maintenance with Samsara

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Thu, 24 Sep 2026 07:35:24 +0000
**URL:** https://www.logisticsmanager.com/webinar-moving-from-reactive-to-preventative-maintenance-with-samsara/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Webinar: Moving from reactive to preventative maintenance with Samsara appeared first on Logistics Manager .

---

## 12. Hacis extends SuperLink China Direct service to Vietnam

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Wed, 23 Sep 2026 16:21:18 +0000
**URL:** https://www.logisticsmanager.com/hacis-extends-superlink-china-direct-service-to-vietnam/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Hacis extends SuperLink China Direct service to Vietnam appeared first on Logistics Manager .

---

## 13. Weather events delay Asian ocean freight, but port operations are recovering

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Wed, 23 Sep 2026 15:48:57 +0000
**URL:** https://www.logisticsmanager.com/weather-events-delay-asian-ocean-freight-but-port-operations-are-recovering/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Weather events delay Asian ocean freight, but port operations are recovering appeared first on Logistics Manager .

---

## 14. Penske Logistics automates bakery fulfilment operation in Illinois

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Wed, 23 Sep 2026 07:37:41 +0000
**URL:** https://www.logisticsmanager.com/penske-logistics-automates-bakery-fulfilment-operation-in-illinois/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Penske Logistics automates bakery fulfilment operation in Illinois appeared first on Logistics Manager .

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

## 16. Air IT launches AI services for SMEs lacking plans - IT Brief UK

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Thu, 24 Sep 2026 07:15:00 GMT
**URL:** https://news.google.com/rss/articles/CBMihAFBVV95cUxPWFVHS0x0ZWxQX2xpcmRuU0xEanVtYTVuUm4tR0tJLWN4T1lJVEgzSHJFamphenl2Z0pqZF9mUmp3bFdwT1hIaWhWWkdaYnRVQnVGOHJsWnY3TkhvaDdGQkNZX1lYMng3SnN2cXpUbWVsOUZNVVBXQl81UzNWc1NPWjM0Tmw?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Air IT launches AI services for SMEs lacking plans IT Brief UK

---

## 17. Sustainability Concerns Present a Serious Barrier to AI Adoption for SME’S - Business News Wales

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Tue, 22 Sep 2026 02:22:47 GMT
**URL:** https://news.google.com/rss/articles/CBMipwFBVV95cUxOcW1mT3k3d0pvMTNDanpQZTZ1TFBHb2pWYkdTc2lqRGlaWi1YSmREbWxHell2WFJ3OGlsUkY4SUE3RzVPX3E3MVRFaGJHZXhVMmIzTmxRcl93a3E2WXVPdllOWE82SF9aeWpySGRUTmtMa0RfMzk5U1dvRTR3RExCWlMwSDNVbngtX3hBenUzVHZ4SEs2U29RbDZ1Qk5RSG9nbGxid204NA?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Sustainability Concerns Present a Serious Barrier to AI Adoption for SME’S Business News Wales

---

## 18. Anthropic Dominates UK SME AI Spending as Adoption Surges 1,000% Since 2023 - FF News

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Mon, 14 Sep 2026 07:00:00 GMT
**URL:** https://news.google.com/rss/articles/CBMisgFBVV95cUxNelREUTY5VzJNcFFKbHR2UmQ5TEFMcFYyQkdrcGpwdEE1UERZNTkxM29NSzRqSng5WER5Q2lDSVlnTWdXc1JIVjJQSHNpbTY3MGc0V0xBak5ablR0SGJMWnhjb1h4V2t3LUZseU83MHZRd0Y4d3ptbU9kS0hjUmp6RklnU0EtV3E1NTdMS0tiMGdpdHNzTUFBM3BmWl9UT19DNUE0N1FFYmFnZ2RCSEpHa3lB?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Anthropic Dominates UK SME AI Spending as Adoption Surges 1,000% Since 2023 FF News

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

## 20. Are business decision makers in the UK embracing AI? - YouGov

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Mon, 14 Sep 2026 07:00:00 GMT
**URL:** https://news.google.com/rss/articles/CBMilgFBVV95cUxNT0h6bWYxaEpwZ0t0WF9Tb1BBejJnaGJ2d2FHZElyVUFMRFlUaTBUcVpGeUZnS1c3dmdadUJDZjNEc2tTaXNwbndVcnpkbE0xZUJISEtlZk9aZkJGclFKXzZaei1LZ2lmUW5MS0FMUlZuNUp6bzhkOXphOFVrOVBkdlQtQ1F2TDB5SnVWMlg0dUF0V2NFTGc?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Are business decision makers in the UK embracing AI? YouGov

---

## 21. Green Logistics Market Size, Share | Growth Report [2026-2034] - Fortune Business Insights

**Source:** Google News - FMCG AI supply chain UK
**Type:** news_search
**Published:** Mon, 31 Aug 2026 07:00:00 GMT
**URL:** https://news.google.com/rss/articles/CBMieEFVX3lxTE52RHl1amJBbkxYT2JDNVZ6NmdCMzlxd0Q1M0JXV2JMNVZ2ZmdRZjdKZXZvMElkRW1xQmItaVhXZzdlRnBneEhWSmt2RWFmM2Y4UUdZaE5GR0ppMzRsMlJxTWhNUUtnQkxxWVRJRlE4Tkl5dlh0Q01RZQ?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Green Logistics Market Size, Share | Growth Report [2026-2034] Fortune Business Insights

---

## 22. Innowise joins Creatio partner ecosystem to deploy AI workflows - Portal ERP

**Source:** Google News - business intelligence AI workflow
**Type:** news_search
**Published:** Tue, 15 Sep 2026 09:29:08 GMT
**URL:** https://news.google.com/rss/articles/CBMinAFBVV95cUxPSFFXRzhfOE45RzJuN2VGRFZpYkdqOGpxSi1NWDZyQktla0hvaGJNcUFHWFZQaExfRXZLTEJwaUlINGFoZWhmUk84eHRqRlk4RzJGN0RqLUNISVlsNTcxSnJJa1d4OVd0TkRYMk5XYzFSMGVhVUVtSDVkUUNUY3ludTc4MFZoY0FiblJROG5HQ3h3ekp4cU5BN01UQUU?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Innowise joins Creatio partner ecosystem to deploy AI workflows Portal ERP

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

## 24. Building Enterprise AI Workflow Automation Systems: Key Architectures and Best Practices - Nasscom

**Source:** Google News - business intelligence AI workflow
**Type:** news_search
**Published:** Sun, 20 Sep 2026 13:19:21 GMT
**URL:** https://news.google.com/rss/articles/CBMivgFBVV95cUxPMlZzS2pwSTBleTJObnZFYVhnby1wSzhfaWdUS243aW5udEVFOEhIeVVxUlBoUlBLdW5BSFUzUURLWENVMWxidDNBZ1hPVXptM2VRRHdGU0p3NzZrNFBBbFlzVnE2UDM1MEZSRzd2bXdteHRaVkZqZW05WjdQemdkbHI3XzNUOEZ4WUIxcGlKSzZJYU5WdFowYmN0SjJDRGtzM3dZb01nVllmM3NSWEFvZ0VSVXlRN2hzcDNFdG1R?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Building Enterprise AI Workflow Automation Systems: Key Architectures and Best Practices Nasscom

---

## 25. Brokerages increase AI adoption as business priorities shift - HousingWire

**Source:** Google News - business intelligence AI workflow
**Type:** news_search
**Published:** Tue, 15 Sep 2026 22:59:46 GMT
**URL:** https://news.google.com/rss/articles/CBMinwFBVV95cUxOSEFkWklNVHQzUnpEOTd5VEJFcGRHenhRUVE5YUxGWHJDeDk5S1hxTU1xamhvTkd5NlpwZlZWS3JKY3kyYTJXOXRkY3hOcmFGS2VvR0VJRWJDR0lKY01JVTlfTEd5anExd0FMYld6bk9TYnhwRVdPN1lnOV9SN25hQzkzQzAyR2FYWElSSTRiNEFmeVlWSHRTWG1kUTV6ZWM?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Brokerages increase AI adoption as business priorities shift HousingWire

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
**Published:** 2026-09-25
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
**Published:** 2026-09-25
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
**Published:** 2026-09-25
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
**Published:** 2026-09-25
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
**Published:** 2026-09-25
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
**Published:** 2026-09-25
**URL:** https://nielseniq.com/global/en/insights/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.
**Manual check:** Yes - this source is included as a watchlist item.

**Summary:**

Professional retail and FMCG data source for market trends, consumer behaviour and category performance.

---

## 33. From portal-hopping to instant answers: HEMA’s journey with MCP and Amazon Bedrock

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Wed, 23 Sep 2026 18:41:09 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/from-portal-hopping-to-instant-answers-hemas-journey-with-mcp-and-amazon-bedrock/
**Relevance score:** 4/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

HEMA, a 100-year-old Dutch retailer, turned developer portal-hopping into instant answers by building HAL, an internal AI assistant on Amazon Bedrock AgentCore. Using Model Context Protocol (MCP), HAL delivers governed knowledge inside the tools teams already use, with no AWS credentials on the client and security anchored in Microsoft Entra ID.

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

## 35. Billion-dollar beauty: The odds of scaling a breakout brand

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Thu, 24 Sep 2026
**URL:** https://www.mckinsey.com/industries/consumer-packaged-goods/our-insights/billion-dollar-beauty-the-odds-of-scaling-a-breakout-brand
**Relevance score:** 4/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Our new analysis reveals the odds of reaching $1 billion in sales—and how the paths to that milestone differ by category and ownership.

---

## 36. Harnessing AI to make mining safer

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Wed, 23 Sep 2026
**URL:** https://www.mckinsey.com/industries/metals-and-mining/our-insights/harnessing-ai-to-make-mining-safer
**Relevance score:** 4/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

AI could improve both safety and productivity by anticipating problems before they arise, detecting worker fatigue, and automating dangerous tasks.

---

## 37. Build a multi-account AI agent with AgentCore Gateway and MCP

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Thu, 24 Sep 2026 16:12:47 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/build-a-multi-account-ai-agent-with-agentcore-gateway-and-mcp/
**Relevance score:** 3/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Build a multi-account architecture that keeps each team's data in its own AWS account while giving AI agents a unified way to query across them. A central platform account runs the agent using Amazon Bedrock AgentCore Gateway and MCP, while line-of-business accounts expose their data as MCP servers with secure cross-account access and fine-grained authorization.

---

## 38. Aderant builds intelligent ticket triage with Amazon Nova

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Thu, 24 Sep 2026 16:06:46 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/aderant-builds-intelligent-ticket-triage-with-amazon-nova/
**Relevance score:** 3/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Learn how Aderant built an intelligent ticket triage system on Amazon Nova Lite through Amazon Bedrock, automating context gathering, classification, routing, and knowledge enrichment for its cloud operations team.

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

## 40. Five Urgent Priorities for CMOs in 2027

**Source:** MIT Sloan Management Review
**Type:** professional_insight
**Published:** Tue, 22 Sep 2026 11:00:03 +0000
**URL:** https://sloanreview.mit.edu/article/five-urgent-priorities-for-cmos-in-2027/
**Relevance score:** 3/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Matt Harrison Clough/Ikon Images In an unpredictable economy and fractured media landscape, marketing leaders are navigating a period of profound transformation and disruption — and as AI technologies evolve, the pace of change will only increase. In response, the highest priorities of chief marketing officers today are shifting, and understanding their concerns is essential to [&#8230;]

---

## 41. Democratized superintelligence is coming: The world needs to get ready

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Thu, 24 Sep 2026
**URL:** https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/democratized-superintelligence-is-coming-the-world-needs-to-get-ready
**Relevance score:** 3/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Bret Taylor, Sierra cofounder and OpenAI chair, believes AI’s near-term cybersecurity risks are real but solvable, and its greater power lies in delivering the world’s best knowledge to everyone.

---

## 42. Maintenance meets AI: A proven approach for asset-heavy industries

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Wed, 23 Sep 2026
**URL:** https://www.mckinsey.com/capabilities/operations/our-insights/maintenance-meets-ai-a-proven-approach-for-asset-heavy-industries
**Relevance score:** 3/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Embedding the latest AI and technology within day-to-day operations is transforming maintenance from a cost center into a significant driver of value.

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

## 45. Speaker-labeled transcription with WhisperX on SageMaker AI

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Thu, 24 Sep 2026 16:20:12 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/speaker-labeled-transcription-with-whisperx-on-sagemaker-ai/
**Relevance score:** 2/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

The AWS WhisperX Deep Learning Container packages Whisper, wav2vec2 forced alignment, and speaker diarization into a GPU-ready image. Learn how to deploy it to Amazon SageMaker AI real-time and asynchronous endpoints for word-level, speaker-labeled transcription, plus the production details that matter: the GPU AMI pin, scaling, and cost controls.

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

## 50. The new growth mandate: A conversation with LinkedIn CMO Jessica Jensen

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Thu, 24 Sep 2026
**URL:** https://www.mckinsey.com/capabilities/growth-marketing-and-sales/our-insights/the-new-growth-mandate-a-conversation-with-linkedin-cmo-jessica-jensen
**Relevance score:** 2/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

At Cannes Lions 2026, LinkedIn CMO Jessica Jensen and McKinsey senior partner Dianne Esber discussed what it takes to turn AI from experimentation into a catalyst for growth.

---

## 51. France says EU’s ‘Made in Europe’ law should not include the UK

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Thu, 24 Sep 2026 17:42:23 GMT
**URL:** https://www.theguardian.com/world/2026/sep/24/france-says-eus-made-in-europe-law-should-not-include-the-uk
**Relevance score:** 2/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

‘If you’re not in the internal market, you don’t get the same protection,’ says French minister of policy designed to curb Chinese competition France is leading a push to exclude the UK from the EU’s “Made in Europe” policy that could result in British companies losing out in the race to supply European countries with low-carbon technologies and electric cars. The plans were raised by Andy Burnham when he met the European Commission president, Ursula von der Leyen, on the sidelines of the UN general assembly earlier this week. Continue reading...

---

## 52. Launch of UK’s ‘largest AI supercomputer’ delayed by power supply problems

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Thu, 24 Sep 2026 17:26:26 GMT
**URL:** https://www.theguardian.com/technology/2026/sep/24/construction-largest-supercomputer-delayed
**Relevance score:** 2/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Datacentre hailed by government was supposed to start operating next year but may be held back into mid-2030s A huge datacentre project hailed by the UK government will miss its launch date next year and could be delayed into the mid-2030s. The site in Loughton, Essex, was described as the country’s largest AI supercomputer when it was announced in 2025, but power supply problems mean it now faces a lengthy wait before coming online. Continue reading...

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

## 58. Introducing Gemini 3.8 Live with Live Avatar

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Thu, 24 Sep 2026 16:20:39 +0000
**URL:** https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**



---

## 59. Advancing Private AI Compute with secure, server-side memory

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Wed, 23 Sep 2026 16:00:57 +0000
**URL:** https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Introducing private, server-side memory to Private AI Compute for personal AI.

---

## 60. Gemini 3.8 text-to-speech says hello

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Wed, 23 Sep 2026 15:25:14 +0000
**URL:** https://deepmind.google/blog/say-hello-to-gemini-38-text-to-speech/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**



---

## 61. Introducing Gemini 3.8 Live and 3.8 Live Extended Thinking

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Tue, 15 Sep 2026 17:05:57 +0000
**URL:** https://deepmind.google/blog/introducing-gemini-3-8-live-and-3-8-live-extended-thinking/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**



---

## 62. AlphaGenome Atlas: A predictive map of every possible DNA letter change in the human genome

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** Tue, 08 Sep 2026 14:00:15 +0000
**URL:** https://deepmind.google/blog/alphagenome-atlas-a-predictive-map-of-every-possible-dna-letter-change-in-the-human-genome/
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

AlphaGenome Atlas maps the molecular effects of 9 billion single-letter DNA variants across the human genome.

---

## 63. 'We're all broke': Would you chase a friend for £5?

**Source:** BBC Business
**Type:** independent_news
**Published:** Thu, 24 Sep 2026 23:00:45 GMT
**URL:** https://www.bbc.co.uk/news/articles/cmly439q4y27o?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

What's the smallest amount of money you would ask a friend to pay you back?

---

## 64. Farmers down 240 million litres of milk after heat

**Source:** BBC Business
**Type:** independent_news
**Published:** Fri, 25 Sep 2026 05:30:13 GMT
**URL:** https://www.bbc.co.uk/news/articles/cjvgy7qd20wgo?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Milk yield was affected by a series of extreme heatwaves which led to poor grazing conditions, researchers say.

---

## 65. Trump and Xi exchange warm words at state dinner but little progress on key issues

**Source:** BBC Business
**Type:** independent_news
**Published:** Fri, 25 Sep 2026 08:09:26 GMT
**URL:** https://www.bbc.co.uk/news/articles/cxq63dqp93n1o?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Despite diplomatic niceties and gifts, little was shared on substantial issues separating the leaders.

---

## 66. Why Australia chose the world's biggest political stage to reveal OpenAI hack

**Source:** BBC Business
**Type:** independent_news
**Published:** Thu, 24 Sep 2026 18:06:40 GMT
**URL:** https://www.bbc.co.uk/news/articles/cr3eqk15ld14o?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Australia, which has strict social media restrictions and has proposed controls on algorithms and smart glasses, announced the breach at the UN.

---

## 67. Scam hotel booking sent family to Wetherspoon pub

**Source:** BBC Business
**Type:** independent_news
**Published:** Fri, 25 Sep 2026 05:02:48 GMT
**URL:** https://www.bbc.co.uk/news/articles/c3zxzqyj24xeo?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Which? says staff are turning away up to 20 tourists a day after scammers used the pub's address.

---

## 68. UK consumer confidence hits two-year high, but ‘Burnham bounce’ may be fading – business live

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Fri, 25 Sep 2026 09:35:04 GMT
**URL:** https://www.theguardian.com/business/live/2026/sep/25/uk-consumer-confidence-burnham-bounce-bank-of-england-oil-inflation-stock-markets-bonds-latest-news-updates
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Rolling coverage of the latest economic and financial news Capital gains tax: how it works, benefits and pitfalls of another hike TalkTalk is scrambling to secure its future amid the threat of administration, closing in on deals to sell its consumer and broadband arms as it seeks to save 900 jobs. The telecoms company said on Friday it is in the final stages of sealing deals to sell its consumer business as well as its wholesale operation, PXC. Continue reading...

---

## 69. Capital gains tax: how it works, and the pros and cons of another rise

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Fri, 25 Sep 2026 05:00:40 GMT
**URL:** https://www.theguardian.com/money/2026/sep/25/capital-gains-tax-how-it-works-benefits-and-pitfalls-of-another-hike
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Increasing the rate of CGT is one of the levers available to the chancellor as he considers revenue-raising options Capital gains tax (CGT) has been widely cited as a possible revenue-raiser as the chancellor, John Healey, prepares to deliver a tough budget next month. How does it work, and what are the pros and cons of raising it further? Continue reading...

---

## 70. TalkTalk races to sell consumer and broadband arms as administration looms

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Fri, 25 Sep 2026 08:07:52 GMT
**URL:** https://www.theguardian.com/business/2026/sep/25/talktalk-administration-deal-sell-consumer-arm
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Customers and jobs ‘top priority’ as company closes in on deals with Opus Broadband and investment group Octopus Business live – latest updates TalkTalk is scrambling to secure its future amid the threat of administration, closing in on deals to sell its consumer and broadband arms as it seeks to save 900 jobs. The telecoms company said on Friday it was in the final stages of sealing deals to sell its consumer business as well as its wholesale operation, PXC. Continue reading...

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
