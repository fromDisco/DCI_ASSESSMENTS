data = {
    'students': [
        {
            'name': 'Josephine',
            'subjects': [
                {
                    'name': 'English',
                    'teacher': 'Mr. Hoover'
                }
            ]
        },
        {
            'name': 'Luke',
            'subjects': [
                {
                    'name': 'History',
                    'teacher': 'Mrs. Peters'
                }
            ]
        },
        {
            'name': 'Julia',
            'subjects': [
                {
                    'name': 'Chemistry',
                    'teacher': 'Mrs. Fauci'
                }
            ]
        }
    ]
}


def get(db, path):
    """
    Accessing a value in a nested dictionary

    Parameters:
        db (dict): dict with nested lists and dicts
        path (str): path to desired value, seperated by "."

    Returns:
        value (str): if path is valid
        (None): if path is not valid
    """
    split_path = path.split(".")
    temp_obj = db

    for path in split_path:
        if path.isdigit():
            path = int(path)

        try:
            temp_obj = temp_obj[path]
        except (KeyError, IndexError):
            return

    return temp_obj


print("\n# students.1.subjects.0.name:")
print(get(data, 'students.1.subjects.0.name'))
# History

print("\n# students.0.subjects.0.teacher:")
print(get(data, 'students.0.subjects.0.teacher'))
# Mr. Hoover

print("\n# students.8.subjects.0.name:")
print(get(data, 'students.8.subjects.0.name'))
# IndexError -> None

print("\n# students.1.sports.0.name:")
print(get(data, 'students.1.sports.0.name'))
# KeyError -> None
