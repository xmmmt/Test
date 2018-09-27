'''
#EP:1 
import math
r = float(raw_input("Enter the length the center to a vertex: "))
s = float(math.sin(math.pi/5) * 2 * r)
area = float((5 * s * s) / ((math.tan(math.pi/5)) * 4))
print("The area of the pentagon is : {}".format(area))

#EP:2
import math
x1,y1 =eval(raw_input("Enter point 1 (latitude and longitude) in degrees: "))
x2,y2 =eval(raw_input("Enter point 2 (latitude and longitude) in degrees: "))
x1 = math.radians(x1)
x2 = math.radians(x2)
y1 = math.radians(y1)
y2 = math.radians(y2)
a = math.sin(x1) * math.sin(x2)
b = math.cos(x1) * math.cos(x2) * math.cos(y2 - y1) 
d = 6371.01 * (math.acos(a + b))
print("The distance between the two points is {} KM".format(d))

#EP:3
import math
s = float(eval (raw_input("enter the side: ")))
area = (5 * s * s) / (4 * (math.sin(math.pi/5)) / (math.cos(math.pi/5)))
print("The area of the pentagon is {}".format(area))

#EP:4
import math
n = eval(raw_input("Enter the number of side: "))
s = eval(raw_input("Enter the side: "))
area = (n * pow(s,2)) / (4 * (math.sin(math.pi/n))/(math.cos(math.pi/n)))
print("The area of the pentagon is {}".format(area))

#EP:5
A = eval(raw_input("Enter an ASCII code: "))
a = chr(A)
print("The character is {}".format(a))
'''

#EP：6
name = raw_input("Enter empolyee's name: ")
hour = eval(raw_input("Enter number of days elapsed since today： "))
rate = eval(raw_input("Enter hourly pay rate: "))
federal = eval(raw_input("Enter federal tax withholding rate: "))
state = eval(raw_input("Enter state tax withholding rate: "))
print("Employee name: {} ".format(name))
print("Hours worked: {} ".format(hour))
prinx
