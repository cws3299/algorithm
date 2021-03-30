import sys
sys.stdin = open('2075.txt','r')
import heapq

n = int(input())

pq = []

for _ in range(n):
    arr = list(map(int,input().split()))

    for ar in arr:
        heapq.heappush(pq,ar)

    ll = len(pq)
    # print(ll,pq)

    while ll>n:
        # print(ll,n)
        r = heapq.heappop(pq)
        ll -= 1

# print(pq)
answer = 0
# for _ in pq:
p = heapq.heappop(pq)
answer = p

print(answer)
