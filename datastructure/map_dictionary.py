# 맵 Map (dictionary)
# - Key, Value 형태의 자료구조
# - 파이썬에서 hash로 구현되어 있기 때문에 삽입/삭제 O(1)
# - C++ 에서는 red-black tree로 구현되어있어 삽입/삭제가 O(logN)


m = {}
m["Yoondy"] = 40
m["Sky"] = 100
m["Jerry"] = 50

print(f"size : {len(m)}")

for k in m:
    print(k, m[k])