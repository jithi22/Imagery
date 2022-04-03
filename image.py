import cv2 as cv

file = input('Enter a the File path : ')

img = cv.imread(file)



gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)



try:
    cv.imwrite('gray_goku.jpg',gray_image)
    print("\nWrite Success !!")
except:
    print("Write failed...!")    

cv.waitKey(0)