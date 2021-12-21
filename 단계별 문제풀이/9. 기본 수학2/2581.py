# 브루트 포스 방식으로 해도 풀린다.
# 다만, ans에서 소수가 아닌 것을 제외하므로, 반복문에 들어가는 리스트는 기존 리스트를 복사한 값이어야한다.
# 역시 제일 좋은 것은 아라크네토스의 체.

a = int(input())
b = int(input())
ans = list(range(a, b+1))
for i in ans[:]:
  if i == 1:
      ans.remove(i)
  for j in range(2, int(i**0.5) + 1):
      if i % j == 0:
         ans.remove(i)
         break
if len(ans):
    print(sum(ans), ans[0], sep='\n')
else:
    print(-1)

# 아라토스테네스의 체
a = int(input())
b = int(input())
l = [0, 0]+[1]*(b-1)
ans = []
for i in range(2, b+1):
    if l[i]:
        if i >= a:
          ans.append(i)
        for j in range(i*2, b+1, i):
            l[j] = 0
if len(ans):
    print(sum(ans), ans[0], sep='\n')
else:
  print(-1)
