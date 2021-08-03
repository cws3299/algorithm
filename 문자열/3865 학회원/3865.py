import sys
input = sys.stdin.readline
sys.stdin = open('3865.txt','r')
from collections import defaultdict
from copy import deepcopy

def dfs(name):
    global n,dict,visit,g_dict,final

    for nxt in dict[name]:
        if nxt not in g_dict:
            final.add(nxt)
        else:
            if visit[nxt] == 0:
                visit[nxt] = 1
                dfs(nxt)

    return

while True:
    n = int(input())
    if n != 0:
        dict = defaultdict(list)
        visit = defaultdict(int)
        g_dict = []
        final = set()

        for _ in range(n):
            arr = input().split('.')
            arr = arr[0]
            arr = arr.split(':')
            group = arr[0]
            members = arr[1]
            members = members.split(',')
            # print(group,members)

            dict[group] = members
            g_dict.append(group)

        one = deepcopy(g_dict[0])

        for k in dict[one]:
            if k not in g_dict:
                final.add(k)
            else:
                visit[k] = 1
                dfs(k)


        print(len(final))
    else:
        break