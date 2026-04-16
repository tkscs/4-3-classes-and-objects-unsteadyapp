import turtle as t
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def draw(self):
        t.up()
        t.goto(self.x,self.y)
        t.down()
        t.write(str(self))
        t.dot()
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