#!/usr/bin/python
import requests
import sys

BASE_URL = "https://www.ida.liu.se/~TDDE44/pokeapi"

def fetch_json_as_dict(url):
    resp = requests.get(url)

    if resp.status_code != 200:
        print(f"Got unexpected status code: %d" % (resp.status_code))
        return None
    elif resp.headers.get("Content-Type") != "application/json":
        print("URL did not return JSON data")
        return None
    
    return resp.json()

def fetch_all_blank(endpoint):
    body = fetch_json_as_dict("{}/{}".format(BASE_URL, endpoint))

    if body == None:
        raise Exception("Could not get endpoint '{}'".format(endpoint))
    
    data = {}
    for obj in body["results"]:
        data[obj["name"]] = obj["url"]

    return data

def fetch_all_pokemons():
    return fetch_all_blank("/api/v2/pokemon")

def fetch_all_abilities():
    return fetch_all_blank("/api/v2/ability")

def fetch_specific_blank(endpoint: str):
    body = fetch_json_as_dict("{}/{}".format(BASE_URL, endpoint))

    if body == None:
        raise Exception("Could not get endpoint '{}'".format(endpoint))
    
    return body


def fetch_specific_pokemon(pokemon_url: str):
    return fetch_specific_blank(pokemon_url)

def fetch_specific_ability(ability_url: str):
    return fetch_specific_blank(ability_url)


def get_pokemon_abilities(pokemon_data):
    ability_urls = []

    for a in pokemon_data.get("abilities"):
        ability_urls.append(a["ability"]["url"])
        
    return ability_urls


def main():
    n = len(sys.argv)

    if n == 1:
        print("User did not input pokemon name")
        return 1

    pokemon_name = str(sys.argv[1]).lower()
    lang = "en"
    if n == 3:
        lang = sys.argv[2]
    
    pokemons = fetch_all_pokemons()
    pokemon_id = pokemons.get(pokemon_name)
    if pokemon_id == None:
        print("No information about '{}' was found.".format(pokemon_name))
        return None

    pokemon_data = fetch_specific_pokemon(pokemon_id)
    ability_urls = get_pokemon_abilities(pokemon_data)

    abilities = []
    for ability_url in ability_urls:
        ability_data = fetch_specific_ability(ability_url)

        if ability_data != None:
            ability_name = next((x["name"] for x in ability_data["names"] if x["language"]["name"] == lang), None)
            flavor_text = next((x["flavor_text"] for x in ability_data["flavor_text_entries"] if x["language"]["name"] == lang), None)

            if None not in [ability_name, flavor_text]:
                abilities.append((ability_name, flavor_text))

    print("{} has {} abilities.".format(pokemon_name, len(abilities)))
    print()

    for i, ability in enumerate(abilities):
        print("Ability '{}':".format(ability[0]))
        print(ability[1])

        if i < len(abilities) - 1:
            print()

main()