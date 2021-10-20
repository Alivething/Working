import cv2
import numpy as np

img = cv2.imread("path.png")
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
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img,50,150,apertureSize = 3)
minLineLength = 1000
maxLineGap = 10
lines = cv2.HoughLinesP(edges,50,np.pi/180,100,minLineLength,maxLineGap)
i=0
for x1,y1,x2,y2 in lines[i]:
    i+=1
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),9)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()