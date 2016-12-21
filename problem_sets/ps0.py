# Problem Set 0, from Lecture 1 https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/unit-1/lecture-2-core-elements-of-a-program/MIT6_00SCS11_ps0.pdf

# Problem 1
#
# Write a program that does the following in order:
#     - Asks the user to enter his/her date of birth.
#     - Asks the user to enter his/her last name.
#     - Prints out the user’s last name and date of birth, in that order.

dob = raw_input("Enter your date of birth.")
lastName = raw_input("Enter your last name.")
print(lastName + ", " + dob)
