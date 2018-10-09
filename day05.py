#_*_coding:utf8-
'''
#1:类
class Joker(object):
    print'[+] Joker is a good man'
class Joker2:
    a = 1000
    print a
if __name__ == '__main__':
    pass

#2:初始化的类
class joker:
    def __init__(self):
    #   print'hiahiahia~'
    self.shuai = 'lalalal'
    self.chou = 'hiahiahiah'
def fuc(self):
    print self.shuai
    print self.chou
#if __name__=='__main__':
#    joker().fuc()                #括号很重要

#3:类 奇偶数
class joker1:
    def __init__(self):
        self.num = 10000
    def check(self):
        if self.num % 2 == 0:
            print'[+] ou'
        else:
            print'[+] ji'
if __name__=='__main__':
    joker1().check()

#4:
class joker2:
    def __init__(self):
        self.num = 10
        print'[+] init over'
    def num_2(self):
        self.num = self.num ** 2
        print self.num
    def num_3(self):
        self.num = self.num ** 3
        print self.num
a = joker2()
a.num_2()
a.num_3()
'''  
#5:类长方形（继承）
class Rectangle:
    def __init__(self,width =1,height =2):
        self.width =width
        self.height =height
    def getArea(self):
        res = self.width * self.height
        print res
    def getPerimeter(self):
        res2 = (self.width + self.height) * 2
        print res2
Rectangle(4,40).getArea()
Rectangle(4,40).getPerimeter()

Rectangle(3.5,35.7).getArea()
Rectangle(3.5,35.7).getPerimeter()
