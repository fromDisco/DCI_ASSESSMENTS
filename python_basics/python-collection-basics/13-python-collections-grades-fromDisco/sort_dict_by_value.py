students = [
    {
        'name': 'Peter',
        'subjects': [
            {'name': 'English', 'grade': 'A'},
            {'name': 'German', 'grade': 'C'},
            {'name': 'Maths', 'grade': 'B'}
        ]
    },
    {
        'name': 'Robin',
        'subjects': [
            {'name': 'English', 'grade': 'D'},
            {'name': 'German', 'grade': 'B'},
            {'name': 'Maths', 'grade': 'B'}
        ]
    },
    {
        'name': 'Michael',
        'subjects': [
            {'name': 'English', 'grade': 'A'},
            {'name': 'German', 'grade': 'F'},
            {'name': 'Maths', 'grade': 'F'}
        ]
    },
]


def sort_out(people):
    """
    Sort students out, who have 2 or more F notes

    Parameters:
        people (list): list contains dicts, 
        each one for one student.

    Returns: 
        passed (list): list contains dicts,
        is cleaned up, students with to many 
        Fs are sorted out
    """
    # empty list for students who passed the class
    passed = []

    for student in people:
        # counter for the F grades
        counter = 0

        # dive one step into the dict, before the next loop starts
        student_subjects = student["subjects"]

        for subjects in student_subjects:
            if subjects["grade"] == "F":
                counter += 1

        if counter < 2:
            # if student has less than 2 Fs,
            # add to passed (list)
            passed.append(student)

    return passed


print(sort_out(students))
