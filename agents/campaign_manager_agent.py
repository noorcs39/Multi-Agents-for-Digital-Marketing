from crewai import Agent
from langchain.llms import Ollama
from tools.campaign_tool import CampaignTool

llm = Ollama(model="llama3")

def campaign_manager_agent():
    return Agent(
        role="Campaign Manager",
        goal="Review results and adjust overall strategy",
        backstory="Oversees the marketing workflow and fine-tunes strategies for best results.",
        tools=[CampaignTool()],
        llm=llm,
        verbose=True
    )
