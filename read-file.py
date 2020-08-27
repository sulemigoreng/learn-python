'''
r read
r+ read and write
w write
a append
'''

employee_file = open("employees.txt", "r")

print(employee_file.readable())  # return a boolean value whether the file is readable or not

# print(employee_file.readline())
# print(employee_file.readline())

# print(employee_file.readlines())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()