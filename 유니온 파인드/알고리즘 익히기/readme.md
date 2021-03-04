사실상 거의 잊고 있던 알고리즘인 유니온 파인드

기억이 전혀 안나서 인터넷 글을 보면서 공부를 했다. 조만간 유니온 파인드를 완벽하게 익힌 후

서로소 집합 문제를 풀어봐야 겠다





참고 자료

(https://velog.io/@woo0_hooo/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-union-find-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)



### <b>서로소란?</b>

-  공통 원소가 없는 두 집합
  - {1,2}, {3,4}는 서로소
  - {1,2}, {2,3}은 서로소가 아님



##### <b>Union - Find는 서로소 집합을 효율적으로 관리하기 위한 자료구조</b>

- <b>union</b>
  - 두 개의 집합을 하나의 집합으로 합치기
- <b>find</b>
  - 특정 원소가 속한 집합이 무엇인지 알려주는 연산



#### 동작 방법

1. union 연산
   - 서로 연결된 두 노드를 확인한다.
   - 1-1. A의 루트 노드 A'와 B의 루트 노드 B'를 찾는다. (find)
   - 1-2. A'를 B'의 부모 노드로 설정 -> 이 과정을 통해 B집합이 A집합의 아래로 들어가게 된다.
   - 2.  모든 union 연산을 처리할 때 까지 위의 과정을 반복



#### 구체적인 알고리즘 동작방법

1. 부모 테이블 초기화

   - 노드 개수 크기의 부모 테이블을 초기화 한다. 초기값은 자기 자신을 부모로 가지도록 설정한다.
     - ex . 노드번호  1 2 3 4 5 6
     - ​                부모 1 2 3 4 5 6

   - 각각의 union 연산을 확인한다. -> ex. union 1,4
     - 1과 4의 루트노드를 찾는다.
     - 각 루트노드는 1과4임을 알게되고 1이 4보다 작으므로 4의 루트 노드를 1로 변환



- 참고 소스코드

  ```oython
  # 특정 원소가 속한 집합을 찾기
  def find_parent(parent, x):
      # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
      
      1->2->3 # 루트 노드가 1인 경우
      ex. find_parent(parent,3) -> find_parent(parent,2) -> find_parent(parent,1) / 결과적으로 리턴값 순서 : 1(parent,1) ,1(parent,2) ,1(parent,3) => 1이 출력됨
      
      if parent[x] != x:
          return find_parent(parent, parent[x])
      return x
  
  # 두 원소가 속한 집합을 합치기
  def union_parent(parent, a, b):
      a = find_parent(parent, a)
      b = find_parent(parent, b)
      
      a집합과 b집합의 루트를 찾은 후 더 작은 값을 루트노드로 가진 값에 다른 집합을 합친다.
      
      if a < b:
          parent[b] = a
      else:
          parent[a] = b
  
  # 노드의 개수와 간선(Union 연산)의 개수 입력 받기
  v, e = map(int, input().split())
  parent = [0] * (v + 1) # 부모 테이블 초기화하기
  
  # 부모 테이블상에서, 부모를 자기 자신으로 초기화
  for i in range(1, v + 1):
      parent[i] = i
  
  # Union 연산을 각각 수행
  for i in range(e):
      a, b = map(int, input().split())
      union_parent(parent, a, b)
  
  # 각 원소가 속한 집합 출력하기
  print('각 원소가 속한 집합: ', end='')
  for i in range(1, v + 1):
      print(find_parent(parent, i), end=' ')
  
  print()
  
  # 부모 테이블 내용 출력하기
  print('부모 테이블: ', end='')
  for i in range(1, v + 1):
      print(parent[i], end=' ')
  ```

  

###### 위의 코드로 진행하는 경우 find 함수는 비효율적이다.

그래서 이를 해결하기 위해 find 함수를 살짝만 바꿔준다

- 변경하면서 부모값으로 리턴을 해주는 방식

```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]
```



### Union - Find를 활용하면 무방향 그래프 내에서 사이클 또한 판별할 수 있다.

- 서로 다른 두 노드( 같은 집합이 아닌)의 루트노드가 같을 경우 cycle 발생