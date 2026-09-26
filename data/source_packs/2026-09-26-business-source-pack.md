# Business Source Pack - 2026-09-26

Purpose: source material for practical AI business adoption and market intelligence briefs.

Use this file as input for `prompts/business_insight_prompt.md`.

## Source selection reminder

- Prefer implementation evidence over hype.
- Treat vendor/company sources as biased primary signals.
- Separate fact, meaning, risk and application.
- Look for BI/workflow, FMCG/distribution, SME and market intelligence relevance.

---

## 1. How Datacor built self-service rental analytics with Amazon Quick Sight

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Fri, 25 Sep 2026 15:54:42 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/how-datacor-built-self-service-rental-analytics-with-amazon-quick-sight/
**Relevance score:** 5/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Learn how Datacor built a self-service rental analytics experience for gas and welding distributors by embedding Amazon Quick Sight dashboards and natural language querying into its TrackAbout platform, powered by an automated cross-cloud data pipeline and multi-tenant row-level security.

---

## 2. Power BI Q&A retirement reminder: February 2027 timeline update

**Source:** Microsoft Power BI Blog
**Type:** bi_tooling
**Published:** Thu, 10 Sep 2026 16:00:00 GMT
**URL:** https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Power-BI-Q-A-retirement-reminder-February-2027-timeline-update/ba-p/5365841
**Relevance score:** 5/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

In December, we announced the retirement of Power BI Q&A , our legacy natural-language querying experience, with retirement planned for December 2026. To give current Q&A user's additional time to assess their dependencies and transition to newer Copilot-powered solutions, we’re extending the retirement date to February 2027. This post recaps the affected experiences and provides updates on Copilot capacity availability, embedded scenarios, and sovereign clouds. Recap of the January announcement What is being deprecated? The retirement applies to both the end-user Q&A experiences, and the associated Q&A configuration tools. Retiring experience Recommended alternative Q&A in reports Copilot with Power BI reports Q&A on a dashboard Copilot standalone experience Q&A virtual analyst in mobile app Copilot in Power BI Mobile Q&A in Power BI embedded analytics Copilot for SaaS scenarios . For embedded PaaS scenarios, refer to the updates later in this post. Q&A Setup Prep Data for AI What happens at retirement? Beginning in February 2027, Q&A will no longer work in Power BI. The Q&A visual will be removed, and existing reports that contain Q&A visuals will display an error in place of the

---

## 3. Modern Power BI architecture choices for reporting on Azure Databricks: A performance benchmark for Power BI storage modes

**Source:** Microsoft Power BI Blog
**Type:** bi_tooling
**Published:** Thu, 03 Sep 2026 11:30:43 GMT
**URL:** https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Modern-Power-BI-architecture-choices-for-reporting-on-Azure/ba-p/5364286
**Relevance score:** 5/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Many enterprise Power BI semantic models use Azure Databricks as a data source. When building these models, developers and architects face an early and consequential decision: which storage mode to use. Cost, security, and ease of development and tuning all factor in — but report performance is probably the most important of them, because reports that are slow to load are one of the most common causes of end-user dissatisfaction. In practice, that decision is often made on intuition rather than evidence. To help change that, we've published a new white paper, Modern Power BI Architecture Choices for Reporting on Azure Databricks , benchmarking four ways of serving the same Delta tables to a Power BI report: Direct Lake on OneLake — over Delta tables in a Fabric lakehouse or warehouse Direct Lake on mirrored Unity Catalog tables — shortcuts, no copy DirectQuery — on a Databricks SQL warehouse Composite Model on Databricks — DirectQuery combined with Import-mode aggregations Figure: The four Power BI storage modes benchmarked to evaluate their impact on report performance and scalability. What the results suggest: there's no universal winner — but there are clear patterns. Direct Lak

---

## 4. Upgrade Power BI Dataflows Gen1 to Fabric Dataflows Gen2 with the Upgrade Wizard (Preview)

