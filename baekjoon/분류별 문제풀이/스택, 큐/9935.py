# 문자열 조작에 대한 개념을 생각해야한다.
"""
replace를 사용할 경우, 리스트의 길이만큼의 연산이 소요된다. 스택의 개념을 사용하자.
또한 리스트에서 인덱싱과 join에 대해서도 알아두면 좋다.
"""
a = input()
b = input()
s = []
l = len(b)
for i in a:
    s.append(i)
    if i == b[-1] and b == ''.join(s[-l:]):
        del s[-l:]
print(''.join(s) if s else 'FRULA')