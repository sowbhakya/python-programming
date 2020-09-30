    a=input("Enter the number")
   
    if(a>0):
        while(a>1):
            a=a*(a-1)
        print"factorial",a
    elif(a==0):
        print "factorial 1"
    else:
        print"Enter positive number only"
