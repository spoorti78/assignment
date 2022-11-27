# program to find the sum of all elements in the
# list using add function of operator module
 
from operator import*
list1 = [8,9,0,7]
result = 0
for i in list1:
  
    result = add(i, result)
# printing the result
print(result)