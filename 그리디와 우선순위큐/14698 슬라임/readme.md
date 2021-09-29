[ 백준 : 전생했더니 슬라임 연구자였던 건에 대하여 (Hard)] (https://www.acmicpc.net/problem/14698)



- 이게 왜 골드4인지 모르겠다. 아이디어만 생각하면 너무 쉬운 문제
- heapq에서 현재 가장 작은 두개를 빼서 곱한다. 그 후 곱한 값을 다시 heapq에 넣는다.
- 곱하면서 쌓이는 축적값을 answer라는 값에 지속적으로 더해준다.



```python
import sys
sys.stdin = open('14698.txt','r')
import heapq

t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    heapq.heapify(arr)
    answer = 1

    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        heapq.heappush(arr,a*b)
        answer *= a*b

    print(answer%1000000007)
```

![20210929_171715](20210929_171715.png)