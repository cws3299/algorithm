import sys
sys.stdin = open('1781.txt','r')
import heapq

n = int(input())
visit = [0]*(n+1)
pq = []
for k in range(n):
    a,b = map(int, input().split())
    heapq.heappush(pq,[a,b,k])

x,y,z = -1,-1,-1
answer = 0
cnt = 1
while pq:

    ramen = 0
    # flag = False
    while pq[0][0] <= cnt:
        dead,cup,pos = heapq.heappop(pq)

        if cup > ramen:
            ramen = cup
            # flag = True
        
        if len(pq) == 0:
            break

    # print(answer)

    ramen2 = 0
    dead2 = 0
    tmp = -1
    tm = -1
    aq = []
    # if flag == False:
    cn = 0
    ll = len(pq)
    
    while cn < ll:
        dead,cup,pos = heapq.heappop(pq)

        if visit[pos] == 0:
            if dead2 < dead:
                ramen2 = 0
                dead2 = dead
                if ramen2 < cup:
                    ramen2 = cup
                    visit[tmp] = 0
                    tmp = pos
                    visit[tmp] = 1
                    tm = tmp
                    x = dead
                    y = cup
                    z = pos

        
        if tm == tmp:
            aq.append([dead,cup,pos])
        cn += 1

    if rame    
    
    if z != -1:
        visit[z] = 1
        answer += ramen2

    for a in aq:
        if visit[a[2]] == 0:
            heapq.heappush(pq,a)

    cnt += 1
    answer += ramen

print(answer)