for _ in range(int(input())):
    S, s = input(), 0
    for i in S:
        s += 2*(i == '(')-1
        if s < 0:
            break
    print('NO' if s else 'YES')
