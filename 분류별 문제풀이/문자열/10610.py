# 3의 배수 조건
"""
모든 자릿수의 합이 3의 배수면 그 수도 3의 배수이다.
0의 유무에 따라 첫번재 예외처리를 하고, 자릿수의 합을 계산한다.
3의 배수가 맞다면 join을 통해 답을 생성한다.
"""
n = list(input())
n.sort(reverse=True)
if '0' in n:
    sum = 0
    for i in n:
        sum += int(i)
    if sum % 3 == 0:
        print(''.join(n))
    else:
        print(-1)
else:
    print(-1)
