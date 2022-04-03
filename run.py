import os
def clean():
    os.remove('bsImage.jpg')
    os.remove('resized_image.jpg')
    os.remove('binarized.txt')
    

try:
    clean()
    print("Starting Printer\n\n")

except:
    print("Starting Printer\n\n")

import image
import resize
import binary
import printer
clean()

