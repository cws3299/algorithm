import sys
sys.stdin = open('14888.txt','r')
from copy import deepcopy
import math
sys.setrecursionlimit(10**5)

def dfs(pos,val):
    global n , arr ,visit , answer


    if pos == n-1:
        answer.add(val)
        return
    
    for k in range(4):
        if k == 0:
            if visit[0] > 0:
                visit[0] -= 1
                pos += 1
                val += arr[pos]
                dfs(pos,val)
                val -= arr[pos]
                pos -= 1
                visit[0] += 1
        if k == 1:
            if visit[1] > 0:
                visit[1] -= 1
                pos += 1
                val -= arr[pos]
                dfs(pos,val)
                val += arr[pos]
                pos -= 1
                visit[1] += 1
        if k == 2:
            if visit[2] > 0:
                visit[2] -= 1
                pos += 1
                copy_val=deepcopy(val)
                val *= arr[pos]
                dfs(pos,val)
                val = copy_val
                pos -= 1
                visit[2] += 1
        if k == 3:
            if visit[3] > 0:
                visit[3] -= 1
                pos += 1
                if val >= 0:
                    copy_val=deepcopy(val)
                    val //= arr[pos]
                    dfs(pos,val)
                    val = copy_val
                else:
                    copy_val = deepcopy(val)
                    copy_val = -copy_val
                    copy_val //= arr[pos]
                    copy_val = -copy_val
                    dfs(pos,copy_val)
                    val = copy_val
                    # if abs(copy_val) <= abs(arr[pos]):
                    #     val = 0
                    # else:
                    #     val = math.trunc(copy_val / arr[pos])
                    #     dfs(pos,val)
                    #     val = copy_val
                pos -= 1
                visit[3] += 1

    return


n = int(input())
arr = list(map(int, input().split()))
visit = list(map(int, input().split()))
answer = set()

dfs(0,arr[0])


print(max(answer))
print(min(answer))