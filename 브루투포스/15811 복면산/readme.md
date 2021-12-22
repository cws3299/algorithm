[백준 : 복면산]  (https://www.acmicpc.net/problem/15811)



- 단순한 재귀를 활용해서 들어갈 숫자를 구한 후 정답을 구했다.
- 처음에 자료구조를 만드는 과정빼면 일반 브루투포스랑 똑같다.



```python
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

```

![20211125_182121](C:\Users\cws89\Desktop\aaa\15811 복면산\20211125_182121.png)