**Source:** Microsoft Power BI Blog
**Type:** bi_tooling
**Published:** Mon, 24 Aug 2026 15:00:00 GMT
**URL:** https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Upgrade-Power-BI-Dataflows-Gen1-to-Fabric-Dataflows-Gen2-with/ba-p/5360422
**Relevance score:** 5/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Upgrading Power BI Dataflows Gen1 is now easier with the Dataflows Upgrade Wizard. Now in preview for eligible workspaces assigned to Fabric capacity, the wizard provides a guided experience to upgrade Power BI Dataflows Gen1 items to Fabric Dataflows Gen2 (CI/CD). The wizard preserves key properties of the existing dataflow and assesses each item before you begin, helping you understand the upgrade scope and expected follow-up actions. Modernize at your own pace Power BI Dataflows Gen1 remains supported in a legacy state, while new feature investment focuses on Fabric Dataflows Gen2 (CI/CD), as shared in a previous post about the future of Dataflows . The Upgrade Wizard gives dataflow owners a guided self-service path to start that modernization without rebuilding their Power Query logic. You don't need to upgrade your full estate at once. Start with a representative set of dataflows, validate the results, and expand at a pace that works for your organization. For detailed migration planning and inventory guidance, review Migrate from Dataflow Gen1 to Dataflow Gen2 . Build on the benefits of Dataflows Gen2 Fabric Dataflows Gen2 (CI/CD) builds on the Power Query authoring experienc

---

## 5. USPS warns of Indianapolis, Louisville delays due to facility upgrades

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Fri, 25 Sep 2026 14:56:00 -0400
**URL:** https://www.supplychaindive.com/news/usps-warns-of-indianapolis-louisville-delays-due-to-facility-upgrades/831390/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The agency said the installation of new sorting equipment could temporarily disrupt package flows but benefit its peak season operations.

---

## 6. 6 food manufacturers talk supply chain tactics

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Fri, 25 Sep 2026 10:48:00 -0400
**URL:** https://www.supplychaindive.com/news/6-food-manufacturers-talk-supply-chain-tactics/831214/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

General Mills, Nestl&eacute; and more discussed how they are cutting operational costs, navigating uneven freight rates and sharpening demand forecasting at a Barclays conference.

---

## 7. Lego to spend $400M to add warehouse space at Mexico plant

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Fri, 25 Sep 2026 10:29:00 -0400
**URL:** https://www.supplychaindive.com/news/lego-to-spend-400m-to-add-warehouse-space-at-mexico-plant/831302/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The toymaker's investment will also support expanded packing capabilities to strengthen its regional supply chain network in the Americas.

---

## 8. Carrier diversity key to holiday success in a high cost environment

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Fri, 25 Sep 2026 10:22:49 -0400
**URL:** https://www.supplychaindive.com/news/carrier-diversity-key-to-holiday-success-in-a-high-cost-environment/831027/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

Even saving a few dollars per order on shipping fees can free up capital for other parts of a business, UniUni Chief Revenue Officer Sheila Berry said.

---

## 9. Shippers are exploring port-to-inland transit to de-risk supply chains

**Source:** Supply Chain Dive
**Type:** fmcg_supply_chain_news
**Published:** Fri, 25 Sep 2026 07:21:00 -0400
**URL:** https://www.supplychaindive.com/news/shippers-are-exploring-port-to-inland-transit-to-de-risk-supply-chains/831261/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

Inland routes offer a stable alternative to heavily utilized routes, APM Terminals Mobile managing director Brian Harold told Supply Chain Dive.

---

## 10. Aldi begins fresh produce operations at UK warehouse

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Fri, 25 Sep 2026 15:52:24 +0000
**URL:** https://www.logisticsmanager.com/aldi-begins-fresh-produce-operations-at-uk-warehouse/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Aldi begins fresh produce operations at UK warehouse appeared first on Logistics Manager .

---

## 11. Quadient to sell parcel locker business, starting with UK

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Fri, 25 Sep 2026 15:36:59 +0000
**URL:** https://www.logisticsmanager.com/quadient-to-sell-parcel-locker-business-starting-with-uk/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Quadient to sell parcel locker business, starting with UK appeared first on Logistics Manager .

