def snail(array):
    print(array)
    results = []
    while len(array) > 0:
        # go right
        results.append(array[0])
        del array[0]
        # go down
        if len(array) > 0:
            for i in range(len(array)):
                results.append(array[i][-1])
                del array[i][-1]

        # go left
        if len(array) > 0:
            results.append(list(reversed(array[len(array) - 1])))
            del array[len(array) - 1]

        # go up
        if len(array) > 0:
            for i in reversed(range(len(array))):
                results.append(array[i][0])
                del array[i][0]

    results2 = []

    for i in results:
        if type(i) is list:
            for j in i:
                results2.append(j)
        else:
            results2.append(i)
    return results2