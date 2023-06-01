def numeros_primos(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(2, 201):
    if numeros_primos(i):
        print(i)
