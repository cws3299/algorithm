import sys
sys.stdin = open('15811.txt','r')
sys.setrecursionlimit(10**5)

def dfs(now):
    global wordA, wordB, wordC, wordCnt, dict, reverse_dict, stack, visit,answer

    if now == wordCnt:
        wA = ''
        wB = ''
        wC = ''

        for w in wordA:
            wA += str(stack[w])

        for w in wordB:
            wB += str(stack[w])

        for w in wordC:
            wC += str(stack[w])
        
        wA = int(wA)
        wB = int(wB)
        wC = int(wC)
        
        if wA + wB == wC:
            answer = True
        return

    for k in range(10):
        if visit[k] == 0 and answer == False:
            visit[k] = 1
            stack.append(k)
            now +=1 
            dfs(now)
            stack.pop()
            now -=1
            visit[k] = 0

    return

stringA, stringB, stringC = map(str, input().split(' '))

numbers = []

stringA = list(stringA)
stringB = list(stringB)
stringC = list(stringC)
total = stringA + stringB + stringC
total = set(total)
total = list(total)
dict = {}
reverse_dict = {}
wordA = []
wordB = []
wordC = []
total.sort()
wordCnt = len(total)

cnt = 0
for t in total:
    dict[cnt] = t
    reverse_dict[t] = cnt
    cnt += 1

for s in stringA:
    wordA.append(reverse_dict[s])
for s in stringB:
    wordB.append(reverse_dict[s])
for s in stringC:
    wordC.append(reverse_dict[s])

visit = [0] * 10
stack = []
answer = False

dfs(0)

if answer == False:
    print('NO')
else:
    print('YES')
