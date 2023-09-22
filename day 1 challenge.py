
#Declare your age as integer variable
age = 30
print('I am', age)

#Declare your height as a float variable
height = 171.01
print('My height is: ', height)

#Declare a variable that store a complex number
complex_number = 1+1j
print('this complex number is: ', complex_number)

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = 20
height = 10
area = base * height * 0.5
print('this triangle are is :', int(area))

base = input('what is the base?')
height = input('what is the height?')
area = int(base) * int(height) * 0.5
print('area of your triangle is: ', int(area))

'''
Write a script that prompts the user to enter side a, side b, 
and side c of the triangle. 
Calculate the perimeter of the triangle (perimeter = a + b + c).
'''
a = input('enter side a: ')
b = input('enter side b: ')
c = input('enter side c: ')
perimeter = int(a) + int(b) + int(c)
print("your triangle's perimeter is:", float(perimeter))

# Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) 
# and perimeter (perimeter = 2 x (length + width))

length = input('enter rectangle length: ')
width = input('get the rectangle width: ')
area = int(length) * int(width)
perimeter = 2 * (int(length) + int(width))
print("rectangle's area is", area, "and its perimeter is", perimeter)


'''
Get radius of a circle using prompt. Calculate the area 
(area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
'''
radius = input('what is the radius?')
area = 3.14 * (int(radius) ** 2)
circumference = 2 * 3.14 * int(radius)
print("your circle's area and circumference are as follows: ", area, "and", circumference)

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
point_1 = (0, -2)
point_2 = (1, 0)
'''
We see that:
x changes from 0 to 1
y changes from -2 to 0

To calculate slope, we use the formula:
slope = (change in y) / (change in x)
'''
slope =  (0 - (-2)) / (1 - 0)
print(int(slope))

#So slope is 2
'''
The x/y-intercept is the point where the line crosses the x/y-axis.
To find it, set y=0 and solve for x. then set x=0 and solve for y.
y = 2x - 2
so, x becomes 1 and y becomes -2
and x intercept is (1, 0) and y intercept is (0, -2)
'''

#Slope is (m = y2-y1/x2-x1). 
#Find the slope and Euclidean distance between point (2, 2) and point (6,10)

x1 = int(input("what is x1?"))
x2 = int(input("what is x2?"))
y1 = int(input("what is y1?"))
y2 = int(input("what is y2?"))

#slope
slope = (x2-x1)/(y2-y1)
print("slope is: ", slope)

#Euclidean distance
import math
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Euclidean distance is: ", distance)

'''
Calculate the value of y (y = x^2 + 6x + 9). 
Try to use different x values and figure out at what x value y is 
going to be 0.
'''
# Function to calculate y 
def calculate_y(x):
  y = x**2 + 6*x + 9
  return y

# Try different x values
x = -3 
y = calculate_y(x)
print(f"X = {x}, Y = {y}")

x = -2
y = calculate_y(x)  
print(f"X = {x}, Y = {y}")

x = -1
y = calculate_y(x)
print(f"X = {x}, Y = {y}") 

x = 0
y = calculate_y(x)
print(f"X = {x}, Y = {y}")
# We can see when x = -3, y = 0

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.

print(len('python') > len('dragon'))
print(len('python') != len('dragon'))

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon is in 'I hope this course is not full of jargon': ", 'jargon' in 'I hope this course is not full of jargon')

#There is no 'on' in both dragon and python
print('on'not in ('dragon' and 'python'))

#Find the length of the text python and convert the value to float and convert it to string.
def get_str(text) :
    string = str(float(len(text)))
    
    return string
text = 'python'
print(get_str(text))

'''
Even numbers are divisible by 2
and the remainder is zero. 
How do you check if a number is even or not using python?
'''

def even_checker(x):
  
 if x % 2 == 0:
  print(x, "is even")
 else:
  print(x, "is odd")

x = 8 
print(even_checker(x))


#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
check = 7//3
print(check is 2)

#Check if type of '10' is equal to type of 10
print(not(type('10') == type(10)))

#Check if int('9.8') is equal to 10
print(int(9.8) == 10)

'''
Writ a script that prompts the user to enter hours and rate per hour. 
Calculate pay of the person?
'''
def get_hours_wage():
  hours = float(input('hours: '))
  pr = float(input('pay rate: '))
  wage = int(hours*pr)

  print(f"wage this week is : {wage}")
get_hours_wage() 
  

#Write a script that prompts the user to enter number of years.
#Calculate the number of seconds a person can live.
def life_in_seconds():
    age = float(input('How old are you? '))
    seconds = int(age * 31_536_000)  # Use underscores for readability
    print(f"You have lived for {seconds} seconds.")

life_in_seconds()

#Write a Python script that displays the following table
#this s a matrix! it is not a day one challenge!
def generate_matrix(rows, cols):
    matrix = [[0] * cols for _ in range(rows)]
    for i in range(1, rows + 1):
        matrix[i - 1][0] = i
        matrix[i - 1][1] = 1
        matrix[i - 1][2] = i
        matrix[i - 1][3] = i ** 2
        matrix[i - 1][4] = i ** 3
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))

rows = 5 # Number of rows
cols = 5 # Number of columns
matrix = generate_matrix(rows, cols)
print_matrix(matrix)