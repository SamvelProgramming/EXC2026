def interval1(intervals):
    intervals.sort()
    result = []
    for i in intervals:
        if len(result) == 0:
            result.append(i)
        else:
            last = result[-1]
            if i[0] <= last[1]:
                if i[1] > last[1]:
                    last[1] = i[1]
            else:
                result.append(i)
    return result
print(interval1([[1,3],[2,6],[8,10],[15,18]]))

def interval2(intervals, newInterval):
    intervals.append(newInterval)
    intervals.sort()
    result = []
    for i in intervals:
        if len(result) == 0:
            result.append(i)
        else:
            last = result[-1]
            if i[0] <= last[1]:
                if i[1] > last[1]:
                    last[1] = i[1]
            else:
                result.append(i)
    return result
print(interval2([[1,3],[6,9]], [2,5]))