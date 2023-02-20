N, K = map(int, input().split())
h_list = list(input())
ret = 0
h_idx = 0
for idx, val in enumerate(h_list):
    if val == "P":
        # 전체 배열 인덱스를 넘기면 안된다. 0 ~ N 사이
        for i in range(max(idx-K, 0), min(idx+K+1, N)):
            if h_list[i] == "H":
                h_list[i] = "N"
                ret += 1
                break

print(ret)