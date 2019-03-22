#import the datetime module to get current year
from datetime import datetime

#user inputs name
name = input("Enter your name: ")
#user inputs age and convert to integer
age = int(input("Enter your age: "))

#get current year and convert to integer
current_year = int(datetime.now().strftime("%Y"))
#print(current_year)
#calculate date of birth of the user from current year and age
dob = current_year - age
#get age of 100 by adding 100 to date of birth
age_of_100 = dob + 100
#output the message
print(name + ", you will turn 100 years in the year " + str(age_of_100))
