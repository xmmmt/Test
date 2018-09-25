'''
#EP:1
celsius = float (raw_input("Enter a degree in celsius: "))
fahrenheit = (9 / 5) * celsius + 32
print('{} celsius is {} fahrenheit'.format(celsius,fahrenheit))

#EP:2
radius = eval (raw_input("Enter a degree radius,length: "))
area = radius * radius * 3.14
volume = area * length 
print("The area is {} , the volume is {}".format(area,volume))

#EP:3
feet = float (raw_input("Enter a degree in feet: "))
meter = feet * 0.305
print("{} feet is {} meters".format(feet,meter))

#EP:4
mass = float (raw_input("Enter the amount of water in kilograms: "))
initial = float (raw_input("Enter the initial temperature: "))
final = float (raw_input("Enter the final temperature: "))
Q = mass * (final-initial) * 4184
print("The energy needed is {}".format(Q))

#EP:5
balance,rate = eval(raw_input("Enter balance,rate: "))
interest = balance * (rate / 1200)
print("The interest is {}".format(interest))

#EP:6
v0,v1,t = eval(raw_input("Enter v0,v1,t: "))
a = (v1 - v0) / t
print("The average accelration is {}".format (a))

#EP:7
saving = float (raw_input("Enter the monthly saving: "))
a = (((((((((saving * (1 + 0.00417))+saving) * (1 + 0.00417)) + saving) * (1 + 0.00417)) + saving) * (1 + 0.00417)) + saving) * (1 + 0.00417) + saving) * (1 + 0.00417)
print("After the sixth month,the account value is {} : ".format(a))

'''
#EP:8
number = int (raw_input("Enter a number between 0 and 1000: "))
a = number % 10
b = ( number / 10 ) % 10
c = ( number / 100 )
digits = a + b + c
print("the sum of the digits is {}".format(digits))
