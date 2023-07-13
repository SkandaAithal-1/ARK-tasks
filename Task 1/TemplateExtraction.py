import cv2
import numpy as np
    

img=cv2.imread("C:\\Users\Skanda\Downloads\pi_image.png",0)
pic=cv2.imread("artwork_picasso.png",0)
pic1=cv2.imread("C:\\Users\Skanda\Downloads\collage.png",0)
cv2.imshow("Img1",img)
print(img)
cv2.waitKey(0)
kernel=[[282,251],[94,0]]  # The kernel formed by the missing digits transformed according to instructions.
test=[[2,1],[2,2]] # The combination of operations that I found satisfactory
img1=np.zeros((100,100))
print(pic.shape)


for i in range(50):
    for j in range(50):
        if (img[i,j]==255) :
            img[7,48]=0
            print((i*50)+j)
'''for test[0][0] in range(3):
    for test[0][1] in range(3):
        for test[1][0] in range(3):
            for test[1][1] in range(3):

If the below code is put inside the above for loop, all the combinations of the three operations would be performed.
'''
for i in range(99):
    for j in range(99):
        if (i%2==0 and j%2==0):
            for k in range(2):
                for l in range(2):
                    if (test[k][l]==0):
                        img1[i+k,j+l]=(kernel[k][l]&pic[i+k,j+l])
                    elif (test[k][l]==1):
                        img1[i+k,j+l]=(kernel[k][l]|pic[i+k,j+l])
                    elif (test[k][l]==2):
                        img1[i+k,j+l]=(kernel[k][l]^pic[i+k,j+l])

cv2.imwrite("TemplateARK.png",img1)
img1/=255
cv2.imshow("Img", img1)

print(test)
cv2.waitKey(0)
cv2.destroyAllWindows()


