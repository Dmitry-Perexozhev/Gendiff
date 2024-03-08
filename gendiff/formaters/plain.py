
def is_correct_output(obj):
    correct_output = {False: 'false', True: 'true', None: 'null'}
    if obj is None or isinstance(obj, bool):
        return correct_output.get(obj)
    elif isinstance(obj, dict):
        return '[complex value]'
    return "\'"+str(obj)+"\'"


def gen_plain_format(dict_diffs, path):
    result = []
    for dif in dict_diffs:
        if dif['status'] == 'has_children':
            result += gen_plain_format(dif["value"], path + [dif["key"]])
        elif dif['status'] == 'added':
            result.append(f'Property \'{".".join(path+[dif["key"]])}\' was added with value: {is_correct_output(dif["value"])}')
        elif dif['status'] == 'removed':
            result.append(f'Property \'{".".join(path+[dif["key"]])}\' was removed')
        elif dif['status'] == 'updated':
            result.append(f'Property \'{".".join(path+[dif["key"]])}\' was updated. From {is_correct_output(dif["old_value"])} to {is_correct_output(dif["new_value"])}')
    return result


