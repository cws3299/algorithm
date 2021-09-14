import sys
sys.stdin = open('1781.txt','r')
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    deadline,cup_ramen = map(int, input().split())
    arr.append([deadline,cup_ramen])

arr.sort()
pq = []

for deadline, cup_ramen in arr:
    heapq.heappush(pq,cup_ramen)
    if deadline < len(pq):
        heapq.heappop(pq)

print(sum(pq))