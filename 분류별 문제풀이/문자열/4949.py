# 정석 풀이법이 있는 문제. 
"""
딕셔너리를 만든 후, 닫힌 괄호가 나오면 y에서 빼내 값을 비교한다.
"""
import sys
input = sys.stdin.readline
x = {']': '[', ')': '('}
while True:
    y = []
    err = 0
    n = input()
    if n == '.\n':
        break
    for i in n:
        if i in ')]':
            if not y or x[i] != y.pop():
                err = 1
                break
        elif i in '([':
            y.append(i)
    if len(y):
        err = 1
    print('no' if err else 'yes')
