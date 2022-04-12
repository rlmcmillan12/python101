def print_basic_stats(character):
    print(
        f"""
    Character {character['name']}
    Race {character['race']}
    Gender {character['gender']}
    Height {character['height']}
    Weight {character['weight']}
    """
    )


dragonball_dictionary = [
    {
        "name": "goku",
        "race": "saiyan",
        "gender": "male",
        "height": "5'9\"",
        "weight": "137",
        "occupation": ["martial artist", "milkman", "firefighter"],
        "allegiance": ["dragon team", "turtle school"],
        "power level": "145000",
    },
    {
        "name": "gohan",
        "race": ["1/2 sayan", "1/2 human"],
        "gender": "male",
        "height": "5'9\"",
        "weight": "134",
        "occupation": ["super hero", "supreme kai disciple"],
        "allegiance": ["dragon team", "saiyan squad"],
        "power level": "95000",
    },
    {
        "name": "vegeta",
        "race": "saiyan",
        "gender": "male",
        "height": "5'5\"",
        "weight": "123",
        "occupation": [
            "prince of planet vegeta",
            "high class warrior",
            "galactic patrolman",
        ],
        "allegiance": ["dragon team", "galactic patrol"],
        "power level": "140000",
    },
    {
        "name": "frieza",
        "race": "frieza race",
        "gender": "male",
        "height": "5'2\"",
        "weight": "137",
        "occupation": ["emperor", "agent of destruction"],
        "allegiance": ["frieza force"],
        "power level": "145000",
    },
    {
        "name": "goku",
        "race": "saiyan",
        "gender": "male",
        "height": "5'9\"",
        "weight": "137",
        "occupation": ["martial artist", "milkman", "firefighter"],
        "allegiance": ["dragon team", "turtle school"],
        "power level": "145000",
    },
]
print_basic_stats(dragonball_dictionary[1])
