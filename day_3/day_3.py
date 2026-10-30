#variables Q1,Q2,Q3
age=23
height=5.3
complex_num=1+2j
print("Age:",age)
print("Height:",height)
print("Complex Number:",complex_num)

#area of traiangle Q4
base=float(input("Enter base:"))
height=float(input("Enter height:"))
area=0.5*base*height
print("The area of the triangle is ",area)

#Q5.perimeter of triangle
a=float(input("Enter side a:"))
b=float(input("Enter side b:"))
c=float(input("Enter side c:"))
perimeter=a+b+c
print("The perimeter of the triangle is ",perimeter)

#Q6.rectangle
length=int(input("Enter length: "))
width=int(input("Enter width:"))
areaRect=length*width
perimeterRect=2*(length+width)
print("The area of the rectangle is ",areaRect)
print("The perimeter of the rectangle is ",perimeterRect)

#Q7.circle
radius=float(input("Enter radius:"))
areaCircle=3.14*radius*radius  
perimeterCircle=2*3.14*radius
print("The area of the circle is ",areaCircle)
print("The perimeter of the circle is ",perimeterCircle)

# Q8 - My first attempt
x = float(input("Enter x:"))
y = 2*x - 2
print("Calculated y:", y)

# Correct calculation
slope = 2
x_intercept = 1
y_intercept = -2

print("Slope:", slope)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

#Q9.euclidean distance
x1=float(input("Enter x1:"))    
y1=float(input("Enter y1:"))
x2=float(input("Enter x2:"))
y2=float(input("Enter y2:"))
eucli_dist=((x2-x1)**2+(y2-y1)**2)**0.5
m=(y2-y1)/(x2-x1)
print("The slope is ",m)
print("The Euclidean distance is ",eucli_dist)

# Q10
print("Are both slopes equal:", m == slope)

#Q11.quadratic formula
x3=int(input("input value:"))
y3=x3**2+6*x3+9
print("value of y:",y3)
for x3 in range(-9,10):
    y3=x3**2+6*x3+9
    if y3==0:
        print("y is 0 ,when x is:",x3)

#Q12.comparison
print("length of python:",len("python"))
print("length of dragon:",len("dragon"))
print("python is equal to Dragon",len("python") != len("dragon"))
#Q13

if "on" in "python" and "on" in  "dragon":
    print("True")
else:
    print("False")

#Q14
print("Checking jargon is in I hope this course is not full of jargon:","jargon" in "I hope this course is not full of jargon")
#Q15
if "on" not in "python" and "on" not in  "dragon":
    print("True")
else:
    print("False")

#Q16
value=len("python")
print("length of python:",value)
print("value into float :",float(value))
print("value into  string:",str(value))

#Q17
num1=int(input("Enter a number:"))
if num1%2==0:
    print("Number is even")
else:
    print("Number is odd")
#Q18
num2=2.7
if 7//3==int(num2):
    print("True")
else:
    print("False")
#Q19
print("Check if type of '10' is equal to type of 10",type('10') is type(10) )
#Q20
print(int(float('9.8'))==10)
#Q21
hours=int(input("Enter hours:"))
rate=float(input("Enter rate per hour:"))
print("Your weekly earning is:",hours*rate)
#Q22
year=int(input("Enter numbers of years you  lived:"))
print("You have lived for approximately",year*365*24*60*60,"seconds.")
#Q23
for i in range(1,6):
    print(i,"\t1","\t",i,"\t",i**2,"\t",i**3)