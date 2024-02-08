
def generate_diff(key, value_of_file1, value_of_file2):
    diff = {'key': key, 'old_value': value_of_file1, 'new_value': value_of_file2}
    if value_of_file1 == value_of_file2:
        diff['status'] = 'unchanged'
    elif value_of_file1 is None:
        diff['status'] = 'added'
    elif value_of_file2 is None:
        diff['status'] = 'removed'
    else:
        diff['status'] = 'updated'
    return diff
