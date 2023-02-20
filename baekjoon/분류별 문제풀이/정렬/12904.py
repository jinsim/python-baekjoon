# 투 포인터를 이용한 풀이
"""
b를 a로 만들기 위해서는, 맨 뒤에 a가 있을 경우에는 a만 제거하고, b가 있을 경우에는 제거 후에 문자열을 뒤집어야한다.
문자열을 고정으로 두면, 양 끝부분에서 줄어든다고 생각하면 된다. 이를 나타내는 것이 rev이다. rev가 True일 때는 'B'로 인해서 뒤집어진 상태이며, 이 때는 left가 증가한다.
False일 때는 'B'가 짝수번 나와 정상적인 상태이며, 이 때는 right가 감소한다.
문자열의 길이가 같아진다면 a와 비교를 통해 출력한다.
"""
a = input()
b = input()
left = 0
right = len(b)-1
rev = False

for _ in range(len(b)-len(a)):
    if rev:
        if b[left] == 'B':
            rev = not rev
        left += 1
    else:
        if b[right] == 'B':
            rev = not rev
        right -= 1
        
if rev:
    print(int(b[left:right+1][::-1] == a))
else: 
    print(int(b[left:right+1] == a))
