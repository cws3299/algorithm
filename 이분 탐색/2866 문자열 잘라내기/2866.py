import sys
sys.stdin = open('2866.txt','r')

def confirm(mid):
    global n,m,arr

    lst = set()
    for x in range(m):
        string = ''
        for y in range(mid,n):
            string += arr[y][x]
        lst.add(string)

    if len(lst) == m:
        return True
    else:
        return False


n,m = map(int, input().split())
arr = []
for _ in range(n):
    ar = list(input())
    arr.append(ar)

left = 0
right = n-1
answer = None

while left <= right:
    mid = (left + right) // 2

    result = confirm(mid)
    if result == True:
        answer = mid
        left = mid +1
    else:
        right = mid - 1

print(answer)