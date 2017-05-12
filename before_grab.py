# -*- coding: utf-8 -*-
import cv2  
import dlib  
import numpy as np
import sys  
from get_coor import get_coor
from rgbdetect import rgb_skin
from get_dlib import get_dlib_face
from slic_ import slic_output
def pre_grab(im):
    predictor_path = "./shape_predictor_68_face_landmarks.dat"  

    #1.使用dlib自带的frontal_face_detector作为我们的人脸提取器  
    detector = dlib.get_frontal_face_detector()

    #2.使用官方提供的模型构建特征提取器  
    predictor = dlib.shape_predictor(predictor_path)

    class NoFaces(Exception):
        pass  
    
    #im = cv2.imread("./test1.jpg")  

    #3.使用detector进行人脸检测 rects为返回的结果  
    rects = detector(im,1)
    '''#多个脸的时候
    #4.输出人脸数，dets的元素个数即为脸的个数  
    if len(rects) >= 1:  
        print("{} faces detected".format(len(rects)))  

    if len(rects) == 0:  
        raise NoFaces  

    for i in range(len(rects)):  

        #5.使用predictor进行人脸关键点识别
        landmarks = np.matrix([[p.x,p.y] for p in predictor(im,rects[i]).parts()])

        im = im.copy()  
        #使用enumerate 函数遍历序列中的元素以及它们的下标
        #landmarks是68个点的坐标
        for idx,point in enumerate(landmarks):  
            pos = (point[0,0],point[0,1])  
            cv2.circle(im,pos,3,color=(0,255,0))  

    cv2.namedWindow("im",2)
    cv2.imshow("im",im)  
    cv2.waitKey(0)  
    '''
    #landmarks是进过检测的68个点
    for i in range(len(rects)):  
        landmarks = np.matrix([[p.x,p.y] for p in predictor(im,rects[i]).parts()])
    #get_dlib_face函数是指提取五官
    im_dlib = im.copy()
    im_dlib=get_dlib_face(im_dlib,landmarks)
    #rgb_skin函数是指肤色辅助检测
    img_skin=rgb_skin(im_dlib)
    #
    slic_means=slic_output(img_skin)

    return slic_means

'''
cv2.namedWindow("im",2)
cv2.imshow("im",slic_means)  
cv2.waitKey(0)
'''
