# 상당히 어려운 문제
"""
배열 끝과 끝에서 각각 추출되는 경우가 있으므로 deque을 사용해야한다. 
입력된 배열이 아무것도 없는 경우를 예외처리 해주고, deque로 만든다. 
명령어를 하나씩 출력하며 각각에 해당하는 계산을 해주면 되는데, 
R인 경우 짝수번 회전과 홀수번 회전으로 나눌 수 있으므로 숫자를 세는 것으로 대체한다. 
출력 양식이 정해져있으므로 join을 활용한다.
"""
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
