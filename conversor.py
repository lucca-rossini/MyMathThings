import operations, pyautogui as pag

op2 = operations.decbin
op1 = operations.bindec

x = pag.password

while True:

    senha = x(text="senha: ", title="Insert the magic password!", mask="*")

    if senha == 'lovemath':

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


            numb = int(input("Value to convert: "))


            if option == 1:
                op1(numb)
                

            elif option == 2:
                op2(numb)
                
            else:
                print("Invalid option! Try again!\n")
                continue

            print("\ncontinue? ([y]/n)\n")
            sn = input()
            if sn == 'n':
                break
            else:
                continue
            
        break

    elif senha == None or senha == '':
        pag.alert(text="Ok, you've choose to quit!", title="That's fine!", button="See ya")
        break
    else:
        pag.alert(text="Wrong code, try again!", title="Oh No!", button="Sure bro")
        continue


