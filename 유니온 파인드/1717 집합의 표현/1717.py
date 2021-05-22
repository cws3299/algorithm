import sys
sys.stdin = open('1717.txt','r')

def find(a):
    if arr[a] == a:
        return a
    arr[a] = find(arr[a])
    return arr[a]

def union(a,b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        arr[rootB] = rootA
    return

def check(a,b):
    if find(a) == find(b):
        return True
    else:
        return False



n,m = map(int, input().split())
arr = [i for i in range(n+1)]
for _ in range(m):
    choice,a,b = map(int,input().split())
    if choice == 0:
        union(a,b)
    else:
        ans = check(a,b)
        if ans == True:
            print('YES')
        else:
            print('NO')
