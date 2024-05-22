def Lucky(x):
    mid = len(x) // 2
    sum1 = sum(x[:mid])
    sum2 = sum(x[mid:])
    if sum1 == sum2:
        return True
    else:
        return False