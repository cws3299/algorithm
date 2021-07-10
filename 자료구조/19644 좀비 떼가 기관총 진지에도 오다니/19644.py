import sys
sys.stdin = open('19644.txt','r')
input = sys.stdin.readline

l = int(input())
n,m = map(int,input().split())
bombs = int(input())
arr = []
for _ in range(l):
    zombie = int(input())
    arr.append(zombie)

attacks = []

for a in range(n-1):
    attacks.append((a+1)*m)

for a in range(n-1,l):
    attacks.append(n*m)


# print(arr)
# print(attacks)

plus = 0
cnt = 0
answer = True
while cnt <l:
    if attacks[cnt]-plus >= arr[cnt]:
        pass
    else:
        if bombs > 0:
            bombs -= 1
            plus += m
        else:
            answer = False
            break

    cnt += 1

if answer == True:
    print('YES')
else:
    print('NO')