---

## 12. Waitrose commits to responsible cocoa sourcing in expanded Tony’s Open Chain partnership

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Thu, 24 Sep 2026 11:17:34 +0000
**URL:** https://www.logisticsmanager.com/waitrose-commits-to-responsible-cocoa-sourcing-in-expanded-tonys-open-chain-partnership/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Waitrose commits to responsible cocoa sourcing in expanded Tony&#8217;s Open Chain partnership appeared first on Logistics Manager .

---

## 13. Webinar: Moving from reactive to preventative maintenance with Samsara

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Thu, 24 Sep 2026 07:35:24 +0000
**URL:** https://www.logisticsmanager.com/webinar-moving-from-reactive-to-preventative-maintenance-with-samsara/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Webinar: Moving from reactive to preventative maintenance with Samsara appeared first on Logistics Manager .

---

## 14. Hacis extends SuperLink China Direct service to Vietnam

**Source:** Logistics Manager
**Type:** logistics_distribution_news
**Published:** Wed, 23 Sep 2026 16:21:18 +0000
**URL:** https://www.logisticsmanager.com/hacis-extends-superlink-china-direct-service-to-vietnam/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.

**Summary:**

The post Hacis extends SuperLink China Direct service to Vietnam appeared first on Logistics Manager .

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

## 16. How business adoption of AI can power UK economic growth - NatWest Group

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Fri, 25 Sep 2026 08:59:25 GMT
**URL:** https://news.google.com/rss/articles/CBMi-AFBVV95cUxQVkVGNnhQa0hDTWloRHphRW9kLTNyTl8ySG9fVE5TdnQ5MGlDYlBDY1lUWUlzNWdDUmhJT2Y1MGJJS0JUcjZxbjc3UHU5aFVqY3NIdmFnR2VBLUU2NnFQTHlkckVxU3NIUHJEZ2pYbHEzLXZUeE9EdC1JdkVvbzJFcXhJekpyZ184bFZpcjBUU2lJaVZtTUQ2a2kwNTlhZFRlLVdKakRMalU0VGVLU3Y4VVlIb1ZYS3NYbUxDelRyQ0xzTUR5Mk9QenpiUjJ2cXZUTndGSmtSTXJubTF3R2RaXzBoR1J6MXN4OEt3bWRhMUYzTm5qcEM3cA?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

How business adoption of AI can power UK economic growth NatWest Group

---

## 17. Air IT launches AI services for SMEs lacking plans - IT Brief UK

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Thu, 24 Sep 2026 07:15:00 GMT
**URL:** https://news.google.com/rss/articles/CBMihAFBVV95cUxPWFVHS0x0ZWxQX2xpcmRuU0xEanVtYTVuUm4tR0tJLWN4T1lJVEgzSHJFamphenl2Z0pqZF9mUmp3bFdwT1hIaWhWWkdaYnRVQnVGOHJsWnY3TkhvaDdGQkNZX1lYMng3SnN2cXpUbWVsOUZNVVBXQl81UzNWc1NPWjM0Tmw?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Air IT launches AI services for SMEs lacking plans IT Brief UK

---

## 18. UK Small Business AI Adoption Doubles to 47% as Confidence Gap Persists - FF News

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Tue, 08 Sep 2026 14:34:47 GMT
**URL:** https://news.google.com/rss/articles/CBMinAFBVV95cUxOWU9KQ0xhLUpsa3ZHelZuejNvMEw2Nkt6azN6Mm95M0xLSkFtTzRsVkFYMmlsVW8wRFVwTEluc2dTVHlvQV95MXVlTEI1M0JyTUt6RHZ3ejZDWlZVOWJkTkZSQUg2SjRtamdXMGlEbWpxQzNkYXNOTVNqWjVhVllnRnNnd0ItanlNU0dlYkRXTFZrWVlZMWdNeVVlOC0?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

UK Small Business AI Adoption Doubles to 47% as Confidence Gap Persists FF News

