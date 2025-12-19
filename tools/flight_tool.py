import json
from langchain.tools import tool

@tool
def search_flights(source: str, destination: str) -> dict:
    """Find cheapest and fastest flights between cities."""
    with open("data/flights.json") as f:
        flights = json.load(f)

    filtered_flights = [
        f for f in flights
        if f["source"].lower() == source.lower()
        and f["destination"].lower() == destination.lower()
    ]

    cheapest = min(filtered_flights, key=lambda x: x["price"])
    fastest = min(filtered_flights, key=lambda x: x["duration"])

    return {
        "cheapest": cheapest,
        "fastest": fastest
    }