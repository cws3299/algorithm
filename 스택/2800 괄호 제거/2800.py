import sys
sys.stdin = open('2800.txt','r')
sys.setrecursionlimit(10**5)
from collections import deque
from itertools import *
from copy import deepcopy


lstt = list(input())

lst = deque()
for ls in lstt:
    lst.append(ls)

delete_lst = []
left = deque()
answer= []

cnt = 0
while lst:
    now = lst.popleft()
    if now == '(':
        left.append(cnt)
    elif now == ')':
        k = left.pop()
        delete_lst.append([k,cnt])

    cnt += 1

ll = len(delete_lst)

lst1 = list(combinations(delete_lst,1))
lst2 = list(combinations(delete_lst,2))
lst3 = list(combinations(delete_lst,3))
lst4 = list(combinations(delete_lst,4))
lst5 = list(combinations(delete_lst,5))
lst6 = list(combinations(delete_lst,6))
lst7 = list(combinations(delete_lst,7))
lst8 = list(combinations(delete_lst,8))
lst9 = list(combinations(delete_lst,9))
lst10 = list(combinations(delete_lst,10))
a_lst = []
a_lst += lst1
a_lst += lst2
a_lst += lst3
a_lst += lst4
a_lst += lst5
a_lst += lst6
a_lst += lst7
a_lst += lst8
a_lst += lst9
a_lst += lst10


# print(a_lst)

while a_lst:
    k = a_lst.pop()
    delete = []
    for kk in k:
        for kkk in kk:
            delete.append(kkk)

    answer.append(delete)

# print(answer)

temp = deepcopy(lstt)
# print(temp)
answers = set()

string = ''
for ans in answer:
    for tmp in range(len(temp)):
        if tmp not in ans:
            string += temp[tmp]
    answers.add(string)
    string = ''

answers = list(answers)
answers.sort()
for ans in answers:
    print(ans)












    

