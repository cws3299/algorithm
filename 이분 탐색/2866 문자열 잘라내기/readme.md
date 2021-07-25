[ 백준: 문자열 잘라내기 ] (https://www.acmicpc.net/problem/2866)



- 2021-07-24에 푼 문제

- 이분탐색 문제이다.
- left는 0 부터 시작 right는 끝행의 번호
- 이를 토대로 mid위치를 설정후 mid부터 끝행까지의 문자에 중복이 있는지 확인
- 중복이 없다면 right를 mid-1로 있다면 left를 mid+1로 변환 
- answer의 경우 중복이 없는 경우를 기준으로 하기 때문에 left가 변화할 때 값이 바뀌게 설정



```python
import sys
sys.stdin = open('2866.txt','r')

def confirm(mid):
    global n,m,arr

    lst = set()
    for x in range(m):
        string = ''
        for y in range(mid,n):
            string += arr[y][x]
        lst.add(string)

    if len(lst) == m:
        return True
    else:
        return False


n,m = map(int, input().split())
arr = []
for _ in range(n):
    ar = list(input())
    arr.append(ar)

left = 0
right = n-1
answer = None

while left <= right:
    mid = (left + right) // 2

    result = confirm(mid)
    if result == True:
        answer = mid
        left = mid +1
    else:
        right = mid - 1

print(answer)
```

![20210724_124103](20210724_124103.png)