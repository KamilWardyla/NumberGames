def over_the_road(address, n):
    list_parz = []
    list_nie_parz = []
    for x in range(1, n * 2 + 1):
        if x % 2 == 0:
            list_parz.append(x)
        elif x % 2 != 0:
            list_nie_parz.append(x)

    list_parz = list_parz[::-1]

    if address % 2 == 0:
        return list_nie_parz[(list_parz.index(address))]
    else:
        return list_parz[(list_nie_parz.index(address))]


print(over_the_road(23633656673, 310027696726))