import cv2  
import dlib  
import numpy as np
import sys 
from get_coor import get_coor
def get_dlib_face(img_dlib,landmarks):
    con=[]
    #contours_neck=np.array(landmarks[0])

    contours_neck1=np.array(landmarks[0:17])
    contours_neck2=np.array([[1728,800],[1728,1000],[1728,2592],[600,2592],[100,2592],[0,2592],[0,1000],[0,800]])
    contours_neck = np.row_stack((contours_neck1, contours_neck2))
    contours_leye=np.array(landmarks[36:42])
    contours_reye=np.array(landmarks[42:48])
    contours_leye=np.array(get_coor(contours_leye))
    contours_reye=np.array(get_coor(contours_reye))
    contours_mouth=np.array(landmarks[48:60])

    con.append(contours_neck)
    con.append(contours_leye)
    con.append(contours_reye)
    con.append(contours_mouth)
    cv2.drawContours(img_dlib, con, -1, [0,0,0], -1)

    for i in range(17,21):
        cv2.line(img_dlib,(landmarks[i][0,0],landmarks[i][0,1]-75),(landmarks[i+1][0,0],landmarks[i+1][0,1]-75),[0,0,0],111)#.....................BUG........

    for i in range(22,26):
        cv2.line(img_dlib,(landmarks[i][0,0],landmarks[i][0,1]-75),(landmarks[i+1][0,0],landmarks[i+1][0,1]-75),[0,0,0],111)
    
    return img_dlib