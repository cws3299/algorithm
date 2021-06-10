[프로그래머스 : 보석 쇼핑] (https://programmers.co.kr/learn/courses/30/lessons/67258)



- 두포인터 사용 문제
- 정확성은 다 맞았지만 시간초과가 계속 발생했다.
- 이를 해결하기위해 길이를 체크하는 set과 dict를 while문 밖에 만들어주었다.
- 기존에는 `len(set(gems[left:right+1])) == ll` 이런식으로 한 번 비교할 때 마다 시간이 오래걸리는 방법을 사용했었다.

```python
from copy import deepcopy
from collections import defaultdict

def solution(gems):
    answer = []
    gems.insert(0,gems[0])
    ll = len(set(gems))
    ans = [[] for _ in range(len(gems)+1)]
    
    if ll == 1:
        answer = [1,1]
    else:
        left = 1
        right = 2
        gg = set()
        g_lst = defaultdict(int)
        g_lst[gems[1]] += 1
        g_lst[gems[2]] += 1
        gg.add(gems[1])
        gg.add(gems[2])

        while left<right or (left==1 and right==1):
            size = len(gg)
            if size == ll:
                diff = right-left+1
                ans[diff].append([left,right])
                g_lst[gems[left]] -= 1
                if g_lst[gems[left]] == 0:
                    gg.remove(gems[left])
                left += 1
                if diff == ll:
                    break
            elif size < ll:
                if right == len(gems)-1:
                    break
                else:
                    right += 1
                    gg.add(gems[right])
                    g_lst[gems[right]] += 1


        flag = True
        for an in ans:
            for a in an:
                answer = [a[0], a[1]]
                flag =  False
                break
            if flag == False:
                break
        
    
    return answer
```

