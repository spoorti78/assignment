# program to find number of uppercase and lowercase letter.
# input is taken from user.
x=input("Enter the string:- ")
def char(x):
  u=0
  l=0
  for i in x:
      if i>='a' and i<='z':
       l+=1

      if i >='A' and i<='Z':
       u+=1

  print("LowerCase letter in the String",l)
  print("UpperCase letter in the String",u)
char(x)