# Name: Markayla Brown
# working-time.py
#
# Problem: Calculate the working time of employees on a team and outputs them.
# Certification of Authenticity:
# <include one of the following>
# I certify that this assignment is entirely my own work.
# I certify that this assignment is my own work, but I
# discussed it with: <Name(s)>


#variables for time
hours, minutes = 0, 0
#ask the user how many employees are on the team
employees = eval(input("How many employees are on your team? "))
#loopemp = employees + 1
#loop to count the employees
for i in range(employees):
    #creates a clean number for the sentence asking about each employee
    empsent = i + 1
    #sets the times entered to temp values to be added to actual time
    newHours, newMinutes = eval(input("How much time did employee #" + str(empsent) + " work?"))
    #adds temp hours to hours accumulator variable
    hours = hours + newHours
    #adds temp minutes to the accumulator variable
    minutes = minutes + newMinutes
print(hours, minutes)
#print(loopemp)
print(empsent)