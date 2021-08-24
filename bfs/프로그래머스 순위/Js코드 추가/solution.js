class Deque{
    constructor(){
        this.data = []
        this.rear = 0;
    }

    push_front(item){
        this.data.unshift(item)
        this.rear++
    }
    push_back(item){
        this.data[this.rear] = item
        this.rear++
    }
    pop_front(){
        if (this.rear !== 0){
            this.rear--
            return this.data.shift()
        }
        return null
    }
    pop_back(){
        if (this.rear !== 0){
            this.rear--
            return this.data.pop()
        }
        return null
    }
}



function solution(n, results) {
    var answer = 0;
    
    const wins = Array.from(Array(n+1), () => new Array())
    const loses = Array.from(Array(n+1), () => new Array())
    
    function winBfs(i,end,wins){
        const q = new Deque()
        
        let cnt = 0
        const visit = new Array(end+1).fill(0)
        visit[i] = 1
        q.push_back(i)

        while (q.rear > 0){
            let now = q.pop_front()
            
            if (wins[now].length >0){
                wins[now].forEach(function(nxt){
                    if (visit[nxt] === 0){
                        visit[nxt] = 1
                        q.push_back(nxt)
                        cnt++
                    }
                })
            }
        }
        return cnt
    }

    function loseBfs(i,end,loses){
        const q = new Deque()
        
        let cnt = 0
        const visit = new Array(end+1).fill(0)
        visit[i] = 1
        q.push_back(i)
        
        while (q.rear>0){
            let now = q.pop_front()
            
            if (loses[now].length > 0){
                loses[now].forEach(function(nxt){
                    if (visit[nxt] === 0){
                        visit[nxt] = 1
                        q.push_back(nxt)
                        cnt++
                    }
                })
            }
        }
        return cnt
    }
    
    
    results.forEach(function(result){
        wins[result[0]].push(result[1])
        loses[result[1]].push(result[0])
    })
    

    
    for (let i = 1; i<n+1; i++ ){
        let win_cnt = winBfs(i,n,wins)
        let lose_cnt = loseBfs(i,n,loses)
        if (win_cnt + lose_cnt === n-1){
            answer++
        }
    }
    
    
    console.log(answer)
    return answer;
}

solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])