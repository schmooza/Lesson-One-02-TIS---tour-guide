import turtle
# def is like a musitician it plays just one instrument. 

def turtleSetUp():

	
	screen = turtle.Screen()

	#screen size
	screen.setup(400, 400)

	# TIS image must be a gif
	screen.bgpic("images/school.gif")
	
	# your character
	you = turtle.Turtle()
	image = "images/blip.gif"

	
	screen.addshape(image)
	you.shape(image)
	
	
	you.speed(1)
	you.color("red")
	you.pensize(4)
	you.penup()

	# start postion
	you.goto(-90, 50)
	you.pendown()
	return you


	

# add code here to move the turtle
def moveTurtle(you):
	you.forward(10)
	you.left(90)
	you.forward(10)
	you.right(90)
	you.forward(10)
	you.left(90)
	you.forward(10)


