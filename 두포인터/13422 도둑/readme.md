[ 백준 : 도둑 ] (https://www.acmicpc.net/problem/13422)



- 2021년 8월 3일에 해결한 문제

- 일반적인 두 포인터 문제이다.
- 다만 주의해야할 점은 n == m인 경우 이 경우의 예외처리를 해줘야한다.



```python
import sys
sys.stdin = open('13422.txt','r')
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    n,m,k = map(int, input().split())
    arr = list(map(int, input().split()))
    if n != m:
        tmp = arr[0:m]
        arr += tmp
        arr.insert(0,0)
        n = len(arr)-1

        start = 0
        end = 1
        answer = 0
        now = arr[1]

        while start < n:
            if end != n:
                if end - start == m:
                    if now < k:
                        answer += 1
                    start += 1
                    now -= arr[start]
                else:
                    if end < n:
                        end += 1
                        now += arr[end]
            else:
                now -= arr[start]
                start += 1

        print(answer)
    else:
        if sum(arr) < k:
            print(1)
        else:
            print(0)


```

![20210803_095827](20210803_095827.png)