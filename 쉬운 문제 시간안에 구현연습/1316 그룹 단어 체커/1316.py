import sys
sys.stdin = open('1316.txt','r')
from copy import deepcopy

### 2021.04.24 pm 4:27 시작 pm 4:53 완료 -> 26분 소요


t = int(input())
answer = deepcopy(t)
for _ in range(t):
    string = input()

    visit = [0]*26

    ll = len(string)
    cnt = 0
    # print('---------------------------------',string,ll,visit)
    while cnt < ll:
        # print(cnt,answer)
        word = string[cnt]
        if visit[ord(word)-97] == 0 :
            visit[ord(word)-97] = 1
            cnt += 1
            if cnt < ll:
                while cnt < ll:
                    if string[cnt] == word:
                        cnt += 1
                    else:
                        break
        else:
            answer -= 1
            break


print(answer)
            
