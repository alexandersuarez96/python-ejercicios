def factorial(n):
    fact = (1)
    while (n != 0):
        fact = n * fact
        n = n - 1
    print ("el factorial del numero ingresado->", fact)
if (__name__ == '__main__'):
    n=int(input("Digite un numero"))
    factorial(n)