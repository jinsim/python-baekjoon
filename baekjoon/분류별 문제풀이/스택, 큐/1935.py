# 후위 표기식을 연산한다.
"""
알파벳인 경우 딕셔너리에서 값을 조회해서 스택에 push한다.
연산인 경우 2번 pop을 해서 연산한 결과를 스택에 push 한다.
마지막 남은 요소를 출력하면 답이다.
"""
num = int(input())
exp = input()
a = {}
s = []
for i in exp:
    if i.isalpha():
        if i not in a:
            a[i] = input()
        s.append(a[i])
    else:
        v1 = s.pop()
        v2 = s.pop()
        s.append(str(eval(v2+i+v1)))
print(f'{float(s[-1]):.2f}')