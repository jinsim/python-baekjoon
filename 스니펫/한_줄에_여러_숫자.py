# input이 "1, 2, 3, 4" 로 주어질 때.

# 리스트로 변환
list(map(int, input().split()))  
# [1, 2, 3, 4]

# 바로 반복문 사용
for i in map(int, input().split()): 
    print(i)
# 1
# 2
# 3
# 4