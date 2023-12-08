import fnmatch

def compare_dicts(dict1, dict2, glob_pattern='*'):
    different_keys = [key for key in dict1 if key in dict2 and dict1[key] != dict2[key] and fnmatch.fnmatch(key, glob_pattern)]
    first_extra_keys = [key for key in dict1 if key not in dict2 and fnmatch.fnmatch(key, glob_pattern)]
    second_extra_keys = [key for key in dict2 if key not in dict1 and fnmatch.fnmatch(key, glob_pattern)]
    return (different_keys, first_extra_keys, second_extra_keys)