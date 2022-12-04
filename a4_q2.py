#Python program to triple all numbers of a given list of integers using map.

lst=[]
length=int(input("enter length of the list: "))
for i in range(length):
    number=int(input("enter number: "))
    lst.append(number)
print(lst) 
def triple(num):
    return num*3
result=list(map(triple,lst))
print(result)
