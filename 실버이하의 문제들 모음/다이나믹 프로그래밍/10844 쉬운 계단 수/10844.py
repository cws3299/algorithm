import sys
sys.stdin = open('10844.txt','r')
sys.setrecursionlimit(10**5)

n = int(input())
start = (10**(n-1))
end = (10**(n)) - 1

print(start,end)