---

## 19. Sustainability Concerns Present a Serious Barrier to AI Adoption for SME’S - Business News Wales

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Tue, 22 Sep 2026 02:22:47 GMT
**URL:** https://news.google.com/rss/articles/CBMipwFBVV95cUxOcW1mT3k3d0pvMTNDanpQZTZ1TFBHb2pWYkdTc2lqRGlaWi1YSmREbWxHell2WFJ3OGlsUkY4SUE3RzVPX3E3MVRFaGJHZXhVMmIzTmxRcl93a3E2WXVPdllOWE82SF9aeWpySGRUTmtMa0RfMzk5U1dvRTR3RExCWlMwSDNVbngtX3hBenUzVHZ4SEs2U29RbDZ1Qk5RSG9nbGxid204NA?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Sustainability Concerns Present a Serious Barrier to AI Adoption for SME’S Business News Wales

---

## 20. Why small businesses could be the big winners from AI - UKTN

**Source:** Google News - UK SME AI adoption
**Type:** news_search
**Published:** Wed, 16 Sep 2026 11:11:59 GMT
**URL:** https://news.google.com/rss/articles/CBMikwFBVV95cUxPQzA4OGJsazhjekFQZlRyMFNXbWZtQUo2Tlp2a0FNMTloX3VFZ2pvTkVWb2Vjdi1abjBscG92U2kwTUgyTkpSRlAzR19nd204M0d4MkViNXRabFRGck5GMkJ0QVc2bmRfakRPa0JnM0R4S2stLU40NVg5V3dET0twVTNJeVVuSDVia3Y2RHJEUTlldlU?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Why small businesses could be the big winners from AI UKTN

---

## 21. Building Enterprise AI Workflow Automation Systems: Key Architectures and Best Practices - Nasscom

**Source:** Google News - business intelligence AI workflow
**Type:** news_search
**Published:** Fri, 25 Sep 2026 08:31:04 GMT
**URL:** https://news.google.com/rss/articles/CBMivgFBVV95cUxPMlZzS2pwSTBleTJObnZFYVhnby1wSzhfaWdUS243aW5udEVFOEhIeVVxUlBoUlBLdW5BSFUzUURLWENVMWxidDNBZ1hPVXptM2VRRHdGU0p3NzZrNFBBbFlzVnE2UDM1MEZSRzd2bXdteHRaVkZqZW05WjdQemdkbHI3XzNUOEZ4WUIxcGlKSzZJYU5WdFowYmN0SjJDRGtzM3dZb01nVllmM3NSWEFvZ0VSVXlRN2hzcDNFdG1R?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Building Enterprise AI Workflow Automation Systems: Key Architectures and Best Practices Nasscom

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

## 24. Brokerages increase AI adoption as business priorities shift - HousingWire

**Source:** Google News - business intelligence AI workflow
**Type:** news_search
**Published:** Tue, 15 Sep 2026 22:59:46 GMT
**URL:** https://news.google.com/rss/articles/CBMinwFBVV95cUxOSEFkWklNVHQzUnpEOTd5VEJFcGRHenhRUVE5YUxGWHJDeDk5S1hxTU1xamhvTkd5NlpwZlZWS3JKY3kyYTJXOXRkY3hOcmFGS2VvR0VJRWJDR0lKY01JVTlfTEd5anExd0FMYld6bk9TYnhwRVdPN1lnOV9SN25hQzkzQzAyR2FYWElSSTRiNEFmeVlWSHRTWG1kUTV6ZWM?oc=5
**Relevance score:** 5/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Brokerages increase AI adoption as business priorities shift HousingWire

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
**Published:** 2026-09-26
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
**Published:** 2026-09-26
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
**Published:** 2026-09-26
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
**Published:** 2026-09-26
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
**Published:** 2026-09-26
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
**Published:** 2026-09-26
**URL:** https://nielseniq.com/global/en/insights/
**Relevance score:** 5/5
**Quality note:** Industry source: useful sector context, but check whether evidence is narrow or anecdotal.
**Manual check:** Yes - this source is included as a watchlist item.

