d = {"apple": 3, "car": 99, "blue": 87, "string": 33, "app": 123}

sorted(d.items())
# 키 순서대로 정렬. 리스트로 반환
[('app', 20), ('apple', 3), ('blue', 87), ('car', 99), ('string', 33)]

sorted(d)
# 키만 빼서 정렬. 리스트로 반환
['app', 'apple', 'blue', 'car', 'string']


