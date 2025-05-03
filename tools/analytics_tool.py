from langchain.tools import Tool

def AnalyticsTool():
    return Tool.from_function(
        func=lambda query: f"Analyzed performance for: {query}",
        name="Analytics Tool",
        description="Analyzes campaign and user engagement performance"
    )
