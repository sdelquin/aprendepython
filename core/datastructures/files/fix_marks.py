marks = {
    'John': 4,
    'Marc': 7,
    'Meryl': 2,
    'Anthony': 8,
    'Carol': 3,
    'Sarah': 6,
}

passed = {student.upper(): mark for student, mark in marks.items() if mark >= 5}
failed = {student.lower(): mark for student, mark in marks.items() if mark < 5}

print(f'Aprobaron: {passed}')
print(f'Suspendieron: {failed}')
