from Student import Student  # From the Student File, import the Student class

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 3.6, False)

print(student1.gpa)
print(student2.gpa)

print(student1.on_honor_roll())
print(student2.on_honor_roll())