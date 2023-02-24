import functools

# a가 앞에 있는 게 크면 1, b가 앞에 있는 게 크면 -1, 같으면 0 반환
def check(a,b):
    v1, v2 = a+b, b+a
    return (v1 < v2) - (v1 > v2)

def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key=functools.cmp_to_key(check))
    return str(int(''.join(numbers)))