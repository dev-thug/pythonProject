# N = int(input())
# my_card = list(map(int, input().split(" ")))
# M = int(input())
# check_card = list(map(int, input().split(" ")))
#
# my_card.sort()
#
#
# def is_card(check):
#     low = 0
#     high = N
#     while low < high:
#         mid = (low + high) // 2
#         if check > my_card[mid]:
#             low = mid + 1
#         elif check == my_card[mid]:
#             return True
#         else:
#             high = mid - 1
#     return False
#
#
# for check in check_card:
#     if is_card(check):
#         print("1", end=" ")
#     else:
#         print("0", end=" ")


from bisect import bisect_left, bisect_right

N = int(input())
cards = sorted(list(map(int, input().split(" "))))
M = int(input())
qry = list(map(int, input().split(" ")))

ans = []

for q in qry:
    l = bisect_left(cards, q)
    r = bisect_right(cards, q)
    ans.append(1 if r - l else 0)

# print(" ".join(map(str, ans)))
print(*ans)
