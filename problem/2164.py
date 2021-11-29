n = int(input())
card = [i for i in range(n)]
command = True
while len(card) > 1:
    if command:
        card.pop(0)
        command = False
    else:
        card.append(card[0])
        card.pop(0)
        command = True

print(card[0]+1)