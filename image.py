import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from outcome import capture

img = cv.imread('goku.jpg')

#cv.imshow('goku in color ',img)

gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#cv.imshow('gray',gray_image)

try:
    cv.imwrite('gray_goku.jpg',gray_image)
    print("\nWrite Success !!")
except:
    print("Write failed...!")    

cv.waitKey(0)