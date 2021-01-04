def hist_area(histogram):
    stack = []
    index = 0
    max_area = 0

    while index < len(ip):

        if not stack or histogram[index] >= histogram[stack[-1]]:
            stack.append(index)
            index += 1

        else:
            top = stack.pop()

            area = histogram[top] * ((index - stack[-1] - 1) if stack else index)
            max_area = max(area, max_area)

    while stack:
        top = stack.pop()
        area = histogram[top] * ((index - stack[-1] - 1) if stack else index)
        max_area = max(area, max_area)


    return max_area

if __name__ == "__main__":
    ip = list(map(int, input().split(", ")))
    res = hist_area(ip)
    print(res)
