a, b = map(int, input().split())
if b > 44:
    print(a, b-45)
else:
    if a == 0:
        print(23, end=' ')
    else:
        print(a-1, end=' ')
    print(b+15)