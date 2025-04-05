import random

# 1.3.1
def concatenate_strings(string1, string2):
    return string1 + string2

# 1.3.2
def use_the_linebreak():
    a = "rad 1\nrad 2"
    print(a)
    return a

# 1.3.3
def generate_pokemon_name(prefixes, suffixes):
    return random.choice(prefixes) + random.choice(suffixes)

# 1.3.4
def first_word(s):
    return s.split()[0]

# 1.3.5
def join_list(values):
    return ":".join(values)

# 1.3.6
def remove_spaces(s):
    return s.rstrip()
assert remove_spaces("   mellanslag i början ska vara kvar.     ") == '   mellanslag i början ska vara kvar.'

# 1.3.7
def get_characters(s, pos, num_of_chars):
    return s[pos:pos+num_of_chars]