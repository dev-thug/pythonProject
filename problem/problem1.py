def solution(vote):
    dic = {}
    dic["A"] = 0
    dic["B"] = 0
    dic["C"] = 0
    n = len(list(vote))
    for i in list(vote):
        dic[i] += 1

    answer = []
    max_vote = 0
    for key in dic.keys():
        if dic[key] > max_vote:
            max_vote = dic[key]

    if dic["C"] >= (n / 2):
        return "C"

    if dic["A"] > dic["B"]:
        return "A"
    elif dic["A"] < dic["B"]:
        return "B"
    elif dic["A"] == dic["B"]:
        return "AB"

    # for key in dic.keys():
    #     if dic[key] == max_vote:
    #         answer.append(key)
    #
    # if answer == "BA":
    #     return "AB"
    # return ''.join(answer)


vote = "AAAABCCCCC"  # "AAACABCBBB"  # "ABBCCCBBAB"
print(solution(vote))
