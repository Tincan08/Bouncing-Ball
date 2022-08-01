import random

class Ball:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts =[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x= starts[0]
        self.y= -3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x= 3
        if pos[1] <=0:
            self.y = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        if pos[3] >= self.canvas_height:
            self.y = -3
