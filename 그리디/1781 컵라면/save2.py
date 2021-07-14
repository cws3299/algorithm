import sys
sys.stdin = open('1781.txt','r')
import heapq

n = int(input())
day = 0
pq = []
for s in range(1,n+1):
    d,c = map(int, input().split())
    heapq.heappush(pq,[-d,c,s])
    if abs(d) > abs(day):
        day = -d

tq = []
answer = 0

while pq and day < 0:
    r_dead = 0
    r_cup = 0
    r_number = 0
    flag = False
    dead,cup,s = heapq.heappop(pq)
    # print('-----------------',dead,cup,s)
    # if dead <= day: 
    r_dead = dead
    r_cup = cup
    r_number = s 
    
    while pq and pq[0][0] <= day:
        flag = True
        dead2,cup2,s2 = heapq.heappop(pq)
        if cup2 > r_cup:
            heapq.heappush(tq,[r_dead,r_cup,r_number])
            r_dead = dead2
            r_cup = cup2
            r_number = s2
        elif cup2 <= r_cup:
            heapq.heappush(tq,[dead2,cup2,s2])
        
    # print(r_dead)
    if flag == False and day<r_dead:
        heapq.heappush(tq,[r_dead,r_cup,r_number])

    
    # print(tq,pq)

    pq += tq
    
    tq = []
    # print(pq)

    # print('=/==',pq)

    if day >= r_dead:
        answer += r_cup
    # print(day,r_number,r_dead,r_cup,pq)

    day += 1
    


print(answer)