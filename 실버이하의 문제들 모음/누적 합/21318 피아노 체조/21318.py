import sys
sys.stdin = open('21318.txt','r')
input = sys.stdin.readline

def _sum():
    global n,arr,brr

    cnt = 1
    fail = 0
    while cnt < n:
        if arr[cnt] > arr[cnt+1]:
            fail += 1
            brr[cnt] = fail
        else:
            brr[cnt] = fail
        
        cnt += 1

    return

n = int(input())
arr = [float('inf')] + list(map(int,input().split()))
brr = [0]*(n+1)

_sum()

m = int(input())
for _ in range(m):
    s,e = map(int, input().split())
    print(brr[e-1]-brr[s-1])