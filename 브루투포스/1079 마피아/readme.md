[ 백준 : 마피아 ] (https://www.acmicpc.net/problem/1079)



- 골드2의 브루투포스 문제
- 재귀를 사용해서 쉽게 품
- 다만 예외 하나에 대한 처리를 안해줘서 계속 63%에서 틀리다가 예외 발견후 정답



```python
import sys
sys.stdin = open('1079.txt','r')
sys.setrecursionlimit(10**5)

def dfs(cnt,time):
    global n,points,arr,me,lives,answer,lives_cnt

    if lives_cnt == 1:
        if cnt > answer:
            answer = cnt
        return

    if cnt > answer:
        answer = cnt

    if time == 0: # 밤
        for nxt in range(n):
            if lives[nxt] == 0 and nxt != me:
                lives[nxt] = 1
                for who in range(n):
                    points[who] += arr[nxt][who]
                cnt += 1
                time = 1
                lives_cnt -= 1
                dfs(cnt,time)
                lives_cnt += 1
                lives[nxt] = 0
                time = 0
                cnt -= 1
                for who in range(n):
                    points[who] -= arr[nxt][who]
    else: # 낮
        die = -1
        die_point = 0
        for nxt in range(n):
            if lives[nxt] == 0:
                if points[nxt] > die_point:
                    die_point = points[nxt]
                    die = nxt
        if die == me:
            return
        
        lives[die] = 1
        time = 0
        lives_cnt -= 1
        dfs(cnt, time)
        lives_cnt += 1
        time = 1
        lives[die] = 0
    
    return


n = int(input())
points = list(map(int, input().split()))
arr = []
for _ in range(n):
    ar = list(map(int,input().split()))
    arr.append(ar)
me = int(input())

lives = [0] * n
lives_cnt = n
flag = False

if n%2 == 1:
    die = -1
    die_point = 0
    for k in range(n):
        if points[k] > die_point:
            die_point = points[k]
            die = k
    
    lives[die] = 1
    lives_cnt -= 1
    if die == me:
        flag = True

answer = 0

# 밤 부터 시작
if lives_cnt > 0 and flag == False:
    dfs(0,0)

print(answer)
```



- 실수했던 예외는 맨 처음이 낮인경우인데 심지어 은진이의 유죄지수가 가장 높은 경우
  - 이 경우에는 dfs를 안들어가야한다.

![20211222_131719](20211222_131719.png)