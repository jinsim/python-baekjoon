"""
집 사이의 거리를 이분탐색해야하는 문제이다.
start(최소 거리, 1), end(최대 거리, 가장 먼 것 - 가장 짧은 것) 을 정하고,
mid 앞뒤로 start와 end를 옮기며,
원하는 수의 집이 mid 이상으로 간격을 가지는 mind의 최댓값을 찾는다.
즉, 인접한 공유기의 간격를 이분탐색하여 정한다.

이분 탐색의 시간 복잡도는 O(log2 N). 여기서 집의 개수는 200,000 이고, 좌표는 1,000,000,000 이다.
1) 입력 집 좌표 정렬: O(n log_2 n)
2) 이진 탐색: O(log_2 maxDist)
maxDist = 정렬된 homes[n-1] - homes[0]
3) 이진 탐색 1회 마다 설치 공유기 개수 계산: O(n)

총 시간 복잡도 = O(n log_2 n + n log_2 maxDist) = O(n log_2 (n x maxDist))
=> 최대 (2 x 10^5) log_2 (2 x 10^5 x 10^9)
= (2 x 10^5) log_2 (2 x 10^14) = (2 x 10^5) x (log_2 2 + log_2 10^14)
= (2 x 10^5) x (1 + 14 log_2 10) ~= (2 x 10^5) x 43 = 86 x 10^5 << 2억
"""
import sys

#표준입력을 파일로 설정
sys.stdin = open("../../input.txt","r")
input = sys.stdin.readline

N, C = map(int, input().split())

houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

start = 1
end = houses[-1]-houses[0]
result = 0

# 집이 2개면 무조건 최대 거리
if C == 2:
    print(end)
else:
    while (start <= end):
        cnt = 1     # start에 있는 집 포함
        mid = (start+end)//2
        val = houses[0]     # 이전 집의 위치 알려주는 역할
        # 모든 집을 확인하며 현재 정한 공유기의 간격(mid)보다 긴 집의 수를 센다.
        for i in range(1, N):
            if houses[i] >= val+mid:        # 이전 집 위치에 간격 더한 것보다 크게 나온다면, 공유기 설치 가능
                cnt+=1
                val = houses[i]     # 새로운 좌표를 이전 집 위치로 갱신

        # 집의 수가 목표 값보다 많다면, 공유기 간격을 더 늘려서 집 개수를 줄여야 한다.
        # 같다면, 더 큰 간격에도 조건에 맞춰 설치할 수 있는지 확인하기 위해 간격을 더 늘려야 한다.
        if cnt >= C:
            start = mid + 1
            result = mid
        # 적다면, 간격을 더 작게 해서 집 개수를 늘려야 한다.
        else:
            end = mid-1
    print(result)