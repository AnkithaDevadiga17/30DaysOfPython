#day 2
#level-1
first_name="Anki"
last_name="devadiga"
full_name="Ankitha Devadiga"
country="India"
city="Udupi"
age=23
year=2026
is_married=False
is_true=True
is_light_on=True
course,subject,hobby="MCA","Python","Dance"

#printing
print("First Name:", first_name)
print("Last Name:", last_name)
print("Full Name:", full_name)
print("Country:", country)
print("City:", city)
print("Age:", age)
print("Year:", year)
print("Is Married:", is_married)
print("Is True:", is_true)
print("Is Light On:", is_light_on)
print("Course:", course)
print("Subject:", subject)
print("Hobby:", hobby)

#level2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(course))
print(type(subject))
print(type(hobby))

print(len(first_name))
length1=len(first_name)-len(last_name)
print("Comparing first and last name..")
print(len(first_name) == len(last_name))
num_1=5
num_2=4
sum=num_1+num_2
diff=num_1-num_2
mul=num_1*num_2
div=num_1/num_2
remainder=num_2%num_1
power=num_1**num_2
floor=num_1//num_2
#print values
print("Sum=",sum)
print("difference=",diff)
print("multiplication=",mul)
print("division=",div)
print("remainder=",remainder)  
print("power=",power)
print("floor division=",floor)

#circle problem
radius=30
area_of_circle=3.14*radius**2
circum_of_circle=2*3.14*radius
print("Area of circle",area_of_circle)
print("Circumference of circle:", circum_of_circle)
r=float(input("Enter the radius:"))
area_of_circle1=3.14*r**2
print("Radius :",r)
print("Area of Circle with user input=",area_of_circle1)

#input from user
firstNmae=input("Enter first name:")
lastName=input("Enter Last name:")
countryName=input("Country:")
age1=int(input("Age:"))
print("First Name:",firstNmae)
print("Last Name:",lastName)
print("Country:",countryName)
print("Age:",age1)
#keywords
help('keywords')