#     /#\
#    /###\
#   /#####\
#  /#######\
# /#########\
#|###########|
# \#########/
#  \#######/
#   \#####/
#    \###/
#     \#/
#
# Desafio do diamnte:
# Fazer com que o retorno seja o desenho de um diamante proporcional ao numero informado.
# 

def primeira_parte(n):
    inicio = int(n/2)
    contador = 1
    for i in range(inicio):
        linha  = " "
        for j in range(n):
            if (j < inicio- 1):
                linha = (linha+ " ")
            elif (j == inicio- 1):
                linha = (linha+ "/")
                for x in range(i+ contador):
                    if (x % 2 == 0):
                        linha = (linha+ "#")
                    else:
                        linha = (linha+ " ")
                linha = (linha+ "\\")
                contador = (contador+ 1)
                inicio = (inicio- 1)
                print(linha)
                break
    
def meio(n):
    linha = "|"
    for i in range(n+1):
        if (i == n):
            linha = (linha+ "|")
        else:
            if (i % 2 == 0):
                linha = (linha+ " ")
            else:
                linha = (linha+ "#")
    print(linha)

def segunda_parte(n):
    inicio = 1
    contador = (n- 1)
    for i in range(int(n/ 2)):
        linha  = " "
        for j in range(n):
            if (j < inicio- 1):
                linha = (linha+ " ")
            elif (j == inicio- 1):
                linha = (linha+ "\\")
                for x in range(contador):
                    if (x % 2 == 0):
                        linha = (linha+ "#")
                    else:
                        linha = (linha+ " ")
                linha = (linha+ "/")
                contador = (contador- 2)
                inicio = (inicio+ 1)
                print(linha)
                break

def __main__():
    while True:
        tamanho = int(input("Digite o tamanho do cristal ou 0 para sair: "))
        if tamanho == 0:
            print("Programa finalizado!")
            break
        if (tamanho % 2 == 0):
            primeira_parte(tamanho)
            segunda_parte(tamanho)
        else:
            metade = int((tamanho-1))
            primeira_parte((metade))
            meio(tamanho)
            segunda_parte((metade))
    
__main__()
