primero = 0
segundo = 1
decision = None
value = None

decision = input("Do you want to know the first value of the Fibonacci Sequence? y or n: ")

if decision == "y":
    print(primero)
    decision = input("Do you want to know the next value in the sequence? y or n: ")
    if decision == "y":
        print(segundo)
        decision = input("Do you want to know the next value in the sequence? y or n: ")
        if decision == "y":
            segundo = primero + segundo
            print(segundo)
            decision = input("Do you want to know the next value in the sequence? y or n: ")
            if decision == "y":
                while decision == "y":
                    value = value + segundo
                    segundo = value
                    print (value)
                    decision = input("Do you want to know the next value in the sequence? y or n: ")
                print("Thanks")
            else:
                print("Gracias")
        else:
            print("Gracias")
    else:
        print("Gracias")
else:
    print("Gracias")