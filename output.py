def WriteOutput():
    f=open("output.txt","w")
    a = input("Enter contents of the file:")
    f.write(a)
    f.write("\n")
    f.close()
def AddOutput():
    f=open("output.txt","a")
    c='y'
    while c=='y':
        a = input("Enter additional text to append:")
        f.write(a)
        f.write("\n")
        c=input("Want to enter more lines y/n:")
    f.close()
def ReadOutput():
    f=open("output.txt","r")
    print("Final content of the output")
WriteOutput()
AddOutput()
ReadOutput()