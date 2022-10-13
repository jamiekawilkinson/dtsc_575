# Create a program, change.py, that has a function that takes 5 arguments that
# correspond to the number of $1 dollar bills, quarters, dimes, nickels, and
# pennies, respectively. Calculate the total value of that change, and print "The
# total value of your change is $x" where x is equal to the total value.


'''
def change():
    dollars = int(input("Enter the number of $1 bills: "))
    quarters = int(input("Enter the number of quarters: "))
    dimes = int(input("Enter the number of dimes: "))
    nickles = int(input("Enter the number of nickles: "))
    pennies = int(input("Enter the number of pennies: "))
    
    change = (dollars * 1) + (quarters * 0.25) + (dimes * 0.10) \
        + (nickles * 0.05) + (pennies * 0.01)
    change = round(change, 2)
        
    print("The total value of your change is $", change)
    
change()
'''

import sys

dollars = int(sys.argv[1])
quarters = int(sys.argv[2])
dimes = int(sys.argv[3])
nickles = int(sys.argv[4])
pennies = int(sys.argv[5])


def change():
    change = (dollars * 1) + (quarters * 0.25) + (dimes * 0.10) \
        + (nickles * 0.05) + (pennies * 0.01)
    change = round(change, 2)
    print("The total value of your change is $" + str(change))
    
change()