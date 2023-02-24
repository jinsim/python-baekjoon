def solution(citations):
    n=len(citations)
    citations.sort()
    for i in range(n):
        if citations[i] >= n-i:
            return n-i
    else: return 0