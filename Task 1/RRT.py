import cv2
import random
import math

class Maze:
    def __init__(self):
        self.maze=cv2.imread("maze.png")
        self.startEasy=(160,25)  #(40,320)
        self.endEasy=(440,305)  #(100,320)

class RRT:
    def __init__(self, maze, start, end):
        self.start=start
        self.maze=maze
        self.end=end
        self.ext=100
        self.points=[[self.start, None]]
        self.x=None
        self.y=None
        cv2.circle(maze,start,4,(255,0,0),-1)
        cv2.circle(maze,end,4,(255,0,0),-1)
        super().__init__()

    def sample(self):
        self.x=random.randint(self.start[0],self.end[0])
        self.y=random.randint(1,self.end[1])
    
    def inObstacle(self, ind)->bool:
        self.uX=(self.x-self.points[i][0][0])/self.ext
        self.uY=(self.y-self.points[i][0][1])/self.ext
        for j in range(self.ext+1):
            if (self.maze[int(self.points[i][0][1]+(j*self.uY)),int(self.points[i][0][0]+(j*self.uX))]==(0,0,0)).all():
                return True
        return False

    def dist(self, ind)->float:
        return math.sqrt((self.x-self.points[ind][0][0])**2+(self.y-self.points[ind][0][1])**2)

    def inRange(self)->bool:
        if (math.sqrt((self.x-self.end[0])**2+(self.y-self.end[1])**2)<30):
            return True
    
def findParent(coord):
    for i in Algo.points:
        if i[0]==coord :
            return i[1]
    
Map=Maze()
Algo=RRT(Map.maze, Map.startEasy, Map.endEasy)

while True:
    flag=0
    Algo.sample()
    print(len(Algo.points))
    for i in range(len(Algo.points)):
        if Algo.inObstacle(i):
            pass
        else:
            if (flag==0):
                flag=1
                cv2.circle(Algo.maze,(Algo.x,Algo.y),2,(0,255,0),-1)
                Algo.points.append([(Algo.x,Algo.y),None])
                minDist=Algo.dist(i)
                minInd=i
            elif (Algo.dist(i)<minDist):
                minDist=Algo.dist(i)
                minInd=i
    if (flag==0):
        continue
    Algo.points[-1][1]=Algo.points[minInd][0]
    cv2.line(Algo.maze,Algo.points[minInd][0],(Algo.x,Algo.y),(0,255,0),1)
    if (Algo.inRange()):
        cv2.circle(Algo.maze, Algo.end, 2, (0,255,0), -1)
        cv2.line(Algo.maze, Algo.end, Algo.points[-1][0], (0,255,0), 1)
        Algo.points.append([Algo.end, Algo.points[-1][0]])
        cv2.imshow("Maze", Algo.maze)
        cv2.waitKey(1)
        break
    cv2.imshow("Maze", Algo.maze)
    k=cv2.waitKey(1)
    if (k==ord("q")):
        break

prev=None
backStart=Algo.end
while (backStart!= None):
    cv2.circle(Algo.maze, backStart, 2, (0,0,255), -1)
    cv2.imshow("Backtracking", Algo.maze)
    cv2.waitKey(1)
    prev=backStart
    backStart=findParent(backStart)
    if (backStart!=None):
        cv2.line(Algo.maze, prev, backStart, (0,0,255), 1)
    cv2.imshow("Backtracking", Algo.maze)
    cv2.waitKey(1000)
cv2.imshow("Final", Algo.maze)
cv2.waitKey(0)

cv2.destroyAllWindows()
