import math

def power(n):
    return (n!= 0) and ((n & (n-1))==0)

n = int(input())
arr = list(map(int, input().split()))

sum = 0
count = 0

for i in range:
    if not power(arr[i]):
        sum += (arr[i])
        count += 1

avg = sum/count

print (math.floor(avg))