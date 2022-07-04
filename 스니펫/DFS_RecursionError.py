""" Recursion Error가 발생한 경우
RecursionError는 재귀와 관련된 에러입니다. 가장 많이 발생하는 이유는 Python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어질 때입니다.

Python이 정한 최대 재귀 깊이는 sys.getrecursionlimit()을 이용해 확인할 수 있습니다. BOJ의 채점 서버에서 이 값은 1,000으로 되어 있습니다.
"""
#1. DFS를 이용했다면 BFS로, 다이나믹 프로그래밍을 재귀로 구현했다면 반복문으로 구현하는 것 처럼 재귀를 사용하지 않게 구현하는 방법으로 해결할 수 있습니다.

#2. Python이 정한 최대 재귀 갚이를 변경
import sys
sys.setrecursionlimit(10**6)