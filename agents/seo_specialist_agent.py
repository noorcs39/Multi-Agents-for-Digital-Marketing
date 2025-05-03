from crewai import Agent
from langchain.llms import Ollama
from tools.keyword_tool import KeywordTool

llm = Ollama(model="llama3")

def seo_specialist_agent():
    return Agent(
        role="SEO Specialist",
        goal="Identify high-potential keywords to drive traffic",
        backstory="An expert in search engine optimization, trained to detect high-performing keywords.",
        tools=[KeywordTool()],
        llm=llm,
        verbose=True
    )
