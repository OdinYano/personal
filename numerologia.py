from tkinter import *
import pyttsx3

corFundo = '#00CED1'
fonte = ["News701 BT Bold", "12", "bold"]
# Função da fala
texto_fala = pyttsx3.init()

class Application:
    def __init__(self, master=None):
        self.fontePadrao = fonte
        self.fundoPadrao = corFundo
        self.primeiroContainer = Frame(master, bg=self.fundoPadrao)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer["padx"] = 10
        self.primeiroContainer.place(relx=0.01, rely=0.07, relwidth=0.2, relheight=0.1)

        self.segundoContainer = Frame(master, bg=self.fundoPadrao)
        self.segundoContainer["pady"] = 10
        self.segundoContainer["padx"] = 20
        self.segundoContainer.place(relx=0.2, rely=0.04, relwidth=0.6, relheight=0.1)

        self.personalidadeContainer = Frame(master, bg=self.fundoPadrao)
        self.personalidadeContainer["pady"] = 10
        self.personalidadeContainer["padx"] = 20
        self.personalidadeContainer.place(relx=0.85, rely=0.05, relwidth=0.1, relheight=0.1)

        self.destinoContainer = Frame(master, bg=self.fundoPadrao)
        self.destinoContainer["pady"] = 10
        self.destinoContainer["padx"] = 20
        self.destinoContainer.place(relx=0.85, rely=0.10, relwidth=0.1, relheight=0.1)

        self.almaContainer = Frame(master, bg=self.fundoPadrao)
        self.almaContainer["pady"] = 10
        self.almaContainer["padx"] = 20
        self.almaContainer.place(relx=0.85, rely=0.15, relwidth=0.1, relheight=0.1)

        self.leremvozalta = Frame(master, bg=self.fundoPadrao)
        self.leremvozalta["pady"] = 10
        self.leremvozalta["padx"] = 20
        self.leremvozalta.place(relx=0.85, rely=0.20, relwidth=0.1, relheight=0.1)

        self.quartoContainer = Frame(master, bg=self.fundoPadrao)
        self.quartoContainer["pady"] = 10
        self.quartoContainer["padx"] = 50
        self.quartoContainer.place(relx=0.02, rely=0.25, relwidth=0.96, relheight=0.7)

        self.titulo = Label(self.primeiroContainer, text="Digite seu nome:", bg=self.fundoPadrao)
        self.titulo["font"] = self.fontePadrao
        self.titulo.pack()

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 100
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.autenticar = Button(self.personalidadeContainer)
        self.autenticar["text"] = "Personalidade"
        self.autenticar["font"] = self.fontePadrao
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.descricao_personalidade
        self.autenticar.pack()

        self.autenticar = Button(self.destinoContainer)
        self.autenticar["text"] = "Destino"
        self.autenticar["font"] = self.fontePadrao
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.descricao_destino
        self.autenticar.pack()

        self.autenticar = Button(self.almaContainer)
        self.autenticar["text"] = "Alma"
        self.autenticar["font"] = self.fontePadrao
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.descricao_alma
        self.autenticar.pack()

        self.autenticar = Button(self.leremvozalta)
        self.autenticar["text"] = "Ler em voz Alta"
        self.autenticar["font"] = self.fontePadrao
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.falar
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao, bg=self.fundoPadrao)        
        self.mensagem.place(relx=0.02, rely=0.2, relwidth=0.96, relheight=0.7)

    # função para retornar a descrição da personalidade (Consoantes)
    def descricao_personalidade(self):
        nome_personalidade = ''.join([i for i in self.nome.get() if i not in 'aeiouAEIOU'])
        numero = soma_nomes(nome_personalidade)
        if numero == 1:
            self.mensagem["text"] = str(numero)+" -  Se o nome da pessoa retorna o número 1 através da numerologia, significa que essa pessoa tem uma personalidade criativa,\n\
independente e ambiciosa. Ela tem uma mente aberta e está sempre disposta a experimentar coisas novas. Gosta de liderar e \n\
tem uma grande força de vontade para alcançar seus objetivos.\n\
Pessoas com o número 1 são frequentemente vistas como pioneiras e\n\
empreendedoras. Elas têm uma paixão pela inovação e uma habilidade para identificar novas oportunidades de negócios.\n\
Elas têm uma abordagem muito proativa para a vida, buscando sempre maneiras de se destacar e realizar grandes coisas.\n\
Essas pessoas geralmente têm um forte senso de autoconfiança e são muito seguras de si mesmas.\n\
Elas tendem a ser líderes naturais e muitas vezes são vistas como inspirações para aqueles ao seu redor.\n\
Elas também têm uma forte motivação e perseverança, nunca desistindo facilmente de seus objetivos.\n\
No entanto, as pessoas com o número 1 também podem ser teimosas e impacientes às vezes.\n\
Elas tendem a querer que as coisas sejam feitas do seu jeito e podem se frustrar facilmente com a falta de progresso.\n\
Por causa disso, elas precisam trabalhar para manter uma mente aberta e estar dispostas a considerar outras opções.\n\
No geral, as pessoas com o número 1 têm um grande potencial para o sucesso. Com sua criatividade, independência e ambição,\n\
elas têm a capacidade de alcançar grandes coisas em qualquer área que escolherem seguir."
        elif numero == 2:
            self.mensagem["text"] = str(numero)+" -  Se o nome da pessoa retorna o número 2 através da numerologia, significa que essa pessoa tem uma personalidade diplomática,\n\
sensível e cooperativa. Ela tem uma forte capacidade de se conectar com outras pessoas e é frequentemente vista como um bom ouvinte e conselheiro.\n\
Pessoas com o número 2 tendem a ser muito sensíveis às necessidades e emoções dos outros.\n\
Elas têm uma habilidade natural para lidar com conflitos e trabalhar para encontrar soluções que sejam mutuamente tolerantes para todas as partes envolvidas.\n\
Elas são muitas vezes vistas como mediadoras e pacificadoras em situações difíceis.\n\
Essas pessoas geralmente têm um grande senso de empatia e compaixão.\n\
Elas são muito cuidadosas e atenciosas com as pessoas ao seu redor, muitas vezes trabalhando como necessidades dos outros antes das suas próprias.\n\
Elas também tendem a ser muito intuitivas e têm uma habilidade para entender as emoções e motivações dos outros sem que sejam ditas.\n\
No entanto, as pessoas com o número 2 também podem ser muito indecisas e inseguras em suas próprias decisões.\n\
Elas podem ter dificuldade em se colocar em primeiro lugar e tomar decisões que sejam melhores para elas mesmas.\n\
Elas precisam trabalhar para desenvolver a autoconfiança e a habilidade de tomar decisões firmes e seguras.\n\
No geral, as pessoas com o número 2 têm um grande potencial para trabalhar em áreas como aconselhamento, psicologia, educação e relações públicas.\n\
Com sua diplomacia, sensibilidade e habilidade para se conectar com as pessoas, \n\
elas podem fazer uma grande diferença na vida dos outros e tornar o mundo um lugar mais harmonioso."
        elif numero == 3:
            self.mensagem["text"] = str(numero)+" -  Se o nome da pessoa retorna o número 3 através da numerologia, significa que essa pessoa tem uma personalidade expressiva, criativa e sociável.\n\
Ela tem uma grande habilidade para se comunicar e pode ser muito eloquente em suas lembranças com os outros.\n\
Pessoas com o número 3 tendem a ser muito otimistas e alegres.\n\
Elas têm uma atitude positiva em relação à vida e buscam sempre encontrar alegria e diversão em tudo o que fazem.\n\
Elas também são muito criativas e têm uma grande habilidade para se expressar através da arte, música, escrita ou outras formas de expressão criativa.\n\
Essas pessoas geralmente têm uma personalidade muito sociável e são vistas como divertidas e encantadoras pelos outros.\n\
Eles têm uma grande habilidade para se conectar com pessoas de todas as idades e origens e são frequentemente vistos como líderes em grupos sociais ou comunitários.\n\
No entanto, as pessoas com o número 3 também podem ser um pouco dispersas e transformadas em seus interesses.\n\
Elas podem ter dificuldade em se concentrar em uma tarefa única por um longo período de tempo e podem precisar de estímulos constantes para manter o interesse em algo.\n\
No geral, as pessoas com o número 3 têm um grande potencial para trabalhar em áreas como comunicação, marketing, entretenimento e artes.\n\
Com sua habilidade para se expressar criativamente e se conectar com as pessoas,\n\
elas podem ser muito bem-sucedidas em áreas que envolvem a comunicação e a interação com os outros."
        elif numero == 4:
            self.mensagem["text"] = str(numero)+" -  Se o nome da pessoa retorna o número 4 através da numerologia, significa que essa pessoa tem uma personalidade prática, confiável e responsável.\n\
Ela tem uma grande habilidade para lidar com tarefas complexas e pode ser muito organizada e metódica em suas atividades.\n\
Pessoas com o número 4 tendem a ser muito resistentes e livres.\n\
Elas são vistas como pessoas muito responsáveis ​​e trabalhadoras, que se dedicam completamente a tudo o que fazem.\n\
Elas são muito ansiosas e se orgulham de cumprir seus compromissos e obrigações.\n\
Essas pessoas geralmente têm uma personalidade muito prática e orientada para os detalhes.\n\
Elas têm uma grande habilidade para planejar e executar tarefas complexas de forma eficiente e eficaz.\n\
Elas também são muito persistentes e determinadas, e não desistiram facilmente diante de um desafio.\n\
No entanto, as pessoas com o número 4 também podem ser um pouco inflexíveis e teimosas em suas crenças.\n\
Elas podem ter dificuldade em se adaptar às mudanças ou aceitar ideias novas e diferentes das suas.\n\
Elas precisam trabalhar para desenvolver uma mente mais aberta e flexível para lidar com situações imprevisíveis.\n\
No geral, as pessoas com o número 4 têm um grande potencial para trabalhar em áreas como finanças, contabilidade, engenharia e construção.\n\
Com sua habilidade para lidar com tarefas complexas e sua personalidade confiável e responsável,\n\
elas podem ser muito bem sucedidas em áreas que tiveram atenção aos detalhes e organização."
        elif numero == 5:
            self.mensagem["text"] = str(numero)+" -  Se o nome da pessoa retorna o número 5 através da numerologia, significa que essa pessoa tem uma personalidade enérgica, aventureira e adaptável.\n\
Ela tem uma grande habilidade para lidar com situações imprevisíveis e pode ser muito versátil em suas atividades.\n\
Pessoas com o número 5 tendem a ser muito curiosas e inquietas.\n\
Elas são vistas como pessoas muito ativas e que gostam de experimentar coisas novas.\n\
Elas têm uma grande habilidade para se adaptar a mudanças e lidar com situações imprevisíveis.\n\
Essas pessoas geralmente têm uma personalidade muito sociável e comunicativa.\n\
Elas têm uma grande habilidade para se conectar com pessoas de diferentes origens e culturas e são vistas como pessoas muito extrovertidas e amigáveis.\n\
Elas também são muito criativas e têm uma grande habilidade para se expressar artisticamente.\n\
No entanto, as pessoas com o número 5 também podem ser um pouco impulsivas e impacientes em suas decisões.\n\
Elas podem ter dificuldade em se comprometer com uma única atividade ou projeto por um longo período de tempo e podem precisar de mudanças frequentes para se manterem motivadas.\n\
No geral, as pessoas com o número 5 têm um grande potencial para trabalhar em áreas como marketing, vendas, jornalismo e turismo.\n\
Com sua habilidade para se adaptar a diferentes situações e se comunicar com as pessoas,\n\
elas podem ser muito bem-sucedidas em áreas que tenham versatilidade e habilidades de comunicação."
        elif numero == 6:
            self.mensagem["text"] = str(numero)+" -  Se o nome da pessoa retorna o número 6 através da numerologia, significa que essa pessoa tem uma personalidade equilibrada, amorosa e responsável.\n\
Ela tem uma grande habilidade para lidar com questões emocionais e pode ser muito atenciosa com as pessoas ao seu redor.\n\
Pessoas com o número 6 tendem a ser muito preocupadas com a harmonia e a paz ao seu redor.\n\
Elas são vistas como pessoas muito amorosas e que se preocupam com o bem-estar dos outros.\n\
Elas têm uma grande habilidade para lidar com questões emocionais e são vistas como pessoas muito empáticas e compreensivas.\n\
Essas pessoas geralmente têm uma personalidade muito responsável e confiável.\n\
Elas têm uma grande habilidade para cuidar das necessidades das pessoas ao seu redor e são vistas como pessoas muito comprometidas com seus relacionamentos e obrigações.\n\
No entanto, as pessoas com o número 6 também podem ser um pouco críticas e perfeccionistas em suas expectativas dos outros.\n\
Elas podem ter dificuldade em lidar com conflitos e podem ser um pouco inflexíveis em suas crenças.\n\
No geral, as pessoas com o número 6 têm um grande potencial para trabalhar em áreas como aconselhamento, educação, cuidados de saúde e serviços sociais.\n\
Com sua habilidade para lidar com questões emocionais e seu compromisso com a harmonia e bem-estar dos outros,\n\
elas podem ser muito bem aceitas em áreas que envolvem cuidado e atenção às necessidades das pessoas."
        elif numero == 7:
            self.mensagem["text"] = str(numero)+" -  Se o nome da pessoa retorna o número 7 através da numerologia, significa que essa pessoa tem uma personalidade profunda, introspectiva e analítica.\n\
Ela tem uma grande habilidade para pensar criticamente e pode ser muito reservada em sua abordagem com as pessoas ao seu redor.\n\
Pessoas com o número 7 tendem a ser muito focadas em sua busca por conhecimento e sabedoria.\n\
Elas são vistas como pessoas muito intelectuais e que têm uma grande capacidade de reflexão e análise.\n\
Elas têm uma grande habilidade para se concentrar em tarefas complexas e podem ser muito perspicazes em suas observações.\n\
Essas pessoas geralmente têm uma personalidade muito reservada e introspectiva.\n\
Elas preferem passar o tempo sozinhas em vez de estar cercadas por muitas pessoas.\n\
Elas são vistas como pessoas muito misteriosas e que podem ser difíceis de entender em um primeiro momento.\n\
No entanto, as pessoas com o número 7 também podem ser um pouco distantes e céticas em suas confortáveis ​​com os outros.\n\
Elas podem ter dificuldade em confiar nas pessoas e podem ser um pouco reservadas em suas emoções.\n\
No geral, as pessoas com o número 7 têm um grande potencial para trabalhar em áreas como pesquisa, tecnologia, filosofia e ciências.\n\
Com sua habilidade para pensar criticamente e se concentrar em tarefas complexas,\n\
elas podem ser muito bem sucedidas em áreas que desenvolveram pensamento analítico e reflexivo."
        elif numero == 8:
            self.mensagem["text"] = str(numero)+" -  Se o nome da pessoa retorna o número 8 através da numerologia, significa que essa pessoa tem uma personalidade ambiciosa, determinada e empreendedora.\n\
Ela tem uma grande habilidade para assumir riscos calculados e pode ser muito bem sucedida em seus empreendimentos.\n\
Pessoas com o número 8 tendem a ser muito focadas em suas ambições e objetivos de carreira.\n\
Elas são vistas como pessoas muito empreendedoras e que têm uma grande capacidade para lidar com o dinheiro e os negócios.\n\
Elas têm uma grande habilidade para tomar decisões rápidas e precisas e podem ser muito eficientes em suas tarefas.\n\
Essas pessoas geralmente têm uma personalidade muito forte e determinada.\n\
Elas têm um grande senso de autoconfiança e podem ser muito persuasivas em suas relações com os outros.\n\
Elas são vistas como pessoas muito práticas e que sabem exatamente o que querem na vida.\n\
No entanto, as pessoas com o número 8 também podem ser um pouco teimosas e inflexíveis em suas abordagens.\n\
Elas podem ter dificuldade em lidar com a mudança e podem ser muito exigentes consigo mesmas e com os outros.\n\
No geral, as pessoas com o número 8 têm um grande potencial para trabalhar em áreas como finanças, administração, direito e empreendedorismo.\n\
Com sua habilidade para assumir riscos calculados e sua experiência em alcançar seus objetivos,\n\
elas podem ser muito bem sucedidas em áreas que lideraram, eficiência e capacidade para lidar com grandes responsabilidades."
        elif numero == 9:
            self.mensagem["text"] = str(numero)+" -  Se o nome da pessoa retorna o número 9 através da numerologia, significa que essa pessoa tem uma personalidade humanitária, carismática e altruísta.\n\
Ela tem uma grande habilidade para se relacionar com as pessoas e se importa profundamente com questões sociais e humanitárias.\n\
Pessoas com o número 9 tendem a ser muito focadas em ajudar os outros e fazer a diferença no mundo.\n\
Elas são vistas como pessoas muito carismáticas e que têm uma grande habilidade para inspirar e motivar os outros.\n\
Elas têm uma grande sensibilidade e empatia para com as necessidades dos outros e podem ser muito compassivas em suas felizes.\n\
Essas pessoas geralmente têm uma personalidade muito generosa e altruísta.\n\
Elas têm um grande senso de responsabilidade social e podem ser muito ativas em causas humanitárias e de justiça social.\n\
Elas são vistas como pessoas muito espirituais e que têm uma grande conexão com o mundo ao seu redor.\n\
No entanto, as pessoas com o número 9 também podem ser um pouco emocionais e sensíveis demais em suas confortáveis ​​com os outros.\n\
Elas podem se preocupar demais com as necessidades dos outros e podem ter dificuldade em lidar com a injustiça e o sofrimento no mundo.\n\
No geral, as pessoas com o número 9 têm um grande potencial para trabalhar em áreas como psicologia, serviço social, humanitarismo e advocacia.\n\
Com sua habilidade para se conectar com as pessoas e sua forte ética de trabalho, elas podem ser muito bem aceitas em áreas que toleram compaixão,\n\
liderança e capacidade para fazer a diferença no mundo."
        else:
            self.mensagem["text"] = str(numero)+" - Número inválido para numerologia."
    
    # função para retornar a descrição da personalidade (vogais)
    def descricao_destino(self):
        nome_destino = ''.join([i for i in self.nome.get() if i in 'aeiouAEIOU'])
        numero = soma_nomes(nome_destino)
        if numero == 1:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de destino é 1, isso indica que você tem um grande\n\
