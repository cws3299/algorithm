import sys
sys.stdin = open('1581.txt','r')
sys.setrecursionlimit(10**5)

def dfs(ff1,fs1,sf1,ss1,cnt,now):
    global answer

    if cnt > answer:
        answer = cnt

    if now == 0:
        for k in range(2):
            if k == 0:
                if ff1 > 0:
                    cnt += 1
                    ff1 -= 1
                    dfs(ff1,fs1,sf1,ss1,cnt,0)
                    cnt -= 1
                    ff1 += 1
            elif k == 1:
                if fs1 > 0:
                    cnt += 1
                    fs1 -= 1
                    dfs(ff1,fs1,sf1,ss1,cnt,1)
                    cnt -= 1
                    fs1 += 1
    elif now == 1:
        for k in range(2):
            if k == 0:
                if sf1> 0:
                    cnt += 1
                    sf1 -= 1
                    dfs(ff1,fs1,sf1,ss1,cnt,2)
                    cnt -= 1
                    sf1 += 1
            elif k == 1:
                if ss1 > 0:
                    cnt += 1
                    ss1 -= 1
                    dfs(ff1,fs1,sf1,ss1,cnt,3)
                    cnt -= 1
                    ss1 += 1
    elif now == 2:
        for k in range(2):
            if k == 0:
                if ff1 > 0:
                    cnt += 1
                    ff1 -= 1
                    dfs(ff1,fs1,sf1,ss1,cnt,0)
                    cnt -= 1
                    ff1 += 1
            elif k == 1:
                if fs1 > 0:
                    cnt += 1
                    fs1 -= 1
                    dfs(ff1,fs1,sf1,ss1,cnt,1)
                    cnt -= 1
                    fs1 += 1
    elif now == 3:
        for k in range(2):
            if k == 0:
                if sf1> 0:
                    cnt += 1
                    sf1 -= 1
                    dfs(ff1,fs1,sf1,ss1,cnt,2)
                    cnt -= 1
                    sf1 += 1
            elif k == 1:
                if ss1 > 0:
                    cnt += 1
                    ss1 -= 1
                    dfs(ff1,fs1,sf1,ss1,cnt,3)
                    cnt -= 1
                    ss1 += 1





    return





ff,fs,sf,ss = map(int, input().split())

answer = 0

if ff == 0 and fs ==0:
    if sf == 0 and ss != 0:
        print(ss)
    elif sf != 0 and ss == 0:
        print(1)
    elif sf != 0 and ss != 0:
        print(ss+1)        
else:
    if ff >0:
        ll = min(fs,sf)-1
        if fs > 0 and sf > 0:
            dfs(0,fs-ll,sf-ll,0,(ll*2)+ff+ss,0)
        elif fs == 0 and sf >0:
            dfs(0,0,sf,ss,ff,0)
        elif sf == 0 and fs >0:
            dfs(0,fs,0,0,ff+ss,0)
        elif sf == 0 and fs ==0:
            dfs(0,0,0,0,ff,0)
    elif fs>0:
        ll = min(fs,sf)-1
        if  sf > 0:
            dfs(0,fs-ll-1,sf-ll,0,(ll*2)+1+ff+ss,1)
        elif sf == 0:
            dfs(0,fs-1,0,0,ff+ss+1,1)

    print(answer)