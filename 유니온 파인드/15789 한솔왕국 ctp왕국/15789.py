import sys
sys.stdin = open('15789.txt','r')

def find(a):
    global n,m,parents

    if parents[a] == a:
        return a
    parents[a] = find(parents[a])
    return parents[a]

def union(a,b):
    global n,m,parents

    rootA = find(a)
    rootB = find(b)

    if rootA < rootB:
        parents[rootB] = rootA
        numbers[rootA] += numbers[rootB]
    elif rootA == rootB:
        pass
    else:
        parents[rootA] = rootB
        numbers[rootB] += numbers[rootA]
    
    return


n,m = map(int, input().split())
parents = [i for i in range(n+1)]
numbers = [1 for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    union(a,b)


c,h,k = map(int, input().split())

cc = find(c)
hh = find(h)

# print(parents)
# print(cc,hh)

lst = []
for idx, val in enumerate(numbers):
    lst.append([idx,val])

lst.sort(key=lambda lst:(lst[1]))
# lst.reverse()
visit = [0]*(n+1)

# print(lst)
answer = numbers[cc]

cnt = 0
# print(parents,cc,hh)
while lst and cnt<k:

    idx,val = lst.pop()
    vv = find(idx)
    # print('vv',vv)
    if vv != hh and vv != cc:
        # print(vv)
        if visit[vv] == 0:
            visit[vv] = 1
            answer += numbers[find(vv)]
            cnt += 1
            if cnt == k:
                # print(cnt)
                break


print(answer)