# Import the date class from the datetime module
# This is used to get today's current date
from datetime import date

# Ask the user to enter their name
# input() takes data from the keyboard and stores it in the variable 'name'
name = input("Enter your name: ")

# Ask the user to enter their internship role
# The entered value is stored in the variable 'role'
role = input("Enter your internship role: ")

# Get today's date using the date.today() function
# The current date is stored in the variable 'today_date'
today_date = date.today()

# Print the user's name
print("Name:", name)

# Print the user's internship role
print("Internship Role:", role)

# Print today's date
print("Today's Date:", today_date)
