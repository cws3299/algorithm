[백준 : 압축] (https://www.acmicpc.net/problem/1662)



- 되게 풀기 힘들었던 문제..... 반례가 너무 많았다.



```python
import sys
sys.stdin = open('1662.txt','r')
from collections import deque
sys.setrecursionlimit(10**5)
from copy import deepcopy

def dfs(k,total_m,m):
    global string,answer,ll,final,flag,p,tt

    if k == ll:
        final = deepcopy(answer)
        return

    # print(string[k],answer,total_m)
    
    if string[k] == '(':
        if string[k-1] == '0':
            p.append(int(string[k-1]))
            tt += 1
        else:
            total_m *= int(string[k-1])
            m = int(string[k-1])
            p.append(m)
    elif string[k] == ')':
        kk = p.pop()
        # print(kk)
        if kk == 0:
            tt -= 1
            pass
        else:
            total_m //= kk
    elif string[k] != '(' and string[k] != ')' and  tt == 0:
        if k < ll-1:
            if string[k+1] != '(':
            # print(string[k],total_m)
                answer += total_m
        elif k == ll-1:
            answer += total_m

        


    dfs(k+1,total_m,m)    

string = list(input())

final = 0
answer = 0
tt = 0
ll = len(string)
p = []

flag = False
dfs(0,1,1)

print(int(answer))
```

![20210501_210242](C:\Users\cws89\Documents\algorithm\dfs\1662 압축\20210501_210242.png)