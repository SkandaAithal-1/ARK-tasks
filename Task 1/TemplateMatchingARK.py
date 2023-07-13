import cv2
import numpy as np

template=cv2.imread("templateARK.png",0)
img=cv2.imread("C:\\Users\Skanda\Downloads\collage.png",0)
mat=np.zeros((64,3))
r=0
indList=[0,100,200,300,400,500,600,700]
print(template.shape)
img1=np.zeros((100,100))


for i in indList:
    for j in indList:
        for p in range(100):
            for q in range(100):
                img1[p,q]=(template[p,q]-img[i+p,j+q])**2
        mat[r,0]=i
        mat[r,1]=j
        mat[r,2]=np.sum(img1)
        r+=1
locmin=np.where(mat==min(mat[:,2]))
print(mat[locmin[0],0],mat[locmin[0],1])  #Printing the indices of the topleft corner of the part where template is matched
cv2.imshow("Img", template)
cv2.waitKey(0)
cv2.destroyAllWindows()
