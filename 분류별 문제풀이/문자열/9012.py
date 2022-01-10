# 답을 쉽게 도출하는 방법을 생각해보자
"""
2*1 -1은 1이고
2*0 -1은 -1이다.
따라서 (가 나올 때는 1, )가 나올 때는 -1을 더해 음수가 되면 실패한 것이다.
0으로 끝나면 YES, 음수로 끝나면 NO이다.
"""
for _ in range(int(input())):
    S, s = input(), 0
    for i in S:
        s += 2*(i == '(')-1
        if s < 0:
            break
    print('NO' if s else 'YES')
