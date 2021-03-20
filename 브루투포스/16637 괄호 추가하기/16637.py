import sys
sys.stdin = open('16637.txt','r')

n = int(input())
arr = list(input())
answer = None

for i in range(0,len(arr),2):
    arr[i] = int(arr[i])

m = (n-1)//2

for k in range(1<<m):

    ok = True
    for s in range(m-1):
        if (k&(1<<s)) > 0 and (k&(1<<(s+1))) >0:
            ok = False

    if ok == False:
        continue

    brr = arr[:]
    for s in range(m):
        if (k&(1<<s)) > 0:
            mm = 2*s+1
            if brr[mm] == '+':
                brr[mm-1] += brr[mm+1]
                brr[mm+1] = 0
            if brr[mm] == '*':
                brr[mm-1] *= brr[mm+1]
                brr[mm] = '+'
                brr[mm+1] = 0
            if brr[mm] == '-':
                brr[mm-1] -= brr[mm+1]
                brr[mm] = '+'
                brr[mm+1] = 0
    temp = brr[0]
    for s in range(m):
        mm = 2*s+1
        if brr[mm] == '+':
            temp += brr[mm+1]
        if brr[mm] == '-':
            temp -= brr[mm+1]
        if brr[mm] == '*':
            temp *= brr[mm+1]

    # print(temp)

    if answer is None:
        answer = temp
    if answer < temp:
        answer = temp

print(answer)
