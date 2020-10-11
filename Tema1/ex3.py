phone_int = input("Introduceti numarul de telefon  in format 07XXXXXXXX urmat de tasta ENTER: ")
phoneisvalid_bol = True
userphone_str = str(phone_int)

if userphone_str[0] == "0" and userphone_str[1] == "7" and len(userphone_str) == 10:
    for counter_int in range(0, 9, 1):
        if not userphone_str[counter_int].isdigit():
            phoneisvalid_bol = False
            print(userphone_str[counter_int])
            print("Numarul de telfon trebuie sa contian doar cifre!")

elif userphone_str[0] != "0" or userphone_str[1] != "7" or len(userphone_str) != 10:
    print(userphone_str[0], userphone_str[1], len(userphone_str))
    phoneisvalid_bol = False
    print("Eroare de format!")

if phoneisvalid_bol:
    print("Numarul de telefon este valid!")
elif not phoneisvalid_bol:
    print("Numarul de telefon NU este valid!")
