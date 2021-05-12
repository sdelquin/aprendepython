students = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}

cleaned_students = {}
for key, value in students.items():
    new_key = key.replace(' ', '')
    cleaned_students[new_key] = value

print(cleaned_students)
