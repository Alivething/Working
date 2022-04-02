import cv2
from cv2 import GaussianBlur
from cv2 import dilate
from cv2 import erode
from matplotlib import pyplot as plt
import numpy as np

#Video capture
cap = cv2.VideoCapture('winterschoolCV\default.mp4')

#Extracting frames
while(cap.isOpened()):
    ret, ogframe = cap.read()

    #Converting to greyscale
    frame = cv2.cvtColor(ogframe, cv2.COLOR_BGR2HSV)
    lower_bound_yellow = np.array([10, 120, 150])
    upper_bound_yellow = np.array([15, 190, 180])
    lower_bound_white = np.array([0, 10, 90])
    upper_bound_white = np.array([20, 15, 200])
    frame_yellow = cv2.inRange(frame, lower_bound_yellow, upper_bound_yellow)
    frame_white = cv2.inRange(frame, lower_bound_white, upper_bound_white)

    frame = cv2.bitwise_xor(frame_yellow, frame_white)

    #Applying filters
    frame = GaussianBlur(frame, (5,5), 0)
    
    #Edge detection
    edges = cv2.Canny(frame,50,100)

    kerneld = np.ones((7,7), np.uint8)
    edges = dilate(edges, kerneld, 0, iterations=1)
    kernele = np.ones((5,5), np.uint8)
    edges = erode(edges, kernele, 0, iterations=2)
    kerneld = np.ones((3,3), np.uint8)
    edges = dilate(edges, kerneld, 0, iterations=3)

    #ROI extraction 
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(edges, contours, -1, (0, 255, 0), 3)
    
    
    #Hough Lines Transform
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, np.array([]), minLineLength=10, maxLineGap=1000) 
    for line in lines: 
        x1,y1,x2,y2 = line[0]
        if(abs(y1-y2)>200):
            cv2.line(ogframe, (x1,y1), (x2,y2), (255, 0, 127), 3)

    # cv2.imshow('Frame', frame_yellow)
    cv2.imshow('Edges', edges)
    cv2.imshow('Frames', ogframe)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()