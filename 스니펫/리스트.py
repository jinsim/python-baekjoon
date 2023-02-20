l = [1, 2, 3]
# "123"으로 가져오고 싶다. 
''.join(str(e) for e in l)
''.join(map(str, l)) 
print(*l, sep='')

a = [1, 2, 3, 4, 5, 5, 5]
a.remove(3) # 제일 첫번째 요소만 제거
remove_set = {3, 5} # 집합에 있는 요소를 모두 제거
result = [i for i in a if i not in remove_set]  # [1, 2, 4]
