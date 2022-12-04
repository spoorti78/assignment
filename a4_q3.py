#  Python program to square the elements of a list using map() function

lst=[]
length=int(input(" length of the list: "))
for i in range(length):
    element=int(input(" enter element:  "))
    lst.append(element)
print(lst)
def square(data):
    return data*data
result=list(map(square,lst))
print(result)