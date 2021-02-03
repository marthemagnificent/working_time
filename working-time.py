# Name: Markayla Brown
# working-time.py
#
# Problem: Calculate the working time of employees on a team and outputs them.
# Certification of Authenticity:
# <include one of the following>
# I certify that this assignment is entirely my own work.
# I certify that this assignment is my own work, but I
# discussed it with: <Name(s)>


def main():
    #variables for time
    hours, minutes = 0, 0
    tempHours, tempMinutes = 0, 0
    #ask the user how many employees are on the team
    employees = eval(input("How many employees are on your team? "))
    #loopemp = employees + 1
    #loop to count the employees
    for i in range(employees):
        #creates a clean number for the sentence asking about each employee
        empsent = i + 1
        #sets the times entered to temp values to be added to actual time
        #these variables hold the user amounts temp
        newHours, newMinutes = eval(input("How much time did employee #" + str(empsent) + " work? "))
        #add input hours to temp for math
        tempHours = tempHours + newHours
        #adds input minutes to temp for math
        tempMinutes = tempMinutes + newMinutes
        #math to turn the minutes into hours
        carryHours = tempMinutes // 60
        #math to get remainder minutes from full minute amount
        minutes = tempMinutes % 60
        #add carry over hours to hours 
        hours = tempHours + carryHours
    print("Your team has worked " + str(hours) + " hours and " + str(minutes) +" minutes")
    #print(loopemp)
    print(empsent)


main()    