num1 = int(input("Enter the Value of N1 :"))
num2 = int(input("Enter the Value of N2 :"))
num3 = int(input("Enter the Value of N3 :"))

if(num1 > num2):
    #num1
    if(num1 > num3):
        print("Number 1 is Greater")
    elif(num3 > num1):
        print("Number 3 is Greater")
    else:
        #num1=num3
        print("Number 1 and Number 3 are same and Greater.")
elif(num2 > num1):
    #num2
    if(num2 > num3):
        print("Number 2 is Greater")
    elif(num3 > num2):
        print("Number 3 is Greater")
    else:
        #num2=num3
        print("Number 2 and Number 3 are same and Greater.")
else:
    # both equal num1 num2 ==
    if(num1 > num3):
        #num1 and num2 both are same and Greater."
        print("Number 1 and Number 2 are same and Greater.")
    elif(num3 > num1):
        #num3
        print("Number 3 is Greater")
    else:
        # all are equals
        print("All are Equal")