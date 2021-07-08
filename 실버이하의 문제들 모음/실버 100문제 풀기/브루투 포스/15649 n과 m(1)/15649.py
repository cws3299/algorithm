import sys
sys.stdin = open('15649.txt','r')

def dfs(now):
    global n,m,visit,arr

    if now == m:
        for a in arr:
            print(a, end = ' ')
        print()
        return


    for nxt in range(1,n+1):
        if visit[nxt] == 0:
            visit[nxt] = 1
            now += 1
            arr.append(nxt)
            dfs(now)
            arr.pop()
            now -= 1
            visit[nxt] = 0

    return


n,m = map(int, input().split())
visit = [0]*(n+1)
arr = []

dfs(0)