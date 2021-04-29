while True:
    print("Options:\n[1] Binary -> Decimal\n[2] Decimal -> Binary \n")

    while True:
        try:
            option = int(input('Select an option:'))
        except ValueError:
                print("Options must be integers!!")
                continue
        else:
            break


    if option == 1:
        print("Chosen: Binary to Decimal")
        print("continue? ([y]/n)")
        sn = input()
        if sn == 'n':
            break
        else:
            continue
        

    elif option == 2:
        print("Chosen: Decimal to Binary")
        print("continue? ([y]/n)")
        sn = input()
        if sn == 'n':
            break
        else:
            continue
        

    else:
        print("Invalid option!!")
        continue