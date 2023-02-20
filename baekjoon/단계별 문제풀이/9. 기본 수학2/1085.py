# 케이스만 잘 생각하면 쉽게 풀 수 있다. 
x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))
