from crewai import Agent
from langchain.llms import Ollama
from tools.writing_tool import WritingTool

llm = Ollama(model="llama3")

def content_creator_agent():
    return Agent(
        role="Content Creator",
        goal="Write engaging blog posts based on selected keywords",
        backstory="A skilled writer focused on producing content optimized for SEO.",
        tools=[WritingTool()],
        llm=llm,
        verbose=True
    )
