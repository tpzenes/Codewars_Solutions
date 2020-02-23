from itertools import combinations_with_replacement


def find_all(sum_dig, digs):
    sayi = ""
    sayi_liste = []
    result = []
    aba = list(combinations_with_replacement(range(1, 10), digs))
    for i in aba:
        if sum(i) == sum_dig:
            for j in range(digs):
                sayi += str(i[j])
            sayi_liste.append(int(sayi))
            sayi = ""
    if len(sayi_liste) < 1:
        return []

    result.append(len(sayi_liste))
    result.append(min(sayi_liste))
    result.append(max(sayi_liste))

    return result