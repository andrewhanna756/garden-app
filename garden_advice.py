"""Gardening advice based on the season and the type of plant.

Gives a gardener two pieces of guidance: what the current season
demands, and what their particular plant needs.
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


def generate_advice(season, plant_type):
    """Return the combined advice for a season and a plant type.

    Kept separate from printing so the advice can be tested, reused or
    displayed some other way without changing this function.
    """
    return (
        f"{get_season_advice(season)}\n"
        f"{get_plant_advice(plant_type)}"
    )


def main():
    """Print advice for the configured season and plant type."""
    season = "summer"
    plant_type = "flower"

    print(generate_advice(season, plant_type))


# Only runs when the file is executed directly, so the functions above
# can be imported by tests or other modules without printing anything.
if __name__ == "__main__":
    main()
