a, b = map(int, input().split())
while a*b != 0:
    print(a+b)
    try:
        a, b = map(int, input().split())
    except:
        break
