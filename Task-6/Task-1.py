num = int(input("Input number of terms :"))
sum = 0 
print("The odd number are :" ,end=",")
for i in range(1,(num*2)+1):
    if(i%2!=0):
        sum = sum + 1
        print(i,end=",")

print("")
print("The sum of odd Natural Number upto 10 terms :",sum)