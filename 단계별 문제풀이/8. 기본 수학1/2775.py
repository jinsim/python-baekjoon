# 재귀함수로 풀었을 때 시간 초과가 나옴(너무 큰 수라). 역시 수학적인 생각 필요.
"""
k층n호에 사는 사람 수는, k-1층n호, k층n-1호에 사는 사람 수를 합친 것과 같다
호의 크기만큼 배열을 만들고 for문을 돌려 직전 인덱스와 본인 자리 인덱스를 합치면 새로운 자리의 사람 수가 나온다. 
"""
for _ in range(int(input())):
    k = int(input())
    n = int(input())
    a = list(range(1, n+1))
    for _ in range(k):
        for j in range(1, n):
            a[j] += a[j-1]
    print(a[-1])
