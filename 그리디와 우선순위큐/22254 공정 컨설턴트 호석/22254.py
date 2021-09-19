import sys
sys.stdin = open('22254.txt','r')
import heapq
input = sys.stdin.readline

def work(m):
    global n,x,arr

    c = 0
    result = 0

    robots = [0]*m
    heapq.heapify(robots)


    while c < n:
        now = arr[c]
        t = heapq.heappop(robots)
        if t+now > result:
            result = t+now
            if result > x:
                break

        heapq.heappush(robots,t+now)
        c += 1
        
    if result > x:
        return False

    return True

n,x = map(int, input().split())
arr = list(map(int, input().split()))


left = 1
right = n

answer = 0

while left<=right:
    mid = (left+right) // 2

    if work(mid) == True:
        answer = mid
        right = mid-1
    else:
        left = mid+1

print(answer)

