import sys
sys.stdin = open('2841.txt','r')
from collections import deque
input = sys.stdin.readline

n , m = map(int, input().split())
stack = [[] for _ in range(7)]
answer = 0
ss = 0
arr = deque()

for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])


while arr:
    string , flat = arr.popleft()
    if stack[string] == [] or stack[string][-1] < flat:
        answer += 1
        stack[string].append(flat)
    elif stack[string][-1] == flat:
        pass
    else:
        while stack[string] and stack[string][-1] > flat:
            answer += 1
            stack[string].pop()
        if stack[string] == []:
            answer += 1
            stack[string].append(flat)
        elif stack[string] and stack[string][-1] <flat:
            answer += 1
            stack[string].append(flat)
        else:
            # answer += 1
            pass
    # print(flat,stack[string],answer)

print(answer)
    


    

