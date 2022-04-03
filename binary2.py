

fhandle = open(r"binarized.txt")
fhandle2 = open('store.txt','a')
for line in  fhandle:
    fhandle2.write('\n')
    for ch in line:
     if ch == ' ' or ch == '\n':continue   
     if int(ch) == 1:
        fhandle2.write('*')
     else:
         fhandle2.write('.')   
fhandle2.close()        
    
    