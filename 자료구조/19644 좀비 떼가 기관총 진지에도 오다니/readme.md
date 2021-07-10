[백준 : 좀비 떼가 기관총 진지에도 오다니] (https://www.acmicpc.net/problem/19644)



- 생각보다 시간초과가 안나고 한 번에 풀려서 기분이 좋았던 문제

- zombie의 체력을 나타내는 arr
- 좀비에게 기관총만 쐈을때 피해를 입힐 수 있는 양을 나타내는 attacks
- 폭탄을 쓰는경우 좀비에게 총을 못쏘니 폭탄 쏜 개수 * 폭탄 데미지를 의미하는 plus 만큼 while문 안에서 값을 구해줄 때 빼준다.



```python
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
```

![20210710_185527](20210710_185527.png)