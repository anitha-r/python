#!/usr/bin/env python
# coding: utf-8

# In[1]:
##Compilation of face recognition code in Python found online.
##I didnt have to install VS 2015 just yet.
##Updated conda and Installed dlib and face_recognition packages before running this code.

# import libraries
import cv2
import face_recognition


cap = cv2.VideoCapture(0)

face_locations=[]

while(True):
    ret, frame = cap.read()
    
    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces in the current frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    
     # Display the results
    for top, right, bottom, left in face_locations:
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (255, 255, 255), 2)
        
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
cap.release()
cv2.destroyAllWindows()


# In[ ]:




