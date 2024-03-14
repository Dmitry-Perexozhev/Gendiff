def is_correct_output_plain(obj):
    correct_output = {False: 'false', True: 'true', None: 'null'}
    if obj is None or isinstance(obj, bool):
        return correct_output.get(obj)
    elif isinstance(obj, dict):
        return '[complex value]'
    elif isinstance(obj, int):
        return obj
    return "\'" + str(obj) + "\'"


def gen_plain_format(dict_diffs, path):
    result = []
    for dif in dict_diffs:
        value = is_correct_output_plain(dif.get("value"))
        new_value = is_correct_output_plain(dif.get("new_value"))
        old_value = is_correct_output_plain(dif.get("old_value"))
        dict_path = ".".join(path + [dif["key"]])
        if dif['type'] == 'has_children':
            result += gen_plain_format(dif["value"], path + [dif["key"]])
        elif dif['type'] == 'added':
            result.append(f'Property \'{dict_path}\' was added '
                          f'with value: {value}')
        elif dif['type'] == 'removed':
            result.append(f'Property \'{dict_path}\' was removed')
        elif dif['type'] == 'updated':
            result.append(f'Property \'{dict_path}\' was updated. '
                          f'From {old_value} to {new_value}')
    return result
