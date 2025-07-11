def WriteSample():
    f=open("Sample.txt","w")
    ch='y'
    while ch=='y':
        a=input("Enter a line:")
        f.write(a)
        f.write("\n")
        ch=input("Want to enter more lines y/n:")
    f.close()
def ReadSample():
    f=open("Sample.txt","r")
    print("Reading file content")
    c=1
    lines = f.readlines()
    for i in lines:
        try:

            print("Line",c,":",i)
            c+=1
        except FileNotFoundError:
            print("Error: File Sample.txt not found")
    f.close()
WriteSample()
ReadSample()
