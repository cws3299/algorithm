import sys
sys.stdin = open('2493.txt','r')

n = int(input())
arr = list(map(int,input().split()))

stack = []
idx_stack = []
answer = []

idx = 0
while True:
    h = arr[idx]
    if stack == []:
        stack.append(h)
        idx_stack.append(idx)
        answer.append(-1)
    else:
        if stack and h >stack[-1]:
            flag = True
            while stack and h > stack[-1]:
                stack.pop()
                idx_stack.pop()
                if stack == []:
                    stack.append(h)
                    idx_stack.append(idx)
                    answer.append(-1)
                    flag = False
                    break
            if flag == True:
                answer.append(idx_stack[-1])
                stack.append(h)
                idx_stack.append(idx)
        elif stack and h <= stack[-1]:
            answer.append(idx_stack[-1])
            stack.append(h)
            idx_stack.append(idx)


    idx += 1

    if idx == n:
        break

for ans in answer:
    print(ans+1, end= ' ')