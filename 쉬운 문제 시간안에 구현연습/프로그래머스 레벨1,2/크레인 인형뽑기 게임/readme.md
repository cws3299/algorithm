[크레인 인형뽑기 게임] 



- 10분정도 걸린거 같다.
- 진짜 정말 열심히 해야지

```python
from collections import deque

def solution(board, moves):
    answer = 0
    ll = len(board)
    stack = deque()
    
    move = deque()
    for mo in moves:
        move.append(mo-1)
        
    while move:
        out = move.popleft()
        # print(out,stack)
        
        for depth in range(ll):
            if board[depth][out] != 0:
                stack.append(board[depth][out])
                board[depth][out] = 0
                break
                
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2
                
    # print('------')
    # print(answer)
    # print(move)
    return answer
```

