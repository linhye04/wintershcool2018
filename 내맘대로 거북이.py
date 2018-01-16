import turtle

t=turtle.Turtle()
t.width(3)
t.shape("turtle")
t.color("hotpink")
t.shapesize(2,2)
#거북이를 2배로 늘린다

while True:
    command=input("명령어를 입력하시오.")
    if command=="l":
        t.left(90)
        t.fd(100)
    if command=="r":
        t.right(90)
        t.fd(100)
    if command=="g":
        t.fd(100)
    if command=="b":
        t.back(100)
