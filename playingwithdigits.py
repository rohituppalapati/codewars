def dig_pow(n, p):

    #Convert n to str and then to an array
    digitString = str(n)
    digitArray = []
    for digit in digitString:
        digitArray.append(int(digit))

    #check the condition in a loop
    total = 0
    for i in range(0, len(digitArray), 1):
        foo = digitArray[i] ** (p + i)
        total += foo
    k = float(total) / n
    foo = int(k)
    if k == foo:
        return k

    return -1