[프로그래머스 : 다리를 지나는 트럭]



- 생각보다 애를 많이 먹은문제다.
- heapq를 사용해서 겨우 풀었다.



```python
import heapq

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truck_weights.reverse()
    ss = len(truck_weights)
    
    now_weight = 0
    time = 1
    
    pq = []
    end = 0
    
    while True:
        
        
        while len(pq) > 0 and pq[0][0] <= time:
            t,o = heapq.heappop(pq)
            now_weight -= o
            end += 1
            
        if end == ss:
            break
            
        if len(truck_weights) > 0:
            out = truck_weights.pop()
            if now_weight + out <= weight:
                heapq.heappush(pq,[time+bridge_length,out])
                now_weight += out
            else:
                truck_weights.append(out)
            
        time += 1
        
        
            
            
    
    return time
```

