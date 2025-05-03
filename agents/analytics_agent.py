from crewai import Agent
from langchain.llms import Ollama
from tools.analytics_tool import AnalyticsTool

llm = Ollama(model="llama3")

def analytics_agent():
    return Agent(
        role="Analytics Agent",
        goal="Analyze content performance and provide insights",
        backstory="An expert in campaign metrics and user engagement analysis.",
        tools=[AnalyticsTool()],
        llm=llm,
        verbose=True
    )
