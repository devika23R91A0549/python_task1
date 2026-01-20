# Import date module to get today's date
from datetime import date

# Take user input for name and internship role
name = input("Enter your name: ")
role = input("Enter your internship role: ")

# Get today's date
today_date = date.today()

# Print the user details
print("Name:", name)
print("Internship Role:", role)
print("Today's Date:", today_date)