**Summary:**

Professional retail and FMCG data source for market trends, consumer behaviour and category performance.

---

## 32. Manage semantic model settings in context with the default settings pane (Preview)

**Source:** Microsoft Power BI Blog
**Type:** bi_tooling
**Published:** Thu, 17 Sep 2026 16:00:00 GMT
**URL:** https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Manage-semantic-model-settings-in-context-with-the-default/ba-p/5366792
**Relevance score:** 4/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

The semantic model settings pane is becoming the default way to configure semantic models in the Power BI service. The pane opens alongside your workspace, so you can review and change settings without leaving the current page. It provides the same settings as the full semantic model settings page while keeping the surrounding context visible. The classic settings page remains available during this transition, but it no longer opens first. This change builds on the settings pane preview and provides a more focused experience for managing semantic models. Why it matters The pane helps you stay in context while you manage a semantic model. It opens on the right side of the browser window and keeps your workspace visible. Settings are organized into expandable sections and tabs, including refresh, data access, performance, and OneDrive and SharePoint. You can use the search box at the top of the pane to find a setting across all sections and tabs. For example, enter "re" and select View refresh history to go directly to refresh history instead of opening sections one at a time. This organization is especially useful for semantic models with several connection, refresh, or performance 

---

## 33. Billion-dollar beauty: The odds of scaling a breakout brand

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Thu, 24 Sep 2026
**URL:** https://www.mckinsey.com/industries/consumer-packaged-goods/our-insights/billion-dollar-beauty-the-odds-of-scaling-a-breakout-brand
**Relevance score:** 4/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Our new analysis reveals the odds of reaching $1 billion in sales—and how the paths to that milestone differ by category and ownership.

---

## 34. Harnessing AI to make mining safer

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Wed, 23 Sep 2026
**URL:** https://www.mckinsey.com/industries/metals-and-mining/our-insights/harnessing-ai-to-make-mining-safer
**Relevance score:** 4/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

AI could improve both safety and productivity by anticipating problems before they arise, detecting worker fatigue, and automating dangerous tasks.

---

## 35. OpenAI says agents leaked 53 images from ChatGPT users in latest example of rogue activity

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Sat, 26 Sep 2026 00:24:43 GMT
**URL:** https://www.theguardian.com/technology/2026/sep/25/openai-agents-leaked-53-images-chatgpt
**Relevance score:** 4/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Disclosure reveals ⁠new area of privacy risk for the company and illustrates ​how difficult it is to inventory unauthorized activity tied to its agents Two ⁠months after OpenAI disclosed the accidental hacking of Hugging Face, the ChatGPT maker is still working to understand the full scope of its rogue agent activity, two people briefed on the matter told Reuters. The latest example came on Friday when OpenAI said its agents had leaked 53 images from ChatGPT users. OpenAI declined to say if the images were AI-generated or identified real people. It also declined to ⁠say when the images were posted. Continue reading...

---

## 36. Proaction boosts sales 60% and saves 75+ hours with Codex

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Fri, 25 Sep 2026 19:00:00 GMT
**URL:** https://openai.com/index/proaction
**Relevance score:** 3/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

With Codex, GPT-Live-1, and GPT-6 Astra, Proaction builds, operates, and sells modern fleet management faster.

---

## 37. Power BI sample reports, refreshed with modern visual defaults

**Source:** Microsoft Power BI Blog
**Type:** bi_tooling
**Published:** Wed, 02 Sep 2026 16:00:00 GMT
**URL:** https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/Power-BI-sample-reports-refreshed-with-modern-visual-defaults/ba-p/5363807
**Relevance score:** 3/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Microsoft has refreshed its Power BI sample reports with modern visual defaults, stronger semantic models, mobile-optimized layouts, and newer authoring features to help creators build clearer, more effective reports.

---

## 38. Five Urgent Priorities for CMOs in 2027

