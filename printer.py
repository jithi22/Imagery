dark ='*'
light ='.'

choice = input("Do you Want custom Symbol (press 1)\n Default Symbols * & . in Use (press any key): ")
if choice == 1:
 dark =  input('Enter the symbol to use for dark color :')
 light =input('Enter the symbol yo use for light color :')
fhandle = open(r"binarized.txt")

for line in  fhandle:
    print('\n')
    for ch in line:
     if ch == ' ' or ch == '\n':continue   
     if int(ch) == 1:
        print(dark,end="")
     else:
        print(light,end="") 
fhandle.close()
    
    