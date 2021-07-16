import sys
sys.stdin = open('9935.txt','r')
from collections import deque

arr = list(input())
arr = deque(arr)
bomb = list(input())
bomb = deque(bomb)
stack = deque()
ll = len(arr)
ls = len(bomb)
answer = ''

cnt = 0
l = 0
while cnt < ll:
    now = arr.popleft()
    stack.append(now)
    l += 1

    if  l>= ls:
        compare = deque()
        c = 0
        while c < ls:
            s = stack.pop()
            c += 1
            l -= 1
            compare.appendleft(s)

        if compare != bomb:
            stack += compare
            l += ls
    


    cnt += 1
    

if len(stack) == 0:
    print('FRULA')
else:
    for s in stack:
        sys.stdout.write(s)