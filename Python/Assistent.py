import pyttsx3
import datetime
import speech_recognition as sr
import time
import tensorflow as tf
from tensorflow import keras
import pandas as pd


# Carregando os dados de treinamento
data = pd.read_csv('treinamento.csv')
perguntas = data['Pergunta'].values
respostas = data['Resposta'].values

# Pré-processando os dados de treinamento
tokenizer = keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(perguntas)
X_train = tokenizer.texts_to_sequences(perguntas)
maxlen = max([len(x) for x in X_train])
X_train = keras.preprocessing.sequence.pad_sequences(X_train, maxlen=maxlen)

# Codificando as respostas
label_tokenizer = keras.preprocessing.text.Tokenizer()
label_tokenizer.fit_on_texts(respostas)
y_train = label_tokenizer.texts_to_sequences(respostas)

# Criando o modelo
model = keras.Sequential()
model.add(keras.layers.Embedding(len(tokenizer.word_index)+1, 64, input_length=maxlen))
model.add(keras.layers.Bidirectional(keras.layers.LSTM(20)))
model.add(keras.layers.Dense(len(label_tokenizer.word_index)+1, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')

# Treinando o modelo
model.fit(X_train, y_train, epochs=10)

def get_response(user_input):
    # Pré-processando a entrada do usuário
    user_input = tokenizer.texts_to_sequences([user_input])
    user_input = keras.preprocessing.sequence.pad_sequences(user_input, maxlen=maxlen)
    
    # Fazendo a previsão
    prediction = model.predict(user_input)
    index = prediction.argmax()
    
    # Decodificando a resposta
    response = label_tokenizer.sequences_to_texts([[index]])[0]
    
    return response

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
