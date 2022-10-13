# DTSC 575: Principles of Python Programming

This repository contains all programming assignments and projects completed in DTSC 575.

**Course Description:** This course will teach students the introductory skills of programming, problem solving, and algorithmic thinking in Python. Topics include variables, input/output, conditional statements/logic, Boolean expressions, flow control, loops and functions. Approachable for students who have no experience with Python.

## Project Descriptions:

1. array.py:** Create a program called array.py that has a function that takes four integer arguments.  Those arguments should be put into an Numpy array.  The function will have two print statements.  The first will print the type of the array you create (which should be <class ‘numpy.ndarray’>).  The second will print the multiplication of the four items in your array. 

2. capcount.py: Create a program called capCount.py that has a function that takes in a string and prints the number of capital letters in the first line, then prints the sum of their indices in the second line.

3. change.py: Create a program, change.py, that has a function that takes 5 arguments that correspond to the number of $1 dollar bills, quarters, dimes, nickels, and pennies, respectively.  Calculate the total value of that change, and print "The total value of your change is $x" where x is equal to the total value.

4. classname.py: Create a program called classname.py.  The program should define a class called person that has one method called hello, and one attribute called name, which represents the name of the person.

5. countVowels.py: Create a program called countVowels.py that has a function that takes in a string then prints the number of unique vowels in the string (regardless of it being upper or lower case).

6. digits.py: Create a program, digits.py, that has a function that takes a number and prints the number of digits in the number.  It should work for numbers with decimals, too.

7. fastfood.py: Use the fastfood.csv file to complete the following assignment. Create a file, fastfood.py, that loads the .csv file and runs a regression predicting calories from total_fat, sat_fat, cholesterol, and sodium, in that order.  Add a constant using sm.add_constant(data).

8. german.py: Use the german_credit_data.csv file to complete the following assignment. Create a file, german.py, that loads the .csv file and runs a regression predicting credit amount from age and duration, in that order.  Add a constant using sm.add_constant(data).  You will need to rename the column 'Credit amount' and should change it to 'Credit_amount'. 

9. gpacalc.py: Use this exact dictionary to complete this assignment (Do NOT alter this dictionary - points will be deducted if dictionary is changed): 
{'A':4.0, 'A-':3.66, 'B+':3.33, 'B':3.0, 'B-':2.66, 'C+':2.33, 'C':2.0, 'C-':1.66, 'D+':1.33, 'D':1.00, 'D-':.66, 'F':0.00}

Create a program, gpacalc.py, that takes four letter grade arguments and prints out the corresponding GPA, to two decimals.  Your program should work both in arguments are upper-case and lower-case.  The values should be in two decimal places. Your program should print in the form: “My GPA is x”, where x is equal to the GPA calculation.

10. inrange.py: Create a program inrange.py that has a function that takes one integer argument.  The function will print a list of all values between 5000 and 8000 that is divisible by (1) the integer argument, and (2) the argument + 4.

11. longest.py: Create a program, longest.py, that has a function that takes one string argument and prints a sentence indicating the longest word in that string.  If there is more than one word print only the first.  Your print statement should read: “The longest word is x”, where x = the longest word.  The word should be all lowercase.

12. luke.py: Create a program, luke.py, using the following dictionary: relations = {'Darth Vader':'father', 'Leia':'sister', 'Han':'brother in law', 'R2D2':'droid', 'Rey':'Padawan', 'Tatooine':'homeworld'}. 

The program will take one argument, corresponding to one of the relations’ keys.  The program will print out the statement: Luke, I am your x, where x = the relationship.  

13. max3.py: Create a program, max3.py, that has a function that takes three integer arguments.  The program will then print out the highest of the three values.

14. mintosec.py: Create a program, mintosec.py, that takes one integer argument representing a number of minutes.  The program will convert the argument to the corresponding number of seconds, and print that value out.

16. palindrome.py: Create a program, palindrome.py, that has a function that takes one string argument and prints a sentence indicating if the text is a palindrome.  The function should consider only the alphanumeric characters in the string, and not depend on capitalization, punctuation, or whitespace.

17. presidents.py: You should use Pandas (import pandas as pd) for this assignment. Create a program, presidents.py, that takes two arguments.  These arguments will correspond to the start and stop of a slice, respectively.  It will slice the heights column in the president_heights.csv files. Then print off the average height, rounded to two decimals, of the selected presidents in the following form:

The average height of presidents number x to y is z where:
x = start of the slice
y = end of the slice
z = calculated average

18. quadratic.py: Create a program, quadratic.py, that takes in three arguments that represent the a, b, and c values in the quadratic formula.  The values should be in two decimal places.  You do not need to account for imaginary values.  Then print out both roots in the form: “The solutions are x and y”, where x and y correspond to the positive and negative roots, respectively.

19. randdf.py: Create a program called randdf.py that has a function that takes two integer arguments and prints a Pandas dataframe.  The two arguments will correspond to the number of rows and number of columns, respectively.  The dataframe should be filled with random integers from 0 to 100.  Set your random seed to 56. 

20. reallyrandom.py: Create a program called reallyrandom.py that has a function that takes in three arguments and prints one integer.  Your random seed should be set to 42.

The first argument should correspond to the size of a np.randint that has values from 0 to 10.  
The second is an integer that you will multiply the randint by.  
The third argument is a value you will index the result of the multiplication by. 

You will print the integer that was indexed as ‘Your random value is x’ where x = the result of the indexing. The program should not crash if the third value is larger than the first.

21. sacramento.py: Use the sacramento.csv file to complete the following assignment.  Create a file, sacramento.py, that loads the .csv file and runs a logistic regression.  The regression should predict whether or not a house has 1 or more than one bathroom based on beds, sqft, and price, in that order.  Note: you will not need to upload the .csv to CodeGrade because I have pre-loaded it.

You will need to create a new variable from baths, and it should make it such that those observations of 1 bath correspond to a value of 0, and those with more than 1 bath correspond to a 1.

Make sure to add a constant using sm.add_constant(X)

Your file should print the results in this way:

print(mod.params.round(2))
print(mod.pvalues.round(2))
print('The smallest p-value is for sqft')

22. temp.py: Create a program, temp.py, that takes in one numeric argument representing a Celsius value.  Then, print out the corresponding Fahrenheit value to two decimals in the form: The temperature is x degrees Fahrenheit, where x is the calculated Fahrenheit value.

23. username.py: Create a program, username.py, that has a function that takes as arguments a first and last name and creates a username.  The username will be the first letter of the first name in lowercase, the last 7 of the last name in lowercase, and the total number of characters in the first and last names.  For example, Eastern University would be eversity17. The program should print "Your username is x" where x is the username.
