from langchain.tools import tool

@tool
async def calculate_budget(
    total_budget: float,
    venue_cost: float = 0,
    catering_cost: float = 0,
    photography_cost: float = 0,
    decor_cost: float = 0,
    entertainment_cost: float = 0,
    travel_cost: float = 0,
    other_costs: float = 0
):
    """Calculate total wedding spend and remaining budget."""

    total_spend = (
        venue_cost
        + catering_cost
        + photography_cost
        + decor_cost
        + entertainment_cost
        + travel_cost
        + other_costs
    )

    return {
        "total_budget": total_budget,
        "total_spend": total_spend,
        "remaining_budget": total_budget - total_spend,
        "over_budget": total_spend > total_budget,
    }