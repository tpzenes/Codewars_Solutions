def decompose(n):
    remain = 0
    result = [n]
    while result:
        current = result.pop()
        remain += current ** 2
        for i in reversed(range(1,current)):
            if remain - (i ** 2) >= 0:
                remain -= i ** 2
                result.append(i)
                if remain == 0:
                    result.sort()
                    return result
    return None