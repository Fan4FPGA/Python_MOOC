#函数复用

'''
import turtle
import time
def drawgap():
    turtle.penup()
    turtle.fd(5)

def drawline(draw):
    drawgap()
    turtle.pendown()if draw else turtle.penup()
    turtle.fd(40)
    drawgap()
    turtle.right(90)

def drawdigit(digit):
    drawline(True) if digit in [2,3,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,1,3,4,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,6,8] else drawline(False)
    turtle.left(90)
    drawline(True) if digit in [0,4,5,6,8,9] else drawline(False)
    drawline(True) if digit in [0,2,3,5,6,7,8,9] else drawline(False)
    drawline(True) if digit in [0,1,2,3,4,7,8,9] else drawline(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)

def drawdate(date):#data为日期，格式为：'%Y-%m=%d+'
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=("Arial",18,"normal"))
            turtle.pencolor("green")
            turtle.fd(40)
        elif i == '=':
            turtle.write('月',font=("Arial",18,"normal"))
            turtle.pencolor("blue")
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=("Arial",18,"normal"))
        else:
            drawdigit(eval(i))


def main():
    turtle.setup(800, 350, 200, 200)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawdate(time.strftime('%Y-%m=%d+',time.gmtime()))
    turtle.hideturtle()
    turtle.done()

main()
'''


#函数递归
'''
def fact(n):
    if n == 0:
	    return 1;
    else:
	    return n*fact(n-1)
print(fact(5))
'''
'''
def rvs(s):
    if s == "":
	    return s
    else:
	    return rvs(s[1:]) + s[0]
print(rvs('123456789'))
'''
'''
def feibo(n):
    if n == 1 or n == 2:
	    return 1;
    else:
	    return feibo(n - 1) + feibo(n - 2)
for n in range (1,13):
    print(feibo(n))
'''

count = 0
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("{}:{}-->{}".format(1,src,dst))
        count += 1
    else:
        hanoi(n-1,src,mid,dst)
        print("{}:{}-->{}".format(n,src,dst))
        count += 1
        hanoi(n-1,mid,dst,src)

hanoi(3,"A","B","C")















