import sys
sys.stdin = open('1092.txt','r')
from collections import deque

c = int(input())
crr = list(map(int, input().split()))
b = int(input())
brr = list(map(int, input().split()))

crr.sort()
brr.sort()
brr = deque(brr)
max_c = max(crr)
max_b = max(brr)

ccrr = [0]*(len(crr))

if max_c < max_b:
    print(-1)
else:
    second = 0
    while brr:
        # print(brr)
        k = c-1
        temp = []
        while k!=-1 and brr: 
            box = brr.pop()
            if crr[k] >= box:
                k -= 1
            else:
                # k-=1
                temp.append(box)

        temp.reverse()
        for t in temp:
            brr.append(t)
        
        second += 1

    print(second)
            

        
