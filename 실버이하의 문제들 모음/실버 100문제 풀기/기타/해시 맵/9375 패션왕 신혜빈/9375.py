import sys
sys.stdin = open('9375.txt','r')
from collections import defaultdict

t = int(input())
for tc in range(t):
    n = int(input())
    _dict = defaultdict(int)

    for _ in range(n):
        a,b = map(str, input().split())
        _dict[b] += 1

    answer = 1

    for nxt ,wt in _dict.items():
        answer *= (wt+1)

    print(answer-1)
