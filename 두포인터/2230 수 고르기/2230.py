import sys
sys.stdin = open('2230.txt','r')

n,m = map(int, input().split())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)

arr.sort()

left = 0
right = 0
answer = float('inf')

while left != n-1:
    if m<=arr[right] - arr[left]:
        if m<=arr[right]-arr[left] <=answer:
            answer = arr[right]-arr[left]
        left += 1
    else:
        if right != n-1:
            right += 1
        else:
            left += 1
        
    

print(answer)

                    
