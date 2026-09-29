import asyncio
from langchain.agents import create_agent
from tools.maps_mcp import client

async def get_tools():
    return await client.get_tools()

maps_tools = asyncio.run(get_tools())

venue_agent = create_agent(
    model="google_genai:gemini-3.1-flash-lite",
    tools=maps_tools,
    system_prompt="""
    You are a wedding venue specialist.

    Find venues matching the user's:
    - location
    - guest count
    - preferred style
    - indoor/outdoor preference

    Use the available Maps tools when needed.
    Do not invent venue details.
    """
)