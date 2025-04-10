import requests

# Övning 1 och 2
def print_url_content(url: str):
    resp = requests.get(url)

    if resp.status_code != 200:
        print(f"Got unexpected status code: %d" % (resp.status_code))
        # raise Exception("Something went wrong fetching the resource")
        return None
    
    t = resp.text

    print(t)

# # Testing
# print_url_content("https://www.ida.liu.se/~TDDE44/kursmaterial/lektion3/exempel.html")
# print_url_content("https://www.ida.liu.se/~TDDE44/kursmaterial/lektion3/exempel.txt")
# print_url_content("https://www.ida.liu.se/~TDDE44/kursmaterial/lektion3/exempel.json")

# print_url_content("https://www.ida.liu.se/~TDDE44/kursmaterial/lektion3/exempel.html")
# print_url_content("https://www.ida.liu.se/~TDDE44/kursmaterial/lektion3/exempel.txt")
# print_url_content("https://www.ida.liu.se/~TDDE44/kursmaterial/lektion3/exempel.json")
# print_url_content("https://www.ida.liu.se/~TDDE44/kursmaterial/lektion3/finnsinte")
# print_url_content("https://www.ida.liu.se/~TDDE44/kursmaterial/tenta-tdde44.txt")

# Övning 3
def get_json_as_dict(url):
    resp = requests.get(url)

    if resp.status_code != 200:
        print(f"Got unexpected status code: %d" % (resp.status_code))
        return None
    elif resp.headers.get("Content-Type") != "application/json":
        print("URL did not return JSON data")
        return None
    
    return resp.json()

# # Testing 
# print(get_json_as_dict("https://www.ida.liu.se/~TDDE44/kursmaterial/lektion3/exempel.json"))
# print(get_json_as_dict("https://www.ida.liu.se/~TDDE44/kursmaterial/tenta-tdde44.json"))
# print(get_json_as_dict("https://www.ida.liu.se/~TDDE44/pokeapi/api/v2/pokemon/"))

# Övning 4
def get_pokemon_url(name: str):
    BASE_URL = "https://www.ida.liu.se/~TDDE44/pokeapi/api/v2/pokemon/"
    body = get_json_as_dict(BASE_URL)

    if body == None:
        raise Exception("Could not get pokemans at all...")

    pokimans = {}
    for obj in body["results"]:
        pokimans[obj["name"]] = obj["url"].split("/")[-2]

    found = pokimans.get("-".join(name.strip().split(" ")).lower())
    return BASE_URL + found if found != None else found

print(get_pokemon_url(" pikachu     "))