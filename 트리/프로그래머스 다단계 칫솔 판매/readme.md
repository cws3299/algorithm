[프로그래머스 : 다단계 칫솔 판매] (https://programmers.co.kr/learn/courses/30/lessons/77486#)



- 2021 - 07 -23에 해결한 문제



- 로직을 잘못짜서 굉장히 많은 시간동안 해맨 문제
- 정말 리얼 완전탐색 형식으로 아래에서 부터 center방향으로 10%씩 올려주면서 해결했다.
- 굉장히 오래 틀렸던 이유는
- `sam `이라는 사람이 `500원,600원`의 돈을 벌 경우 처음에는 이를 합쳐 1100원을 번 형식으로 구현했는데 이 경우 에러가 발생한다,. 500 , 600을 경우별로 나눠서 올려줘야한다.
  - 그 이유는 1100 일경우 990 - 99 - 10 - 1 이런형식으로 네단계 올라가지만
  - 500 / 450 - 45 - 5
  - 600 / 540 - 54 - 6 
  - 아래의 두 경우는 세단계 올라가며 각 단계의 합 또한 다르게 표현된다.



```python
import sys
sys.setrecursionlimit(10**5)
from collections import defaultdict

max_depth = 0

def solution(enroll, referral, seller, amount):
    global max_depth
    
    def dfs(now,dep):
        global max_depth
        
        if dep > max_depth:
            max_depth = dep
        
        for nxt in tree[now]:
            if visit[nxt] == 0:
                visit[nxt] = 1
                dep += 1
                depth[dep].append(nxt)
                parents[nxt] = now
                dfs(nxt,dep) 
                dep -= 1
        return
    
    def ten(pos,mo):

        now_money = mo
        if mo < 10:
            all_money[pos] += mo
            return
        else:
            ten_money = int(now_money/10)

            if ten_money < 1:
                return
            else:
                all_money[pos] += (mo-ten_money)
                money[parents[pos]].append(ten_money)
                return
    
    answer = []
    len_enroll = len(enroll)
    len_seller = len(seller)
    
    visit = defaultdict(int)
    tree = defaultdict(list)
    money = defaultdict(list)
    depth = defaultdict(list)
    parents = defaultdict(str)
    all_money = defaultdict(int)
    
    for k in range(len_enroll):
        if referral[k] == "-":
            tree["CENTER"].append(enroll[k])
        else:
            tree[referral[k]].append(enroll[k])
            
        visit[enroll[k]] = 0
        money[enroll[k]] = []
        all_money[enroll[k]] = 0
            
    for s in range(len_seller):
        money[seller[s]].append(amount[s]*100)
        
    visit["CENTER"] = 1
    dfs("CENTER",0)

    for depp in range(max_depth,0,-1):
        for noww in depth[depp]:
            for now in money[noww]:
                ten(noww,now)
            
    for member in enroll:
        answer.append(all_money[member])
        
        
    
    return answer
```