potencial para liderança e independência.\n\
Você é uma pessoa ambiciosa, determinada e motivada,\n\
que está constantemente buscando o sucesso em sua vida.\n\
Você tem uma personalidade forte e confiante, e geralmente sabe exatamente o que quer.\n\
Você é uma pessoa criativa e inovadora,\n\
capaz de pensar fora da caixa e encontrar soluções únicas para os problemas.\n\
Você tem uma mente rápida e aguçada, e é capaz de aprender\n\
rapidamente e aplicar novos conhecimentos de forma eficaz.\n\
Como um número de destino 1, você é uma pessoa muito independente,\n\
e tende a preferir fazer as coisas do seu próprio jeito.\n\
Você não gosta de ser controlado por outras pessoas,\n\
e pode se sentir frustrado ou limitado por regras e restrições impostas por outros.\n\
No entanto, você também pode ser um pouco impaciente e teimoso às vezes,\n\
e pode achar difícil trabalhar em equipe ou seguir a liderança de outras pessoas.\n\
Você pode precisar trabalhar em desenvolver suas habilidades de colaboração\n\
e comunicação para alcançar o sucesso em seus objetivos.\n\
Em resumo, como um número de destino 1, você é uma pessoa ambiciosa e motivada,\n\
com uma personalidade forte e independente.\n\
Você tem um grande potencial para liderança e inovação,\n\
mas pode precisar trabalhar em desenvolver suas habilidades de colaboração \n\
e comunicação para alcançar o sucesso em todas as áreas da vida."
        elif numero == 2:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de destino é 2, isso indica que você é uma pessoa muito sensível e empática,\n\
