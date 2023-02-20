def solution(number, k):
    s = []
    for num in number:
        # 해당 숫자가 stack의 마지막 요소보다 크다면 stack의 수 대신 위 수를 넣는다.
        while s and s[-1] < num and k > 0:
            k -= 1
            s.pop()
        s.append(num)
    # 이 경우, 숫자가 이미 내림차순인 것이다.
    if k != 0:
        s = s[:-k]
    return ''.join(s)