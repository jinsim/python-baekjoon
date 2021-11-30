for i in range(1, int(input())+1):
    a, b = map(int, input().split())
    print(f"Case #{i}", end='')
    print(":", a, "+", b, "=", a+b)