com uma natureza carinhosa e amorosa.\n\
Você valoriza profundamente as relações pessoais e se esforça para manter a harmonia\n\
e o equilíbrio em todos os aspectos da sua vida.\n\
Como um número de destino 2, você tem uma grande habilidade para compreender\n\
os sentimentos e necessidades dos outros,\n\
e é capaz de se adaptar facilmente a diferentes situações e ambientes.\n\
Você é uma pessoa diplomática e gentil,\n\
que busca sempre a cooperação e a colaboração em vez da competição.\n\
No entanto, você também pode ser um pouco tímido e inseguro,\n\
e pode achar difícil expressar seus próprios sentimentos e opiniões em situações de conflito.\n\
Você pode precisar trabalhar em desenvolver sua confiança e assertividade para alcançar seus objetivos.\n\
Como um número de destino 2, você é uma pessoa criativa e artística, com um grande talento para a música,\n\
a dança, a poesia, ou outras formas de expressão artística.\n\
Você é sensível às nuances e às sutilezas do mundo,\n\
e é capaz de encontrar beleza e significado nas coisas mais simples.\n\
Em resumo, como um número de destino 2, você é uma pessoa carinhosa e empática,\n\
com uma habilidade natural para a cooperação e a colaboração.\n\
Você é sensível e artístico, mas pode precisar trabalhar em desenvolver sua confiança\n\
e assertividade para alcançar seus objetivos pessoais e profissionais."
        elif numero == 3:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de destino é 3, isso indica que você é uma pessoa muito criativa e expressiva,\n\
