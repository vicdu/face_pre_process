import cv2  
import dlib  
import numpy as np
import sys  
def get_coor(contours_eye):
    x=0
    y=0
    contours_eye_list=[]
    for i in range(6):
        x=x+contours_eye[i][0]
        y=y+contours_eye[i][1]
    x=x/6
    y=y/6
    for i in range(6):
        slope=(y-contours_eye[i][1])/(x-contours_eye[i][0])
        while slope==0:
            slope=(y-contours_eye[i][1]-6)/(x-contours_eye[i][0]+6)+0.2#..............................BUG.............................................
        deltx=x-contours_eye[i][0]
        delty=y-contours_eye[i][1]
        newx=contours_eye[i][0]+52
        newy=contours_eye[i][1]+slope*52
        isx=-deltx
        isy=-slope*delty
        if isx<0 or isy<0:
            newx=contours_eye[i][0]-52
            newy=contours_eye[i][1]-slope*52
        contours_eye_list.append([(int)(newx),(int)(newy)])

    return contours_eye_list