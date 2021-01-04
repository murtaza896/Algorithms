# Return the count of occurrence of digit one in [1 ... n]

# Method 1, Time = O(Nlog(N))
# convert each number into string and count the frequency of "1" in every str(i)
def no_of_digit_one_1(n):
    cnt = 0
    for i in range(1, n+1):
        s = str(i)
        cnt += s.count("1")
    return cnt

# Method 2, Time = O(log(N))
# identifying a pattern in one occurence in one's ten's hundred's place
def no_of_digit_one_2(n):
    cnt = 0
    i = 1
    while i<=n:
        divider = i * 10
        cnt += (n // divider * i + min(max(n%divider - i + 1, 0), i))
        i *= 10

    return cnt


if __name__ == "__main__":
    n = int(input())
    print(no_of_digit_one_2(n))
