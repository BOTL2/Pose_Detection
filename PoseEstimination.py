import time

import cv2
import mediapipe as mp
import datetime

desired_width = 640
desired_height = 480

cap=cv2.VideoCapture("Resources/1.mp4")
pTime=0
motion_pose=mp.solutions.pose
pose=motion_pose.Pose()
mpDraw=mp.solutions.drawing_utils





while True:
    success,image=cap.read()
    imgRgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    result=pose.process(imgRgb)
    print(result.pose_landmarks)

    if result.pose_landmarks:
        mpDraw.draw_landmarks(image,result.pose_landmarks,motion_pose.POSE_CONNECTIONS)

        for id,lm in enumerate(result.pose_landmarks.landmark):
            x,y,z=image.shape
            print(id,lm)

            height=int(lm.x*y)
            weight=int(lm.y*x)
            cv2.circle(image,(height,weight),2,(255,0,0),cv2.FILLED)

    #FPS
    cTime=time.time()
    FPS=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(image, f"FPS: {int(FPS)}", (34,40), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 2)
    #img_resize=cv2.resize(image,(desired_width,desired_height))

    cv2.imshow("Image",image)
    cv2.waitKey(1)

def main():
    pass










if __main__=="__name__":
    main()






