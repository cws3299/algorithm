[ 백준 : 북쪽나라의 도로 ] (https://www.acmicpc.net/problem/1595)



- 일반적인 트리의 지름 문제이다

- 너무 쉽다

- ```python
  import sys
  sys.stdin = open('1595.txt','r')
  input = sys.stdin.readline
  sys.setrecursionlimit(10**5)
  
  def dfs1(now,distance):
      global roads, visit, first_destination, first_distance
  
      if distance > first_distance:
          first_destination = now
          first_distance = distance
  
      for nxt, wt in roads[now].items():
          if visit[nxt] == 0:
              visit[nxt] = 1
              distance += wt
              dfs1(nxt,distance)
              distance -= wt
              visit[nxt] = 0
  
      return
  
  
  def dfs2(now,distance):
      global roads, visit, answer_destination, answer_distacne
  
      if distance > answer_distacne:
          answer_destination = now
          answer_distacne = distance
  
      for nxt, wt in roads[now].items():
          if visit[nxt] == 0:
              visit[nxt] = 1
              distance += wt
              dfs2(nxt,distance)
              distance -= wt
              visit[nxt] = 0
  
      return
  
  
  roads = {i:{} for i in range(10001)}
  
  village = 0
  while True:
      try:
          a,b,w = map(int,input().split())
          roads[a][b] = w
          roads[b][a] = w
          village += 1
      except:
          break
  
  visit = [0]*10001
  
  first_destination = 0
  first_distance = 0
  
  visit[1] = 1
  dfs1(1,0)
  
  visit = [0]*10001
  answer_destination = 0
  answer_distacne = 0
  
  dfs2(first_destination,0)
  
  
  if village <=1:
      print(0)
  else:
      print(answer_distacne)
  ```

  ![20211015_174852](20211015_174852.png)