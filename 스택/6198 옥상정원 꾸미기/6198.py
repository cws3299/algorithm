import sys
sys.stdin = open('6198.txt','r')
from collections import deque

n = int(input())

stack = deque()

answer = 0

for _ in range(n):
    new = int(input())
    # print(new)
    if len(stack) == 0:
        stack.append(new)
    else:
        ll = len(stack)
        # if ll == 1:
        #     ll = 2
        for k in range(ll-1,-1,-1):
            if stack[k] <= new:
                stack.pop()
                if len(stack) == 0:
                    stack.append(new)
            else:
                # print(stack)
                answer+=len(stack)
                stack.append(new)
                break
    
    # print('----',stack)


print(answer)
