""" 실버 3 - 영단어 암기는 괴로워
3가지 조건을 저장해놓고 정렬하면 된다.
"""

import sys
from collections import defaultdict
input = sys.stdin.readline
print = sys.stdout.write

dic = defaultdict(int)

N, M = map(int,input().split())
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        dic[word] += 1

print('\n'.join(sorted(dic.keys(),key=lambda x:(-dic[x],-len(x),x))))
