numero = 0
numero_in = 0
#numero_in = int(input("Escriba números para sumar hasta 100 "))
#numero = numero + numero_in

while numero < 100 and numero != 100:
    print(numero)
    numero_in = int(input("Escriba otro número para sumar hasta 100 "))
    numero = numero + numero_in
    
print("Finalmente, su suma es ", numero)