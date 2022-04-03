import cv2 as cv


try:
  file = input('Enter a the File path : ')
  scrImage = cv.imread(file)
  gray_image = cv.cvtColor(scrImage, cv.COLOR_BGR2GRAY)
except:
    print(file +' Image not Found !!!')
    import image
    exit()    
try:
    ret , bw = cv.threshold(gray_image,127,255,cv.THRESH_BINARY)
    cv.imwrite('bsImage.jpg',bw)
    print("\nImage converted to binary scale  ٩(•̤̀ᵕ•̤́๑)ᵒᵏOKᵎᵎᵎᵎ")
except:
    print("Error converting to binary Scale (=.=) !!!")    

