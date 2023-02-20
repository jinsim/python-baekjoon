# 이중 리스트가 상당히 편하다. 
"""
둘씩 비교를 진행한다. 둘다 큰 경우에는 작은 것의 순위를 늘린다.
"""
n = int(input())
li = []
val_list = [1]*n
for _ in range(n):
    li.append(list(map(int, input().split())))

for i in range(n-1):
    for j in range(i+1, n):
        if li[i][0] > li[j][0] and li[i][1] > li[j][1]:
            val_list[j] += 1
        if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
            val_list[i] += 1
print(*val_list)