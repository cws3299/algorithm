import sys
sys.stdin = open('17828.txt','r')
from copy import deepcopy
sys.setrecursionlimit(10**5)

def dfs(l,s):
    global n,x,answer,string,end_value

    # print(l,s)

    if s > x:
        return

    if l == n:
        if s == x:
            answer = True
            end_value = deepcopy(value)
        return
    
    for k in range(26,0,-1):
        l += 1
        s += k
        # string.append(chr(k+64))
        value[k-1] += 1
        if answer == None:
            dfs(l,s)
        value[k-1] -= 1
        l -= 1
        s -= k
        # string.pop()

    return


n,x = map(int, input().split())
answer = None
string = []
flag = False
value = [0]*26
end_value = []

t = 0
s = x // 26
if n-s < x-(26*s):
    flag = True
    for _ in range(s):
        value[25] += 1
        t += 1

if flag == True:
    if n * 26 >= x:
        dfs(t,s*26)
        answer = []

        for idx,val in enumerate(end_value):
            answer.append([idx,val])


        result = ''
        for lst in list(answer):
            idx = lst[0]
            val = lst[1]
            if val > 0:
                for _ in range(val):
                    result += chr(idx+65)

        print(result)
    else:
        print("!")

else:
    if n * 26 >= x:
        dfs(0,0)
        # print(end_value)
        answer = []

        for idx,val in enumerate(end_value):
            answer.append([idx,val])


        result = ''
        for lst in list(answer):
            idx = lst[0]
            val = lst[1]
            if val > 0:
                for _ in range(val):
                    result += chr(idx+65)

        print(result)
    else:
        print("!")


