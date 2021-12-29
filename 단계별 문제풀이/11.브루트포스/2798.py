# 실행 시간을 줄일 방법을 찾는다. 
"""
값을 역순으로 정렬하고 조건을 걸면, 
i와 j값에 대한 조건에 부합하는 가장 큰 값들만 모을 수 있다. 
"""
n, m = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
vals = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if l[i]+l[j]+l[k] <= m:
                vals.append(l[i]+l[j]+l[k])
                break

print(max(vals))
