def canCompleteCircle(station, cost):
    total = 0
    fuel = 0
    start = 0

    for i in range(len(station)):
        j = station[i] - cost[i]
        total += j
        fuel += j

        if fuel < 0:
            start = i + 1
            fuel = 0

    if total >= 0:
        return start
    else:
        return -1
    
station = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(canCompleteCircle(station, cost))