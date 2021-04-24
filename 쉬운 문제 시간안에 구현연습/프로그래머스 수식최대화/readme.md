프로그래머스 - 수식최대화



- 실전에서 만나면 멘탈 갈렸을거 같은 구현문제.....



```python
from itertools import permutations
from copy import deepcopy

answer = 0

def calculation(per,temp):
    global answer
    
    # print(per,temp)
    tmp = deepcopy(temp)
    tmpp = deepcopy(temp)
    # print(per)
    for p in per:
        # print(p,tmp,tmpp)
        k = 0
        while True:
            # print(k,tmpp)
            flag = False
            if k < len(tmpp):
                # print('====')
                if tmp[k] == p:
                    # print('--------')
                    if p == '-':
                        t = int(tmp[k-1]) - int(tmp[k+1])
                        del tmp[k+1]
                        del tmp[k]
                        tmp[k-1] =  t
                        tmpp = deepcopy(tmp)
                        flag = True
                    if p == '+':
                        t = int(tmp[k-1]) + int(tmp[k+1])
                        del tmp[k+1]
                        del tmp[k]
                        tmp[k-1] =  t
                        tmpp = deepcopy(tmp)
                        flag = True
                    if p == '*':
                        t = int(tmp[k-1]) * int(tmp[k+1])
                        del tmp[k+1]
                        del tmp[k]
                        tmp[k-1] =  t
                        tmpp = deepcopy(tmp)
                        flag = True
                if flag == False:
                    k += 1
                else:
                    k = 0
            else:
                break
                
    if len(tmp) == 1:
        if abs(tmp[0]) > answer:
            answer = abs(tmp[0])
    # else:
    #     if tmp[1] == '-':
    #         answer = abs(int(tmp[0]) - int(tmp[2]))
    #     if tmp[1] == '*':
    #         answer = abs(int(tmp[0]) * int(tmp[2])) 
    #     if tmp[1] == '+':
    #         answer = abs(int(tmp[0]) + int(tmp[2])) 
                
    # print(tmp,'---')
                    
                    

def solution(expression):
    global answer
    
    giho = set()
    for e in expression:
        if e == '-':
            giho.add(e)
        if e == '+':
            giho.add(e)
        if e == '*':
            giho.add(e)
    perm = list(permutations(giho,len(giho)))
    
    # print(perm)
    
    temp = []
    ll = len(expression)
    
    number = ''
    for k in range(ll):
        if expression[k] != '-' and expression[k] != '*' and expression[k] != '+' and k != ll-1:
            number += expression[k]
        elif k == ll-1:
            number += expression[k]
            temp.append(number)
        else:
            if len(number) != 0:
                temp.append(number)
            number = ''
            temp.append(expression[k])
            
    for per in perm:
        calculation(per,temp)
    
    return answer
```

