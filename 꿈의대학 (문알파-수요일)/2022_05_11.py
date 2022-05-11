# # #프린트물

# #문제 1

# import datetime as dt

# now = dt.datetime.now()
# name = input("이름을 입력하시오: ")
# age = int(input("나이를 입력하시오: "))
# year_100 = 100 - age
# print(f"{name}씨는 {now.year + year_100}년에 100살이시네요!")

# #문제 2

# n1 = int(input("첫 번째 숫자를 입력하시오: "))
# n2 = int(input("두 번째 숫자를 입력하시오: "))
# n3 = int(input("세 번째 숫자를 입력하시오: "))

# sum = n1 + n2 + n3
# avg = sum / 3

# print(f"{n1} {n2} {n3} 의 평균은 {avg} 입니다.")

# # 문제 3

# r = int(input("반지름을 입력하시오: "))
# pi = 3.141592
# print(f"반지름이 10 인 원의 넓이 = {(r ** 2) * pi}")

# # 문제 4

# import turtle as tr
# tr.shape("turtle")

# radius = 50

# for i in range(3):
#     x = i * 100
#     tr.up()
#     tr.goto(x, 0)
#     tr.down()
#     tr.circle(radius = radius)
#     radius += 20

# # 문제 5

# import turtle as tr

# tr.shape("turtle")
# side = 100

# for _ in range(3):
#     tr.forward(side)
#     tr.left(120)

# # 문제 6

# import turtle as tr

# tr.shape("turtle")
# side = 200

# for _ in range(3):
#     tr.forward(side)
#     tr.left(120)

# # 문제 7

# import turtle as tr

# tr.shape("turtle")

# side = 100
# angle = 90

# for i in range(8):
#     tr.forward(side)
#     if(i < 4):
#         tr.right(angle)
#     elif(i >= 4):
#         tr.left(angle)

# tr.left(180)

# for i in range(8):
#     tr.forward(side)
#     if(i < 4):
#         tr.left(angle)
#     elif(i >= 4):
#         tr.right(angle)
    
# x = 7
# y = 6
# print(type(x + y))
# print(x + y)

# x = '7'
# y = '6' 
# print(type(x + y))
# print(x + y)

# x = 100
# y = 200
# sum = x + y
# print(x, "과", y, "의 합은", sum, "입니다.")

# name = input("이름을 입력하시오: ")
# print(name, "씨, 안녕하세요?")
# print("파이썬에 오신 것을 환영합니다.")
# print(type(name))

# x = int(input("첫번째 정수를 입력하시오:"))
# y = int(input("첫번째 정수를 입력하시오:"))

# sum = x + y
# print(x, "과", y, "의 합은", sum, "입니다.")

# p = int(input("분자를 입력하시오:"))
# q = int(input("분모를 입력하시오:"))

# print("나눗셈의 몫 = ", p // q)
# print("나눗셈의 나머지 = ", p % q)

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return fact(n - 1) * n

# num = int(input("팩토리얼을 구할 숫자를 입력하시오."))
# print(f"{num}! = {fact(num)}")