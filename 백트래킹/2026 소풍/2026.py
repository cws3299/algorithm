import sys
sys.stdin = open('2026.txt','r')
from copy import deepcopy

def dfs(now):
    global kk,n,p,arr,visit,answer,flag,final

    

    if len(answer) == kk:
        flag = True
        final = deepcopy(answer)
        return

    for k in range(now,n+1):
        if visit[k] == 0:
            result = confirm(k)
            if result == True and flag == False:
                visit[k] = 1
                answer.append(k)
                dfs(k)
                answer.pop()
                visit[k] = 0

    return

def confirm(now):
    global kk,n,p,arr,visit,answer,flag

    for k in answer:
        if k not in arr[now]:
            return False

    return True
    


kk,n,p = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(p):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

answer = []
visit = [0]*(n+1)
flag = False
final = []

for k in range(1,n+1):
    visit[k] = 1
    answer.append(k)
    dfs(k)
    if flag == True:
        break
    answer.pop()
    visit[k] = 0

if len(final) == 0:
    print(-1)
else:
    for f in final:
        print(f)