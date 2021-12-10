# 방정식 세우기.
"""
방의 크기는 기존에 6의 배수 씩 더해진다. cnt는 개수, val은 누적 번호이다.
"""
a = int(input())
cnt = val = 1
while val < a:
    val += cnt*6
    cnt += 1
print(cnt)