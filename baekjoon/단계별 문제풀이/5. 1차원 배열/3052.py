# 집합의 사용법
t = set()
for _ in range(10):
    t.add(int(input()) % 42)
print(len(t))