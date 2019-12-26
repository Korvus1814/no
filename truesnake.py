import cTurtle
import time
import random

# string, tuple of int -> Turtle object
def create_segment(color, position):
    """Creates a turtle object and places it at the given position. The turtle is displayed as a circle with the given color."""
    segment = cTurtle.Turtle()
    segment.speed(0)
    segment.shape("circle")
    segment.color(color)
    segment.penup()
    segment.goto(position)
    return segment

# SnakeGame object, Snake object -> void
def define_keys(game, snake):
    """Binds arrow and return keys to functions."""
    (snake.front).listen()
    (snake.front).onKey(game.play, "Return")
    (snake.front).onKey(snake.go_up, "Up")
    (snake.front).onKey(snake.go_down, "Down")
    (snake.front).onKey(snake.go_right, "Right")
    (snake.front).onKey(snake.go_left, "Left")

# void -> void
def draw_boundary():
    """Draws the boundary for the snake window."""
    boundary = cTurtle.Turtle()
    boundary.speed(0)
    boundary.hideturtle()
    boundary.penup()
    boundary.goto(-300,-250)
    boundary.pendown()
    boundary.goto(300,-250)
    boundary.goto(300,250)
    boundary.goto(-300,250)
    boundary.goto(-300,-250)

class Apple:
    #Apple(turtle)
    def __init__(self):
        """Create the turtle object "apple"."""
        self.apple = cTurtle.Turtle()
        (self.apple).up()
        (self.apple).shape("circle")
        (self.apple).color("red")
        (self.apple).speed(0)
    #void -> int, int
    def get_Position(self):
        """Sets the initial position for the apple at a random position within the boundaries."""
        return (self.apple).pos()
    #void -> void
    def move(self):
        """The apple will move to a new location that is within the bounds, and not
            at the same coordinates as any part of the snake."""
        (self.apple).goto((random.randint(-14,14)*20),(random.randint(-12,12)*20))
            
        
class ScoreBoard:
    #ScoreBoard(void)
    def __init__(self):
        """Creates the turtle object "pen", which will modify the score."""
        self.pen = cTurtle.Turtle()
        (self.pen).penup()
        (self.pen).hideturtle()
        (self.pen).goto(0,260)
        (self.pen).write("Score: 0 High Score: 0", align = "center", font = ("Arial", 14, "normal"))
        self.score = 0
        self.high = 0
    #void -> void
    def display_score(self):
        (self.pen).clear()
        (self.pen).write("Score: "+ str(self.score) + " High Score: " +str(self.high), align = "center", font = ("Arial", 14, "normal"))
    #void -> void
    def add_score(self):
        self.score += 1
        if self.score > self.high:
            self.high = self.score
        self.display_score()
    #void -> void
    def reset_score(self):
        self.score = 0

        

class Snake:
    #Snake(void)
    def __init__(self):
        self.front = create_segment("black", (0,0))
        self.body = []
        self.direction = "right"
    #void -> void
    def go_right(self):
        if self.direction != "left":
            self.direction = "right"
            #self.move()
    #void -> void        
    def go_left(self):
        if self.direction != "right":
            self.direction = "left"
            #self.move()
    #void -> void
    def go_up(self):
        if self.direction != "down":
            self.direction = "up"
            #self.move()
    #void -> void
    def go_down(self):
        if self.direction != "up":
            self.direction = "down"
            #self.move()
    #void -> float, float
    def get_position(self):
        return (self.front).pos()
    #void -> float
    def get_y(self):
        return (self.front).ycor()
    #void -> float
    def get_x(self):
        return (self.front).xcor()
    #void -> void
    def add_segment(self):
        (self.body).append(create_segment("gray", self.get_position()))
    #void -> void                       
    def move(self):                                     
        if len(self.body) > 0:
            length = len(self.body)
            for i in range(length,1,-1):
                ((self.body)[i-1]).goto(((self.body)[i-2]).pos())
            (self.body[0]).goto(self.get_position())  
        if self.direction == "right": 
            (self.front).goto(self.get_x()+20, self.get_y())
        elif self.direction == "left":
            (self.front).goto(self.get_x()-20, self.get_y())
        elif self.direction == "up":
            (self.front).goto(self.get_x(), self.get_y()+20)
        elif self.direction == "down":
            (self.front).goto(self.get_x(), self.get_y()-20)

    def out_of_bounds(self):
        if int(self.get_x()) >= 300 or int(self.get_x()) <= -300 or int(self.get_y()) >= 250 or int(self.get_y()) <= -250:
            return True
        else:
            return False

    def apple_hit(self,apple):
        if (self.front).distance(apple) < 15:
            return True
        else:
            return False

    def body_hit(self):
        for i in self.body:
            if (self.front).distance(i) < 15:
                return True
        return False

    def dedsnek(self):
        for i in self.body:
            i.hideturtle()
        self.body = []
        (self.front).goto(0,0)
        self.direction = "right"
        
class SnakeGame:
    # SnakeGame()
    def __init__(self):
        """Draws the boundary, and initializes the snake, apple, and scoreboard for the game; binds keys"""
        draw_boundary()
        self.snake = Snake()
        self.apple = Apple()
        self.score_board = ScoreBoard()
        define_keys(self, self.snake)
        (self.score_board).display_score()
        (self.apple).move()
        self.again = cTurtle.Turtle()
        (self.again).hideturtle()
        (self.again).up()
        (self.again).goto(0,125)
        
    # void -> void
    def play(self):
        """Runs the snake game"""
        (self.again).clear()
        (self.score_board).reset_score()
        (self.snake).dedsnek()
        (self.apple).move()        
        alive = True
        while alive:
            (self.snake).move()
            if (self.snake).out_of_bounds():
                alive = False
            if (self.snake).body_hit():
                alive = False
            if (self.snake).apple_hit((self.apple).apple):
                (self.snake).add_segment()
                (self.apple).move()
                (self.score_board).add_score()
            time.sleep(.1)
        (self.again).write("Press Return to play again", align = "center", font = ("Arial", 22, "normal"))

                
           
            

                
                
            
