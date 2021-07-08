[백준 : n과m(1)] (https://www.acmicpc.net/problem/15649)



- python으로 먼저 푼 후 js로 이식한 첫 번째 알고리즘!!!!!

- 구조분해할당을 활용하면 보다 쉽게 풀 수 있다는 힌트 또한 얻었기 때문에 자고 일어나서는 구조 

  분해 할당을 공부해봐야겠다.

- 자바스크립트의 블록을 조심하자!!!!!!





```python
import sys
sys.stdin = open('15649.txt','r')

def dfs(now):
    global n,m,visit,arr

    if now == m:
        for a in arr:
            print(a, end = ' ')
        print()
        return


    for nxt in range(1,n+1):
        if visit[nxt] == 0:
            visit[nxt] = 1
            now += 1
            arr.append(nxt)
            dfs(now)
            arr.pop()
            now -= 1
            visit[nxt] = 0

    return


n,m = map(int, input().split())
visit = [0]*(n+1)
arr = []

dfs(0)
```

```javascript
const fs = require('fs');
const input = fs.readFileSync('15649.txt').toString().split(' ')

const N = Number(input[0]);
const M = Number(input[1]);

const visited = new Array(N+1);

for (let i=0; i<=N; i++){
    visited[i] = false
}

let output = [];

function print() {
  console.log(output.join(' '));
}

function dfs(cnt) {
  if (cnt === M) {
    print();
    return;
  }

  for (let i = 1; i <= N; i++) {
    if (visited[i] === false){
        visited[i] = true;
        output.push(i);
        cnt += 1
        dfs(cnt);
        cnt -= 1
        output.pop();
        visited[i] = false;
        }
    }
}

dfs(0);
```

