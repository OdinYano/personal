# pip install chatterbot==1.0.4

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Crie um chatbot
chatbot = ChatBot('MeuChatBot')

# Treine o chatbot com base em um conjunto de dados de conversas pré-existentes
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.portuguese.greetings", "chatterbot.corpus.portuguese.conversations")

# Inicie o loop principal do chatbot
while True:
    try:
        # Obtenha a entrada do usuário
        user_input = input("Você: ")

        if user_input == "sair":
          # Se o usuário digitar "sair", encerre o loop principal
          print("Bot: Até mais!")
          break
        else:
          # Obtenha a resposta do chatbot
          bot_response = chatbot.get_response(user_input)

          # Imprima a resposta do chatbot
          print("Bot: ", bot_response)

    # Se o usuário digitar "sair", encerre o loop principal
    except (KeyboardInterrupt, EOFError, SystemExit):
        break