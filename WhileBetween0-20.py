numero = int(input("Escriba un número entre 0 y 20 "))
while numero <= 0 or numero >= 20:
    print("Este número no está entre 0 y 20")
    numero = int(input("Escriba un número entre 0 y 20 "))
print(numero)