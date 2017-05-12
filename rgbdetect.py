import cv2  
import numpy as np  
from matplotlib import pyplot as plt 

def rgb_skin(img): 
    rows,cols,channels = img.shape  
    
    # prepare an empty image space  
    imgSkin = np.zeros(img.shape, np.uint8)  
    # copy original image  
    imgSkin = img.copy()  
    
    for r in range(rows):  
        for c in range(cols):  
    
            # get pixel value         
            B = img.item(r,c,0)  
            G = img.item(r,c,1)  
            R = img.item(r,c,2)  
            
            # non-skin area if skin equals 0, skin area otherwise          
            skin = 0  
                    
        #  if (abs(R - G) > 15) and (R > G) and (R > B):  
            if (R > 150) and (G > 100) and (B > 100) and (R - B > 15):                 
                skin = 1      
                # print 'Condition 1 satisfied!'  
            elif (R > 200) and (G > 210) and (B > 170) and abs(R-B)<15 and R>B and G>B:  
                skin = 1  
            elif (R > 75) and (G > 40) and (B > 20):  
                skin = 1
                # print 'Condition 2 satisfied!'  
            
            if 0 == skin:  
                imgSkin.itemset((r,c,0),0)  
                imgSkin.itemset((r,c,1),0)                  
                imgSkin.itemset((r,c,2),0)  
                           

    return imgSkin

