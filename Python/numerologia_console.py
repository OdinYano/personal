import unicodedata
from datetime import datetime

mensagem = ""

# Função principal que executa o programa
def __main__():   
    # Pede ao usuário para inserir um nome completo
    nome = input("Digite o nome completo: ")
    capitalizar_nome(nome)
    # Prepara o nome removendo espaços em branco e acentos e convertendo para letras minúsculas
    nome = prepara_nome(nome)
    quebra_linha()
    # Busca o dia da semana em que a pessoa nasceu
    data_nascimento = input("Digite a data de nascimento: ")
    # Ajusta a data para um formato correto
    data_nascimento = ajusta_data(data_nascimento)
    monta_mensagem(f"A data de nascimento é {data_nascimento}")
    quebra_linha()
    # Busca o dia da semana em que a pessoa nasceu
    dia_da_semana(data_nascimento)
    quebra_linha()
    # Calcula e imprime o número da personalidade usando apenas consoantes
    descricao_personalidade(nome)
    # Calcula e imprime o número do destino usando apenas vogais
    descricao_destino(nome)
    # Calcula e imprime o número da alma usando todas as letras
    descricao_alma(nome)
    # Calcula e imprime o número do objetivo usando a data de nascimento
    objetivo = objetivo_vida(data_nascimento)
    quebra_linha()
    # Calcula e imprime as deficiencias e excessos usando a data de nascimento e o numero do objetivo de vida
    deficiencias_excessos(data_nascimento, objetivo)
    quebra_linha()
    # Agrupa as letras do nome em grupos específicos e imprime a contagem de cada grupo
    contar_letras(nome)
    global mensagem
    print(mensagem)

def monta_mensagem(texto):
    global mensagem
    mensagem = mensagem + texto
    mensagem = mensagem + "\n"

def capitalizar_nome(nome):
    # Verificar se o nome é válido (não vazio e contém apenas letras e espaços)
    if not nome or not all(c.isalpha() or c.isspace() for c in nome):
        print("Erro: Por favor, insira um nome válido (apenas letras e espaços)")
        return
    # Dividir nome em palavras
    palavras = nome.split()
    # Lista de preposições e artigos que não devem ser capitalizados
    nao_capitalizar = ['da', 'de', 'do', 'das', 'dos', 'a', 'o', 'as', 'os']
    # Capitalizar cada palavra que não está na lista de preposições e artigos
    palavras_capitalizadas = [palavra.capitalize() if palavra not in nao_capitalizar else palavra for palavra in palavras]
    # Juntar as palavras capitalizadas em uma única string
    nome_capitalizado = ' '.join(palavras_capitalizadas)
    global nome_completo
    nome_completo = nome_capitalizado
    monta_mensagem(f"Seu nome é {nome_capitalizado}")

# Ajusta a data para um formato correto    
def ajusta_data(data):
  # Verificar se a data está no formato ddmmyyyy
    if len(data) == 8 and data.isdigit():
        # Ajustar a data para o formato dd/mm/yyyy
        data = f'{data[:2]}/{data[2:4]}/{data[4:]}'
    # Verificar se a data está no formato dd/mm/yyyy
    elif len(data) != 10 or not data[:2].isdigit() or not data[3:5].isdigit() or not data[6:].isdigit() or data[2] != '/' or data[5] != '/':
        # A data não está em nenhum dos formatos válidos
        print('Erro: A data deve estar no formato dd/mm/yyyy ou ddmmyyyy')
        return None
    return data

# Função para preparar o nome removendo espaços em branco e acentos e retornando com apenas letras minúsculas
def prepara_nome(nome):
    # Remover espaços em branco
    nome = nome.replace(" ", "")
    # Converter para minúsculas para considerar letras maiúsculas e minúsculas iguais
    nome = nome.lower()
    # Remover acentos usando o módulo unicodedata
    nome_preparado = ''.join(ch for ch in unicodedata.normalize('NFKD', nome) if not unicodedata.combining(ch))
    return nome_preparado

def dia_da_semana(data_nascimento):
    # Converter a data de nascimento para um objeto datetime
    data = datetime.strptime(data_nascimento, '%d/%m/%Y')
    # Obter o dia da semana como um número (0 = segunda-feira, 6 = domingo)
    dia_da_semana_numero = data.weekday()
    # Mapear o número do dia da semana para o nome do dia da semana
    dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
    monta_mensagem(f"O dia do seu nascimento foi: {dias_da_semana[dia_da_semana_numero]}")

# Função para calcular o número da personalidade (usando apenas consoantes)
def descricao_personalidade(nome):
    # Remover vogais do nome
    nome_personalidade = ''.join([i for i in nome if i not in 'aeiouAEIOU'])
    # Calcular o número da numerologia usando a função soma_nomes
    numero = soma_nomes(nome_personalidade)
    monta_mensagem(f"Personalidade: {numero}")

