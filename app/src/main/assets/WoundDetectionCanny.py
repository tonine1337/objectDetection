###Import required packages

import cv2
import numpy as np
import os
print("All Imports Done!!")

#== Set Canny Threshold Parameters =======================================================================
CANNY_THRESH_1 = 50
CANNY_THRESH_2 = 100


##Save the names of all JPG files from the folder into 'file_names'

relevant_path = "./"
included_extensions = ['jpg','JPG']
file_names = [fn for fn in os.listdir(relevant_path)
              if any(fn.endswith(ext) for ext in included_extensions)]
print(file_names)


def detect_wound(imagename):
    img = cv2.imread("./"+imagename)

    ##Canny Edge Detection
    edges = cv2.Canny(img, CANNY_THRESH_1, CANNY_THRESH_2)
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)
    
    #-- Find contours in edges, sort by area ---------------------------------------------
    contour_info = []
    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for c in contours:
        contour_info.append((
            c,
            cv2.isContourConvex(c),
            cv2.contourArea(c),
        ))
    contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
    max_contour = contour_info[0]
    
    #Draw Contour on the Image
    
    shape = img.copy() 
    cv2.drawContours(shape, max_contour[0], -1, (0, 255, 0), 2)
    
    #Write the Output
    outputname="Wound_"+imagename
    cv2.imwrite(outputname,shape)
	
	
for imagename in file_names:
    detect_wound(imagename)