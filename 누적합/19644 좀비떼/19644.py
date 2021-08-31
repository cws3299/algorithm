import sys
sys.stdin = open('19644.txt','r')
input = sys.stdin.readline
from collections import deque

n = int(input())
l,damage = map(int,input().split())
bomb = int(input())
zombie = [0]
for _ in range(n):
    a = int(input())
    zombie.append(a)

now = 0
# attacks = []*len(zombie)
answer = True
attacks = [0]
for k in range(1,l+1):
    attacks.append(k*damage)
for k in range(l+1,n+1):
    attacks.append(l*damage)

plus_list = deque()
plus = 0

for k in range(n):
    if len(plus_list) > 0:
        if k - plus_list[-1] >l:
            plus -= damage
            plus_list.popleft()

    if zombie[k+1] > attacks[k+1]-plus:
        if bomb <= 0:
            answer = False
            break
        else:
            bomb -= 1
            plus += damage
            plus_list.append(k)
            # if k+1+l >n:
            #     for nxt in range(k+2,n+1):
            #         attacks[nxt] -= damage
            # else:
            #     for nxt in range(k+2,k+l+1):
            #         attacks[nxt] -= damage

if answer == True:
    print('YES')
else:
    print('NO')