com uma personalidade vibrante e carismática.\n\
Você é extrovertido e adora socializar, e tende a ser o centro das atenções em qualquer situação.\n\
Como um número de destino 3, você tem um grande talento para a comunicação e a expressão artística,\n\
e pode ser um excelente orador, escritor, ator, músico ou artista.\n\
Você é capaz de transmitir suas ideias e emoções de forma clara e cativante,\n\
e tem um dom para entreter e inspirar os outros.\n\
No entanto, você também pode ser um pouco impulsivo e imaturo às vezes,\n\
e pode ter dificuldade em assumir responsabilidades e compromissos a longo prazo.\n\
Você pode precisar trabalhar em desenvolver sua disciplina e\n\
sua capacidade de planejar e organizar seus objetivos.\n\
Como um número de destino 3, você é uma pessoa otimista e entusiasta,\n\
com uma paixão pela vida e pela diversão.\n\
Você é capaz de encontrar alegria e beleza nas coisas mais simples,\n\
e tende a ver o lado positivo em todas as situações.\n\
Em resumo, como um número de destino 3, você é uma pessoa criativa e expressiva,\n\
com um talento natural para a comunicação e a arte.\n\
Você é otimista e entusiasmado, mas pode precisar trabalhar\n\
em desenvolver sua disciplina e capacidade de planejamento\n\
para alcançar seus objetivos a longo prazo."
        elif numero == 4:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de destino é 4, isso indica que você é uma pessoa muito prática e organizada,\n\
com uma natureza estável e confiável.\n\
Você é trabalhador e comprometido, e tende a se dedicar incansavelmente aos seus objetivos até alcançá-los.\n\
Como um número de destino 4, você tem uma forte ética de trabalho e valoriza a estrutura e a ordem em sua vida.\n\
Você é capaz de assumir responsabilidades e compromissos a longo prazo,\n\
e tende a ser um pilar de força para os outros em sua vida pessoal e profissional.\n\
No entanto, você também pode ser um pouco inflexível e teimoso às vezes,\n\
e pode ter dificuldade em se adaptar a mudanças ou em aceitar ideias diferentes das suas.\n\
Você pode precisar trabalhar em desenvolver sua capacidade de flexibilidade e abertura para novas possibilidades.\n\
Como um número de destino 4, você é uma pessoa prática e realista, com um talento para a organização e gestão.\n\
Você é capaz de encontrar soluções criativas e eficazes para problemas complexos,\n\
e é um excelente planejador e estrategista.\n\
Em resumo, como um número de destino 4, você é uma pessoa prática e organizada,\n\
com uma forte ética de trabalho e um talento para a gestão e a solução de problemas.\n\
Você pode precisar trabalhar em desenvolver sua capacidade de flexibilidade e abertura para novas possibilidades,\n\
mas, em geral, é uma pessoa confiável e comprometida com seus objetivos."
        elif numero == 5:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de destino é 5, isso indica que você é uma pessoa curiosa e aventureira,\n\
com uma personalidade vibrante e excitante.\n\
Você está sempre movido pela busca de novas experiências e desafios,\n\
e tende a se adaptar facilmente a diferentes situações e ambientes.\n\
Como um número de destino 5, você tem uma grande habilidade para se comunicar e expressar suas ideias e emoções.\n\
Você é extrovertido e adora socializar, e tende a ser muito popular e atraente para os outros.\n\
No entanto, você também pode ser um pouco impulsivo e indisciplinado às vezes,\n\
e pode ter dificuldade em assumir responsabilidades e compromissos a longo prazo.\n\
Você pode precisar trabalhar em desenvolver sua disciplina e sua capacidade de planejar e organizar seus objetivos.\n\
Como um número de destino 5, você é uma pessoa automática e independente, com uma paixão pela vida e pela aventura.\n\
Você é capaz de se adaptar facilmente a mudanças e experiências,\n\
e tende a ser muito bem-sucedido em carreiras que tiveram flexibilidade e inovação.\n\
Em resumo, como um número de destino 5, você é uma pessoa curiosa e aventureira,\n\
com uma habilidade natural para se comunicar e socializar.\n\
Você é corajoso e independente, mas pode precisar trabalhar em desenvolver\n\
sua disciplina e capacidade de planejamento para alcançar seus objetivos a longo prazo."
        elif numero == 6:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de destino é 6, isso indica que você é uma pessoa carinhosa e compassiva,\n\
