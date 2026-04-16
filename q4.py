import turtle as t

mode = "turtle"

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def add(self,point):
        return Point(self.x+point.x, self.y + point.y)
    def draw(self,mode = "not",surface = None):
        if(mode == pygame):
            pass
        else:
            t.up()
            t.goto(self.x,self.y)
            t.down()
            t.write(str(self))
            t.dot()
if(mode == "pygame"):
    import pygame
    pygame.init()
    
    screen = pygame.display.set_mode((400,400))
    while True:
        for event in pygame.event.get():
            if(event == pygame.QUIT):
                quit()
        screen.fill(255,255,255)
        pygame.draw.circle(screen)
        pygame.display.flip()
else:
    
    newpoint = Point(100,10)
    
    print(newpoint.x)
    pointList = [(0,0),(100,0),(100,100),(0,100)]
    newList = []
    for i in pointList:
        newList.append(Point(i[0],i[1]))
    for j in newList:
        print(j)
        j.draw()
    t.exitonclick()