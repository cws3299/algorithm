[백준 : 나무 위의 빗물] (https://www.acmicpc.net/problem/17073)



- 깊이 우선 탐색을 활용해야 할 줄 알았으나 문제를 읽자마자 그냥 리프노드 수 구해서 빗물을 나눠준 값을 출력하면 되겠다고 생각했는데 , 그대로 풀림 



```python
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
```

![20210422_112102](20210422_112102.png)