def is_correct_output(obj):
    correct_output = {False: 'false', True: 'true', None: 'null'}
    if obj is None or isinstance(obj, bool):
        return correct_output.get(obj)
    elif isinstance(obj, dict):
        return '[complex value]'
    return "\'" + str(obj) + "\'"


def gen_plain_format(dict_diffs, path):
    result = []
    for dif in dict_diffs:
        value = is_correct_output(dif.get("value"))
        new_value = is_correct_output(dif.get("new_value"))
        old_value = is_correct_output(dif.get("old_value"))
        dict_path = ".".join(path + [dif["key"]])
        if dif['status'] == 'has_children':
            result += gen_plain_format(dif["value"], path + [dif["key"]])
        elif dif['status'] == 'added':
            result.append(f'Property \'{dict_path}\' was added '
                          f'with value: {value}')
        elif dif['status'] == 'removed':
            result.append(f'Property \'{dict_path}\' was removed')
        elif dif['status'] == 'updated':
            result.append(f'Property \'{dict_path}\' was updated. '
                          f'From {old_value} to {new_value}')
    return result
