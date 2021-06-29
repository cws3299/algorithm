import sys
sys.stdin = open('20438.txt','r')

def send(message):
    global n,k,q,m,students,sleeps

    cnt = message
    while cnt<=n:
        if sleeps[cnt] == 0:
            students[cnt] = 1
        cnt += message

    return


n,k,q,m = map(int,input().split())
n += 2
students = [0]*(n+1)
sleeps = [0]*(n+1)
in_sleep = list(map(int, input().split()))

for i in in_sleep:
    sleeps[i] = 1

messages = list(map(int, input().split()))
messages.sort()


temp = set()
for mm in range(len(messages)-1,-1,-1):
    num = messages[mm]
    flag = False
    for message in messages:
        if num != message:
            if num % message == 0:
                flag = True
                break
    if flag == False:
        temp.add(num)          

for message in temp:
    if sleeps[message] != 1 and students[message] == 0:
        send(message)



answer = [0]*(n+1)

c = 3
cc = 0
while c<n+1:
    if students[c] ==0:
        cc += 1
        answer[c] = cc
    else:
        answer[c] = cc

    c += 1
# print(answer)
for k in range(m):
    s,e = map(int, input().split())
    print(answer[e]-answer[s-1])
