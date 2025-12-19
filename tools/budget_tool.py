from langchain.tools import tool

@tool
def estimate_budget(flight_cost: int, hotel_cost: int, days: int) -> dict:
    """Estimate total trip cost."""
    local_expense = days * 1200
    total = flight_cost + hotel_cost + local_expense

    return {
        "flight": flight_cost,
        "hotel": hotel_cost,
        "local": local_expense,
        "total": total
    }
