ip = list(map(int, input().strip().split(", ")))

# Calculate tallest building
# traverse on left side to get the maxL, which will determine the height of water collected [ maxR = tallest_building ]
# traverse on right side to get the maxR, which will determine the height of water collected [ maxL = tallest_building ]

tallest_building = 0
pos = 0
unit = 0

for i in range(0, len(ip)):
    if ip[i] > tallest_building:
        tallest_building = ip[i]
        pos = i

maxL = ip[0]
posL = 0

for i in range(1, pos):
    if ip[i] > maxL:
        maxL = ip[i]
        posL = i

    height = maxL - ip[i]
    # width = i - posL
    area = height
    # print(area)
    unit += area


maxR = ip[-1]
posR = len(ip) - 1
for i in range(len(ip)-2, pos, -1):
    if ip[i] > maxR:
        maxR = ip[i]
        posR = i

    height = maxR - ip[i]
    area = height
    # print(area)
    unit += area

print(unit)