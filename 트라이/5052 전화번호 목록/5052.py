import sys
sys.stdin = open('5052.txt','r')

class Node(object):
    def __init__(self,key,data=None):
        self.key = key
        self.data = data
        self.child = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)


    def insert(self,string):
        curr_node = self.head

        nxt = 1
        for char in string:
            if char not in curr_node.child:
                curr_node.child[char] = Node(char)
                
            if curr_node.child[char].data != None and nxt == len(string):
                # print(string,nxt,curr_node.child[char].data)
                return False
            else:
                curr_node.child[char].data = string
            curr_node = curr_node.child[char]
            nxt += 1

        curr_node.data = string
        return True
        # if curr_node.data == None:
        #     curr_node.data = string
        # else:
        #     print('----',curr_node.data)

    def search(self,string):
        curr_node = self.head

        for char in string:
            if char in curr_node.child:
                curr_node = curr_node.child[char]
            else:
                return False
        
        if curr_node.data != None:
            return True

t = int(input())
for tc in range(t):
    trie = Trie()
    n = int(input())
    brr = []
    for _ in range(n):
        brr1 = input()
        # print(brr1)
        brr2 = brr1.replace(" ","")
        # print(brr2)
        brr1 = int(brr2)
        brr.append([brr1,brr2])
    brr.sort(key=lambda x:x[0])
    brr.reverse()
    arr = []
    for br in brr:
        b = str(br[1])
        arr.append(b)
    # print(arr)

    # arr.sort(key=lambda x:len(x))
    # arr.reverse()
    # print(arr)
    flag = False
    for ar in arr:
        ss= trie.insert(ar)
        if ss == False:
            flag = True
            print('NO')
            break
    if flag == False:
        print('YES')
    # flag = False
    # for ar in arr:
    #     s = trie.search(ar)
    #     if s == False:
    #         flag = True
    #         print('No')
    #         break
    # if flag == False:
    #     print('Yes')