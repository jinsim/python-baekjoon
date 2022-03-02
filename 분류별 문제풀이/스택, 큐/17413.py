# 스택을 사용하는 풀이법, 리스트로 변경해서 문자열 조작하는 풀이법이 있다.
"""
t로 <> 안에 있는지를 파악하였다. 
기존의 문자는 s에 넣고,
<>안에 있는 문자는 s_t에 넣는다.
<만나면 기존에 s에 있는 요소들을 pop으로 출력한다.
>를 만나면 s_t에 저장되어있는 문자열을 그냥 출력한다. 
공백을 만나면 t의 유무로 <>안에 있는지를 파악 후, 적절히 처리한다.
반복이 끝나고 s에 남아있는 요소들을 pop으로 출력한다. 
"""
import sys
input = sys.stdin.readline

t = False
s = []
s_t = ''
str = input().rstrip()
for i in str:
    if i != ' ':
        if i == '<':
            if s:
                while s:
                    print(s.pop(), end='')
            t = True
            s_t+=i
        elif i == '>':
            t = False
            s_t+=i
            print(s_t, end='')
            s_t = ''
        else:
            if t:
                s_t+=i
            else:
                s.append(i)
    else:
        if t:
            s_t+=i
        else:
            while s:
                print(s.pop(), end='')
            print(' ', end='')

while s:
    print(s.pop(), end='')
print(' ', end = '')
            