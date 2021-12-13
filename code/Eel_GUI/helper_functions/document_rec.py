# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 01:07:26 2021

@author: Pranav
"""

import numpy as np
import cv2
#import time

cap=cv2.VideoCapture(0)

while True:
    ret, frame= cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    
    
    #corners
    w=105
    h=149
    scale=1.25
    l=int((width/2) - w*scale)
    r=int((width/2) + w*scale)
    u=int((height/2) - h*scale)
    d=int((height/2) + h*scale)
    
    #lines
    length=20
    thickness=2
    colour=(255,0,0)
    
    img=frame
    
    img=cv2.line(img,(l,u),(l,u+length),colour,thickness)
    img=cv2.line(img,(l,u),(l+length,u),colour,thickness)
    
    img=cv2.line(img,(r,u),(r-length,u),colour,thickness)
    img=cv2.line(img,(r,u),(r,u+length),colour,thickness)
    
    img=cv2.line(img,(r,d),(r,d-length),colour,thickness)
    img=cv2.line(img,(r,d),(r-length,d),colour,thickness)
    
    img=cv2.line(img,(l,d),(l+length,d),colour,thickness)
    img=cv2.line(img,(l,d),(l,d-length),colour,thickness)
    
    #text
    text="please place document here"
    font=cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.putText(img,text,(l-80,u-20),font,1,colour,1,cv2.LINE_AA)
    
    
    cv2.imshow('document',img) 
    
    
    action=cv2.waitKey(1)
    if action == ord(' '):
        doc=np.zeros((d-u,r-l),np.uint8)
        doc=frame[u:d,l:r]
        cv2.imwrite("captured_doc.jpg",doc)
        break
    
    elif action == ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows()