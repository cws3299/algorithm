[백준 : 지금 만나러 갑니다] (https://www.acmicpc.net/problem/18235)



- 재밌는 bfs문제였다.
- q1 -> 오리의 움직임
- q2 -> 육리의 움직임
- visit -> 오리가 도착한 위치 (해당 위치의 값을 도착한 시간으로 변경)
- 육리도 오리와 같은 visit에 도착했고 값도 같을경우 해당 값을 출력해줌



```python
import sys
sys.stdin = open('18235.txt','r')
from collections import deque

def bfs():
    global n,a,b,visit,answer

    q1 = deque()
    q1.append([a,0])
    q2 = deque()
    q2.append([b,0])

    ll = len(q1)
    ll2 = len(q2)
    flag = True
    while flag and q1:
        for _ in range(ll):
            aa,move_a = q1.popleft()

            nxt_l = aa-(2**move_a)
            nxt_r = aa+(2**move_a)

            if 1<= nxt_l <=n:
                visit[nxt_l] = move_a
                q1.append([nxt_l,move_a+1])

            if 1<= nxt_r <=n:
                visit[nxt_r] = move_a
                q1.append([nxt_r,move_a+1])

        for _ in range(ll2):
            bb,move_b = q2.popleft()

            nxt_l = bb-(2**move_b)
            nxt_r = bb+(2**move_b)


            # if visit[nxt_l] == move_b or visit[nxt_r] == move_b:
            #     answer = move_b+1
            #     flag = False
            #     break

            if 1<= nxt_l <=n:
                if visit[nxt_l] == move_b :
                    answer = move_b+1
                    flag = False
                    break
                q2.append([nxt_l,move_b+1])

            if 1<= nxt_r <=n:
                if visit[nxt_r] == move_b :
                    answer = move_b+1
                    flag = False
                    break
                q2.append([nxt_r,move_b+1])
        ll = len(q1)
        ll2 = len(q2)
    return





n,a,b = map(int, input().split())

visit = [-1]*(n+1)
answer = -1
bfs()

print(answer)
```

![84시간](84시간.png)