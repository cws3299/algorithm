[ 백준 : 애너그램 ] (https://www.acmicpc.net/problem/6443)



- 일반적인 dfs를 활용하는 백트래킹 문제이다.
- set을 통해 중복을 방지해주는 과정과 lambda를 통해서 정렬해주는 과정만 유의하면 된다.

```python
import sys
sys.stdin = open('6443.txt','r')
sys.setrecursionlimit(10**5)

def dfs(now,words):
    global answer,n,remain,l

    if now == l:
        answer.add(words)
        return

    for k in range(26):
        if remain[k] > 0:
            remain[k] -= 1
            words += chr(k+97)
            now += 1
            dfs(now,words)
            now -= 1
            words = words[:-1]
            remain[k] += 1

    return

answer = set()
n = int(input())
for _ in range(n):
    remain = [0]*26
    string = list(input())
    l = len(string)
    for s in string:
        remain[ord(s)-97] += 1
    for k in range(26):
        word= ''
        if remain[k] > 0:
            remain[k] -= 1
            word += chr(k+97)
            dfs(1,word)
            word = ''
            remain[k] += 1


answer = list(answer)
answer.sort(key=lambda x:(len(x),x))
for ans in answer:
    print(ans)
```

![20210904_235220](20210904_235220.png)