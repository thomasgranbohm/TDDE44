"""Pokédex.

Programmet tar in två konsolargument. Den första är pokemonnamnet, och
det andra är vilket språk. Språket defaultar till engelska om inget skrivs in.
Programmet skriver ut information om pokemonen.
"""

import requests
import sys

BASE_URL = "https://www.ida.liu.se/~TDDE44/pokeapi"


def fetch(endpoint):
    """Funktionen tar in en url, returnerar infon hämtat som JSON i en dictionary.

    ifall urlen inte finns, eller den ej innehåller JSON-data
    returnerar funktionen None.
    """
    url = "{}/{}".format(BASE_URL, endpoint)
    resp = requests.get(url)

    if resp.status_code != 200:
        print("Got unexpected status code: %d" % (resp.status_code))
        return None
    elif resp.headers.get("Content-Type") != "application/json":
        print("URL did not return JSON data")
        return None

    body = resp.json()

    if body is None:
        raise Exception("Could not get endpoint '{}'".format(endpoint))

    return body


def get_pokemon_dict(body):
    """Funktionen behandlar råa datan om alla pokemons.

    Funktionen tar in data om alla pokemons och
    returnerar en dict som kopplar pokemonens namn till dess endpoint.
    """
    data = {}
    for obj in body["results"]:
        data[obj["name"]] = obj["url"]

    return data


def get_ability_urls(pokemon_data):
    """Extraherar och returnerar en specifik pokemons abilities endpoints i en lista."""
    ability_urls = []

    for a in pokemon_data.get("abilities"):
        ability_urls.append(a["ability"]["url"])

    return ability_urls


def generate_ability_data(ability_urls, lang):
    """Funktionen hämtar alla abilities och skapar en dict med relevant data."""
    abilities = []

    for ability_url in ability_urls:
        ability_data = fetch(ability_url)

        if ability_data is not None:
            ability_name, flavor_text = None, None

            """Jag håller inte med om rättningen angående next(),
            men här är iaf en annan lösning."""
            for x in ability_data["names"]:
                if x["language"]["name"] == lang:
                    ability_name = x["name"]
                    break

            for x in ability_data["flavor_text_entries"]:
                if x["language"]["name"] == lang:
                    ability_name = x["flavor_text"]
                    break

            if None not in [ability_name, flavor_text]:
                abilities.append((ability_name, flavor_text))

    return abilities


if __name__ == "__main__":
    n = len(sys.argv)

    if n == 1:
        print("User did not input pokemon name")
        exit(1)

    pokemon_name = str(sys.argv[1]).lower()
    lang = "en"
    if n == 3:
        lang = sys.argv[2]

    pokemons_body = fetch("/api/v2/pokemon")
    pokemons = get_pokemon_dict(pokemons_body)
    pokemon_id = pokemons.get(pokemon_name)

    if pokemon_id is None:
        print("No information about '{}' was found.".format(pokemon_name))
        exit(1)

    pokemon_data = fetch(pokemon_id)
    ability_urls = get_ability_urls(pokemon_data)
    abilities = generate_ability_data(ability_urls, lang)

    print("{} has {} abilities.".format(pokemon_name, len(abilities)))
    print()

    for i, ability in enumerate(abilities):
        print("Ability '{}':".format(ability[0]))
        print(ability[1])

        if i < len(abilities) - 1:
            print()
