l = [1, 2, 3]
# "123"으로 가져오고 싶다. 
''.join(str(e) for e in l) # 또는
''.join(map(str, l))

