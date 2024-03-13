def build_diff(dict1, dict2):
    keys = sorted(set(dict1.keys()) | set(dict2.keys()))
    diffs = []
    for key in keys:
        value1 = dict1.get(key)
        value2 = dict2.get(key)
        if value1 == value2:
            diffs.append({
                'key': key,
                'type': 'unchanged',
                'value': value2
            })
        elif key not in dict1.keys():
            diffs.append({
                'key': key,
                'type': 'added',
                'value': value2
            })
        elif key not in dict2.keys():
            diffs.append({
                'key': key,
                'type': 'removed',
                'value': value1
            })
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diffs.append({
                'key': key,
                'type': 'has_children',
                'value': build_diff(value1, value2)
            })
        else:
            diffs.append({
                'key': key,
                'type': 'updated',
                'old_value': dict1[key],
                'new_value': dict2[key]
            })
    return diffs
