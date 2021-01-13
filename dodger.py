import turtle

window = turtle.Screen()
window.setup(width=800, height=600)
window.bgcolor('black')
window.tracer(0)

#Our Game Objects
#Balls

balls = int(input('Set difficulty:'))
for i in range(0, balls):
    ball[] = turtle.Turtle()
    ball.color('green')
    ball.shape('circle')
    ball.penup()
    ball.speed(0)
    ball.dx = 0.2
    ball.dy = 0.2


#The Game Loop
while True:
    window.update()    
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)
#Bouncing off 
    if ball.ycor() > 270:
        ball.sety(270)
        ball.dy *= -1
    if ball.xcor() > 350:
        ball.setx(350)
        ball.dx *= -1
    if ball.ycor() < -270:
        ball.sety(-270)
        ball.dy *= -1
    if ball.xcor() < -370:
        ball.setx(-370)
        ball.dx *= -1
    



    

