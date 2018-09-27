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

#EP:6
name = raw_input("Enter employee's name:")
time = eval(raw_input("Enter number of hours worked in a work:"))
pay = eval(raw_input("Enter hourly pay rate:"))
lb = eval(raw_input("Enter federal tax withholding rate"))
zl = eval(raw_input("Enter state tax withholding rate:"))
print("Employee Name:"+name)
print("Hours Worked:"+str(time))
print("Pay Rate:"+str(pay))
p = time*pay
print("Gross Pay:"+str(p))
print("Deductions")
F = p*0.2
print("  Feseral Withholding:"+str(F))
S = p*0.09
print("  State withholding:"+str(S))
sum1 = F+S
print("  Total Deduction:"+str(sum1))
Np = p - sum1
print("Net Pay"+str(Np))

#EP:7
num = eval(raw_input("Enter an integer:"))
a = num % 10
b = num / 10
c = b % 10
d = b / 10
e = d % 10
f = d /10
print("The reversed number is:"+str(a)+str(c)+str(e)+str(f))

#EP:8
import hashlib
str1 = "wozuishuai"
h1 = hashlib.md5()
h1.update(str1.encode(encoding = 'utf-8'))
print('jiami',h1.hexdigest())

#EP:9
import math
a,b,c = eval(raw_input("Enter a,b,c:"))
if (b*b-4*a*c)>0:
    r1=(-1*b+math.sqrt(b*b-4*a*c))/2*a
    r2=(-1*b-math.sqrt(b*b-4*a*c))/2*a
    print("The roots are"+str(r1)+"and"+str(r2))
elif (b*b-4*a*c)==0:
    r1=(-1*b+math.sqrt(b*b-4*a*c))/2*a
    print("The root is"+str(r1))
else:
    print("The equation has no real roots")
    
#EP:10
import random
s = eval(raw_input(">>"))
a = random.randrange(1,101)
b = random.randrange(1,101)
c = a+b
if s==c:
    print("True")
else:
    print("Flase")
    
#EP:11
day = eval(raw_input("Enter today's day:>>"))
hday = eval(raw_input("Enter the number of days elapsed since today:>>"))
a=day+hday%7
b=a%7
if b==1:
    print("monday")
elif b==2:
    print("tuesday")
elif b==3:
    print("wednesday")
elif b==4:
    print("thursday")
elif b==5:
    print("friday")
elif b==6:
    print("saturday")
elif b==0:
    print("sunday")
