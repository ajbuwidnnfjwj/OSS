# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.
import turtle, random, time
class RunawayGame:
    def __init__(self, canvas, runner, runner2, chaser, catch_radius=40, init_dist=400):
        self.canvas = canvas
        self.runner = runner
        self.runner2 = runner2
        self.chaser = chaser        
        self.catch_radius2 = catch_radius**2

        self.runner.shape('turtle')
        self.runner.color('blue')
        self.runner.penup()
        self.runner.setx(random.randint(-350,350))
        self.runner.sety(random.randint(-350,350))
        self.runner.setheading(random.randint(0,360))
        
        self.runner2.shape('turtle')
        self.runner2.color('green')
        self.runner2.penup()
        self.runner2.setx(random.randint(-350,350))
        self.runner2.sety(random.randint(-350,350))
        self.runner2.setheading(random.randint(0,360))
        
        self.chaser.shape('turtle')
        self.chaser.color('red')
        self.chaser.penup()
        self.chaser.setx(random.randint(-350,350))
        self.chaser.sety(random.randint(-350,350))
        self.chaser.setheading(random.randint(0,360))        

        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.hideturtle()
        self.drawer.penup() 

    def is_catch(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2
    
    def is_catch2(self):
        p = self.runner2.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def start(self, ai_timer_msec=100, total_score=0, blue_num=0, green_num=0):
        self.ai_timer_msec = ai_timer_msec
        self.total_score = total_score
        self.canvas.ontimer(self.step, self.ai_timer_msec)
        self.start_time = time.time()
        self.blue_num = blue_num
        self.green_num = green_num

    def step(self):
        self.runner.run_ai(self.chaser)
        self.runner2.run_ai(self.runner)
        self.chaser.run_ai(self.runner)      
          
        if(abs(self.runner.xcor()) > 400 or abs(self.runner.ycor()) > 400):
            self.runner.setheading(self.runner.heading() + 180)
            self.runner.forward(100)
            
        if(abs(self.runner2.xcor()) > 400 or abs(self.runner2.ycor()) > 400):
            self.runner2.setheading(self.runner2.heading() + 180)
            self.runner2.forward(150)
            
        if(abs(self.chaser.xcor()) > 410 or abs(self.chaser.ycor()) > 410):
             self.chaser.setheading(self.chaser.heading() + 180)
             self.chaser.forward(100)
            
        if(abs(self.runner.heading()-self.chaser.heading()) == 180):
            self.runner.setheading(self.runner.heading() + 90)
            
        if(abs(self.runner2.heading()-self.chaser.heading()) == 180):
            self.runner2.setheading(self.runner2.heading() + 90)
            
        is_catched = self.is_catch()
        is_catched2 = self.is_catch2()
        
        if(is_catched == True):
            self.total_score += 10
            self.blue_num += 1
            self.runner.forward(50)
        
        if(is_catched2 == True):
            self.total_score += 20
            self.green_num += 1
            self.runner2.forward(100)
            

        self.drawer.undo()
        self.drawer.penup()
        elapse = time.time() - self.start_time
        score = self.total_score
        blue_num = self.blue_num
        green_num = self.green_num
        self.drawer.setpos(-380, 380)
        self.drawer.write(f'Is runner catched? {is_catched or is_catched2} / Time: {elapse:.0f} / Score: {score:.0f} / number of catches blue : {blue_num:.0f}, green : {green_num:.0f} ')

        self.canvas.ontimer(self.step, self.ai_timer_msec)

class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opponent):
        pass

class RandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, oppoenent):
        mode = random.randint(0, 2)
        if mode == 0:
            self.forward(self.step_move)
        elif mode == 1:
            self.left(self.step_turn)
        elif mode == 2:
            self.right(self.step_turn)

class LessRandomMover(turtle.RawTurtle): 
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, oppoenent):
        mode = random.random()
        if mode < 0.6:
            self.forward(self.step_move)
        elif mode < 0.9:
            self.left(self.step_turn)
        else:
            self.right(self.step_turn)

if __name__ == '__main__':
    canvas = turtle.Screen()
    runner = RandomMover(canvas)
    runner2 = LessRandomMover(canvas)
    chaser = ManualMover(canvas)

    game = RunawayGame(canvas, runner, runner2, chaser)
    game.start()
    canvas.mainloop()