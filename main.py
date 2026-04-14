for iteracion in range(1, 1001):
    if iteracion % 3 == 0 and iteracion % 5 == 0:   
        print("Fizzbuzz")
    elif iteracion % 3 == 0:
        print("Fizz")
    elif iteracion % 5 == 0:
        print("Buzz")
    else:
        print(iteracion)


        