com uma personalidade amorosa e generosa.\n\
Você é capaz de criar conexões profundas e profundas com os outros,\n\
e tende a ser um pilar de apoio emocional em suas relações pessoais.\n\
Como um número de destino 6, você tem uma grande habilidade para o cuidado e a proteção de outras pessoas.\n\
Você é capaz de oferecer apoio e orientação em momentos difíceis,\n\
e tende a ser muito sensível às necessidades dos outros.\n\
No entanto, você também pode ser um pouco crítico e perfeccionista às vezes,\n\
e pode ter dificuldade em aceitar as falhas e limitação dos outros.\n\
Você pode precisar trabalhar em desenvolver sua capacidade de compaixão e empatia,\n\
e em se permitir ser vulnerável e pedir ajuda quando necessário.\n\
Como um número de destino 6, você é uma pessoa responsável e confiável,\n\
com um grande senso de dever e comprometimento.\n\
Você é capaz de assumir responsabilidades e compromissos a longo prazo,\n\
e tende a ser muito bem-sucedido em carreiras que envolvem cuidado e ajuda aos outros.\n\
Em resumo, como um número de destino 6, você é uma pessoa carinhosa e compassiva,\n\
com uma habilidade natural para o cuidado e a proteção das outras pessoas.\n\
Você é responsável e confiável, mas pode precisar trabalhar em desenvolver sua capacidade de compaixão e empatia,\n\
e em se permitir ser vulnerável e pedir ajuda quando necessário."
        elif numero == 7:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de destino é 7, isso indica que você é uma pessoa reflexiva\n\
e introspectiva, com uma personalidade analítica e investigativa.\n\
Você é capaz de se aprofundar em questões complexas e abstratas, e tende a ser muito intuitivo e perspicaz.\n\
Como um número de destino 7, você tem uma grande habilidade para a pesquisa e o estudo,\n\
e tende a ser muito interessado em assuntos espirituais e filosóficos.\n\
Você é capaz de encontrar significado e propósito em situações aparentemente sem sentido,\n\
e tende a ser muito espiritual e conectado com o universo.\n\
No entanto, você também pode ser um pouco isolado e reservado às vezes,\n\
e pode ter dificuldade em se conectar emocionalmente com os outros.\n\
Você pode precisar trabalhar em desenvolver sua capacidade de expressar suas emoções e se abrir para os outros.\n\
Como um número de destino 7, você é uma pessoa inteligente e perspicaz, com um grande senso de mistério e intriga.\n\
Você é capaz de encontrar soluções criativas para problemas complexos,\n\
e tende a ser muito bem-sucedido em carreiras que envolvem pesquisa e investigação.\n\
Em resumo, como um número de destino 7, você é uma pessoa reflexiva e introspectiva,\n\
com uma habilidade natural para a pesquisa e o estudo.\n\
Você é inteligente e perspicaz, mas pode precisar trabalhar em desenvolver sua capacidade de expressar\n\
suas emoções e se conectar emocionalmente com os outros."
        elif numero == 8:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de destino é 8, isso indica que você é uma pessoa ambiciosa e empreendedora,\n\
com uma personalidade poderosa e decidida.\n\
Você é capaz de assumir grandes desafios e responsabilidades,\n\
e tende a ser muito bem-sucedido em carreiras que envolvem liderança e empreendedorismo.\n\
Como um número de destino 8, você tem uma grande habilidade para administração financeira e empresarial,\n\
e tende a ser muito interessado em questões relacionadas ao dinheiro e ao sucesso material.\n\
Você é capaz de criar oportunidades e gerar riqueza, e tende a ser muito habilidoso em negócios e acordos comerciais.\n\
No entanto, você também pode ser um pouco autoritário e controlador às vezes,\n\
e pode ter dificuldade em delegar responsabilidades e confiar nos outros.\n\
Você pode precisar trabalhar em desenvolver sua capacidade de confiar e colaborar com os outros,\n\
e em equilibrar suas ambições com o cuidado e a consideração pelos sentimentos dos outros.\n\
Como um número de destino 8, você é uma pessoa poderosa e determinada, com um grande senso de propósito e direção.\n\
Você é capaz de enfrentar desafios com confiança e resiliência,\n\
e tende a ser muito bem-sucedido em carreiras que envolvem liderança e gestão empresarial.\n\
Em resumo, como um número de destino 8, você é uma pessoa ambiciosa e empreendedora,\n\
com uma habilidade natural para administração financeira e empresarial.\n\
Você é poderoso e determinado, mas pode precisar trabalhar em desenvolver sua capacidade de confiar e colaborar com os outros,\n\
e em equilibrar suas ambições com o cuidado e a consideração pelos sentimentos dos outros."
        elif numero == 9:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de destino é 9, isso indica que você é uma pessoa altruísta e compassiva,\n\
com uma personalidade humanitária e idealista.\n\
Você é capaz de se conectar profundamente com os outros e com o mundo ao seu redor,\n\
e tende a se interessar muito por questões relacionadas à justiça social e ao bem-estar humano.\n\
Como um número de destino 9, você tem uma grande habilidade para a compaixão e a empatia,\n\
e tende a ser muito preocupado com o sofrimento e a injustiça no mundo.\n\
Você é capaz de se envolver em projetos e causas que visam melhorar a vida dos outros,\n\
e tende a ser muito ativo em trabalhos voluntários e atividades de caridade.\n\
No entanto, você também pode ser um pouco idealista e impraticável às vezes,\n\
e pode ter dificuldade em lidar com a realidade prática das situações.\n\
Você pode precisar trabalhar em desenvolver sua capacidade de equilibrar\n\
sua visão idealista com a compreensão das limitações e complexidades do mundo real.\n\
Como um número de destino 9, você é uma pessoa compassiva e idealista, com um grande senso de propósito e significado.\n\
Você é capaz de se conectar profundamente com as emoções e experiências dos outros,\n\
e tende a ser muito bem-sucedido em carreiras que envolvem serviço social, ativismo ou humanitarismo.\n\
Em resumo, como um número de destino 9, você é uma pessoa altruísta e compassiva,\n\
com uma habilidade natural para a compaixão e a empatia.\n\
Você é idealista e preocupado com o bem-estar humano,\n\
mas pode precisar trabalhar em desenvolver sua capacidade de equilibrar sua visão idealista\n\
com a compreensão das limitações e complexidades do mundo real."
        else:
            self.mensagem["text"] = str(numero)+" - Número inválido para numerologia."
    
    # função para retornar a descrição da alma
    def descricao_alma(self):
        numero = soma_nomes(self.nome.get())
        if numero == 1:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de alma é 1, isso indica que você é uma pessoa independente, criativa e determinada,\n\
