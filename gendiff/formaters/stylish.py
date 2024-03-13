NUMBER_OF_INDENTS = 4
REPLACER = ' '


def is_correct_output(obj):
    correct_output = {False: 'false', True: 'true', None: 'null'}
    if obj is None or isinstance(obj, bool):
        return correct_output.get(obj)
    elif isinstance(obj, dict):
        return '{'
    return obj


def open_dict(obj, depth):
    result_open = []
    indent = REPLACER * (NUMBER_OF_INDENTS * depth - 2)
    if isinstance(obj, dict):
        for key in obj:
            if isinstance(obj[key], dict):
                result_open.append(f'{indent}  {key}: {{')
                result_open += open_dict(obj[key], depth + 1)
            else:
                result_open.append(f'{indent}  {key}: {obj[key]}')
        result_open.append(f'{indent[:-2]}}}')
    return result_open


def gen_stylish_format(dict_diffs, depth):
    result = []
    if depth == 1:
        result.append('{')
    indent = REPLACER * (NUMBER_OF_INDENTS * depth - 2)
    for dif in dict_diffs:
        value = is_correct_output(dif.get("value"))
        new_value = is_correct_output(dif.get("new_value"))
        old_value = is_correct_output(dif.get("old_value"))
        unchanged_str = f'{indent}  {dif["key"]}: {value}'
        added_str = f'{indent}+ {dif["key"]}: {value}'
        removed_str = f'{indent}- {dif["key"]}: {value}'
        has_children_str = f'{indent}  {dif["key"]}: {{'
        updated_old_str = f'{indent}- {dif["key"]}: {old_value}'
        updated_new_str = f'{indent}+ {dif["key"]}: {new_value}'
        if dif['type'] == 'unchanged':
            result.append(unchanged_str)
        elif dif['type'] == 'added':
            result.append(added_str)
            result += (open_dict(dif['value'], depth + 1))
        elif dif['type'] == 'removed':
            result.append(removed_str)
            result += (open_dict(dif['value'], depth + 1))
        elif dif['type'] == 'has_children':
            result.append(has_children_str)
            result += gen_stylish_format(dif["value"], depth + 1)
        elif dif['type'] == 'updated':
            result.append(updated_old_str)
            result += (open_dict(dif['old_value'], depth + 1))
            result.append(updated_new_str)
            result += (open_dict(dif['new_value'], depth + 1))
    result.append(f'{indent[:-2]}}}')
    return result
