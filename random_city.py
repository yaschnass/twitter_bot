import random

# List of major cities worldwide
cities = [
    # USA - West
    "Los Angeles", "San Francisco", "Seattle", "Portland", "San Diego", "Las Vegas", 
    "Phoenix", "Denver", "Salt Lake City", "Honolulu",

    # USA - Midwest
    "Chicago", "Detroit", "Minneapolis", "St. Louis", "Kansas City", "Indianapolis",
    "Cleveland", "Milwaukee", "Columbus", "Omaha",

    # USA - East
    "New York", "Washington D.C.", "Boston", "Philadelphia", "Miami", "Atlanta", 
    "Charlotte", "Orlando", "Nashville", "Pittsburgh",

    # Canada
    "Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa", "Edmonton",

    # Europe
    "London", "Paris", "Berlin", "Madrid", "Rome", "Vienna", "Amsterdam", "Brussels",
    "Moscow", "Istanbul", "Zurich", "Stockholm", "Athens", "Copenhagen", "Oslo",
    "Lisbon", "Warsaw", "Prague", "Budapest", "Dublin", "Helsinki",

    # Asia
    "Tokyo", "Seoul", "Beijing", "Shanghai", "Hong Kong", "Singapore", "Bangkok",
    "Kuala Lumpur", "Jakarta", "Manila", "New Delhi", "Mumbai", "Bangalore",
    "Dubai", "Riyadh", "Tehran", "Tel Aviv",

    # Oceania
    "Sydney", "Melbourne", "Brisbane", "Perth", "Auckland", "Wellington",

    # Africa
    "Cairo", "Lagos", "Nairobi", "Johannesburg", "Cape Town", "Casablanca",
    "Addis Ababa", "Accra", "Algiers", "Dakar",

    # South America
    "São Paulo", "Rio de Janeiro", "Buenos Aires", "Santiago", "Bogotá", "Lima",
    "Caracas", "Quito", "Montevideo", "Asunción"
]

# Function to select a random city
def select_random_city():
    return random.choice(cities)

# If you want to test the module directly
if __name__ == "__main__":
    print(f"Randomly selected city: {select_random_city()}")
