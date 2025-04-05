# 3.1.1
def key_exists(key, d):
    return key in d

# 3.1.2
def value_exists1(value, d):
    return value in d.values()

# 3.1.3
def add_to_dict(key, value, d):
    d[key] = value
    return d

# 3.1.4
def add_new_only_to_dict(key, value, d):
    if key_exists(key, d) is False:
        d[key] = value
    
    return d

# 3.1.5
def increment_dictionary_value1(key, d):
    d[key] += 1
    return d

# 3.1.6
def increment_dictionary_value2(key, d):
    if key_exists(key, d) is False:
        d[key] = 0
    
    d[key] += 1

    return d

# 3.1.7
def add_to_value_list1(key, value, d):
    d[key].append(value)

    return d

# 3.1.8
def return_value_list1(prefix: str, d: dict[str, any]):
    vals = []

    for x in d.keys():
        if x.startswith(prefix):
            vals.append(d[x])
    
    return vals
    
# 3.1.9
def value_exists2(value: any, d: dict):
    for x in d.values():
        if value == x or (type(x) is list and value in x):
            return True
        
    return False
assert value_exists2('hejsan', { "a": "bokstäver", "b": ['h', 'hejsan'] }) == True