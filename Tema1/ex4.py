import datetime

str_cnp = str(input("Introduceti CNP-ul: "))
bol_cnp_valid = True
date_dict = {1: 19, 2: 19, 3: 18, 4: 18, 5: 20, 6: 20}
year_to_test = 0

# Verificare lungime CNP
if len(str_cnp) != 13:
    bol_cnp_valid = False
    print("Ati intodurs prea multe caractere!")

# Verificare caractere numerice din CNP
if bol_cnp_valid:
    for count in range(0, 12):
        if not(str_cnp[count].isdigit()):
            bol_cnp_valid = False
            print("CNP-ul trebuie sa contina doar caractere numerice!")

# Verificare prima cifra din CNP
if bol_cnp_valid:
    if str_cnp[0] == "0":
        bol_cnp_valid = False
        print("Prima cifra din CNP nu poate fi 0!")

# Construie data de nastere din CNP
if bol_cnp_valid:
    if int(str_cnp[0]) in date_dict.keys():
        year_to_test = str(date_dict.get(int(str_cnp[0]))) + str_cnp[1] + str_cnp[2]
    elif str_cnp[0] in ["7", "8", "9"]:
        year_to_test = "20" + str_cnp[1] + str_cnp[2]
    month_to_test = str_cnp[3] + str_cnp[4]
    date_to_test = str_cnp[5] + str_cnp[6]

# Verificare data valida
if bol_cnp_valid:
    try:
        date_to_test = datetime.datetime(int(year_to_test), int(str_cnp[3] + str_cnp[4]),
                                         int(str_cnp[5] + str_cnp[6]))
    except ValueError:
        bol_cnp_valid = False
        print("Data nasterii din CNP nu este valida!")

# Verificare judet
if bol_cnp_valid:
    if not int(str(str_cnp[7] + str_cnp[8])) in range(1, 46) and not int(str(str_cnp[7] + str_cnp[8])) in range(51, 52):
        bol_cnp_valid = False
        print("Codul judatului din CNP nu este valid!")

# Verificare numar odine
if bol_cnp_valid:
    if int(str_cnp[9] + str_cnp[10] + str_cnp[11]) == 0:
        bol_cnp_valid = False
        print("Numarul de ordine nu poate fi 0!")

# Calcul cifra de control
if bol_cnp_valid:
    cnp_check = "279146358279"
    sum_of_cnp = 0
    for count in range(0, 12):
        sum_of_cnp = sum_of_cnp + int(str_cnp[count]) * int(cnp_check[count])

# Verificare cifra de control
    if int(sum_of_cnp) % 11 == 0:
        sum_of_cnp = 1
    else:
        sum_of_cnp = sum_of_cnp % 11
    if int(str_cnp[12]) != sum_of_cnp:
        bol_cnp_valid = False
        print("Cifra de control nu este corecta!")

if bol_cnp_valid:
    print("CNP Valid!")
else:
    print("CNP INALID!")
