def merge(intervals):
    intervals.sort()
    res = []

    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval.copy())

        else:
            res[-1][1] = max(res[-1][1], interval[1])

    return res

intervals = [[4,7],[1,4]]
res = merge(intervals)
print(res)