com uma personalidade forte e confiante.\n\
Você tem uma grande habilidade para liderança e empreendedorismo,\n\
e tende a ser muito ambicioso em alcançar seus objetivos e sonhos.\n\
Como um número de alma 1, você tem uma grande capacidade de inovação e originalidade,\n\
e tende a ser muito criativo em suas ideias e projetos.\n\
Você é capaz de ver oportunidades onde outros não veem,\n\
e tende a ser muito bem-sucedido em carreiras que envolvem empreendedorismo, liderança ou criatividade.\n\
No entanto, você também pode ser um pouco teimoso e egoísta às vezes,\n\
e pode ter dificuldade em ouvir as opiniões e ideias dos outros.\n\
Você pode precisar trabalhar em desenvolver sua capacidade de colaboração e consideração pelos sentimentos dos outros,\n\
e em equilibrar suas ambições com a necessidade de trabalhar em equipe.\n\
Como um número de alma 1, você é uma pessoa independente e determinada, com um grande senso de propósito e direção.\n\
Você é capaz de liderar e motivar os outros com sua confiança e liderança,\n\
e tende a ser muito bem-sucedido em carreiras que envolvem liderança, empreendedorismo ou criatividade.\n\
Em resumo, como um número de alma 1, você é uma pessoa independente, criativa e determinada,\n\
com uma habilidade natural para liderança e empreendedorismo.\n\
Você é original e inovador, mas pode precisar trabalhar em desenvolver\n\
sua capacidade de colaboração e consideração pelos sentimentos dos outros,\n\
e em equilibrar suas ambições com a necessidade de trabalhar em equipe."
        elif numero == 2:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de alma é 2, isso indica que você é uma pessoa empática, sensível e colaborativa,\n\
com uma personalidade gentil e harmoniosa.\n\
Você tem uma grande habilidade para a cooperação e o trabalho em equipe,\n\
e tende a ser muito habilidoso em lidar com situações emocionais e conflitos interpessoais.\n\
Como um número de alma 2, você tem uma grande capacidade para a empatia e a compreensão das emoções e necessidades dos outros.\n\
Você é capaz de criar harmonia e equilíbrio em situações difíceis,\n\
e tende a ser muito bem-sucedido em carreiras que envolvem o trabalho em equipe, aconselhamento ou terapia.\n\
No entanto, você também pode ser um pouco passivo e indeciso às vezes,\n\
e pode ter dificuldade em tomar decisões difíceis ou agir com firmeza quando necessário.\n\
Você pode precisar trabalhar em desenvolver sua capacidade de assertividade e tomada de decisão,\n\
e em equilibrar sua preocupação com os outros com a necessidade de cuidar de si mesmo.\n\
Como um número de alma 2, você é uma pessoa empática e colaborativa, com um grande senso de equilíbrio e harmonia.\n\
Você é capaz de trabalhar bem em equipe e de criar relações positivas e saudáveis ​​com os outros,\n\
e tende a ser muito bem-sucedido em carreiras que envolvem aconselhamento, terapia ou trabalho social.\n\
Em resumo, como um número de alma 2, você é uma pessoa empática, sensível e colaborativa,\n\
com uma habilidade natural para o trabalho em equipe e na solução de conflitos.\n\
Você é capaz de criar harmonia e equilíbrio em situações difíceis,\n\
mas pode precisar trabalhar em desenvolver sua capacidade de assertividade e tomada de decisão,\n\
e em equilibrar sua preocupação com os outros com a necessidade de cuidar de si mesmo."
        elif numero == 3:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de alma é 3, isso indica que você é uma pessoa criativa, expressiva e comunicativa,\n\
com uma personalidade divertida e extrovertida.\n\
Você tem uma grande habilidade para a comunicação e a expressão artística,\n\
e tende a ser muito habilidoso em lidar com as palavras e com a linguagem em geral.\n\
Como um número de alma 3, você tem uma grande capacidade para a criatividade e a originalidade,\n\
e tende a ser muito bem-sucedido em carreiras que envolvem a arte, a escrita,\n\
a música ou outras formas de expressão artística.\n\
Você é capaz de ver a beleza e a inspiração em tudo ao seu redor, e tende a contagiar as pessoas com sua alegria e entusiasmo pela vida.\n\
No entanto, você também pode ser um pouco superficial e impulsivo às vezes,\n\
e pode ter dificuldade em manter o foco e a disciplina necessária para levar seus projetos até o fim.\n\
Você pode precisar trabalhar em desenvolver sua capacidade de concentração e perseverança,\n\
e em equilibrar sua busca pela diversão e pelo prazer com a necessidade de responsabilidade e compromisso.\n\
Como um número de alma 3, você é uma pessoa criativa e expressiva,\n\
com um grande talento para a comunicação e a expressão artística.\n\
Você é capaz de encantar e inspirar as pessoas com sua alegria e entusiasmo pela vida,\n\
e tende a ser muito bem sucedido em carreiras que envolvem a criatividade e a expressão artística.\n\
Em resumo, como um número de alma 3, você é uma pessoa criativa, expressiva e comunicativa,\n\
com uma habilidade natural para a arte, a escrita, a música ou outras formas de expressão artística.\n\
Você é capaz de ver a beleza e a inspiração em tudo ao seu redor,\n\
mas pode precisar trabalhar em desenvolver sua capacidade de concentração e perseverança,\n\
e em equilibrar sua busca pela diversão e pelo prazer com a necessidade de responsabilidade e compromisso."
        elif numero == 4:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de alma é 4, isso indica que você é uma pessoa prática,\n\
