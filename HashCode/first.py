roads = {}
positions = {}
cars = {}

D,I,S,V,F = [int(s) for s in input().split()]
for line in range(S):
    start,end,name,time = [str(s) for s in input().split()]
    start,end,time = int(start), int(end), int(time)
    roads[name] = [start,end,time]

for car in range(V):
    inp = [str(s) for s in input().split()]
    cars[car] = inp[1:]
    if inp[2] in positions:
        positions[inp[2]] = positions[inp[2]].append(car)
    else:
        positions[inp[2]] = [car]


print(roads)
print(cars)
print(positions)
