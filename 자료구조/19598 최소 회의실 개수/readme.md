[백준 : 최소 회의실 개수] (https://www.acmicpc.net/problem/19598)



- 2021년 7월 25일에 품

- 우선순위큐를 두개 활용해서 푸는 문제
- 이러한 유형은 굉장히 많이 풀어봐서 빠르게 해결했다.



```python
import sys
sys.stdin = open('19598.txt','r')
input = sys.stdin.readline
import heapq

n = int(input())
pq = []

for s in range(1,n+1):
    start,end = map(int, input().split())
    heapq.heappush(pq,[start,end,s])

rooms = [0]*100001

tq = []
answer = 0

while pq:
    start,end,number = heapq.heappop(pq)

    while tq and tq[0][0] <= start:
        t_end , t_number = heapq.heappop(tq)
        index = rooms.index(t_number)
        rooms[index] = 0

    result = rooms.index(0)
    rooms[result] = number
    if result > answer:
        answer = result

    heapq.heappush(tq,[end,number])

print(answer+1)

```

![20210725_004109](20210725_004109.png)