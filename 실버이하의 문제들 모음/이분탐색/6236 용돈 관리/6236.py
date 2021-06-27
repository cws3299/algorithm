import sys
sys.stdin = open('6236.txt','r')

def check():
    global mid

    money = 0
    res = 0
    for data in datas:
        if mid < data:
            return 10000000
        
        if money >=data:
            money -= data
        else:
            money = mid-data
            res += 1
    
    return res

n,m = map(int,input().split())
datas = []
for _ in range(n):
    data = int(input())
    datas.append(data)

low = 0
high = 10000000
answer = 10000000

while low <= high:
    mid = (low+high) // 2
    result = check()
    if result > m:
        low = mid +1 
    else:
        answer = min(answer,mid)
        high = mid-1


print(answer)
