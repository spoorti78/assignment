# Program to display the Fibonacci sequence 
nterms = 10

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
    nth=n1,n2
else:
   print("Fibonacci sequence output: " )
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1