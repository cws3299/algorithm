import sys
sys.stdin = open('1107.txt','r')
from collections import deque
from itertools import *

target = int(input())
n = int(input())
visit = [0]*(1000001)

if n>0:
    lstt = list(map(int ,input().split()))
lst = []

for k in range(10):
    if n>0:
        if k not in lstt:
            lst.append(k)
    else:
        lst.append(k)

# q = deque()
# q.append([0,100])

start = 100000000
len_start = 1000000
compare = 1000000000000
answer = 1000000000
ans_lst = []
a1 = list(product(lst , repeat=1))
a2 = list(product(lst , repeat=2))
a3 = list(product(lst , repeat=3))
a4 = list(product(lst , repeat=4))
a5 = list(product(lst , repeat=5))
a6 = list(product(lst , repeat=6))


ans_lst += a1
ans_lst += a2
ans_lst += a3
ans_lst += a4 
ans_lst += a5
ans_lst += a6

# print(ans_lst)
for a in ans_lst:
    number = ''
    for aa in a:
        number += str(aa)
    # print(number)
    if abs(int(number)) - abs(target) < abs(compare):
        # print('---', int(number))
        # len_start = len(number)
        start = int(number)
        compare = abs(int(number)) - abs(target)
        if abs(compare) + len(number) < answer:
            answer = abs(compare) + len(number)

if abs(abs(100) - abs(target)) < answer:
    answer = abs(abs(100) - abs(target))


print(answer)

