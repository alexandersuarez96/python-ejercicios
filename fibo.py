def fibo(num):
    if (num==0):
        return 0
    elif (num==1):
        return 1
    return fibo(num-1)+fibo(num-2)


if (__name__ == '__main__'):
    num = int(input("Numero de elementos:"))
    for i in range (0,num):
        print ((fibo(i)))

