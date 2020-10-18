# Set
# s = {1, 7, 'A', 3, 4, 5}
# a = {'a', 'b'}

# # List
# a = [1, 2, 3]
# b = [4, 5, 2]
# print(set(b) - set(a))
#
# # Dictionar
#
# a = {"3": 3,
#      1: "abv",
#      "2": [1, 2, 3],
#      (1, 2): "a"}
# print(a)
# a["2"] = "abc"  # suprascriere valoare
# print(a)
# a[2] = "ion" # adaugare de cheie + element nou
# print(a)

# for i in range(10, 0, -1):
#     print(i)
lista =[]
aux = input("Adaugati un nou task: ")

while aux != '0':
    lista.append(aux)
    aux = input("Adaugati un nou task: ")

print(lista)