# Função para calcular o número do destino (usando apenas vogais)
def descricao_destino(nome):
    # Manter apenas vogais no nome
    nome_destino = ''.join([i for i in nome if i in 'aeiouAEIOU'])
    # Calcular o número da numerologia usando a função soma_nomes
    numero = soma_nomes(nome_destino)
    monta_mensagem(f"Destino: {numero}")

# Função para calcular o número da alma (usando todas as letras)
def descricao_alma(nome):
    # Calcular o número da numerologia usando a função soma_nomes
    numero = soma_nomes(nome)
    monta_mensagem(f"Alma: {numero}")

# Função que calcula o objetivo de vida
def objetivo_vida(data):
  # Remover os caracteres '/' da data
    data = data.replace('/', '')
    # Calcular a soma dos dígitos da data
    soma = sum(int(d) for d in data)
    # Repetir o cálculo da soma até obter um valor entre 1 e 9
    while soma > 9:
        soma = sum(int(d) for d in str(soma))
    monta_mensagem(f"Objetivo: {soma}")
    return soma

# Função que calcula as deficiencias e excessos
def deficiencias_excessos(data, objetivo):
    # Dividir a data em partes usando o caractere '/'
    partes = data.split('/')
    # Atribuir cada parte a uma variável separada
    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])
    while dia > 9:
        dia = sum(int(d) for d in str(dia))
    while mes > 9:
        mes = sum(int(d) for d in str(mes))
    while ano > 9:
        ano = sum(int(d) for d in str(ano))
    primeiro_ciclo = 36 - objetivo
    linhas = []
    inicio = 0
    fim = primeiro_ciclo
    linhas.append(f"0{inicio} - {fim}: {calculos_somados(dia, mes)} | {calculos_subtraidos(dia, mes)}")
    inicio = fim +1
    fim = inicio + 8
    linhas.append(f"{inicio} - {fim}: {calculos_somados(dia, ano)} | {calculos_subtraidos(dia, ano)}")
    inicio = fim +1
    fim = inicio + 8
    linhas.append(f"{inicio} - {fim}: {calculos_somados(calculos_somados(dia, mes), calculos_somados(dia, ano))} | {calculos_subtraidos(calculos_subtraidos(dia, mes), calculos_subtraidos(dia, ano))}")
    inicio = fim +1
    linhas.append(f"{inicio} -> ~: {calculos_somados(mes, ano)} | {calculos_subtraidos(mes, ano)}")
    monta_mensagem("As deficiencias e excessos são: ")
    for linha in linhas:
      monta_mensagem(linha)

# Função para repetir o cálculo da soma até obter um valor entre 1 e 9
def calculos_subtraidos(x, y):
    soma = x - y
    if(soma < 0):
      soma *= -1
    while soma > 9:
        soma = sum(int(d) for d in str(soma))
    return soma

# Função para repetir o cálculo da soma até obter um valor entre 1 e 9
def calculos_somados(x, y):
    soma = x + y
    if(soma < 0):
      soma *= -1
    while soma > 9:
        soma = sum(int(d) for d in str(soma))
    return soma

# Função que calcula o número da numerologia de uma string
def soma_nomes(nome_completo):
    # Dicionário que mapeia cada letra para um valor numérico específico
    letras = "abcdefghijklmnopqrstuvwxyz"
    valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8]
    # Calcular a soma dos valores das letras do nome
    soma = sum(valores[letras.index(l)] for l in nome_completo if l in letras)
    # Reduzir a soma para um único dígito
    while soma > 9:
        soma = sum(int(d) for d in str(soma))
    return soma

# Função para agrupar as letras do nome em grupos específicos e imprimir a contagem de cada grupo
def contar_letras(nome):
    # Inicializar contadores para cada grupo de letras
    ajs = 0
    bkt = 0
    clu = 0
    dmv = 0
    enw = 0
    fox = 0
    gpy = 0
    hqz = 0
    ir = 0

    # Iterar sobre as letras do nome e incrementar o contador do grupo correspondente
    for letra in nome:
        match letra:
            case "a" | "j" | "s":
                ajs +=1
            case "b" | "k" | "t":
                bkt +=1
            case "c" | "l" | "u":
                clu +=1
            case "d" | "m" | "v":
                dmv +=1
            case "e" | "n" | "w":
                enw +=1
            case "f" | "o" | "x":
                fox +=1
            case "g" | "p" | "y":
                gpy +=1
            case "h" | "q" | "z":
                hqz +=1
            case "i" | "r":
                ir +=1

    # Imprimir os contadores de cada grupo de letras
    monta_mensagem("Contagem das letras agrupadas:")
    monta_mensagem(f"ajs = {ajs}")
    monta_mensagem(f"bkt = {bkt}")
    monta_mensagem(f"clu = {clu}")
    monta_mensagem(f"dmv = {dmv}")
    monta_mensagem(f"enw = {enw}")
    monta_mensagem(f"fox = {fox}")
    monta_mensagem(f"gpy = {gpy}")
    monta_mensagem(f"hqz = {hqz}")
    monta_mensagem(f"ir  = {ir}")

# Imprimir uma quebra para facilitar a vizualização
def quebra_linha():
  monta_mensagem("====================================================================")

__main__()