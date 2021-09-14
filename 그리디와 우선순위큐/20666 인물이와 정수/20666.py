import sys
sys.stdin = open('20666.txt','r')
import heapq

n,m = map(int,input().split())
arr = list(map(int, input().split()))
p = int(input())
minus = {i:{} for i in range(n)}
pq = []
for _ in range(p):
    item , boss, up = map(int, input().split())
    item -= 1
    boss -= 1
    arr[boss] += up
    minus[item][boss] = up

for k in range(len(arr)):
    heapq.heappush(pq,[arr[k],k])

cnt = 0
answer = 0
while pq:
    difficulty,problem = heapq.heappop(pq)
    if arr[problem] == float('inf'):
        continue
    if difficulty > answer:
        answer = difficulty
    cnt += 1
    arr[problem] = float('inf')
    for idx,val in minus[problem].items():
        if arr[idx] != float('inf'):
            arr[idx] -= val
            heapq.heappush(pq,[arr[idx],idx])

    if cnt == m:
        break
    # print(arr)

print(answer)
    
    
    
