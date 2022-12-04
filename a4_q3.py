#  Python program to square the elements of a list using map() function

lst=[]
length=int(input(" length of the list: "))
for i in range(length):
    numbers=int(input(" enter number:  "))
    lst.append(numbers)
print(lst)
def square(data):
    return data*data
result=list(map(square,lst))
print(result)