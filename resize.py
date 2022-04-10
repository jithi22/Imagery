from PIL import Image

fhandle = open(r'./config/Qconf.txt')
file = fhandle.read()
fhandle.close()

#quality = input('Enter the Quality of the image to dispaly \n1)Extreme\n2)High\n3)Medium(default)\n choice : ')

def base(basewidth):  
 img = Image.open('bsImage.jpg')
 wpercent = (basewidth / float(img.size[0]))
 hsize = int((float(img.size[1]) * float(wpercent)))
 img = img.resize((basewidth, hsize), Image.ANTIALIAS)
 img.save('resized_image.jpg')

#def lossLess():
 #img = Image.open('bsImage.jpg')
 #img.save('resized_image.jpg')

if file == '1':
  basewidth = 270
  base(basewidth)
elif file == '2' :
  basewidth = 200
  base(basewidth)
else:
  basewidth = 70
  base(basewidth)
  
