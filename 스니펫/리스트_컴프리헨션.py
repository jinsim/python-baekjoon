arr = [i for i in range(1, 4)]
print(arr)  # [1, 2, 3]

arr = [i for i in range(20) if i % 3 == 0]
print(arr)  # 3의 배수 리스트 출력

# 2차원 리스트
n = 4
m = 3
arr = [n * [0] for _ in range(m)]

print(arr)  # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
