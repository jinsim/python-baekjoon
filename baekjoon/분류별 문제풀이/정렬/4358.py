# 딕셔너리를 이용해서 쉽게 해결할 수 있다. 
"""
각 나무들을 딕셔너리에 저장하고,
딕셔너리를 정렬한 후, 
조건에 맞게 출력하면 끝.
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

dic = defaultdict(int)
cnt = 0

while True:
    tree = input().rstrip()
    if tree:
        dic[tree]+=1
        cnt += 1
    else:
        break
    
dic = dict(sorted(dic.items()))

for key, value in dic.items():
    print(f"{key} {value/cnt*100:.4f}")