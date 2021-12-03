# 관점 생각하기(어떤 식으로 문제를 푸는 게 효과적일지)
a = [0]
for _ in range(1, 10):
    a.append(int(input()))
print(max(a))
print(a.index(max(a)))