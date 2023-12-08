import fnmatch

def check_pattern_match(key, pattern):
    for p in pattern:
        if fnmatch.fnmatch(key, p):
            return True
    return False

def compare_dicts(dict1, dict2, pattern=['*']):
    different_keys = [key for key in dict1 if key in dict2 and dict1[key] != dict2[key] and check_pattern_match(key, pattern)]
    first_only_keys = [key for key in dict1 if key not in dict2 and check_pattern_match(key, pattern)]
    second_only_keys = [key for key in dict2 if key not in dict1 and check_pattern_match(key, pattern)]
    return (different_keys, first_only_keys, second_only_keys)