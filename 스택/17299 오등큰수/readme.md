[백준 : 오등큰수] (https://www.acmicpc.net/problem/17299)



- 오큰수 문제와 유사한 문제

```python
import sys
sys.stdin = open('17299.txt','r')

n = int(input())
count = [0]*1000001
answer = [-1]*n
stack = []
arr = list(map(int, input().split()))

for k in arr:
    count[k] += 1

cnt = 0
while cnt < n:
    a , f = arr[cnt],count[arr[cnt]]
    if stack == []:
        stack.append([a,f,cnt])
    else:
        while True:
            if len(stack) > 0:
                if stack[-1][1] < f:
                    aa,ff,cntt = stack.pop()
                    # print(aa,ff,cntt,stack)
                    answer[cntt] = a
                else:
                    stack.append([a,f,cnt])
                    break
            else:
                stack.append([a,f,cnt])
                break
    cnt += 1


for ans in answer:
    print(ans , end = ' ')
```

![20210617_002501](20210617_002501.png)