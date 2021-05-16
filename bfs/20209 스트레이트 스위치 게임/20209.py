import sys
sys.stdin = open('20209.txt','r')
from collections import deque
from copy import deepcopy

def confirm(dice):

    dice2 = dice[1:]
    for k in range(len(dice2)-1):
        if dice2[k] != dice2[k+1]:
            return False

    return True

def bfs(dice):
    global n,m,visit,button,visit,answer

    q = deque()
    q.append([dice,0])
    visit.add(tuple(dice))

    while q:
        di,move = q.popleft()
        result = confirm(di)
        if result == True:
            answer = move
            break
        
        for a in range(1,m+1):
            tmp = deepcopy(di)
            for aa in button[a]:
                tmp[aa] += a
                if tmp[aa] > 4:
                    tmp[aa] = tmp[aa]%5
            ll = len(visit)
            visit.add(tuple(tmp))
            ll2 = len(visit)
            if ll != ll2:
                q.append([tmp,move+1])

            

n,m = map(int, input().split())
visit = set()
dices = [0] + list(map(int , input().split()))
button = [[] for _ in range(m+1)]
for k in range(1,m+1):
    lst = list(map(int , input().split()))
    if lst[0] == 0:
        pass
    else:
        lst = lst[1:]
        for s in range(len(lst)):
            button[k].append(lst[s])

answer = None
bfs(dices)

# print(button)

if answer == None:
    print(-1)
else:
    print(answer)