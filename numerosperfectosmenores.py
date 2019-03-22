def perfectos(num):
    for i in range(2, num):
        b = 0
        for j in range(1, (i // 2) + 1):
         if (i % j == 0):
                b = b + j
        if (b == i):
         print("", i)

if(__name__=='__main__'):
    num=int(input("Digite un numero"))
    perfectos(num)

