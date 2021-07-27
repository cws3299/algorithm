import sys
sys.setrecursionlimit(100001)
sys.stdin = open('1038.txt','r')
from copy import deepcopy

def dfs(e):
    global n,answer,cnt,flag,stack

    if len(stack) == e:
        cnt += 1
        if cnt == n:
            answer = deepcopy(stack)
            flag = True
        if stack == [9,8,7,6,5,4,3,2,1,0]:
            flag = True
        if cnt == 1000000:
            True
        return

    for k in range(10):
        tmp = deepcopy(stack)
        if stack == []:
            stack.append(k)
        else:
            if k < stack[-1]:
                stack.append(k)
            else:
                return
        
        dfs(e)
        stack = deepcopy(tmp)

    return

n = int(input())
answer = -1
cnt = -1
flag = False
stack = []

while flag == False:

    for k in range(1,100):
        if flag == False:
            dfs(k)



if answer == -1 and flag == True:
    print(-1)
elif answer != -1 and flag == True:
    final = ''
    for a in answer:
        final += str(a)
    print(final)





