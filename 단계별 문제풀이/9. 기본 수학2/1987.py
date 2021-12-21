# 미리 소수 리스트를 만들어놓는 방법, 순서대로 파악하는 방법으로 나눌 수 있다. 
# 물론, 가장 좋은 것은 아라크네토스의 체를 사용하는 방식이다. 
# 미리 리스트 제작
"""
인덱스를 숫자로. 0~1000. 자리수가 0이면 소수다. 
소수파악은 for문을 본인의 제곱근만큼간 파악하면 된다.(예를 들어 20의 경우 제곱근이 4.xx 이므로 4까지만 나눠보면 파악할 수 있다.)
2부터 1000까지의 모든 자리에서 나눌 수 있는 자리를 1로 변경한다. 
"""
n = [0]*1001
for i in range(2, int(1000**0.5)+1):
    if n[i] == 1:
        continue
    for j in range(2, 1000//i+1):
        n[j*i] = 1
n[1] = 1
ans = 0
input()
a = list(map(int, input().split()))
for k in a:
    if not n[k]:
        ans += 1
print(ans)


# 순서대로 판단
input()
t = list(map(int, input().split()))
ans = 0

for i in t:
  if i == 1:
      continue

  cnt = 0
  for j in range(2, int(i**0.5) + 1):
    if i % j == 0:
      cnt += 1
      break

  if cnt == 0:
    ans += 1

print(ans)

# 아라크네토스의 체 사용
input()
l = [0, 0]+[1]*(999)
cnt = 0
for i in range(2, 1001):
    if l[i]:
        for j in range(i*2, 1001, i):
            l[j] = 0

for j in list(map(int, input().split())):
    if l[j]:
        cnt += 1
print(cnt)
