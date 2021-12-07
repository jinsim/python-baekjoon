# 정렬을 활용한 풀이. 곱씹어볼만한 문제인 것 같다.
cnt = 0
for _ in range(int(input())):
    s = input()
    # key에 find를 안넣으면 ba와 같은 경우에서 파악하지 못한다.
    # aba가 나올 때, a는 0, b는 1, a는 다시 0으로 들어가서 list(s)와 달라짐.
    if list(s) == sorted(s, key=s.find):
        cnt += 1
print(cnt)
