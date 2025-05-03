from langchain.tools import Tool

def KeywordTool():
    return Tool.from_function(
        func=lambda query: f"Identified high-potential keywords for: {query}",
        name="Keyword Research Tool",
        description="Finds high-potential SEO keywords for a given topic"
    )
