# Stack
# First In Last Out  FILO
# 삽입/삭제 : O(1)

s = []
s.append(123)
s.append(456)
s.append(789)

print(f"size : {len(s)}")

while len(s) > 0:
    # top
    print(s[-1])
    s.pop() # == s.pop(-1)
