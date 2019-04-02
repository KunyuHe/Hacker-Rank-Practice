def gradingStudents(grades):
    output = []

    for grade in grades:
        if grade >= 38 and grade % 5 >= 3:
            output.append(5 * (grade//5 + 1))
        else:
            output.append(grade)

    return output
