import turtle,time, sys 
#The window where we play the game 
window = turtle.Screen()
window.title('my first game')
window.bgcolor('black')
window.setup(width=800, height=600)
window.tracer(0)

#The objects in play
#paddle one 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.color('orange')
paddle_a.penup()
paddle_a.goto(-370, 0)

#paddle two 
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.color('orange')
paddle_b.penup()
paddle_b.goto(370, 0)

#ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.speed(0) 
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2
#Now let's make it a working game
def paddle_a_up():
    y = paddle_a.ycor()
    y+=20
    if y in range(-240, 260):
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y-=20
    if y in range(-240, 260):
        paddle_a.sety(y)


def paddle_b_up():
    y2 = paddle_b.ycor() 
    y2 += 20
    if y2 in range(-240, 260):
        paddle_b.sety(y2)

def paddle_b_down():
    y2 = paddle_b.ycor()
    y2 -= 20
    if y2 in range(-240, 260):
        paddle_b.sety(y2)



#Key-bindings for the above functionality
window.listen()
window._onkeypress(paddle_a_up, 'w')
window._onkeypress(paddle_a_down, 's')

window.listen()
window._onkeypress(paddle_b_up, "Up")
window._onkeypress(paddle_b_down, 'Down')


#Main game loop
while True:
    window.update()
#The ball movements
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)
#borders 
    if ball.ycor() > 260: 
        ball.sety(260)
        ball.dy *= -1
    if ball.xcor() > 350:
        ball.setx(350)
        ball.dx *= -1
    if ball.ycor() < -240: 
            ball.sety(-240)
            ball.dy *= -1
    if ball.xcor() < -350:
            ball.setx(-350)
            ball.dx *= -1
