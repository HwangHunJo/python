'''
import turtle

colors = ["red", "purple", "blue", "green", "yellow", "orange"]
t = turtle.Turtle()

turtle.bgcolor("black")
t.speed(0)
t.width(3)
length = 10

while length < 500:
    t.forward(length)
    t.pencolor(colors[length % 6])
    t.right(89)
    length += 5
'''

'''
import turtle
t = turtle.Turtle()
t.shape("turtle")
radius = 50

t.circle(radius)
t.fd(30)
t.circle(radius)
t.fd(30)
t.circle(radius)
'''


'''

import turtle
t = turtle.Turtle()


size = int(input("집의 사이즈는 얼마로 할까요?"))


t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)

t.forward(size)    
t.right(90)
    
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
'''

'''
import turtle
t = turtle.Turtle()
t.shape("turtle")
n = int(input("몇각형을 그리시겠어요?(3 - 6): "))

for _ in range(n):
    t.forward(100)
    t.left(360//n)
'''

'''
for i in range(5):
    for j in range(i+1):
        print("*", end = '')

    print()

for i in range(5):
    for j in range(5):
        print("*", end = '')
    print()
'''

'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(100, 100)
t.write("거북이가 여기로 오면 양수입니다.")
t.goto(100, 0)
t.write("거북이가 여기로 오면 0입니다.")
t.goto(100, -100)
t.write("거북이가 여기로 오면 음수입니다.")

t.goto(0, 0)
t.pendown()
s = turtle.textinput("","숫자를 입력하시오:")
n = int(s)

if(n > 0):
    t.goto(100, 100)
if(n == 0):
    t.goto(100, 0)
if(n < 0):
    t.goto(100, -100)
'''

'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("","이름을 입력하시오: ")
t.write("안녕하세요?" + s + "씨, 터틀 인사드립니다!")

for _ in range(4):
    t.left(90)
    t.fd(100)
'''

'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("","도형을 입력하세요:")
if s == "사각형":
    s = turtle.textinput("", "가로: ")
    w = int(s)

    s = turtle.textinput("", "세로: ")
    h = int(s)
    
    t.fd(w)
    t.left(90)
    t.fd(h)
    t.left(90)
    t.fd(w)
    t.left(90)
    t.fd(h)
'''

'''
import turtle
import random as r
t = turtle.Turtle()
t.shape("turtle")

for _ in range(30):
    length = r.randint(1, 100)
    t.forward(length)

    angle = r.randint(-180, 180)
    t.right(angle)
'''

'''
import turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.stamp()
move = 30

for _ in range(12):
    t.penup()
    t.forward(50)
    t.pendown()
    t.forward(25)
    t.penup()
    t.forward(15)
    t.stamp()
    t.home()
    t.right(move)
    move += 30
'''

'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.left(36)
for i in range(5):
    t.forward(200)
    t.left(144)
'''

import turtle

def drawBar(height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height), font = ('Times New Roman', 16, 'bold'))
    t.right(90)

    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

data = [120, 56, 309, 220, 156, 23, 98]

t = turtle.Turtle()
t.color("blue")
t.fillcolor("red")

t.pensize(3)

for d in data:
    drawBar(d)
    

