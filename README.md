# 🧠 Multi Agents: Digital Marketing using (CrewAI + Ollama)

**Author:** Noor Uddin  
**Email:** noor.cs2@yahoo.com

---

## 📁 Project Structure
```
Multi-Agents-for-Digital-Marketing /
├── agents/
│   ├── seo_specialist_agent.py
│   ├── content_creator_agent.py
│   ├── analytics_agent.py
│   └── campaign_manager_agent.py
├── tools/
│   ├── keyword_tool.py
│   ├── writing_tool.py
│   ├── analytics_tool.py
│   └── campaign_tool.py
├── crew.py
├── main.py
├── app.py  # (Streamlit UI)
└── README.md
```

---

## 🧩 Agents Overview

- **SEO Specialist Agent**
  - Role: Identifies high-potential keywords
  - Tool: `KeywordTool`

- **Content Creator Agent**
  - Role: Writes SEO-optimized blog posts
  - Tool: `WritingTool`

- **Analytics Agent**
  - Role: Tracks engagement and campaign metrics
  - Tool: `AnalyticsTool`

- **Campaign Manager Agent**
  - Role: Oversees and adjusts overall strategy
  - Tool: `CampaignTool`

---

## 🧠 How It Works
Each agent will:
- Be defined with its role, goal, and tool(s)
- Be linked via tasks managed by CrewAI
- Use a local LLaMA 3 model (via Ollama) for reasoning

---

## 💻 Tech Stack
- **Python 3.10+**  
- **CrewAI** – Multi-agent orchestration  
- **LangChain** – Tool integration layer  
- **Ollama** – Local LLaMA 3 model execution  
- **Streamlit** – Interactive UI for demo  
- *(Optional: FastAPI, Next.js for production-grade UIs)*

---
## 🖼️ Demo Results

You can view output screenshots in the GitHub repo:

- ![Result Screenshot](https://github.com/noorcs39/Multi-Agents-for-Digital-Marketing/raw/main/Result.png)
- ![Final Analysis](https://github.com/noorcs39/Multi-Agents-for-Digital-Marketing/raw/main/Result%201.png)

---

## 🛠 Next Steps
- Build each agent and tool one by one
- Chain tasks using `crew.py`
- Add client-facing UI using `Streamlit`
- Upgrade to FastAPI + React/Next.js for deployment

Let me know when you're ready to start coding agent #1 (`seo_specialist_agent.py`).
