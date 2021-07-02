[백준 : 행운의 문자열] (https://www.acmicpc.net/problem/1342)



- 풀긴 풀었는데 속도가 이게 맞는건가 싶다....



```python
import sys
sys.stdin = open('1342.txt','r')
from copy import deepcopy

def dfs(string,l):
    global words,visit,answer,ll

    if l == ll:
        answer.add(string)

    for k in range(ll):
        if visit[k] == 0:
            visit[k] = 1
            c_string = deepcopy(string)
            if c_string[-1] != words[k]:
                c_string += words[k]
                l += 1 
                dfs(c_string,l)
                l -= 1
            visit[k] = 0

    return


words = list(input())
ll = len(words)
visit = [0]*ll
answer = set()

for k in range(ll):
    visit[k] = 1
    dfs(words[k],1)
    visit[k] = 0

print(len(answer))
```

![20210702_094406](20210702_094406.png)