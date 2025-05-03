from crewai import Crew, Task
from agents.seo_specialist_agent import seo_specialist_agent
from agents.content_creator_agent import content_creator_agent
from agents.analytics_agent import analytics_agent
from agents.campaign_manager_agent import campaign_manager_agent

def build_crew(topic: str):
    seo = seo_specialist_agent()
    writer = content_creator_agent()
    analyst = analytics_agent()
    manager = campaign_manager_agent()

    task1 = Task(
        description=f"Identify high-potential keywords for: {topic}",
        agent=seo,
        expected_output="List of SEO keywords."
    )
    task2 = Task(
        description="Write a blog post based on those keywords.",
        agent=writer,
        expected_output="SEO blog post draft."
    )
    task3 = Task(
        description="Analyze content engagement and performance.",
        agent=analyst,
        expected_output="Performance report."
    )
    task4 = Task(
        description="Adjust marketing strategy based on performance.",
        agent=manager,
        expected_output="Updated campaign plan."
    )

    crew = Crew(
        agents=[seo, writer, analyst, manager],
        tasks=[task1, task2, task3, task4],
        verbose=True
    )
    return crew
