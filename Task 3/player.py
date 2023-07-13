from utils import Player,WINDOW_WIDTH
import cv2
import numpy as np


player = Player()
    #Initializing a Player object with a random start position on a randomly generated Maze

def strategy():
    Map=player.getMap()
    step=20
    place1=[]
    place2=[]
    place3=[]
    #print(Map.shape)
    area=player.getSnapShot()
    cv2.imshow("MapSnap", area)
    print(player.getSnapShot().shape)
    res=cv2.matchTemplate(Map,area,cv2.TM_CCOEFF_NORMED)
    loc=np.where(res==1.0)
    print(loc)
    hor=player.move_horizontal(step)
    area1=player.getSnapShot()
    res1=cv2.matchTemplate(Map,area1,cv2.TM_CCOEFF_NORMED)
    loc1=np.where(res1==1.0)
    ver=player.move_vertical(step)
    area2=player.getSnapShot()
    res2=cv2.matchTemplate(Map, area2, cv2.TM_CCOEFF_NORMED)
    loc2=np.where(res2==1.0)
    for i in zip(*loc[::-1]):
        h,w=area.shape
        cv2.rectangle(Map,i,(i[0]+w,i[1]+h),0.5,2)
        place1.append((i[0]+25,i[1]+25))
    for i in zip(*loc1[::-1]):
        h,w=area1.shape
        cv2.rectangle(Map,i,(i[0]+w,i[1]+h),0.5,2)
        place2.append((i[0]+25,i[1]+25))
    for i in zip(*loc2[::-1]):
        h,w=area2.shape
        cv2.rectangle(Map,i,(i[0]+w,i[1]+h),0.5,2)
        place3.append((i[0]+25,i[1]+25))
    #print(place1, place2, place3)
    print(hor, ver)
    for i in place1:
        if ((i[0]+hor,i[1]) in place2) and ((i[0]+hor,i[1]+ver) in place3):
            print(i, "is the location")
    cv2.imshow("Map1", Map)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    strategy()
    

























