## task 1
Name = "Zainab"
Hobby = "Reading books"
Age = 20
country = "Pakistan"
current_year=2025
graduation_year = current_year + 4
year_left = graduation_year - current_year
print(f"Full Name: {Name}")
print(f"Age: {Age} years old")
print(f"Country: {country}")
print(f"Current Year: {current_year}")
print(f"Hobby: {Hobby}")
print(f"Expected Graduation Year: {graduation_year}")
print(f"{year_left} years are left until graduation.")




#------------------------------------------------------------------------------------------------------#

# task 2 
# profile of person 1
Name1="Zainab"
Profession1="Data Scientist"
Country1="Pakistan"
is_employed1=True

# profile of person 2
Name2="Ali"
Profession2="Software Engineer"    
Country2="Pakistan"
is_employed2=False

# profile of person 3
Name3="Sara"
Profession3="Web Developer"
Country3="Pakistan" 
is_employed3=True

print("+---------+-------------------+-----------+-----------+")
print("|  Name   |   Profession      | Country   | Employed  |")
print("+---------+-------------------+-----------+-----------+")
print(f"| {Name1:<7} | {Profession1:<17} | {Country1:<9} | {str(is_employed1):<9} |")
print(f"| {Name2:<7} | {Profession2:<17} | {Country2:<9} | {str(is_employed2):<9} |")
print(f"| {Name3:<7} | {Profession3:<17} | {Country3:<9} | {str(is_employed3):<9} |")
print("+---------+-------------------+-----------+-----------+") 
#------------------------------------------------------------------------------------------------------#

# task 3
name="zainab"
age=20
cgpa=3.95
currentlystudying=True
height=5.3

print("Name",name,type(name))
print("Age",age,type(age))
print("CGPA",cgpa,type(cgpa))
print("Student",currentlystudying,type(currentlystudying))
print("Height",height,type(height))

name=int(name)  # This will raise an error because 'name' is a string
age=float(age)  # This will raise an error because 'age' is an integer
cgpa=str(cgpa)  # This will raise an error because 'cgpa' is a float

#------------------------------------------------------------------------------------------------------#

## task 4

oftype=input("Enter any thing for testing purpose: ")
if type(oftype) == str:
    print("You Entered a String")
elif type(oftype) == int:
    print("You Entered an Integer")
elif type(oftype) == float:
    print("You Entered a Float")

#------------------------------------------------------------------------------------------------------#

# task 5  Design a command-line survey 

Name=input("Enter your Name :")
favroitefood=input("Enter your favorite food :")
birthyear=int(input("Enter your Birth year :"))
favoritenumber=int(input("Enter your favorite number :"))
favoritelanguage=input("Enter your favorite language :")
print(f'Survey Results:\nName: {Name}\nFavorite Food: {favroitefood}\nBirth Year: {birthyear}\nFavorite Number: {favoritenumber}\nFavorite Language: {favoritelanguage}')


#------------------------------------------------------------------------------------------------------#

#task 6
yearofbirth=int(input("Enter your Birth year:"))
currentage=2025-yearofbirth
print(f"Your current age is: {currentage}")
if currentage >= 18:
    print("You are eligible to vote.")
else:
    (f"You are not eligible to vote. ")

#------------------------------------------------------------------------------------------------------#

#task 7

English=int(input("Enter your English marks: "))
Urdu=int(input("Enter your Urdu marks: "))
Maths=int(input("Enter your Maths marks: "))
Science=int(input("Enter your Science marks: "))
Computer=int(input("Enter your Computer marks: "))

percentage=(English+Urdu+Maths+Science+Computer)/5
if percentage >= 90:
    grade = "A+"
    print(f"Your percentage is {percentage}%, which is an A+ grade.")
    if 80 <= percentage <= 89:
        grade = "B"
    print(f"Your percentage is {percentage}%, which is an A grade.")
    if 70 <= percentage <= 79:
      grade = "B"
    print(f"Your percentage is {percentage}%, which is a B grade.")
elif percentage > 70:
    grade = "fail"
    print(f"Your percentage is {percentage}%, which is a C grade.")

#------------------------------------------------------------------------------------------------------#

#task 8
try:
    temperature = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (temperature * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit}°F")
    fahrenheit_input = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit_input - 32) * 5/9
    print(f"The temperature in Celsius is: {celsius}°C")
except ValueError:
    print("Invalid input!")
