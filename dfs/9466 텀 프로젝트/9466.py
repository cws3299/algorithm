import sys
sys.stdin = open('9466.txt','r')
sys.setrecursionlimit(123456)
input = sys.stdin.readline

def dfs2(now,start):
    global n,choices,visit,temps,answer,flag,flags


    if now == start:
        answer[now] = start
        return

    if answer[now] == 0:
        answer[now] = start
        dfs2(choices[now],start)

    return

def dfs(now,start):
    global n,choices,visit,temps,answer,flag


    if visit[choices[now]] != 0:
        dfs2(choices[now],now)
        flag = True
        return

    choose = choices[now]

    if visit[choose] == 0 and answer[choose] == 0 and fail[choose] == 0:
        visit[choose] = 1

        dfs(choose,start)
        if flag == False:
            fail[now] = 1
        visit[choose] = 0

    return

t = int(input())
for tc in range(t):
    n = int(input())
    choices = list(map(int, input().split()))
    choices.insert(0,0)

    visit = [0]*(n+1)
    answer = [0]*(n+1)
    fail = [0]*(n+1)

    temps = []

    for k in range(1,n+1):
        if answer[k] == 0 and fail[k] == 0:
            flag = False
            dfs(k,k)
            if flag == False:
                answer[k] = 0
                fail[k] = 1



    answer = answer[1:]

    print(answer.count(0))