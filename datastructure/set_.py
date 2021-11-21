# 집합 Set
# - 중복 X
# - 파이썬에서 삽입/삭제 O(1)

s = set()
s.add(10)
s.add(10)
s.add(50)
s.add(10)
s.add(70)
print(s)
s.remove(50)
print(s)
# 모두 삭제
# s.clear()
