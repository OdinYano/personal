import pyttsx3
import datetime
import speech_recognition as sr
import time
from selenium import webdriver
from selenium.webdriver.common import keys
import re


# Função da fala
texto_fala = pyttsx3.init()

def falar(audio):
    # Velocidade da fala
    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty("rate", 140)
    # Seleciona a voz
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice', voices[2].id)
    # Recebe o áudio para a fala
    texto_fala.say(audio)
    texto_fala.runAndWait()

# Função que busca a hora atual
def tempo():
    Tempo = datetime.datetime.now().strftime("%I:%M")
    falar(f"Agora são: {Tempo}")

# Função que busca a data atual
def data():
    now = datetime.datetime.now()
    dia = now.strftime("%d")
    mes = traduz_mes(now.strftime("%B"))
    ano = now.strftime("%Y")
    falar(f"A data atual é {dia}, de {mes}, de {ano}")

def traduz_mes(mes):

  traducao = {
    "January": "Janeiro",
    "February": "Fevereiro",
    "March": "Março",
    "April": "Abril",
    "May": "Maio",
    "June": "Junho",
    "July": "Julho",
    "August": "Agosto",
    "September": "Setembro",
    "October": "Outubro",
    "November": "Novembro",
    "December": "Dezembro",
  }

  return traducao.get(mes)

# Função de início do programa    
def bem_vindo():
    # Busca a hora atual
    hora = int(datetime.datetime.now().hour)
    # Define o tipo de saudação
    if hora >= 6 and hora < 12:
        saudacao = "Bom dia!"
    elif hora >= 12 and hora < 18:
        saudacao = "Boa tarde!"
    else:
        saudacao = "Boa noite!"
    # Monta a frase inicial
    falar(f"{saudacao} Bem vindo, ")
    tempo()
    data()
    falar("Em que posso ajudar?")

# Função de entrada de dados por voz
def microfone():
    r = sr.Recognizer()
    print("Escutando...")
    
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Reconhecendo...")
        comando = r.recognize_google(audio, language='pt')
        print(comando)

    except sr.UnknownValueError:
        mensagem = "Não foi possível reconhecer a fala. Por favor, repita."
        print(mensagem)
        falar(mensagem)
        comando = ""
        microfone()
        
    except sr.RequestError:
        mensagem = "O serviço de reconhecimento de fala não está disponível."
        print(mensagem)
        falar(mensagem)
        comando = ""
        microfone()
    
    return comando

def previsao_tempo():
    previsao = ""
    navegador = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    navegador = webdriver.Chrome(options=options)
    falar("Para a previsão do tempo, preciso que responda duas perguntas primeiro a cidade depois a sigra do estado. Diga o nome da cidade: ")
    cidade = microfone().lower().replace(" ","-")
    falar("Agora a sigla do estado: ")
    
    cidade = (f"{cidade}-{microfone().lower()}")

    navegador.get(f'https://www.otempo.com.br/tempo/{cidade}')
    previsao = str(navegador.find_element('id','link-5425').text)
    palavra_inicio = "PREVISÃO"
    palavra_fim = "ºC"
    start_index = previsao.find(palavra_inicio)
    end_index = previsao.find(palavra_fim, start_index) + len(palavra_fim)
    previsao.replace('\n',' , ')

    print(previsao[start_index:end_index])
    falar(previsao[start_index:end_index])

def extrair_calculo(comando):
    expressao = str(comando)
    numeros = re.findall(r'\d+', expressao)
    primeiro_numero = numeros[0]
    ultimo_numero = numeros[-1]
    inicio = expressao.find(primeiro_numero) + len(primeiro_numero)
    fim = expressao.rfind(ultimo_numero)
    conteudo = expressao[inicio:fim].strip()
    if '+' in conteudo:
        resposta = (int(numeros[0])+ int(numeros[-1]))
    elif '-' in conteudo:
        resposta = (int(numeros[0])- int(numeros[-1]))
    elif '*' in conteudo or 'x' in conteudo or 'vezes' in conteudo:
        resposta = (int(numeros[0])* int(numeros[-1]))
    elif '/' in conteudo or 'dividido' in conteudo:
        resposta = (int(numeros[0])/ int(numeros[-1]))
    falar(str(resposta))

def resposta_bucador(pergunta):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")

    #navegador = webdriver.Chrome(options=options)
    navegador = webdriver.Chrome()
    navegador.get('https://google.com.br')
    pesquisa = navegador.find_element('id','APjFqb')
    pesquisa.send_keys(f"{pergunta} \n ")

    time.sleep(5)
    
    resposta = navegador.find_element('id','kp-wp-tab-overview').text

    palavra_inicio = "Descrição"
    palavra_fim = "― Google"
    start_index = resposta.find(palavra_inicio)+ 9
    end_index = resposta.find(palavra_fim, start_index) + len(palavra_fim)
    if end_index < 9:
        palavra_fim = "Wikipédia"
        end_index = resposta.find(palavra_fim, start_index) + len(palavra_fim)
    resposta.replace('\n',' , ')

    print(resposta[start_index:end_index])
    falar(resposta[start_index:end_index])
    
# Função principal
if __name__ == "__main__":
    bem_vindo()

    while True:
        comando = ""
        comando = microfone().lower()

        if 'horas são' in comando or 'hora é' in comando:
            tempo()
        elif 'data de hoje' in comando:
            data()
        elif 'previsão' in comando:
            previsao_tempo()
        elif ' + ' in comando or ' - ' in comando or ' x ' in comando or ' / ' in comando or ' vezes ' in comando or ' mais ' in comando or ' menos ' in comando:
            extrair_calculo(comando)
        elif 'pare de escutar' in comando:
            falar("Por quantos minutos você deseja que eu pare de escutar?")
            resposta = int(microfone())
            falar(f"Entendido, voltarei em {str(resposta)} minutos.")
            time.sleep(resposta * 60)
            bem_vindo()
        elif 'desligar' in comando:
            falar("Até logo!")
            quit()
        else:
            resposta_bucador(comando)

        falar("Posso ajudar em mais alguma coisa?")