disciplinada e confiável, com uma personalidade estável e confiável.\n\
Você é uma pessoa que valoriza a ordem, a estabilidade e a segurança,\n\
e tende a ser muito bem-sucedido em carreiras que tiveram um alto grau de organização e habilidades práticas.\n\
Como um número de alma 4, você tem uma grande capacidade para a disciplina e a perseverança,\n\
e tende a ser muito responsável e confiável em tudo o que faz.\n\
Você é capaz de trabalhar duro e de forma consistente para atingir seus objetivos,\n\
e é muito bom em lidar com tarefas práticas e rotineiras.\n\
Você valoriza a honestidade e a integridade, e tende a ser um modelo de estabilidade e confiabilidade para os outros.\n\
No entanto, você também pode ser um pouco inflexível e resistente à mudança,\n\
e pode ter dificuldade em se adaptar a situações novas e imprevistas.\n\
Você pode precisar trabalhar em desenvolver sua capacidade de flexibilidade e de adaptabilidade,\n\
e em equilibrar sua busca pela estabilidade e pela segurança com a necessidade de inovação e mudança.\n\
Como um número de alma 4, você é uma pessoa prática e disciplinada, com uma grande capacidade para a perseverança e a estabilidade.\n\
Você é capaz de trabalhar duro e de forma consistente para atingir seus objetivos,\n\
e é muito bom em lidar com tarefas práticas e rotineiras.\n\
Você valoriza a honestidade e a integridade, e tende a ser um modelo de estabilidade e confiabilidade para os outros.\n\
Em resumo, como um número de alma 4, você é uma pessoa prática, disciplinada e confiável,\n\
com uma grande capacidade para a perseverança e a estabilidade.\n\
Você é capaz de trabalhar duro e de forma consistente para atingir seus objetivos,\n\
mas pode precisar trabalhar em desenvolver sua capacidade de flexibilidade e de adaptabilidade,\n\
e em equilibrar sua busca pela estabilidade e pela segurança com a necessidade de inovação e mudança."
        elif numero == 5:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de alma é 5, isso indica que você é uma pessoa curiosa,\n\
aventureira e emocionalmente expressiva,\n\
com uma personalidade vibrante e entusiasta.\n\
Você é uma pessoa que valoriza a liberdade, a mudança e a variedade,\n\
e tende a ser muito bem-sucedido em carreiras que envolvem comunicação, criatividade e viagens.\n\
Como um número de alma 5, você tem uma grande capacidade para a adaptação e a mudança,\n\
e tende a ser muito aventureiro e corajoso em suas escolhas e ações.\n\
Você valoriza a liberdade pessoal e a independência, e tende a ser muito flexível e aberto a novas experiências e ideias.\n\
Você é capaz de se adaptar a novas situações com facilidade e rapidez, e tende a prosperar em ambientes caóticos e em constante mudança.\n\
No entanto, você também pode ser um pouco impulsivo e inconstante,\n\
e pode ter dificuldade em se comprometer com escolhas ou objetivos a longo prazo.\n\
Você pode precisar trabalhar em desenvolver sua capacidade de perseverança\n\
e em encontrar maneiras de equilibrar sua busca por variedade e mudança com a necessidade de estabilidade e tolerância em sua vida.\n\
Como um número de alma 5, você é uma pessoa curiosa, aventureira e emocionalmente expressiva,\n\
com uma grande capacidade para a adaptação e a mudança. Você valoriza a liberdade pessoal e a independência,\n\
e tende a ser muito flexível e aberto a novas experiências e ideias.\n\
Você é capaz de se adaptar a novas situações com facilidade e rapidez, e tende a prosperar em ambientes caóticos e em constante mudança.\n\
Em resumo, como um número de alma 5, você é uma pessoa vibrante e entusiasta, com uma grande capacidade para a adaptação e a mudança.\n\
Você valoriza a liberdade pessoal e a independência, e tende a ser muito flexível e aberto a novas experiências e ideias.\n\
No entanto, pode precisar trabalhar em desenvolver sua capacidade de perseverança e em encontrar maneiras\n\
de equilibrar sua busca por variedade e mudança com a necessidade de estabilidade e coerência em sua vida."
        elif numero == 6:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de alma é 6, isso indica que você é uma pessoa amorosa,\n\
compassiva e dedicada, com uma forte ética de trabalho e um desejo de servir aos outros.\n\
Você é uma pessoa altamente responsável, confiável e preocupada com o bem-estar dos outros,\n\
e tende a ser muito bem-sucedida em carreiras que envolvem cuidados com a saúde, serviço social, terapia ou educação.\n\
Como um número de alma 6, você é uma pessoa altamente sensível e empática,\n\
com uma grande capacidade de ouvir e entender as necessidades dos outros.\n\
Você é um excelente conselheiro e amigo, e tende a ser muito dedicado e comprometido com os relacionamentos e a comunidade.\n\
Você é uma pessoa angustiada e equilibrada, e tem um forte senso de justiça e equidade.\n\
No entanto, você também pode ser um pouco exigente e perfeccionista, e pode ter dificuldade em aceitar a si mesmo e aos outros como são.\n\
Você pode precisar trabalhar em desenvolver uma maior compaixão e tolerância em relação aos outros e a si mesmo,\n\
e encontrar maneiras de equilibrar sua tendência para cuidar dos outros com a necessidade de cuidar de si mesmo.\n\
Como um número de alma 6, você é uma pessoa amorosa, compassiva e dedicada, com uma forte ética de trabalho e um desejo de servir aos outros.\n\
Você é altamente sensível e empático, e tende a ser muito bem-sucedido em carreiras que envolvem cuidados com a saúde,\n\
serviço social, terapia ou educação.\n\
No entanto, pode precisar trabalhar em desenvolver uma maior tolerância e tolerância em relação aos outros e a si mesmo,\n\
e encontrar maneiras de equilibrar sua tendência para cuidar dos outros com a necessidade de cuidar de si mesmo.\n\
Em resumo, como um número de alma 6, você é uma pessoa amorosa e compassiva, com uma forte ética de trabalho e um desejo de servir aos outros.\n\
Você é altamente sensível e empático, e tende a ser muito bem-sucedido em carreiras que envolvem cuidados com a saúde,\n\
serviço social, terapia ou educação. No entanto, pode precisar trabalhar em desenvolver uma maior tolerância\n\
e tolerância em relação aos outros e a si mesmo, e encontrar maneiras de equilibrar\n\
sua tendência para cuidar dos outros com a necessidade de cuidar de si mesmo."
        elif numero == 7:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de alma é 7, isso indica que você é uma pessoa\n\
