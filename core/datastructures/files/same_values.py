assignments = {'Juan': 5, 'Antonio': 5, 'Inma': 5, 'Ana': 5, 'Esteban': 5}

marks = list(assignments.values())
first_mark = marks[0]
for mark in marks[1:]:
    if mark != first_mark:
        print('Different values')
        break
else:
    print('Same values')
