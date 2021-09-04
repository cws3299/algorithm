import sys
sys.stdin = open('15831.txt','r')

ll,b,w = map(int,input().split())
arr = ['S']+list(input())

start = 0
end = 0
black = 0
white = 0
answer = 0
final = 0

while True:

    if black<=b and white >=w:
        if final < answer:
            final = answer

    if end != ll:
        if arr[end+1] == 'W':
            end += 1
            white += 1
            if black <= b:
                answer += 1
        else:
            if black < b:
                end += 1
                black += 1
                if black <= b:
                    answer += 1
            else:
                if arr[start+1] == 'B':
                    start += 1
                    black -= 1
                    answer -= 1
                else:
                    start += 1
                    white -= 1
                    answer -= 1
    else:
        break
        
print(final)