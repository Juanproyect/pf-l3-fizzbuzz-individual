#forma 1

for iteracion in range(1, 1001):
     if iteracion % 3 == 0 and iteracion % 5 == 0:   
         print("Fizzbuzz")
     elif iteracion % 3 == 0:
         print("Fizz")
     elif iteracion % 5 == 0:
       print("Buzz")
     else:
         print(iteracion)

#comando "cls" para limpiar la consola en windows
#comando "clear" para limpiar la consola en linux o mac
#comando "ctrl + k + c" para comentar varias lineas de codigo en visual studio code

#forma 2
# interacion ={1: "1", 2: "2", 3: "Fizz", 4: "4", 5: "Buzz", 6: "Fizz", 7: "7", 8: "8", 9: "Fizz", 10: "Buzz",}

# print(interacion)