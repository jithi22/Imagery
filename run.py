import os
def clean():
    os.remove('bsImage.jpg')
    os.remove('resized_image.jpg')
    os.remove('binarized.txt')
    os.remove('store.txt')
    print("Starting Printer ..\n\n")

try:
    clean()
except:
    print("Starting Printer\n\n")
import image
import resize
import binary
import binary2
import printer
clean()

