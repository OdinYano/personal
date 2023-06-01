def fatorar(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def __main__():
    while True:
        num = int(input("Digite um numero inteiro maior que 2: "))
        if num < 2:
            print("Programa finalizado!")
            break
        print(f'Os fatores primos de {num} são: {fatorar(num)}')
    
__main__()

