numero = 0
numero_in = 0
numero_in = int(input("Escriba números diferentes de cero para sumar "))

//Inicia el While
while numero_in != 0:
    numero = numero + numero_in
    print(numero)
    numero_in = int(input("Escriba un número diferente de cero para sumar "))

print("Usted ingresó cero, su suma es:", numero)
