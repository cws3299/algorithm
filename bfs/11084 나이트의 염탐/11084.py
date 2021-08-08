import sys
sys.stdin = open('11084.txt','r')
import heapq
from collections import defaultdict

n,m = map(int,input().split())
if n == 1 and m == 1:
    print('{} {}'.format(0,1))
else:
    arr = [[0]*m for _ in range(n)]
    visit = [[0]*m for _ in range(n)]

    pq = []
    heapq.heappush(pq,[0,1,0,0])
    dy = [-2,-2,-1,-1,1,1,2,2]
    dx = [-1,1,-2,2,-2,2,-1,1]
    flag = float('inf')
    answer = 0
    dictt = defaultdict(set)

    while pq:
        move, cnt ,y,x = heapq.heappop(pq)
        # print(move, cnt ,y,x)

        if flag < move:
            break

        if y == n-1 and x == m-1:
            flag = move
            answer = move

        for k in range(8):
            ny = y+dy[k]
            nx = x+dx[k]
            if 0<=ny<n and 0<=nx<m:
                if visit[ny][nx] == 0 or visit[ny][nx] >=move:
                    visit[ny][nx] = move
                    arr[ny][nx] += cnt
                    dictt[move].add((ny,nx))
        
        if pq == []:
            for di in dictt[move]:
                ddy = di[0]
                ddx = di[1]
                heapq.heappush(pq,[move+1,arr[ddy][ddx],ddy,ddx])

        

            

    if answer == 0:
        print('None')
    else:    
        print(answer, end = ' ')
        print(arr[n-1][m-1] % 1000000009)
