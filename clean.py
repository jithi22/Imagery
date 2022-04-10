import os
def clean():
    os.remove('bsImage.jpg')
    os.remove('resized_image.jpg')
    os.remove('binarized.txt')
    

try:
    clean()
    print("\n< Old Files Removed...!! >")

except:
    print("No files found to remove..Starting..Script")

