#### 정렬 알고리즘에 대한 공부

###### 기존에 나는 정렬을 사용할 때, sort와 sorted라는 내장 함수와 같은 기능만을 주로 사용해서 정렬을 실제로 구현하는 알고리즘에 대해서는 부족한 지식을 갖추고 있었다. 오늘 python으로 정렬 알고리즘을 실제로 구현하는 연습을 해보고자 한다.



2021.03.14





래퍼런스

(http://ejklike.github.io/2017/03/04/sorting-algorithms-with-python.html)

(https://potensj.tistory.com/33)

(https://ordo.tistory.com/87)

(https://www.daleseo.com/sort-quick/)



### 1. 버블정렬

- 단순하고 쉽지만 상대적으로 느린 시간복잡도를 갖고 있는 알고리즘 O(N^2)
- 인접한 두 원소를 비교하면서 지속적으로 바꿔주면서 정렬을 함
- 큰 값을 오른쪽으로 계속 이동시키며 비교한 값들 중 최대값이 맨 오른쪽으로 옮겨진다

```python
def bubbleSort(lst):
    for size in reversed(range(len(lst))):
        for i in range(size):
            if lst[i] > lst[i+1]:
           		lst[i],lst[i+1] = lst[i+1],lst[i]
```

-  여러 블로그 글을 봤지만 이 코드가 가장 괜찮은 버블 정렬의 코드인 것 같다.
  - 처음에 reversed를 해주가 처음에는 이해가 안갔는데 손코딩을 하다보니 이해가 갔다.
  - [2,7,3,1,5]의 배열이 있는 경우
  - size 4가 진행 후 [ 2,3,1,5,  ///7 ]
  - size 3이 실행 후 [ 2,1,3    ////5 ]
  - size 2가 실행 후 [1,2, ////// 3]
  - size 1이 실행 후 [ 1 ///// 2]
  - 결국 [1,2,3,5,7]이 정렬됨



### 2. 선택정렬

- 주어진 배열에서 최댓값을 찾아 맨 오른쪽으로 교체한다. 
- 최솟값을 기준으로 할 경우에는 왼쪽으로 교체한다.
- 시간 복잡도는 O(n^2)이다.

```python
def selectionSort(x):
    for size in reversed(range(len(x))):
        max_i = 0
        for i in range(1, 1+size):
            if x[i] > x[max_i]:
                max_i = i
        x[max_i],x[size] = x[size],x[max_i]
```

- 버블정렬보다 조금 이해하기가 더 어려웠다.
- 그런데 이해하고 나니 생각보다 단순한 알고리즘이였다.
- 버블정렬이 모든 좌우를 비교한다면 선택정렬은 좌우비교가 아니라 그냥 맨 큰 값을 오른쪽으로 계속 보내주는 알고리즘이다.



### 3. 삽입정렬

- 아직 정렬 되지 않은 값을 이미 정렬된 배열 사이에 끼워 넣는 과정을 반복한다.
- 시간복잡도는 O(n^2)이지만 일반적으로 버블정렬과 선택정렬에 비해 빠르다.

```python
def insertionSort(x):
    for size in range(1, len(x)):
        val = x[size]
        i = size
        while i > 0 and x[i-1] > val:
            x[i] = x[i-1]
            i -= 1
        x[i] = val
```

- 삽입정렬은 이해하기가 더욱 빡셌다.
- 그러나 역시 해답은 뭐다? 손코딩!!!
- [2,7,3,1,6]의 숫자가 있는경우
- val - 7 , i =1 부터 val - 6 , i = 4까지 오른쪽으로 이동한다.
  - 각 상황에서는 다시 왼쪽으로 정렬을 시작한다.



### 4. 병합정렬

- 약간 신기한 정렬 기법
- 분할정복의 과정을 통해 정렬을 하고자 하는 배열을 끝까지 나눈 후 다시 재배치 과정을 실행한다.

```python
def merge_sort(lst):
    if len(lst)<= 1:
        return lst
    mid = len(lst) //2 
    left = lst[:mid]
    right = lst[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)
    return merge(left1,right1)



def merge(left,right):
    r = 0
    l = 0 
    result = []
    
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
            
    while l<len(left):
        result.append(left[l])
        l += 1
        
    while r<len(right):
        result.append(right[r])
        r += 1
        
   return result
        
        
```



### 5.퀵정렬

- 병합정렬과 마찬가지로 분할정복과 재귀 알고리즘을 이용한 정렬 방법이다.
- 퀵 정렬은 pivot이라고 불리는 임의의 기준값을 사용한다.
- pivot을 중심으로 pivot보다 작은 값들은 왼쪽으로 , pivot보다 큰 값들은 오른쪽으로 이동시킨다.

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)
```

위의 퀵 정렬은 쉽게 이해가 갔다. 그러나 블로그 글을 보던중 위의 퀵 정렬은 메모리 사용에서 비효율적이라 in-place정렬이 선호된다고 하시면서 코드를 작성해 놓은 걸 봤는데..... 멘붕!!!!

이해가 될랑 말랑 한다...... 복습해야지



### 심화 퀵정렬 in-place

```python
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid - 1)
        sort(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low

    return sort(0, len(arr) - 1)
```

