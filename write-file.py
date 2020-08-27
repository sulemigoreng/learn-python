'''
r read
r+ read and write
w write -> overwrite the whole file
a append
'''

employee_file = open("employees.txt", "a")

employee_file.write("\nKelly - Customer Service")

employee_file.close()