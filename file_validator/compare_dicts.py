import fnmatch

def check_pattern_match(key, pattern):
    for p in pattern:
        if fnmatch.fnmatch(key, p):
            return True
    return False

def compare_dicts(dict1, dict2, pattern=['*'], invert = False):
    if invert:
        dict1 = {value: key for key, value in dict1.items()}
        dict2 = {value: key for key, value in dict2.items()}
    different = {key: (dict1[key], dict2[key]) for key in dict1 if key in dict2 and dict1[key] != dict2[key] and check_pattern_match(key, pattern)}
    first_only = {key: dict1[key] for key in dict1 if key not in dict2 and check_pattern_match(key, pattern)}
    second_only = {key: dict2[key] for key in dict2 if key not in dict1 and check_pattern_match(key, pattern)}
    return (different, first_only, second_only)