"""
Garden Advice Generator: Provides gardening tips
based on the season and plant type.
 """

# Dictionary to store gardening advice based on seasons and plant types
gardening_data = {
    "seasons": {
        "summer": "Water your plants regularly and provide some shade.",
        "winter": "Protect your plants from frost with covers.",
        "spring": "Plant new seeds and watch for early blooms.",
        "autumn": "Mulch your beds and prepare for the cold."
    },
    "plants": {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!"
    },
    "recommendations": {
        "summer": "Tomatoes, Sunflowers, and Marigolds.",
        "winter": "Pansies, Kale, and Sweet Peas."
    }
}


def get_gardening_advice(category, choice):
    """
    Fetches advice from the gardening_data dictionary.
    Returns a default message if the choice is not found.
    """
    return gardening_data[category].get(
        choice, f"No advice found for {choice}."
    )


# Get user input
season = input("Enter the current season: ").lower()
plant_type = input("Enter the type of plant: ").lower()

# Fetch all pieces of info using the function
season_advice = get_gardening_advice("seasons", season)
plant_advice = get_gardening_advice("plants", plant_type)
recommended_plants = get_gardening_advice("recommendations", season)

# Print everything out
print("--- Advice ---")
print(season_advice)
print(plant_advice)
print(f"Recommended for {season}: {recommended_plants}")
