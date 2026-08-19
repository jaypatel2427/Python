num = int(input("Input number of terms :"))
sum = 0
print("The even numbers are :" , end="")
for i in range(1,(num*2)+1):
    if(i%2==0):
        sum = sum + i
        print(i,end=",")

print("")
print("The sum of odd Natural Number upto 10 terms :", sum)