import cv2
import mss
import numpy as np


monitor = {"top": 400, "left": 100, "width": 900, "height": 400}
while(1):

    with mss.mss() as sct:

        img = np.array(sct.grab(monitor))

        img = cv2.resize(img, (800, 400))
        BLUE_MIN = np.array([85, 50, 70],np.uint8)
        BLUE_MAX = np.array([90, 255, 255],np.uint8)

        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        frame_threshed = cv2.inRange(hsv_img, BLUE_MIN, BLUE_MAX)

        # Finding center
        avgx, avgy, pix = 0, 0, 0
        for i in range(0,400,3):
            for j in range(0,800,3):
                if(np.any(frame_threshed[i][j] == [255,255,255])):
                    avgx+=i
                    avgy+=j
                    pix+=1

        # Adding a red dot
        if(pix!=0):
            avgx = round(avgx/pix)
            avgy = round(avgy/pix)
            print(avgx, avgy)
            for i in range(-2,2):
                for j in range(-2, 2):
                    img[i+avgx][j+avgy] = [0, 0, 255, 255]


        # Printing img
        cv2.imshow('output', img)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        break


