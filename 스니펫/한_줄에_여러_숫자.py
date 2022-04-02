# input이 "1, 2, 3, 4" 로 주어질 때.

# 여러 요소로 받기
a, b, c, d = map(int, input().split())
# a=1, b=2, c=3, d=4로 저장됨.

# 리스트로 받기
list(map(int, input().split()))  
# [1, 2, 3, 4]

# 바로 반복문 사용
for i in map(int, input().split()): 
    print(i)
# 1
# 2
# 3
# 4