# 메모이제이션을 사용한 풀이
"""
n은 11이하이므로 11까지의 인덱스를 가진 배열을 선언. 
재귀함수 rec을 선언하고, 만약 이미 값이 있다면 그 값을 반환, 
없다면 게산 후에 값을 저장하고 반환.
rec(num)의 의미는, 해당 num을 각각 1 + num-1, 2 + num-2, 3 + num-3으로 나타낸 것이다.
"""
def rec(num):
    if memo[num]:
        return memo[num]
    ans = rec(num-1)+rec(num-2)+rec(num-3)
    memo[num] = ans
    return ans
memo = [0,1,2,4,0,0,0,0,0,0,0,0]
for _ in range(int(input())):
    num = int(input())
    print(rec(num))