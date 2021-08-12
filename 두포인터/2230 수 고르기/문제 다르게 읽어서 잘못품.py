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
now = arr[right]
answer = float('inf')

while left != n-1:
    print('--',left,right,now)
    if m <= now:
        if now <= answer:
            answer = now
        now -= arr[left]
        left += 1
        if m<=now<=answer:
            answer = now
    else:
        if right != n-1:
            right += 1
            now += arr[right]
            if m<=now<=answer:
                answer = now

print(answer)
                    
