def solution(n, lost, reserve):
    # 나눠줄 수 있는지 기록하는 리스트
    st = [False] * (n + 1)
    ret = n

    # 여벌을 가진 학생이 잃어버린 경우는 넘긴다. lost에도 제거해주자.
    for i in reserve:
        if i in lost:
            lost.remove(i)
            continue
        st[i] = True

    # 왼쪽, 오른쪽 순으로 확인할 것이므로, 꼭 정렬해주어야 한다. 문제에 정렬이란 말 없음!
    lost.sort()
    for i in lost:
        # 왼쪽에서 빌릴 수 있는 경우
        if i > 0 and st[i - 1]:
            st[i - 1] = False
            continue
        # 오른쪽에서 빌릴 수 있는 경우
        if i < n and st[i + 1]:
            st[i + 1] = False
            continue
        # 못 빌린 경우
        ret -= 1
    return ret