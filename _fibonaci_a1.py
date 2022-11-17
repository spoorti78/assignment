num=int(input("enter the number:  "))
firstval=0
secondval=1
for n in range(0,num):
    if (n<=1):
        next=n
    else:
        next=firstval+secondval
        firstval=secondval
        secondval=next
    print(next,end=" ")