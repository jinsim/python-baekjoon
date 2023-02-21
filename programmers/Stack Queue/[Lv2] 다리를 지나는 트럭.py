from collections import deque


def solution(bridge_length, weight, truck_weights):
    # IndexError 방지용.
    truck_weights.append(10001)
    Q = deque()
    # 무게, 도착 시간
    Q.append((truck_weights[0], bridge_length))
    time = 1  # 현재 시간
    idx = 1  # 다음 들어올 트럭
    now_weight = truck_weights[0]  # 다리 위의 무게

    while idx < len(truck_weights) - 1:
        w, t = Q[0]  # 나갈 차례의 트럭
        # 트럭이 나갈 차례가 되면, Q에서 제거해주면서 무게도 뺀다.
        if t <= time:
            now_weight -= w
            Q.popleft()

        # 현재 들어올 차례의 트럭로 인해 무게 초과가 된다면, 다음 나갈 차례의 트럭이 나가는 시간까지 증가시킨다.
        if truck_weights[idx] + now_weight > weight:
            time = t
            continue
        # 현재 들어올 차례의 트럭이 들어올 수 있다면, Q에 넣고 무게와 차례와 시간을 늘려준다.
        else:
            Q.append((truck_weights[idx], time + bridge_length))
            now_weight += truck_weights[idx]
            idx += 1
            time += 1

        # 모든 트럭이 다리에 들어왔다면, 가장 끝에 있는 트럭의 나가는 시간에 1을 더해준다.
    return Q[-1][1] + 1