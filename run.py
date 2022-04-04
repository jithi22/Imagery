import os
def clean():
    os.remove('bsImage.jpg')
    os.remove('resized_image.jpg')
    os.remove('binarized.txt')
    

try:
    clean()
    print("\n< Old Files Removed...!! >\nStarting..Script")

except:
    print("No files found to remove..Starting..Script")

import image
import resize
import binary

#import printer


