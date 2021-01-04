ip = list(map(int, input().strip().split()))
method = int(input())

if method == 1:
    #method 1: Time=O(N^2) | Space=O(1) computing maxleft and maxright in loop
    height = 0
    for i in range(len(ip)):
        maxL, maxR = 0, 0
        for j in range(0,i+1):
            if ip[j] > maxL:
                maxL = ip[j]
        for j in range(i+1, len(ip)):
            if ip[j] > maxR:
                maxR = ip[j]

        height = max(height, min(maxL, maxR) - ip[i])
    print(height)

elif method == 2:
    # method 2: Time=O(N) | Space=O(2N) pre-computing maxleft and maxright
    height = 0
    
    maxL = [ip[0]]
    for i in range(1, len(ip)):
        maxL.append(max(ip[i], maxL[i-1]))

    maxR = [ip[len(ip)-1]]
    for i in range(1, len(ip)):
        maxR.append(max(ip[len(ip)-i-1], maxR[i-1]))

    for i in range(len(ip)):
        ml = maxL[i]
        mr = maxR[i]
        height = max(height, min(ml, mr) - ip[i])

    print(height)

elif method == 3:
    # method 3: Time=O(N) | Space=O(1)
    # Divide the problem into 2 parts, left and right of the tallest building
    # for the left part, ans will be decided based on max left, since max right = tallest building
    # for the right part, ans will be decided based on max right, since max left = tallest building

    pos = 0
    tallest_building = 0
    height = 0

    for i in range(0, len(ip)):
        if ip[i] > tallest_building:
            tallest_building = ip[i]
            pos = i

    maxL = ip[0]
    for i in range(1, pos):
        if ip[i] > maxL:
            maxL = ip[i]

        height = max(height, maxL - ip[i])

    maxR = ip[-1]
    for i in range(len(ip)-2, pos, -1):
        if ip[i] > maxR:
            maxR = ip[i]

        height = max(height, maxR - ip[i])

    print(height)