altamente intuitiva, contemplativa e espiritual,\n\
com um forte desejo de aprender e crescer em nível pessoal e espiritual.\n\
Você é uma pessoa altamente analítica e reflexiva,\n\
e tende a ter um forte interesse em filosofia, metafísica e espiritualidade.\n\
Como um número de alma 7, você é uma pessoa profundamente introspectiva e questionadora,\n\
e tende a buscar respostas profundas e pensadas para as questões da vida.\n\
Você é uma pessoa altamente intuitiva e espiritual, e tende a ter um forte senso de propósito e significado em sua vida.\n\
Você é muito seletivo em suas relações pessoais e tende a manter uma certa distância das pessoas até que as conheçam bem.\n\
Você pode ser visto como uma pessoa solitária ou introvertida, mas na verdade,\n\
você valoriza profundamente a sua privacidade e sua necessidade de introspecção para se conectar com o seu eu mais profundo e sua espiritualidade.\n\
Você é uma pessoa altamente criativa e tem uma mente muito afiada,\n\
o que pode tornar você bem-sucedido em carreiras que fornecem análise, pesquisa e pensamento crítico.\n\
No entanto, como um número de alma 7, você também pode ter tendência a ser crítica consigo mesmo e com os outros,\n\
o que pode levar à reserva e desapontamento. Você pode precisar trabalhar na tolerância e tolerância em relação aos outros e si mesmo,\n\
e encontrar maneiras de equilibrar sua tendência para a introspecção e a reflexão com a necessidade de se conectar com os outros e o mundo ao seu redor.\n\
Em resumo, como um número de alma 7, você é uma pessoa altamente intuitiva, contemplativa e espiritual,\n\
com um forte desejo de aprender e crescer em nível pessoal e espiritual.\n\
Você é uma pessoa altamente analítica e reflexiva, e tende a ter um forte interesse em filosofia, metafísica e espiritualidade.\n\
Embora possa ser visto como uma pessoa solitária, você valoriza profundamente a sua privacidade e sua necessidade\n\
de introspecção para se conectar com o seu eu mais profundo e sua espiritualidade."
        elif numero == 8:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de alma é 8, isso indica que você é uma pessoa extremamente ambiciosa,\n\
com uma forte motivação para alcançar o sucesso material e financeiro em sua vida.\n\
Você tem um forte senso de propósito e direção, e tende a ser muito empreendedor e orientado para resultados.\n\
Como um número de alma 8, você é uma pessoa muito prática e orientada para o negócio,\n\
com uma grande habilidade para tomar decisões rápidas e eficazes.\n\
Você é altamente organizado e disciplinado, e tende a ser muito focado em suas metas e objetivos de longo prazo.\n\
Você tem uma grande capacidade para lidar com desafios e pressão, e é capaz de superar obstáculos e adversidades em seu caminho.\n\
No entanto, como um número de alma 8, você também pode ser tolerante a ser fugitivo materialista e preocupado com dinheiro e poder.\n\
É importante que você aprenda a equilibrar sua ambição com uma perspectiva mais ampla e espiritual da vida,\n\
e encontre maneiras de usar seu sucesso e proteção para fazer uma diferença positiva no mundo ao seu redor.\n\
Além disso, como um número de alma 8, você também pode ser tolerante a ser dominante e controlador em seus relacionamentos pessoais e profissionais.\n\
É importante que você aprenda a ser mais colaborativo e compassivo com as pessoas ao seu redor,\n\
e encontre maneiras de trabalhar em equipe para alcançar seus objetivos de longo prazo.\n\
Em resumo, como um número de alma 8, você é uma pessoa extremamente ambiciosa,\n\
com uma forte motivação para alcançar o sucesso material e financeiro em sua vida.\n\
Você é altamente organizado e disciplinado, e tende a ser muito focado em suas metas e objetivos de longo prazo.\n\
É importante que você encontre um equilíbrio entre sua ambição e uma perspectiva mais espiritual e compassiva da vida,\n\
e trabalhe em equipe para alcançar seus objetivos de longo prazo."
        elif numero == 9:
            self.mensagem["text"] = str(numero)+" -  Se o seu número de alma é 9, isso indica que você é uma pessoa extremamente\n\
compassiva e orientada para os outros,\n\
com uma forte motivação para fazer uma diferença positiva no mundo ao seu redor.\n\
Você tem uma grande capacidade de empatia e compaixão, e é naturalmente atraído por causas humanitárias e sociais.\n\
Como um número de alma 9, você tem uma grande habilidade para se conectar com as pessoas e entender suas necessidades e desejos.\n\
Você é uma pessoa muito intuitiva e sensível, capaz de sentir a dor e a alegria dos outros de uma forma muito profunda e autônoma.\n\
Você tem uma grande capacidade para se colocar no lugar dos outros e ver o mundo a partir de suas perspectivas.\n\
No entanto, como um número de alma 9, você também pode ser tolerado a se sacrificar demais\n\
pelos outros e se sentir sobrecarregado com o sofrimento do mundo.\n\
É importante que você encontre maneiras de cuidar de si mesmo e equilibre sua compaixão com uma perspectiva mais ampla da vida.\n\
Além disso, como um número de alma 9, você também tem uma grande habilidade para a criatividade e a expressão artística.\n\
Você tem uma sensibilidade artística natural e uma capacidade de ver beleza e significado em tudo ao seu redor.\n\
É importante que você encontre maneiras de expressar sua criatividade e beleza interior, e use isso para inspirar e elevar os outros.\n\
Em resumo, como um número de alma 9, você é uma pessoa extremamente compassiva e orientada para os outros,\n\
com uma grande habilidade para se conectar e entender as necessidades das pessoas.\n\
Você é naturalmente atraído por causas humanitárias e sociais, e tem uma grande capacidade para a criatividade e a expressão artística.\n\
É importante que você encontre maneiras de equilibrar sua compaixão com uma perspectiva mais ampla da vida,\n\
e use sua sensibilidade artística para inspirar e elevar os outros."
        else:
            self.mensagem["text"] = str(numero)+" - Número inválido para numerologia."

    def falar(self):
        # Velocidade da fala
        rate = texto_fala.getProperty('rate')
        texto_fala.setProperty("rate", 200)
        # Seleciona a voz
        voices = texto_fala.getProperty('voices')
        texto_fala.setProperty('voice', voices[0].id)
        # Recebe o áudio para a fala
        texto_fala.say(self.mensagem["text"])
        texto_fala.runAndWait()

#Função que calcula o numero correspondente a uma stgring
def soma_nomes(nome_completo):
    letras = "abcdefghijklmnopqrstuvwxyz"
    valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8]
    soma = sum(valores[letras.index(l.lower())] for l in nome_completo if l.lower() in letras)
    while soma > 9:
        soma = sum(int(d) for d in str(soma))
    return soma

root = Tk()
root.title("Numerologia")
root.geometry("1800x1000")
root.configure(background=corFundo)
root.resizable(True, True)
Application(root)
root.mainloop()