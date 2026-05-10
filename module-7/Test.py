def city_country(city, country, population=None):
    """Return a string in the form City, Country - population xxx."""
    output = f"{city.title()}, {country.title()}"
    if population:
        output += f" - population {population}"
    return output