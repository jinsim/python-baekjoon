n = int(input())
for _ in range(n):
    l = list(map(int, input().split()))
    u = l[0]
    l = l[1:]
    m = sum(l)/u
    l.sort()
    l.reverse()
    for i in range(0, u):
        if l[i] <= m:
            break
    print("{:0.3f}%".format(i/u*100))
