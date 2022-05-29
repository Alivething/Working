from time import sleep
import cv2
import mss
import numpy as np
from pynput.mouse import Button, Controller

mouse = Controller()

monitor = {"top": 900, "left": 1570, "width": 150, "height": 50}
while(1):

    with mss.mss() as sct:

        img = np.array(sct.grab(monitor))

        img = cv2.resize(img, (90, 30))
        WHITE_MIN = np.array([0,0,100],np.uint8)
        WHITE_MAX = np.array([255,30,180],np.uint8)

        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        frame_threshed = cv2.inRange(hsv_img, WHITE_MIN, WHITE_MAX)

        pix = 0
        for i in range(0,30,3):
            for j in range(0,90,3):
                if(np.any(frame_threshed[i][j] == [255,255,255])):
                    pix+=1
                if(pix>40):break

        if(pix>40):
            mouse.press(Button.right)
            mouse.release(Button.right)
            sleep(3)
            mouse.press(Button.right)
            mouse.release(Button.right)
            sleep(7)

        cv2.imshow('output', frame_threshed)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        cv2.destroyAllWindows()
        break