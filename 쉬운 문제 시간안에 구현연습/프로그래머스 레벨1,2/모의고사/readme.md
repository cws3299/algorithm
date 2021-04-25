[프로그래머스 : 모의고사] 



##### 나의 코드

```python
def solution(answers):
    answer = []
    ll = len(answers)
    
    
    one = 0
    two = 0
    three = 0
    
    ones = [0]*ll
    twos = [0]*ll
    threes = [0]*ll
    
    cnt = 0
    while cnt < ll:
        if cnt % 5 == 0:
            ones[cnt] = 1
        elif cnt % 5 == 1:
            ones[cnt] = 2
        elif cnt % 5 == 2:
            ones[cnt] = 3
        elif cnt % 5 == 3:
            ones[cnt] = 4
        elif cnt % 5 == 4:
            ones[cnt] = 5
            
        cnt += 1
    
    t = [2,1,2,3,2,4,2,5]
    cnt = 0
    while cnt < ll:
        c = cnt%8
        twos[cnt] = t[c]
            
        cnt += 1
        
    th = [3,3,1,1,2,2,4,4,5,5]
    cnt = 0
    while cnt < ll:
        c = cnt%10
        threes[cnt] = th[c]
            
        cnt += 1
        

    for k in range(ll):
        if answers[k] == ones[k]:
            one += 1
        if answers[k] == twos[k]:
            two += 1
        if answers[k] == threes[k]:
            three += 1
    
    _max = max([one,two,three])
    
    if _max == one:
        answer.append(1)
    if _max == two:
        answer.append(2)
    if _max == three:
        answer.append(3)
    
    return answer
```



##### 다른사람의 코드

```python
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
```

`enumerate`를 활용한 풀이방법인데 뭔가 한 수 배운거 같다.





##### 다른사람의 풀이2

```python
from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]
```

cycle이라는 함수랑 next라는 함수 처음알았다.....