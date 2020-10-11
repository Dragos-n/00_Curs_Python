usermail_str = input("Introduceti adresa de email urmata de tasta ENTER: ")
mailisvalid_bol = True
counter_int = 0

# test for count of @  and count of .
if usermail_str.count("@") != 1:
    mailisvalid_bol = False

elif usermail_str.count(".") != 1:
    mailisvalid_bol = False

elif usermail_str.count("@") == 1 and usermail_str.count(".") == 1:

    # test before @
    while usermail_str[counter_int] != "@":
        if not (usermail_str[counter_int].isdigit()) and not (usermail_str[counter_int].isalpha()):
            mailisvalid_bol = False
            break
        counter_int += 1

    counter_int += 1  # increment to get over @ character

    # test between @ and .
    while usermail_str[counter_int] != ".":
        if not (usermail_str[counter_int].isdigit()) and not (usermail_str[counter_int].isalpha()):
            mailisvalid_bol = False
            break
        counter_int += 1

    # test after .
    for counter_int in range(counter_int + 1, len(usermail_str), 1):
        if not usermail_str[counter_int].isalpha():
            mailisvalid_bol = False
            break

if mailisvalid_bol:
    print("Aderesa este valida!")
elif not mailisvalid_bol:
    print("Adrea NU este valida!")
