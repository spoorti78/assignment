#program to reverse a given word 
rev_word1=input("Enter the word   ")
rev_word2=""
for i in rev_word1:
    rev_word2=i+rev_word2
print("orignal= ",rev_word1)
print("reversed=",rev_word2)