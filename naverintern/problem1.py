def solution(cards):

    size = len(cards)
    chance = [True] * size

    for i in range(size):
        for j in range(size):
            if chance[i] and i != j and chance[j]:
                index_min = min(cards[i])
                index_color = cards[i].index(index_min)  # 바꿔야 할 컬러 선택

                target_min = min(cards[j])
                target_color = cards[j].index(target_min)

                if index_color == target_color:
                    break

                if min(cards[i][0:index_color]+cards[i][index_color+1:-1]) - 1 <= index_min:
                    break

                if min(cards[j][0:target_color]+cards[j][target_color+1:-1]) - 1 <= target_min:
                    break

                cards[i][index_color] += 1
                cards[i][target_color] -= 1

                cards[j][index_color] -= 1
                cards[j][target_color] += 1
                chance[i] = chance[j] = False

    answer = 0
    for card in cards:
        answer += min(card)

    return answer


cards = [[10, 5, 15], [5, 15, 10], [10, 11, 9]]
# [[0, 0, 30], [30, 0, 0]] 5
# [[8, 11, 11], [10, 7, 13], [15, 10, 5], [7, 17, 6]] 4
# [[8, 11, 11], [6, 15, 9], [14, 2, 14], [8, 20, 2]] 3
# [[10, 5, 15], [8, 9, 13], [10, 10, 10]] 2
print(solution(cards))
