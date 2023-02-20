# 간단하지만 모른다면 어려운 문제이다. 
"""
str을 list로 하면 각각 나뉘어진다. 
"""
n = list(input())
n.sort(reverse=True)
print(*n, sep='')
