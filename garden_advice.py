"""Gardening advice based on the season and the type of plant.

Asks the gardener which season it is and what they are growing, then
gives advice for both, along with a few plants worth putting in this
time of year.
"""

# Advice is held in dictionaries rather than if/elif chains.
#
# The chains worked, but every new season meant editing the logic
# itself, and a typo in a branch was easy to miss. With a dictionary,
# adding autumn is one new line of data and the lookup code never
# changes. It also means the valid options can be listed to the user
# without repeating them anywhere.
SEASON_ADVICE = {
    "summer": "Water your plants regularly and provide some shade.",
    "winter": "Protect your plants from frost with covers.",
    "spring": "Feed new growth and watch for late frosts.",
    "autumn": "Clear fallen leaves and mulch before the cold sets in.",
}

PLANT_ADVICE = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Pinch out the tips to keep the plant bushy.",
    "shrub": "Prune after flowering to keep a tidy shape.",
}

# Plants worth sowing or planting in each season.
SEASONAL_PLANTS = {
    "summer": ["courgettes", "sunflowers", "basil"],
    "winter": ["garlic", "broad beans", "winter pansies"],
    "spring": ["tomatoes", "sweet peas", "lettuce"],
    "autumn": ["spring bulbs", "onion sets", "kale"],
}

DEFAULT_SEASON_ADVICE = "No advice for this season."
DEFAULT_PLANT_ADVICE = "No advice for this type of plant."


def get_season_advice(season):
    """Return the advice for a season.

    Falls back to a default message if the season is not recognised,
    so an unexpected value produces a sensible line rather than an
    error.
    """
    return SEASON_ADVICE.get(season.lower().strip(),
                             DEFAULT_SEASON_ADVICE)


def get_plant_advice(plant_type):
    """Return the advice for a type of plant.

    Falls back to a default message if the plant type is not
    recognised.
    """
    return PLANT_ADVICE.get(plant_type.lower().strip(),
                            DEFAULT_PLANT_ADVICE)


def get_plant_suggestions(season):
    """Return a list of plants suited to the given season.

    Returns an empty list for an unknown season, so the caller can
    simply skip the suggestion rather than printing a blank heading.
    """
    return SEASONAL_PLANTS.get(season.lower().strip(), [])


def generate_advice(season, plant_type):
    """Return the combined advice for a season and a plant type.

    Kept separate from printing so the advice can be tested, reused or
    displayed some other way without changing this function.
    """
    lines = [
        get_season_advice(season),
        get_plant_advice(plant_type),
    ]

    suggestions = get_plant_suggestions(season)
    if suggestions:
        lines.append(
            f"\nWorth planting now: {', '.join(suggestions)}."
        )

    return "\n".join(lines)


def ask_for_choice(prompt, valid_options):
    """Ask the user to pick one of valid_options, repeating on error.

    Input is validated here rather than trusted, because a typo would
    otherwise fall through to the default message and leave the
    gardener wondering why they got no advice. Showing the accepted
    values in the prompt means they never have to guess.
    """
    options_text = ", ".join(sorted(valid_options))

    while True:
        answer = input(f"{prompt} ({options_text}): ").strip().lower()

        if answer in valid_options:
            return answer

        if not answer:
            print("Please type something.")
        else:
            print(f"'{answer}' is not one of the options. "
                  f"Please choose from: {options_text}.")


def main():
    """Ask the user for a season and plant type, then print advice."""
    print("Garden Advice\n" + "-" * 40)

    season = ask_for_choice("Which season is it", SEASON_ADVICE.keys())
    plant_type = ask_for_choice("What are you growing",
                                PLANT_ADVICE.keys())

    print("\n" + "-" * 40)
    print(generate_advice(season, plant_type))
    print("-" * 40)


# Only runs when the file is executed directly, so the functions above
# can be imported by tests or other modules without prompting anyone.
if __name__ == "__main__":
    main()
