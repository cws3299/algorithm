import sys
sys.stdin = open('16472.txt','r')
from collections import deque

n = int(input())
arr = list(input())
l = len(arr)-1


start = 0
end = 0
answer = 0

brr = [0]*26
brr[ord(arr[end])-97] += 1

while start != l:

    s = brr.count(0)
    ss = 26 - s
    # print(start,end,answer,ss)

    if ss <= n:
        if end < l:
            brr[ord(arr[end+1])-97] += 1
            end += 1
            a = brr.count(0)
            aa = 26 - a
            # print(aa,n,start,end,answer)
            if aa <= n:
                if answer < end - start +1:
                    answer = end - start +1
            else:
                # print('==================================')
                brr[ord(arr[start])-97] -= 1
                start += 1

        else:
            brr[ord(arr[start])-97] -= 1
            start += 1
    else:
        if start<end:
            brr[ord(arr[start])-97] -= 1
            start += 1


    # ll = len(set(brr))
    # if ll <= n:
    #     if end < l:
    #         end += 1
    #         brr.append(arr[end])
    #         if answer < end-start:
    #             answer = end - start
    #     else:
    #         start += 1
    #         brr.popleft()
    # else:
    #     if start < end:
    #         start += 1
    #         brr.popleft()

print(answer)

        


        
