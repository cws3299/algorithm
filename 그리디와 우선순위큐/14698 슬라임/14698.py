import sys
sys.stdin = open('14698.txt','r')
import heapq

t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    heapq.heapify(arr)
    answer = 1

    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        heapq.heappush(arr,a*b)
        answer *= a*b

    print(answer%1000000007)