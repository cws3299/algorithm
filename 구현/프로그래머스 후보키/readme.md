[프로그래머스 : 후보키] (https://programmers.co.kr/learn/courses/30/lessons/42890)



- 조합을 활용해서 풀었다.

- 첫번째 조합은 후보키를 만들 수 있는 모든 케이스를 출력
- 두번째 조합은 찾아낸 모든 케이스중 최소성을 만족하는 케이스를 찾아내 출력



```python
from itertools import combinations

def solution(relation):
    
    def confirm(com):
        compare = set()
        
        # print(com)
        for r in relation:
            ar = []
            for c in com:
                # print(r,c)
                # print(r[c])
                ar.append(r[c])
            ar = tuple(ar)
            compare.add(ar)
        if len(compare) == al:
            return True
        else:
            return False
                
                
            
        
    
    al =len(relation)
    combi = []
    l = len(relation[0])
    arr = [i for i in range(l)]
    lst = []
    for k in range(1,l+1):
        s = list(combinations(arr, k))
        combi += s
    for com in combi:
        result = confirm(com)
        if result == True:
            lst.append(com)
        
    answer = []

    
    for ls in lst:
        if len(ls) == 1:
            answer.append(ls)
        else:
            l = len(ls)
            com = []
            for k in range(1,l+1):
                lstt = list(combinations(ls,k))
                com += lstt
            # print(com)
            # com = com[:-1]
            com.sort()

            m = len(com)
            k = 0
            for c in com:
                for a in answer:
                    if c == a:
                        k += 1

            if k == 0:
                answer.append(ls)
    

    return len(answer)
```

