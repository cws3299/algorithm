[프로그래머스 : 문자열 압축]





- 5시간이 걸렸다.... 나는 구현이 진짜 약한가부다.

```python
from copy import deepcopy

def solution(s):
    
    answer = len(s)
    lengths = len(s)
    string = deepcopy(s)
    
    for length in range(1,lengths):
        # print('--------------------------',length)
        lst = []
        if length > lengths//2:
            break
        for ll in range(0,lengths-length+1,length):
            lst.append(string[ll:ll+length])
            
        # print(lst,length)
        lll = len(lst)
        leng = deepcopy(lengths)
        number_lst = []
        
        now = None
        wt = 0
        for k in range(lll-1):
            if now == None:
                now = lst[k]
                
            if now == lst[k+1]:
                leng -= length
                now = lst[k+1]
                if wt == 0:
                    wt = 2
                else:
                    wt += 1
                    
                if k == lll-2:
                    number_lst.append(wt)
            else:
                now = lst[k+1]
                number_lst.append(wt)
                wt = 0
    
        amm = ''
        for num in number_lst:
            if num != 0:
                amm += str(num)
    
        # print(leng + len(amm))
        if leng + len(amm) < answer:
            answer = leng+len(amm)
#         print(leng,number_lst)
            
               
    return answer
```

