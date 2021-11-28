a = input()
b = input()
for i in b[::-1]:
    print(eval(a+'*'+i))
print(eval(a+'*'+b))
