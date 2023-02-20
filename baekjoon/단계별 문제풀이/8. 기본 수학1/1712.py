# 간단한 계산 문제. 예외 상황만 생각
a, b, c = map(int, input().split())
print(a//(c-b)+1 if b < c else -1)