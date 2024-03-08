NUMBER_OF_INDENTS = 4
REPLACER = ' '


def is_correct_output(obj):
    correct_output = {False: 'false', True: 'true', None: 'null'}
    if obj is None or isinstance(obj, bool):
        return correct_output.get(obj)
    return obj


def gen_stylish_format(dict_diffs, depth):
    result = []
    if depth == 1:
        result.append('{')
    indent = REPLACER * (NUMBER_OF_INDENTS * depth - 2)
    for dif in dict_diffs:
        if 'status' in dif:
            if dif['status'] == 'unchanged':
                result.append(f'{indent}  {dif["key"]}: {is_correct_output(dif["value"])}')
            elif dif['status'] == 'added':
                if isinstance(dif['value'], dict):
                    result.append(f'{indent}+ {dif["key"]}: {{')
                    result += gen_stylish_format(dif['value'], depth + 1)
                else:
                    result.append(f'{indent}+ {dif["key"]}: {is_correct_output(dif["value"])}')
            elif dif['status'] == 'removed':
                if isinstance(dif['value'], dict):
                    result.append(f'{indent}- {dif["key"]}: {{')
                    result += gen_stylish_format(dif['value'], depth + 1)
                else:
                    result.append(f'{indent}- {dif["key"]}: {is_correct_output(dif["value"])}')
            elif dif['status'] == 'has_children':
                result.append(f'{indent}  {dif["key"]}: {{')
                result += gen_stylish_format(dif["value"], depth + 1)
            elif dif['status'] == 'updated':
                if isinstance(dif['old_value'], dict):
                    result.append(f'{indent}- {dif["key"]}: {{')
                    result += gen_stylish_format(dif['old_value'], depth + 1)
                else:
                    result.append(f'{indent}- {dif["key"]}: {is_correct_output(dif["old_value"])}')
                if isinstance(dif['new_value'], dict):
                    result.append(f'{indent}+ {dif["key"]}: {{')
                    result += gen_stylish_format(dif['new_value'], depth + 1)
                else:
                    result.append(f'{indent}+ {dif["key"]}: {is_correct_output(dif["new_value"])}')
        else:
            if isinstance(dict_diffs[dif], dict):
                result.append(f'{indent}  {dif}: {{')
                result += gen_stylish_format(dict_diffs[dif], depth + 1)
            else:
                result.append(f'{indent}  {dif}: {is_correct_output(dict_diffs[dif])}')
    result.append(f'{indent[:-2]}}}')
    return result
