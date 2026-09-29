from tavily import TavilyClient
from langchain.tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool('search_web', description="Search the web for current wedding vendor and venue pricing.")
async def search_web(query: str):
    return TavilyClient().search(query=query, search_depth="advanced", max_results=5)