**Source:** MIT Sloan Management Review
**Type:** professional_insight
**Published:** Tue, 22 Sep 2026 11:00:03 +0000
**URL:** https://sloanreview.mit.edu/article/five-urgent-priorities-for-cmos-in-2027/
**Relevance score:** 3/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Matt Harrison Clough/Ikon Images In an unpredictable economy and fractured media landscape, marketing leaders are navigating a period of profound transformation and disruption — and as AI technologies evolve, the pace of change will only increase. In response, the highest priorities of chief marketing officers today are shifting, and understanding their concerns is essential to [&#8230;]

---

## 39. Democratized superintelligence is coming: The world needs to get ready

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Thu, 24 Sep 2026
**URL:** https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/democratized-superintelligence-is-coming-the-world-needs-to-get-ready
**Relevance score:** 3/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Bret Taylor, Sierra cofounder and OpenAI chair, believes AI’s near-term cybersecurity risks are real but solvable, and its greater power lies in delivering the world’s best knowledge to everyone.

---

## 40. Maintenance meets AI: A proven approach for asset-heavy industries

**Source:** McKinsey Insights
**Type:** professional_insight
**Published:** Wed, 23 Sep 2026
**URL:** https://www.mckinsey.com/capabilities/operations/our-insights/maintenance-meets-ai-a-proven-approach-for-asset-heavy-industries
**Relevance score:** 3/5
**Quality note:** Professional insight source: useful framing, but may be marketing-led.

**Summary:**

Embedding the latest AI and technology within day-to-day operations is transforming maintenance from a cost center into a significant driver of value.

---

## 41. Untitled

**Source:** GOV.UK SMEs digital adoption
**Type:** official_policy
**Published:** 
**URL:** https://www.gov.uk/api/search.json?q=SME%20digital%20adoption%20artificial%20intelligence&count=5&order=updated-newest
**Relevance score:** 3/5
**Quality note:** Official source: credible context, but may be broad or slow-moving.
**Fetch error:** HTTP Error 422: Unknown Error

**Summary:**



---

## 42. Untitled

**Source:** GOV.UK business productivity technology
**Type:** official_policy
**Published:** 
**URL:** https://www.gov.uk/api/search.json?q=business%20productivity%20technology%20SME&count=5&order=updated-newest
**Relevance score:** 3/5
**Quality note:** Official source: credible context, but may be broad or slow-moving.
**Fetch error:** HTTP Error 422: Unknown Error

**Summary:**



---

## 43. Scaling MoE reinforcement learning on Amazon EKS with EFA and DeepEP with 40% more throughput

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Fri, 25 Sep 2026 16:29:50 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/scaling-moe-reinforcement-learning-on-amazon-eks-with-efa-and-deepep-with-40-more-throughput/
**Relevance score:** 2/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Learn how to scale Mixture-of-Experts (MoE) reinforcement learning on Amazon EKS using Elastic Fabric Adapter (EFA) and DeepEP. This post presents an architecture that combines Amazon EKS, EFA, and Amazon S3 and increased aggregate reinforcement learning rollout throughput by 40% for large-scale RLHF and GRPO training.

---

## 44. Accelerate multimodal RL training with SkyRL on Amazon SageMaker HyperPod

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Fri, 25 Sep 2026 16:18:07 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/accelerate-multimodal-rl-training-with-skyrl-on-amazon-sagemaker-hyperpod/
**Relevance score:** 2/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Learn how to run SkyRL, an open-source reinforcement learning framework, on Amazon SageMaker HyperPod to post-train a Qwen3-VL-8B vision-language model with GRPO. This walkthrough covers building the container image, launching a Ray cluster from SageMaker Studio, submitting and monitoring the job, and hosting the trained LoRA adapter for inference.

---

## 45. NarrateAI: production-ready LLM quality assurance on Amazon Bedrock

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Fri, 25 Sep 2026 16:15:22 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/narrateai-production-ready-llm-quality-assurance-on-amazon-bedrock/
**Relevance score:** 2/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

NarrateAI delivers production-ready LLM quality assurance on Amazon Bedrock. This post details five techniques—adaptive pipeline orchestration, cross-account multi-model failover, real-time streaming evaluation, composite evaluation, and data accuracy verification—that reach about 99% numerical accuracy while streaming responses in real time.

---

## 46. Deploying real-time personalized speech with Qwen3-TTS on Amazon SageMaker AI

**Source:** AWS Machine Learning Blog
**Type:** ai_data_tooling
**Published:** Fri, 25 Sep 2026 16:09:46 +0000
**URL:** https://aws.amazon.com/blogs/machine-learning/deploying-real-time-personalized-speech-with-qwen3-tts-on-amazon-sagemaker-ai/
**Relevance score:** 2/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Deploy the publicly available Qwen3-TTS-12Hz-1.7B-Base text-to-speech model from Amazon SageMaker JumpStart to a fully managed, real-time endpoint, and clone a voice from a short reference clip. Cross-lingual cloning preserves the speaker's identity across languages.

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

## 51. OpenAI bots meddled with multiple US government agency sites

**Source:** BBC Business
**Type:** independent_news
**Published:** Sat, 26 Sep 2026 02:50:56 GMT
**URL:** https://www.bbc.co.uk/news/articles/cw62jje658dlo?at_medium=RSS&at_campaign=rss
**Relevance score:** 2/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

OpenAI said its bots accessed public data from a range of institutions during test exercises.

---

## 52. Could an iced coffee freeze you out of the job market?

**Source:** BBC Business
**Type:** independent_news
**Published:** Fri, 25 Sep 2026 23:08:22 GMT
**URL:** https://www.bbc.co.uk/news/articles/cv62k9p1rz4do?at_medium=RSS&at_campaign=rss
**Relevance score:** 2/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Employees and recruiters weigh into the online debate around interview etiquette.

---

## 53. Vast Casino Secrets leak exposes inner workings of offshore gambling firms

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Sat, 26 Sep 2026 05:00:28 GMT
**URL:** https://www.theguardian.com/society/2026/sep/26/casino-secrets-leak-offshore-gambling-firms-curacao-regulator
**Relevance score:** 2/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Files could have seismic consequences for online casinos, including those accused of illegally targeting consumers The secrets of thousands of online casinos have been laid bare in a vast leak of data that could have seismic consequences for offshore gambling firms, including some accused of illegally targeting consumers around the world. The Casino Secrets leak reveals tens of thousands of previously confidential files stored by the gambling regulator on the Caribbean island of Curaçao. Continue reading...

---

## 54. Two years of OpenAI Academy

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Wed, 23 Sep 2026 16:00:00 GMT
**URL:** https://openai.com/index/two-years-of-openai-academy
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

Marking two years of OpenAI Academy and bringing AI skills to even more communities.

---

## 55. OpenAI extends cyber access to Ukraine for civilian defense

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Wed, 23 Sep 2026 13:00:00 GMT
**URL:** https://openai.com/index/openai-extends-cyber-access-to-ukraine-for-civilian-defense
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

OpenAI is extending access to its Daybreak program to the Government of Ukraine to support the cyber defense of civilian infrastructure.

---

## 56. Sam Altman’s remarks at the United Nations Security Council

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Wed, 23 Sep 2026 12:00:00 GMT
**URL:** https://openai.com/index/sam-altman-un-security-council-remarks
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

OpenAI CEO Sam Altman discusses AI safety, human control, and international cooperation in remarks to the United Nations Security Council.

---

## 57. Harvey turns legal context into stronger drafts with GPT-6 Astra

**Source:** OpenAI News
**Type:** company_primary_ai
**Published:** Wed, 23 Sep 2026 12:00:00 GMT
**URL:** https://openai.com/index/harvey-from-context-to-confidence-with-astra
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.

**Summary:**

GPT-6 Astra produces more structured, context-aware legal documents, freeing lawyers to focus on strategy.

---

## 58. Untitled

**Source:** Google DeepMind Blog
**Type:** company_primary_ai
**Published:** 
**URL:** https://deepmind.google/blog/rss.xml
**Relevance score:** 1/5
**Quality note:** Vendor/company source: useful primary signal, but not neutral proof.
**Fetch error:** not well-formed (invalid token): line 1, column 0

**Summary:**



---

## 59. Clubs seek legal advice over Man City charges compensation

**Source:** BBC Business
**Type:** independent_news
**Published:** Fri, 25 Sep 2026 20:13:53 GMT
**URL:** https://www.bbc.co.uk/sport/football/articles/cr89jjwy4nqpo?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Premier League clubs are seeking legal advice as to whether they would have a compensation claim over the Manchester City 115 charges case.

---

## 60. 'We're all broke': Would you chase a friend for £5?

**Source:** BBC Business
**Type:** independent_news
**Published:** Thu, 24 Sep 2026 23:00:45 GMT
**URL:** https://www.bbc.co.uk/news/articles/cmly439q4y27o?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

What's the smallest amount of money you would ask a friend to pay you back?

---

## 61. Sir David Beckham nets £38.5m after World Cup ad deals

**Source:** BBC Business
**Type:** independent_news
**Published:** Fri, 25 Sep 2026 16:00:44 GMT
**URL:** https://www.bbc.co.uk/news/articles/crkgww5j0yzwo?at_medium=RSS&at_campaign=rss
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

His stake in DRJB Holdings has entitled him to almost half of its £85.5m in dividend payments.

---

## 62. Three-quarters of UK’s popular plug-in hybrid cars unable to use rapid chargers

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Sat, 26 Sep 2026 09:00:32 GMT
**URL:** https://www.theguardian.com/environment/2026/sep/26/uk-plug-in-hybrid-electric-vehicles-rapid-chargers-analysis
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Only 26% of PHEVs sold across top 20 models can use chargers with power of 50kW or more, analysis finds Three-quarters of the 20 top-selling plug-in hybrid electric vehicles (PHEVs) in the UK cannot use rapid chargers, research has found, amid concerns that many are essentially “petrol cars pulling round a heavy battery”. The cars, which can run on electric batteries as well as combustion engines, have been promoted by carmakers as a way to cover long distances in a single drive – unlike fully electric cars – while still reducing emissions. Continue reading...

---

## 63. ‘I felt shame’: former BA worker locked in legal battle after losing job of 30 years

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Sat, 26 Sep 2026 07:00:28 GMT
**URL:** https://www.theguardian.com/business/2026/sep/26/british-airways-cabin-crew-legal-battle-employment
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

Cabin crew worker was among thousands of staff laid off during pandemic in what MPs called a ‘national disgrace’ During a 30-year career as a member of British Airways’ cabin crew, Tess De Mello took pride in a job well done, saying she regularly went above and beyond to make passengers more comfortable. To her, the role was more than just employment – it was part of her identity. “I took pride,” she said. “I really took pride in myself, I took pride in my role, I took pride in everything because it was everything I wanted to be.” Continue reading...

---

## 64. Manchester City verdict: what happens next, will club appeal and could they be relegated?

**Source:** The Guardian Business
**Type:** independent_news
**Published:** Sat, 26 Sep 2026 07:00:30 GMT
**URL:** https://www.theguardian.com/football/2026/sep/26/manchester-city-verdict-what-happens-next-appeal-relegated
**Relevance score:** 1/5
**Quality note:** News/search source: useful for current signals, but verify important claims.

**Summary:**

We analyse what City must do to appeal, why even that might not be the end of the legal wrangling, and the penalties that could await if the verdict is upheld Manchester City have been found guilty of the vast majority of the 134 disciplinary charges brought against them by the Premier League. Continue reading...

---

## 65. Untitled

**Source:** GOV.UK AI business adoption
**Type:** official_policy
**Published:** 
**URL:** https://www.gov.uk/api/search.json?q=artificial%20intelligence%20business%20adoption&count=5&order=updated-newest
**Relevance score:** 1/5
**Quality note:** Official source: credible context, but may be broad or slow-moving.
**Fetch error:** HTTP Error 422: Unknown Error

**Summary:**



---
