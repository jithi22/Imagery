from scipy.ndimage import zoom
from PIL import Image
import numpy as np
srcImage = Image.open("resized_image.jpg")
grayImage = srcImage.convert('L')
array = np.array(grayImage)
array = zoom(array, 310/174)
np.savetxt("binarized.txt", array<128, fmt="%d")
print("\n\n Output Stored to binarized.txt.......#")