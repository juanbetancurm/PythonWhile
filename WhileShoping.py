#Declaración

monto = None
acumulado = 0
final = None

#Ingreso

monto = int(input("Type the value of the first object and press enter or press 0 and enter to exit"))

#Procesamiento de información

while monto != 0:
    if monto < 0:
        print("Type a valid value ")
        monto = input("Type the value of the first object and press enter ")
    else:
        acumulado = acumulado + monto
        monto = input("Type the value of the next object or 0 to exit ")

if monto >= 1000:
    final = acumulado*0.9
    print("Thanks for using our service. You have a total of:", acumulado)
    print("However, you have a 10 percent discount and your final charge is: ", final)
else:
    print("Thanks for using our service.")

