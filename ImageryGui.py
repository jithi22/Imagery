from tkinter import *
from tkinter.filedialog import askopenfilename

root = Tk()
root.geometry('800x500')
store =''

def findfile():
 filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
 Label(root,text=filename).grid()
 sep = filename.split('.')
 length = len(sep)
 extenstion = sep[length-1]
 lbl = Label(root,text=extenstion+' is not a image file')
 if not(extenstion == 'jpg' or extenstion == 'png')  :
   lbl.grid()
 else:
     Label(root,text='image Selected').grid()
     fhandle = open('./config/Iconf.txt','w')
     fhandle.write(filename)
     fhandle.close()
 
def runner():
    import run
def cleaner():
    import clean    
    
projectLabel = Label(root,text='IMAGERY v1.3.0')
projectLabel.grid(row=0,column=0)
projectLabel.configure(font=("Times New Roman", 30, "italic"))

selectButton1 = Button(root,text='SELECT   IMAGE ' ,padx=37,pady=40,fg='green', command=findfile)
selectButton2 = Button(root,text='CLEAN ' ,padx=60,pady=40,fg='green',command=cleaner)
selectButton3 = Button(root,text='[[[ RUN  ]]] ' ,padx=60,pady=40,fg='green',command=runner)
selectButton1.grid(row=5,column=0)
selectButton2.grid(row=7,column=0)
selectButton3.grid(row=7,column=3)

labelS = Label(root, text=' OPTIONS')
labelS.grid(row=4,column=4)
labelS.configure(font=("Times NEW Roman",20))

def Quality(data):
    fhandle2 = open('./config/Qconf.txt','w')
    fhandle2.write(data)
    fhandle2.close()

def clearC():
    c1.deselect()
    c2.deselect()
    Quality('1')
def clearC1():
    c.deselect()
    c2.deselect()
    Quality('2')
def clearC2():
    c.deselect()
    c1.deselect()
    Quality('3')
    
c = Checkbutton(root, text = "Extreme", command=clearC)
c1 = Checkbutton(root, text = "High", command=clearC1)
c2 = Checkbutton(root, text = "Medium" ,command=clearC2)

c.grid(row=5,column=4)
c1.grid(row=5,column=5)
c2.grid(row=5,column=6)


root.mainloop()
