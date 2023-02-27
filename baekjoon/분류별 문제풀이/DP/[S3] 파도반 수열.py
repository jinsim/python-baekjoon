P = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for _ in range(int(input())):
    n = int(input())
    p = len(P)
    if p-1 >= n:
        print(P[n])
        continue
    for i in range(p, n+1):
        P.append(P[i-2] + P[i-3])
    print(P[n])