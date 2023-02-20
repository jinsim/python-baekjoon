# 문자열 출력. 곱하기의 쓰임. 반복출력
for _ in range(int(input())):
    a, b = input().split()
    for i in b:
        print(i*int(a), end='')
    print('')
