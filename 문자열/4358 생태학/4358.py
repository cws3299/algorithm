import sys
sys.stdin = open('4358.txt','r')
from collections import defaultdict

_dict = defaultdict(dict)

total_set = set()
total = 0

while True:
    try:
        tree = input()
        list_tree = list(tree)
        length = len(tree)
        head = list_tree[0]

        if len(_dict[head]) == 0:
            _dict[head] = defaultdict(dict)
        if len(_dict[head][length]) == 0:
            _dict[head][length] = defaultdict(dict)
            _dict[head][length][tree] = 0
        else:
            if _dict[head][length][tree] == {}:
                _dict[head][length][tree] = 0

        _dict[head][length][tree] += 1

        total_set.add(tree)
        total += 1

    except:
        break


total_set = list(total_set)

total_set.sort()

for t in total_set:
    print(t, end= ' ')
    head = t[0]
    length = len(t)
    percent = _dict[head][length][t]/total
    percent *= 100
    percent = round(percent,4)
    # print(round(percent,4))
    print("{:.4f}".format(percent))

    
