def bindec():

    while True:
        try: 
            num = int(input('Binary number: '))
        except ValueError:
            print('pls try it with a valid value bro')
            continue
        else:
            break


    digits = str(num)
    leng = len(digits)

    pots = []

    digits = digits[::-1]

    for x in range(leng):
        y = int(digits[x]) * (2 ** x)
        pots.append(y)
    print (sum(pots))


def decbin():

    num = int(input('Decimal number: '))
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

        for j in digits:
            print(j, end="")


    

while True:
    print("Options:\n[1] Binary -> Decimal\n[2] Decimal -> Binary \n")

    while True:
        try:
            option = int(input('Select an option: '))
        except ValueError:
                print("Options must be integers!!\n")
                continue
        else:
            break


    if option == 1:
        print("Chosen: Binary to Decimal\n")
        bindec()
        print("\ncontinue? ([y]/n)\n")
        sn = input()
        if sn == 'n':
            break
        else:
            continue
        

    elif option == 2:
        print("Chosen: Decimal to Binary\n")
        decbin()
        print("\ncontinue? ([y]/n)\n")
        sn = input()
        if sn == 'n':
            break
        else:
            continue
        

    else:
        print("Invalid option! Try again!\n")
        continue