from langchain.tools import Tool

def WritingTool():
    return Tool.from_function(
        func=lambda query: f"Written SEO blog post on: {query}",
        name="Blog Writer Tool",
        description="Writes SEO-optimized blog posts based on keywords"
    )
