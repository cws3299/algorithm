import sys
sys.stdin = open('12764.txt','r')
import heapq

n = int(input())
computers = [0]*(n+1) # 총 갯수
use = [0]*(n+1) # 사용중의 유무 -> 0 대신 끝나는 시간 넣기

pq = []
for _ in range(n):
    start,end = map(int, input().split())
    heapq.heappush(pq,[start,end])

out_cnt = 0
time = 0
now_computer = 0
end_pq = []

while out_cnt != n:
    start,end = heapq.heappop(pq)

    time = start

    while end_pq and end_pq[0][0] < time:
        endd, in_computerr = heapq.heappop(end_pq)
        use[in_computerr] = 0 


    in_computer = use.index(0)
    computers[in_computer] += 1
    use[in_computer] = end
    heapq.heappush(end_pq,[end,in_computer])

    out_cnt += 1

idx = computers.index(0)
# print(idx)
# print(computers)
print(idx)

computers = computers[:idx]

for co in computers:
    print(co, end= ' ')






    