import sys
sys.stdin = open('17073.txt','r')
sys.setrecursionlimit(10**5)

n,m = map(int, input().split())
node = [[] for _ in range(n+1)]

for _ in range(n-1):
    s,e = map(int, input().split())
    node[s].append(e)
    node[e].append(s)

number = 0
for k in range(2,n+1):
    if len(node[k]) == 1:
        number += 1


print("{:.5f}".format(m/number))