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
            while decision == "y":
                value = segundo
                segundo = primero + segundo
                primero = value
                print(segundo)
                decision = input("Do you want to know the next value in the sequence? y or n: ")
            print("Thanks")
        else:
            print("Thanks")
    else:
        print("Thanks")
else:
    print("Thanks")