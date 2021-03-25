import sys
sys.stdin = open('14395.txt','r')
sys.setrecursionlimit(10**5)
import heapq
from copy import deepcopy

n,m = map(int, input().split())
if n == m:
    print(0)
else:
    answer_lst = []
    visit = set()

    pq = []
    heapq.heappush(pq,[0,n,[]])
    visit.add(n)
    ll = len(pq)

    answer = 0
    stop = True

    while stop and pq:

        ll = len(pq)

        for _ in range(ll):
            cnt,now,lst = heapq.heappop(pq)

            # print(cnt,now,lst)

            if now == m:
                answer = cnt
                answer_lst.append(lst)
                stop = False

            # print(now)
            for k in range(4):
                if k == 0:
                    nxt = now*now
                    if nxt not in visit and 0<= nxt < 1000000001:
                        if nxt != m:
                            visit.add(nxt)
                        temp = deepcopy(lst)
                        temp.append('*')
                        heapq.heappush(pq,[cnt+1,nxt,temp])
                if k == 1:
                    nxt = now+now
                    if nxt not in visit and  0<= nxt < 1000000001:
                        if nxt != m:
                            visit.add(nxt)
                        temp = deepcopy(lst)
                        temp.append('+')
                        heapq.heappush(pq,[cnt+1,nxt,temp])
                if k == 2:
                    nxt = now-now
                    if nxt not in visit and  0<= nxt < 1000000001:
                        if nxt != m:
                            visit.add(nxt)
                        temp = deepcopy(lst)
                        temp.append('-')
                        heapq.heappush(pq,[cnt+1,nxt,temp])
                if k == 3 and now != 0:
                    nxt = 1
                    if nxt not in visit and 0<= nxt < 1000000001:
                        if nxt != m:
                            visit.add(nxt)
                        temp = deepcopy(lst)
                        temp.append('/')
                        heapq.heappush(pq,[cnt+1,nxt,temp])

        
    # print(answer_lst)

    if len(answer_lst)>=1:
        answer_lst = sorted(answer_lst, key=lambda x:x)


    
    if len(answer_lst) == 0:
        print(-1)
    else:
        answerr = answer_lst[0]
        for an in answerr:
            print(an , end ='')