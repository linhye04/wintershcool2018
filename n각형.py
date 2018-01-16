import turtle

n=int(input("몇 각형을 그릴까요?"))
w=turtle.Pen()
w.shape("turtle")
w.color("pink")

number=0
while number<n:
   w.fd(123)
   w.left(360/n)
   number=number+1
