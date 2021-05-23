import sys
sys.stdin = open('17616.txt','r')
sys.setrecursionlimit(10**5)

def go_up(now):
    global n,m,up,down,visit_up,up_ans

    # print('up',now)

    for nxt in up[now]:
        if visit_up[nxt] == 0:
            visit_up[nxt] = 1
            up_ans += 1
            go_up(nxt)

    return

def go_down(now):
    global n,m,up,down,visit_down,down_ans

    # print('down',now)
    for nxt in down[now]:
        if visit_down[nxt] == 0:
            visit_down[nxt] = 1
            down_ans += 1
            go_down(nxt)

    return



n,m,p = map(int, input().split())

up = [[] for _ in range(n+1)]
down = [[] for _ in range(n+1)]
visit_up = [0]*(n+1)
visit_down = [0]*(n+1)

up_ans = 0
down_ans = 0

for _ in range(m):
    a,b = map(int, input().split())
    up[b].append(a)
    down[a].append(b)


# print(up)
# print(down)
# visit_up[p] = 1
# visit_down[p] = 1
go_up(p)
go_down(p)

print(up_ans)
print(down_ans)

# print('----------------')
print(down_ans, end =' ')
print(n-up_ans)

