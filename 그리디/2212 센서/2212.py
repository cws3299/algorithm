import sys
sys.stdin = open('2212.txt','r')

n = int(input())
k = int(input())
arr = list(map(int,input().split()))

arr.sort()

start = arr[0]
end = arr[-1]
length = end-start+1

print(length)