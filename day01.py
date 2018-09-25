'''
#EP:1
a = raw_input(">>") # return str
b = raw_input(">>") # return str
int_a = int(a) #int :: change to int type
float_b = float(b) # change to float
area = int_a * float_b
print(area)

#EP:2
time_ = int(raw_input(">>")) # change int,raw_input returns string
min_ = time_ //60 # get mins
times = time % 60 # get times
print('{}mins{}times',format(min_,times))
'''

#EP:3
x,y,a,b,c = 1,1,0,0,0
part1 =(3 + 4 * x) / 5
part2 = 10 * (y-5) * (a + b + c)/ x
part3 = 9 * ((4/x) + (9+x)/y)
res = part1 - part2 + part3
print(res)
