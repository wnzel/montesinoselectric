# Reusable skills for local trade websites

Researched October 9, 2026 across the installed catalog, the OpenAI curated skills catalog, GitHub repositories, and skills.sh. This is a practical shortlist rather than a claim to enumerate every community skill. The OpenAI curated catalog did not contain a dedicated electrician/HVAC/plumber website skill.

| Skill / library | Why it fits | Use here |
| --- | --- | --- |
| [Sites](https://openai.com/) — installed plugin | Static site implementation, local preview, source packaging and private publication | Applied |
| [Frontend Design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Intentional typography, brand-specific design, accessible responsive layouts and visual critique | Installed; guidance read and applied |
| [SEO Local Business](https://github.com/jezweb/claude-skills/tree/main/plugins/web-design/skills/seo-local-business) | Explicitly covers Electrician, Plumber, HVACBusiness and RoofingContractor schema; metadata and sitemap | Installed; adapted Australian examples to US phone and Phoenix context |
| [Local SEO Skills](https://github.com/garrettjsmith/localseoskills) | Local business content, Google Business Profile, citations, local audits and service-area visibility | Recommended for a later marketing phase; live audits need a connected data source |
| [Copywriting](https://github.com/coreyhaines31/marketingskills/tree/main/skills/copywriting) and [CRO](https://github.com/coreyhaines31/marketingskills/tree/main/skills/cro) | Clear service copy and quote/contact paths for a small business | Relevant future reusable skills; not required to install for this build |
| [Homeowner Question Content](https://github.com/unifapi-agent/agents/tree/main/skills/home-services-marketing/homeowner-question-content) | Explicitly targets electrical, HVAC, plumbing and roofing businesses; blog topic research based on homeowner questions | Relevant future blog research; requires UnifAPI for its specified live data workflow |

Also found [SCALA Sites](https://github.com/Alessandro114/scala-sites), which includes electrician, plumber, roofing, landscaping and other business templates. It is a template repository, not an agent skill. The existing Montesinos assets and the user’s local Peralta’s Roofing project were better direct references for this redesign.

## Selection

Use Frontend Design and SEO Local Business alongside the installed Sites workflow. A dedicated electrician skill was not necessary to build a finished electrical business site: reuse these skills for the website structure and local search foundation, then supply verified trade-specific content. Omit unrelated advertising, automation and paid SEO integrations during the redesign.

The two new skills were installed to `C:/Users/Wenzel/.codex/skills/frontend-design` and `C:/Users/Wenzel/.codex/skills/seo-local-business`. They become available in the skill catalog on the next turn. Their full instructions were read directly during this task.
