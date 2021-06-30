import sys
sys.stdin = open('1.txt','r')

n = int(input())
arr = []
for _ in range(n):
    ar = int(input())
    arr.append(ar)

dp = [0]*n

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0]+arr[1])
else:
    for k in range(2,n):
        arr[k] = max(arr[k-2]+arr[k],arr[k-1]+arr[k])

print(arr)

