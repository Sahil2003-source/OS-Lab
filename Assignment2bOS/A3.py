students = {'Amit': 19, 'Bina': 21, 'Chetan': 22, 'Divya': 20, 'Esha': 23}

for name, age in students.items():
    if age > 20:
        print(name, age)

students['Farhan'] = 30

print(students.items())

del students['Amit']

average_age = sum(students.values()) / len(students)
print("Average age:", average_age)
