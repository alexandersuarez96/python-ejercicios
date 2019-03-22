def primo (n):
    for x in range(2, n):
        for i in range(2, x):
            if x % i != 0:
                # si i no es divisor de x, x puede ser primo
                continue
            else:
                # si i es divisor de x, x no es primo
                break  # No es necesario buscar más divisores
        else:
            print('', x)
if (__name__ == '__main__'):
    n=int(input("digite un numero: "))
    primo(n)
