[ 백준 : 학회원 ]  (https://www.acmicpc.net/problem/3865)



- 2021-07-30에 품

- 해쉬를 통해 집합들을 만든다.
- 그룹이 들어있을 경우 dfs를 통해 안의 그룹으로 계속 들어가면서 찾아주도록 설계했다.



```python
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
```

![20210730_145724](20210730_145724.png)