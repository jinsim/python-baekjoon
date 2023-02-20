# 전위 표기식을 후위 표기식으로 변경하는 연산. 중요하다. 
"""
들어오는 문자가 알파벳인 경우, 그냥 ret에 추가하면 된다.
연산 중 하나인 경우, 스택의 마지막 연산과 현재 들어온 연산을 비교한다.
들어온 연산보다 작은 우선순위가 나올 때까지 스택의 연산을 pop해서 ret에 추가한다. 반복문 후에 연산을 스택에 넣는다.
여는 괄호인 경우 스택에 바로 추가한다.
닫는 괄호인 경우, 스택의 요소를 꺼내서 여는 괄호가 나올 때까지 ret에 추가한다.
스택이 남아있으면 ret에 추가한다.
"""
exp = input()
s = []
ret = ''
priority = {'*':2, '/':2, '+':1, '-':1, '(':0}

for v in exp:
    if v.isalpha():
        ret += v
    elif v in '*/+-':
        while s:
            if priority[v] <= priority[s[-1]]:
                ret += s.pop()
            else: 
                break
        s.append(v)
    elif v == '(':
        s.append('(')
    else:
        while s:
            op = s.pop()
            if op == '(':
                break
            else:
                ret += op
while s:
    ret += s.pop()
print(ret)