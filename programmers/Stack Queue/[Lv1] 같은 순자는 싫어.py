def solution(arr):
    answer = [arr[0]]
    for i in arr:
        if answer[-1] == i:
            continue
        answer.append(i)
    return answer