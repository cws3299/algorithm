import sys
sys.stdin = open('1826.txt','r')
import heapq

pq = []
sq = []
n = int(input())
for _ in range(n):
    p,o = map(int, input().split())
    heapq.heappush(pq,[p,o])

end,f = map(int, input().split())
heapq.heappush(pq,[end,0])

answer = 0
flag = True
while len(pq) != 0:
    p,o = heapq.heappop(pq)

    if p>f:
        while p>f:
            oo,pp = heapq.heappop(sq)
            oo = -oo
            f += oo
            answer += 1
            if len(sq) == 0 and p>f:
                flag = False
                break

    heapq.heappush(sq,[-o,p])
    
    if flag == False:
        break

    if f >= end:
        break

if flag == False:
    print(-1)
else:
    print(answer)

            


