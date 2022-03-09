import cv2
import numpy as np

img = cv2.imread("pics/path.png")

#Converting to hsv for preprocessing
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
edges = cv2.Canny(img,50,150,apertureSize = 3)

#Restricting view to Region Of Interest
height = np.size(hsv,0)
width = np.size(hsv,1)
hsv = hsv[(int)(5*height/14):height, 0:width]

#Finding Min and Max HSV
h=[]
s=[]
v=[]

for i in hsv:
    for j in i:
        h.append(j[0])
        s.append(j[1])
        v.append(j[2])

hmin = min(h)
smin = min(s)
vmin = min(v)
hmax = max(h)
smax = max(s)
vmax = max(v)

rangeMin = np.array([hmin, smin, vmin])
rangemax = np.array([hmax, smax, vmax])

#Masking image
mask = cv2.inRange(hsv, rangeMin*1.1, rangemax/1.1)

#Average of pixels in the area
leftTop = 0
rightTop = 0
for i in range(50):
    for j in range(50):
        leftTop += mask[i][j]
for i in range(50):
    for j in range(50):
        rightTop += mask[i][639-j]

rightTop = rightTop/2500
leftTop = leftTop/2500
print(leftTop)
print(rightTop)

#Determining direction
if(rightTop>120):
    if(leftTop>120):
        print("Stright")
    else:
        print("Right")
else:
    if(leftTop>120):
        print("Left")
    else:
        print("Straight")

#Displaying images
cv2.imshow('img', img)
cv2.imshow('gray', hsv)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()








# img = cv2.GaussianBlur(image,(11,11),0)
# cv2.imshow("image", image)
# leftTop = image[0][0]
# rightTop = image[312][639]
# # print(rightTop)
# result = image.copy()
# edges = cv2.Canny(image, 50, 150)
# # cv2.imshow("edges",edges)
# lines = cv2.HoughLinesP(edges,1,np.pi/180,40,minLineLength=30,maxLineGap=30)
# for x1,y1,x2,y2 in lines[0]:
#     cv2.line(result,(x1,y1),(x2,y2),(255,0,0),1)

# cv2.imshow("res",result)
# minLineLength = 1000
# maxLineGap = 10
# lines = cv2.HoughLinesP(edges,50,np.pi/180,100,minLineLength,maxLineGap)
# i=0
# for x1,y1,x2,y2 in lines[i]:
#     i+=1
#     cv2.line(img,(x1,y1),(x2,y2),(255,0,0),9)