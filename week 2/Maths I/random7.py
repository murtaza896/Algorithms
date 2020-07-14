# Given a func rand5() which is built to return a random number in [1 .. 5] with equal probability
# design a func rand7() for the range [1 ... 7]

def rand7():
    #Mapping a function of larger output space to a func of smaller output space
    x = (rand5() - 1)*5 + rand5()

    if x > 21:
        return rand7()
    else:
        return x % 7 + 1 