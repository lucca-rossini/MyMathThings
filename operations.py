def bindec(num):

    digits = str(num)
    leng = len(digits)

    pots = []

    digits = digits[::-1]

    for x in range(leng):
        y = int(digits[x]) * (2 ** x)
        pots.append(y)
    print (num, "in decimals is:", sum(pots))


def decbin(num):
    digits = []

    if num == 0:
        print(0)

    else:

        while num > 0:

            n = num % 2
            k = int(n)
            digits.append(k)

            if num % 2 == 1:
                num -= 1
            else:
                pass

            num = num/2
        
        digits = digits[::-1]


        print(num, "in binaries is:", end=" ")

        for j in digits:
            print(j, end="")
