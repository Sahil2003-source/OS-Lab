students = ("Amit", "Bina", "Chetan", "Divya", "Esha")

print(students)

students = students + ("Farhan",)
print(students)

students = students[:2] + students[3:]
print(students)

print(students[1:4])

temp_list = list(students)
temp_list[2] = "Gaurav"
students = tuple(temp_list)

print(students)
