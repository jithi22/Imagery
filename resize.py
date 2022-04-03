from PIL import Image

quality = input('Enter the Quality of the image to dispaly \n1)Extreme\n2)High\n3)Medium(default)\n choice : ')

if quality == '1':
  basewidth = 200
elif quality == '2':
  basewidth = 70
else:
  basewidth = 50
  
img = Image.open('bsImage.jpg')
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save('resized_image.jpg')