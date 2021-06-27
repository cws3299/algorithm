[백준 : 용돈관리] (https://www.acmicpc.net/problem/6236)



- 해당 문제의 경우 해설을 참조하였음
  - 위 글이 없는 경우는 다 스스로 푼 문항



- 이분탐색이랑 DP구조는 정말 정말 어렵다....... 공부 많이한 알고리즘들은 골드 상위권 문제들도 쉽지는 않아도 평탄하게 풀 수 있는데 이 두 챕터는 나에게 뭔가 항상 어려움을 준다.....
- 빨리 이분탐색이랑 DP를 어느정도 익힌 후 더 어려운 알고리즘에 들어가야겠다.



```python
import sys
sys.stdin = open('6236.txt','r')

def check():
    global mid

    money = 0
    res = 0
    for data in datas:
        if mid < data:
            return 10000000
        
        if money >=data:
            money -= data
        else:
            money = mid-data
            res += 1
    
    return res

n,m = map(int,input().split())
datas = []
for _ in range(n):
    data = int(input())
    datas.append(data)

low = 0
high = 10000000
answer = 10000000

while low <= high:
    mid = (low+high) // 2
    result = check()
    if result > m:
        low = mid +1 
    else:
        answer = min(answer,mid)
        high = mid-1


print(answer)

```

