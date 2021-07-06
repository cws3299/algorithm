# 나의 코드

import sys
sys.stdin = open('15651.txt','r')
sys.setrecursionlimit(10**5)

def dfs(now,ar):
    global n,m,arr,answer


    if now == m:
        answer.add(tuple(ar))
        return

    for k in range(1,n+1):
        now += 1
        ar.append(k)
        dfs(now,ar)
        ar.pop()
        now -= 1

    return


n,m = map(int, input().split())
arr = [m]*(n+1)

answer = set()

dfs(0,[])


answer = list(answer)
answer.sort()

for ans in answer:
    for a in ans:
        print(a, end = ' ')
    print()