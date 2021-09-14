import sys
sys.stdin = open('3430.txt','r')

t = int(input())
for tc in range(t):
    n,m = map(int,input().split())

    pools = [0] + [1]*n
    skys = list(map(int, input().split()))
    eat_list = []
    eat = 0
    flag = True
    for k in range(m-1):
        if k == 0:
            eat += 1
            if skys[k] == skys[k+1]:
                flag = False
                break
            eat_list.append(skys[k])
        else:
            if pools[skys[k]] == 0:
                if eat > 0:
                    eat -= 1
                    eat_list.append(skys[k])
                    pass
                else:
                    pools[skys[k]] = 1
            elif pools[skys[k]] == 1:
                if eat > 0:
                    eat -= 1
                    eat_list.append(skys[k])
                    pass
                else:
                    flag = False
                    break
    
    if flag == False:
        print('NO')
    else:
        print(eat_list)