import pyttsx3
import datetime
import speech_recognition as sr
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Carregando os dados de treinamento
data = pd.read_csv('treinamento.csv')
perguntas = data['Pergunta'].values
respostas = data['Resposta'].values

# Criando o vetorizador
vectorizer = TfidfVectorizer()
vectorizer.fit(perguntas)

def get_response(user_input):
    # Vetorizando a entrada do usuário
    user_input_vector = vectorizer.transform([user_input])
    
    # Calculando a similaridade com as perguntas de treinamento
    similarity = cosine_similarity(user_input_vector, vectorizer.transform(perguntas))
    
    # Encontrando a pergunta mais similar
    index = similarity.argmax()
    
    # Retornando a resposta correspondente
    return respostas[index]

# Função da fala
texto_fala = pyttsx3.init()

def falar(audio):
    # Velocidade da fala
    rate = texto_fala.getProperty('rate')
    texto_fala.setProperty("rate", 150)
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
    mes = now.strftime("%B")
    ano = now.strftime("%Y")
    falar(f"A data atual é {dia}, de {mes}, de {ano}")

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
    except sr.RequestError:
        mensagem = "O serviço de reconhecimento de fala não está disponível."
        print(mensagem)
        falar(mensagem)
        comando = ""
    
    return comando

# Função principal
if __name__ == "__main__":
    bem_vindo()

    while True:
        print("Escutando...")
        comando = microfone().lower()

        if 'horas são' in comando:
            tempo()
        elif 'data de hoje' in comando:
            data()
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
            falar(get_response(comando))
