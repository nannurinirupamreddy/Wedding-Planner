import asyncio
from langchain.tools import tool
from langchain.agents import create_agent
from langchain.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv
from agents.budget_agent import budget_agent
from agents.catering_agent import catering_agent
from agents.cost_agent import cost_agent
from agents.schedule_agent import schedule_agent
from agents.travel_agent import travel_agent
from agents.venue_agent import venue_agent

load_dotenv()

@tool("budget", description="Analyze wedding costs and determine whether the plan fits the user's budget.")
async def budget(request: str):
    response = await budget_agent.ainvoke({
        "messages": [
            {
                "role": "user",
                "content": request
            }
        ]
    })

    return response["messages"][-1].content

@tool("venue", description="Find suitable wedding venues based on location, guest count, style, and preferences.")
async def venue(request: str):
    response = await venue_agent.ainvoke({
        "messages": [
            {
                "role": "user",
                "content": request
            }
        ]
    })

    return response["messages"][-1].content


@tool("cost", description="Research current public pricing for wedding venues, vendors, and services.")
async def cost(request: str):
    response = await cost_agent.ainvoke({
        "messages": [
            {
                "role": "user",
                "content": request
            }
        ]
    })

    return response["messages"][-1].content

@tool("catering", description="Find catering options based on guest count, location, cuisine preferences, dietary restrictions, and budget.")
async def catering(request: str):
    response = await catering_agent.ainvoke({
        "messages": [
            {
                "role": "user",
                "content": request
            }
        ]
    })

    return response["messages"][-1].content


@tool("travel", description="Plan wedding travel, hotels, routes, airports, and guest transportation.")
async def travel(request: str):
    response = await travel_agent.ainvoke({
        "messages": [
            {
                "role": "user",
                "content": request
            }
        ]
    })

    return response["messages"][-1].content


@tool("schedule", description="Create a realistic wedding-day schedule and timeline.")
async def schedule(request: str):
    response = await schedule_agent.ainvoke({
        "messages": [
            {
                "role": "user",
                "content": request
            }
        ]
    })

    return response["messages"][-1].content

PLANNER_AGENT_PROMPT = """
    You are the main wedding planner and coordinator.
    
    You MUST delegate specialized tasks to the corresponding tools.
    
    Rules:
    - ALWAYS use the venue tool for venue recommendations.
    - ALWAYS use the cost tool for current prices or price estimates.
    - ALWAYS use the catering tool for catering recommendations.
    - ALWAYS use the travel tool for hotels, routes, transportation, and travel times.
    - ALWAYS use the budget tool for ANY budget arithmetic, totals, remaining budget,
      per-person calculations, or determining whether the wedding fits the budget.
    - ALWAYS use the schedule tool to create the wedding-day timeline.
    
    Do not perform the work of a specialist yourself when a specialist tool exists.
    
    When necessary, pass results from one specialist into another.
    For example:
    1. Find venues.
    2. Research venue costs.
    3. Research catering.
    4. Pass all known costs to the budget specialist.
    5. Ask the travel specialist for logistics.
    6. Ask the schedule specialist to build the timeline using known venue/travel information.
    7. Combine all specialist outputs into the final plan.
    
    Never invent prices, availability, travel times, vendor details, or budget numbers.
    Clearly label anything that specialists could not verify.
    """

planner_agent = create_agent(
    model="google_genai:gemini-3.1-flash-lite",

    tools=[
        venue,
        cost,
        budget,
        catering,
        travel,
        schedule
    ],

    system_prompt=PLANNER_AGENT_PROMPT
)