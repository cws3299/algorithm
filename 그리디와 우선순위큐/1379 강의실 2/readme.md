[강의실 2] (https://www.acmicpc.net/problem/1379)



- 이 문제 예제가 틀렸는데 아무리 생각해도 제대로 한거 같아서 돌려보니 정답으로 나옴.......

- 뭐지 이거......

- ```python
  import sys
  sys.stdin = open('1379.txt','r')
  import heapq
  
  n = int(input())
  pq = []
  
  for _ in range(n):
      c,s,e = map(int, input().split())
      heapq.heappush(pq,[s,e,c])
  
  tq = []
  rooms = [-1] + [0]*(n)
  answer = 0
  answer_lst = [-1]*(n+1)
  
  
  while pq:
      start,end,cla = heapq.heappop(pq)
  
      while tq and tq[0][0] <= start:
          ed , cl , ss = heapq.heappop(tq)
          rooms[ss] = 0
  
      sss = rooms.index(0)
  
      if sss > answer:
          answer = sss
  
      rooms[sss] = 1
      # print(start,end,cla,sss)
      answer_lst[cla] = sss
  
      heapq.heappush(tq,[end,cla,sss])
  
  # print(answer_lst)
  # print(answer)
  
  # print('-------------------------------------------')
  # print(answer_lst)
  print(answer)
  for ans in answer_lst[1:]:
      print(ans)
  ```

  ![20210614_024111](20210614_024111.png)