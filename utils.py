def find_max(list):
    maxiumum = list[0]
    for number in list:
        if number > maxiumum:
            maxiumum = number
    return maxiumum
    