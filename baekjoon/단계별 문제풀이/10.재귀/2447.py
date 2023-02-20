# 생각을 깊게 해야한다.(더 쉬운 방법도 있음 - 프랙탈)
"""
123
456
789
라고 했을 때, n//3일때의 문양을 5를 제외한 자리에 채우면 된다.
이를 위해 2차원 배열을 만들고, n이 3일때의 문양을 만든 후,
인덱스 012까지를 변경시키고, 이를 점점 늘려간다.
"""
def star(n):
    if n == 3:
        l[0][:3] = l[1][:3] = l[2][:3] = ["*"]*3
        l[1][1] = " "
        return

    n //= 3
    star(n)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(n):
                l[n*i+k][j*n:j*n+n] = l[k][:n]

num = int(input())
l = [[" " for _ in range(num)] for _ in range(num)]
star(num)
for i in l:
    print(*i, sep='')
