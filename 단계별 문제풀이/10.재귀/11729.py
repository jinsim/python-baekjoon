# 문제에 대해 깊은 생각을 해야한다. 
"""
탑을 1, 2, 3이라고 할 때, 1에서 3까지 2개의 탑을 옮긴다고 가정하면,
12, 13, 23 이다. 3개일 때는 13, 12, 32, 13, 21, 23, 13인데, 이정도까지는 머리로 생각할 수 있다. 
이를 정리하면, n-1개까지의 판을 2에 옮긴 후, n번째 판을 3에 옮기고, 나머지 n-1을 3으로 옮기는 과정이다. 
그리고, n-1까지의 판을 2에 옮기는 과정도, n-2개까지의 판을 3에 올리고, 나머지 n-2를 2로 옮기는 과정과 같다.  
그 후의 경우도 마찬가지이므로, 재귀를 구현한다면 아래의 코드가 된다. 
6-start-end의 의미는, 합쳐서 6이 되는 수이므로 나머지 한 수를 구하기 위한 목적이다.
"""
def hanoi(n, start, end):
    if n == 1:
        print(start, end)
    else:
        n -= 1
        hanoi(n, start, 6-start-end)
        print(start, end)
        hanoi(n, 6-start-end, end)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)
