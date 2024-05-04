import turtle
import time
import random
WIDTH, HEIGHT = 600,600
COLORS = ['red','green','blue','orange','yellow','black','purple','pink','brown','cyan']

def get_number_of_races():
    racers =0
    while True:
        racers = input('Enter the number of racers(2-10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Inavlid, Try again!!!")
            continue


        if 2<=racers<=10:
            return racers
        else:
            print("Not a number in range 2 to 10")

def create_turtles(colors):
    turtles = []
    spacingX = WIDTH//(len(colors)+1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        #set pos
        racer.setpos(-WIDTH//2+(i+1)* spacingX,-HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y >=HEIGHT//2-10:
                return colors[turtles.index(racer)]
    


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Race")
    
racers = get_number_of_races()
init_turtle()

random.shuffle(COLORS)
colours = COLORS[:racers]
winner = race(colours)
print(winner)
time.sleep(5)



# r acer  = turtle.Turtle() 
# racer.speed(1)
# racer.penup()
# racer.shape('turtle') 
# racer.color('cyan')
# racer.forward(100)
# racer.left(90)
# racer.pendown()
# racer.forward(100)
# racer.right(90)
# racer.backward(100)
# time.sleep(5)
