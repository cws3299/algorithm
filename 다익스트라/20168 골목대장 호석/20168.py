import sys
sys.setrecursionlimit(10**5)
sys.stdin = open('20168.txt','r')

def dfs(now,vis,_max,total):
    global n,m,start,end,money,roads,visit,result

    # print('------',now,bin(vis),_max,total)

    if total > money:
        return

    if now == end:
        if result > _max:
            result = _max
        return

    for nxt,wt in roads[now].items():
        if not vis&(1<<nxt):
            new_total = total + wt
            # print('1',bin(vis))
            new_vis = vis|(1<<nxt)
            # print('2',bin(new_vis),nxt)
            if new_total <= money:
                if visit[nxt][new_vis] == 0:
                    visit[nxt][new_vis] = 1
                    # print('++')
                    if wt < _max:
                        dfs(nxt,new_vis,_max,new_total)
                    else:
                        dfs(nxt,new_vis,wt,new_total)
                    visit[nxt][new_vis] = 0

    return
            


n,m,start,end,money = map(int,input().split())
roads = {node:{} for node in range(n+1)}
visit = [[0]*(1<<n+1) for _ in range(n+1)]
result = float('inf')

for _ in range(m):
    a,b,w = map(int, input().split())
    roads[a][b] = w
    roads[b][a] = w

dfs(start,(1<<start),0,0)

if result == float('inf'):
    print(-1)
else:
    print(result)