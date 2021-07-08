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