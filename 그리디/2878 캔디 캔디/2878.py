import sys
sys.stdin = open('2878.txt','r')
from collections import deque
import heapq

n,m = map(int, input().split())
wants = []
for _ in range(m):
    a = int(input())
    heapq.heappush(wants,-a)

while n > 0 and len(wants) > 0:

    if len(wants) >= 2:
        one = heapq.heappop(wants)
        two = heapq.heappop(wants)
        one = -one
        two = -two
        if one > two:
            if n >= (one-two)+1:
                n -= (one-two)+1
                heapq.heappush(wants,-(one - (one-two) - 1))
                heapq.heappush(wants,-two)
            else:
                n = 0
                heapq.heappush(wants,-(one-n))
                heapq.heappush(wants,-two)
        else:
            if n >= one:
                n -= 1
                heapq.heappush(wants,-(one-1))
                heapq.heappush(wants,-two)
            else:
                n = 0
                heapq.heappush(wants,-(one))
                heapq.heappush(wants,-two)
    if len(wants) == 1:
        one = heapq.heappop(wants)
        one = -one
        if n >= one:
            pass
        else:
            n = 0
            heapq.heappush(wants,one-n)


answer = 0

if len(wants) == 0:
    print(0)
else:
    for want in wants:
        answer += want**2
    print(answer%(2**64))