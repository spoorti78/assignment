#program to count even and odd days.

numbers  = (1, 2, 3, 4, 5, 8,10,12,15,66, 7, 87, 19)
odd_days = 0
even_days = 0
for x in numbers:
    if not (x % 2==0):  	     
            even_days+=1
    else:
    	     odd_days+=1
print("Number of even numbers :",even_days)
print("Number of odd numbers :",odd_days)
