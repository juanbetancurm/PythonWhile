#Declaración

monto = 0
acumulado = 0
final = 0

#Ingreso

monto = int(input("Type the value of the first object and press enter or press 0 and enter to exit "))

#Procesamiento de información Chequeo por cantidad diferente de 0

while monto != 0:

#Condicional que, una vez descartado el valor cero clasifica las acciones para negativo o positivo

    if monto < 0:
        monto = int(input("Negative prices are not allowed, type a valid quantity: "))
    else:    
        acumulado = acumulado + monto
        monto = int(input("Type a new price to add, please: "))

#Acción tras presionar 0, condicional que clasifica si el monto aplica para descuento

if acumulado > 1000:
    final = acumulado*0.9
    print("Your total is: ", acumulado)
    print("Your final amount with a discount of 10%: ", final)
else:
    print("Your total is: ", acumulado)
    print("Thanks for using our service.")