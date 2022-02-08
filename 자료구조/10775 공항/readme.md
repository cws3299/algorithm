[ 백준 - 공항 ] (https://www.acmicpc.net/problem/10775)



- 생각보다 간단하게 풀려서 당황한 문제
- 분리집합과 그리디를 활용했다.
- 지금 도킹하려는 게이트가 이미 도킹되었을 경우 몇번 게이트에 도킹해야하는지를 생각하는게 중요하다
  - 1,2번 게이트가 도킹 안되어 있고 3,4,5,6,7번 게이트가 도킹되었는데 다음 비행기의 번호가 3~7 중에 하나의 수가 들어 올 경우 2를 바라보도록 분리집합을 활용했다.
  - 1,2,5번 게이트가 도킹 안되어 있고 3,4,6,7번 게이트가 도킹되었는데 6~7번의 비행기가 들어온다면 5를 가리키도록 작업해야한다. 



- parents 배열과 visit 배열을 활용했다.
- parents을 통해 게이트를 연속시켜주었다.
  - 예를들어 현재 2,3,4 번 게이트가 모두 도킹되어 있다면 parent 2부터 4까지 모두 1이라는 숫자로 저장되어 있으며, visit 2부터 4까지도 모두 1로 저장되어 있다. 이 상황에서 4라는 숫자가 다시들어온다면 parent[4]는 1을 가리키기 때문에 parent 1도 도킹되었음을 표시하고 visit도 변경한다. 만약 다음 비행기가 1~4 아무 숫자나 들어온다면 모두 도킹 되어있기 때문에 for문을 종료 시킨다.
  - 종료 로직은 1번 게이트가 도킹되었는데 1번 게이트 까지 서치할경우 0으로 연결시킨다. 0번에 도킹하려할 경우 강제 종료 한다.



```python
import sys
sys.stdin = open('10775.txt','r')
sys.setrecursionlimit(10**5)

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a,b):
    rootA = find(a)
    rootB = find(b)

    parents[rootB] = rootA

n = int(input())
m = int(input())

parents = [i for i in range(n+1)]
visit = [0] * (n+1)

flag = True
answer = 0

# 6에서 6 => 6
# 또 6에서 6 => 5
# 또 6에서 6 => 4

for _ in range(m):
    k = int(input())
    pk = find(k)
    if visit[pk] == 0:
        visit[pk] = 1
        if pk != 1:
            union(pk-1,k)
        else:
            union(pk,k)
    else:
        pk = pk-1
        if pk == 0:
            break
        visit[pk] = 1
        union(pk,k)

    answer += 1

print(answer)


```

![20211231_143033](20211231_143033.png)