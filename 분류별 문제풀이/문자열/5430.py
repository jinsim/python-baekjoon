# 상당히 어려운 문제
from collections import deque
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    err = 0
    rev_cnt = 0
    cmd_li = input().rstrip()
    li_len = int(input())
    li = input().rstrip()
    if li_len:
        li = deque(li[1:-1].split(','))
    else:
        li = deque()
    for i in cmd_li:
        if i == 'R':
            rev_cnt += 1
        else:
            if li:
                if rev_cnt % 2 == 0:
                    li.popleft()
                else:
                    li.pop()
            else:
                err += 1
                break
    if err:
        print('error')
    else:
        if rev_cnt % 2 == 1:
            li.reverse()
        print('['+','.join(li)+']')
