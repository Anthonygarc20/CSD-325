"""
Assignment: Module 7.2
Author: AG
"""

def city_country(city, country, population=None, language=None):
    """Final formatted string with optional parameters."""
    output = f"{city.title()}, {country.title()}"
    if population:
        output += f" - population {population}"
    if language:
        output += f", {language.title()}"
    return output

if __name__ == "__main__":
    # 4k Requirements:
    print(city_country('santiago', 'chile'))
    print(city_country('tokyo', 'japan', 37400000))
    print(city_country('mexico city', 'mexico', 21671908, 'spanish'))