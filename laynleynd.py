n = int(input("Enter a cities number: "))
cities =[int(input("Enter coordinate of cities must be integer!!!: ")) for j in range(n)]#list of cities we need
radius = int(input("Enter a radius: "))
put_zones = []
i = 0
while i < n:
    if i + 1 < n and cities[i + 1] - cities[i] <= radius:
        put_zones.append(cities[i + 1])
        limit = cities[i + 1] + radius
        print(limit)
        while i < n and cities[i] <= limit:#with this loop we are decideing smallest amount off put zones
            i += 1 
            print(f"{i} time i am on this loop")#i am just making sure that i am on this loop 
    else:
        put_zones.append(cities[i])
        i += 1
print(put_zones)#this is the result

