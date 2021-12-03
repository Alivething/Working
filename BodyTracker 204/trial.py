import mediapipe as mp
import cv2 

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)

# frame = cv2.imread("BodyTracker 204\WIN_20211201_17_19_23_Pro.jpg")

# Initiate pose model
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor Feed
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Make Detections
        results = pose.process(image)
        
        # Recolor image back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Pose Detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        #Extracting wrist coordinates
        # lhand = results.pose_landmarks.landmark[16]

        # rhand = results.pose_landmarks.landmark[15]
        # print(lhand, rhand)

        # #Checking if left or right
        # if(lhand.x> rhand.x):
        #     print("Left higher")
        # else: print("No")
        # # Draw connections
        cv2.imshow('Raw Webcam Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()