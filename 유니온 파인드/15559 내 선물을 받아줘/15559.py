import sys
sys.stdin = open('15559.txt','r')


def find(a):
    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a,b):
    rootA = find(a)
    rootB = find(b)
    if rootA == rootB:
        return False

    if rootA < rootB:
        parents[rootB] = rootA
    else:
        parents[rootA] = rootB
    return True

def go(y,x):
    global n,m,parents,visit,arr
    
    print(y,x)

    if arr[y][x] == 'N':
        ny = y-1
        nx = x
        if 0<=ny<n and 0<=nx<m:
            visit[ny][nx] = 1
            result = union(find(parents[(y*m)+(x+1)]),find(parents[(ny*m)+nx+1]))
            if result == False:
                return
            go(ny,nx)
    if arr[y][x] == 'S':
        ny = y+1
        nx = x
        if 0<=ny<n and 0<=nx<m:
            visit[ny][nx] = 1
            result = union(parents[(y*m)+(x+1)],parents[(ny*m)+nx+1])
            if result == False:
                return
            go(ny,nx)
    if arr[y][x] == 'W':
        ny = y
        nx = x-1
        if 0<=ny<n and 0<=nx<m:
            visit[ny][nx] = 1
            result = union(parents[(y*m)+(x+1)],parents[(ny*m)+nx+1])
            if result == False:
                return
            go(ny,nx)
    if arr[y][x] == 'E':
        ny = y
        nx = x+1
        if 0<=ny<n and 0<=nx<m:
            visit[ny][nx] = 1
            result = union(parents[(y*m)+(x+1)],parents[(ny*m)+nx+1])
            if result == False:
                return
            go(ny,nx)

    return




n,m = map(int, input().split())
parents = [i for i in range((n*m)+1)]
visit = [[0]*m for _ in range(n)]
arr = []

for _ in range(n):
    arr1 = list(input())
    arr.append(arr1)


for y in range(n):
    for x in range(m):
        if visit[y][x] == 0:
            visit[y][x] = 1
            go(y,x)
            print(y,x,parents)


# print(visit)
print(parents)

ans = set()
for y in range(n):
    for x in range(m):
        ans.add(find(parents[(y*m)+(x+1)]))

print(ans)