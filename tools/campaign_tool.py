from langchain.tools import Tool

def CampaignTool():
    return Tool.from_function(
        func=lambda query: f"Reviewed campaign and adjusted strategy for: {query}",
        name="Campaign Strategy Tool",
        description="Oversees strategy and adjusts based on performance"
    )
