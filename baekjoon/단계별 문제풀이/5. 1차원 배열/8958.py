# 수학적으로 푸는 것이 가장 효율적이다.
n = int(input())
for _ in range(n):
    l = input().split("X")
    sum = 0
    for i in l:
        m = len(i)
        sum += m*(m+1)//2
    print(sum)
