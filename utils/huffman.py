# import TernaryHeap
from heapq import heapify, heappush, heappop
from collections import Counter

"""Implementation of ternary heap for Huffman coding"""
class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.mid = None
        self.right = None

    def __cmp__(self, other):
        if(other == None):
            return -1
        if(not isinstance(other, HeapNode)):
            return -1
        return self.freq > other.freq
def calc_ternary(n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

# def generatemultipleoftwentyfive():
    
def get_weights(coll):
    # theap = TernaryHeap()
    
    heap = [[wt, [sym, ""]] for sym, wt in coll.items()]
    heapify(heap)
    while len(heap) > 1:
        low = heappop(heap)
        for tri in low[1:]:
            tri[1] = '2' + tri[1]

        mid = heappop(heap)
        for tri in mid[1:]:
            tri[1] = '1' + tri[1]

        if len(heap) != 0:
            hii = heappop(heap)
            for tri in hii[1:]:
                tri[1] = '0' + tri[1]
            heappush(heap, [low[0] + mid[0] + hii[0]] + low[1:] + mid[1:] + hii[1:])
        else:
            heappush(heap, [low[0] + mid[0]] + low[1:] + mid[1:])
        # for i in heap:
        #     print(i[-1])
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

def encode(text, weights):
    out = ''
    for t in text:
        for w, v in weights:
            if t == w:
                out = out + v
    return out

def decode(code, weights):
    out, test = '', ''
    # test = ''
    for c in code:
        if test == '':
            test = c
        else:
            test = test + c
        for w, v in weights:
            if test == v:
                out = out + w
                test = ''
                continue
    return out

# def merge_nodes(self):
#     while(len(self.heap)>1):
#         node1 = heappop(self.heap)
#         node2 = heappop(self.heap)
#         node3 = heappop(self.heap)

#         merged = HeapNode(None, node1.freq + node2.freq + node3.freq)
#         merged.left = node1
#         merged.mid = node2
#         merged.right = node3

#         heappush(self.heap, merged)
txt = "This is an example for Huffman encoding"
bg = "Birney and Goldman"

symb2freq = Counter(txt)


huff = get_weights(symb2freq)
print("Symbol\tWeight\tHuffman Code")
count = 0
for p in huff:
    count = count + int(len(p[1]))
    print("%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1]))

print(count)
s1 = encode(txt, huff)
print(s1)
d1 = decode(s1, huff)
print(d1)
len_s1 = calc_ternary(count)
print('in ternary: ' + calc_ternary(count))

while len(len_s1) < 20:
    len_s1 = '0' + len_s1

print(len_s1)