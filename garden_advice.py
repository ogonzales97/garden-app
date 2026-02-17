# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
season = input("Enter the current season (e.g., summer, winter): ").lower()
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
plant_type = input("Enter the type of plant (e.g., flower, vegetable): ").lower()
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

if season == "summer":
    print("Plants recommended for summer: Tomatoes, Sunflowers, and Marigolds.")
elif season == "winter":
    print("Plants recommended for winter: Pansies, Kale, and Sweet Peas.")

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
