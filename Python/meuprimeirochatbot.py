from chatterbot import ChatBot
from chatterbot.trainers import  ListTrainer

# Crie uma instância do chatbot
chatbot = ChatBot('Meu ChatBot')

# Prepara os dados para o treino
conversa = [
'Bom Dia como você está?'
'Eu estou bem, e você?'
'Eu também estou.'
'Que bom.'
'Sim.'
'Olá'
'Oi'
'Como vai você?'
'Eu estou bem.'
'Que bom'
'Sim.'
'Posso ajudá-lo com alguma coisa?'
'Sim, eu tenho uma pergunta.'
'Qual é a sua pergunta?'
'Eu poderia pedir uma xícara de açúcar?'
'Me desculpe, mas eu não tenho nenhum.'
'Obrigado de qualquer maneira'
'Sem problemas'
'Como vai você?'
'Eu estou bem, e você?'
'Eu também estou bem.'
'Isso é bom.'
'Ouviu as notícias?'
'Que boa notícia?'
Qual é o seu livro favorito?
Eu não sei ler.
Então, qual é a sua cor favorita?
Azul
Quem é você?
Quem? Quem é senão uma forma seguindo a função de quê
Então o que você é?
Um homem em uma máscara.
Eu posso ver isso.
Não é seu poder de observação eu duvido, mas apenas a natureza paradoxal de pedir
um homem mascarado que é. Mas diga-me, você gosta de música?
Eu gosto de ver filmes.
Que tipo de filme você gosta?
Alice no Pais das Maravilhas
Eu gostaria de ser o Chapeleiro Maluco.
Você é totalmente maluco. Mas eu vou te contar um segredo. Todas as melhores pessoas são.
Eu estou trabalhando em um projeto
Em que você está trabalhando?
Eu estou fazendo um bolo.
O bolo é uma mentira.
Não, não é. O bolo é delicioso.
O que mais é delicioso?
Nenhuma coisa
Ou algo
Fale-me sobre você.
O que você quer saber?
Você é um robô?
Sim eu sou.
Como é?
O que é que você quer saber?
Como você trabalha?
É complicado.
Complexo é melhor que complicado.
Complexo é melhor que complicado.
Simples é melhor que complexo.
Diante da ambigüidade, recuse a tentação de adivinhar.
Parece que o seu familiar com o Zen de Python
Eu sou o Batman.
Você sabe tudo isso?
Bonito é melhor que feio.
Explícito é melhor que implícito.
Bom dia! Como você está?
Ah, estou um pouco cansado hoje. E você?
Eu estou bem, obrigado por perguntar.
Olá, como vai você?
Eu estou bem, obrigado. E você?
Também estou bem. O que você tem feito?
Oi, posso ajudá-lo com alguma coisa?
Na verdade, tenho uma pergunta. Você sabe onde posso encontrar um bom restaurante por aqui?
Olá! Qual é o seu livro favorito?
Ah, eu não sei ler, então não tenho um livro favorito. E você?
Personagem A: Quem é você?
Quem? Quem é senão uma forma cumprindo a função de quê.
Você gosta de música?
Na verdade, eu gosto mais de ver filmes. E você?
Estou trabalhando em um projeto.
Legal! Em que tipo de projeto você está trabalhando?
O que mais é delicioso?
Hmm, acho que chocolate é muito gostoso. E para você?
Fale-me sobre você.
Bem, o que você gostaria de saber? Sou um amante da natureza e adoro viajar.
Você é um robô?
Sim, sou um robô. Fui projetado para ajudar com várias tarefas.
Olá! Como você está hoje?
Ah, estou um pouco estressado. E você?
Estou me sentindo bastante tranquilo hoje.
Oi! Como vai você?
Bem, obrigado! E você?
Estou ótimo! Pronto para aproveitar o dia.
Bom dia! Como tem sido sua semana?
No geral, tem sido boa. Algumas coisas aconteceram, mas estou lidando com elas. E você?
Minha semana também tem sido positiva. Estou progredindo em meus projetos.
Ei, posso te fazer uma pergunta?
Claro, fique à vontade!
Qual é o seu lugar favorito para relaxar?
Olá! Você viu o último filme que foi lançado?
Sim, eu assisto. Foi incrível! Você já viu?
Ainda não tive chance, mas estou ansioso para assistir em breve.
Oi! Você já experimentou algum prato novo ultimamente?
Sim, na verdade, eu experimentei um prato exótico em um restaurante novo. Foi uma experiência interessante. E você?
 Ainda não, mas estou sempre em busca de novos sabores para experimentar.
Ei, o que você acha de fazer uma viagem no próximo fim de semana?
Isso parece ótimo! Para onde você sugere irmos?
Que tal uma praia tranquila? Podemos relaxar e aproveitar o sol.
Oi! Qual é a última coisa que aconteceu com você?
Bem, outro dia, eu escorreguei em uma cascata de banana na calçada. Foi um momento hilário! E você?
Recentemente, eu assisto a um show de comédia que me fez rir do começo ao fim.
Ei, você tem algum hobby interessante?
Sim, eu adoro pintar e criar arte. É uma maneira ótima de me expressar. E você?
Eu gosto de tocar violão nas horas vagas. É uma forma relaxante de passar o tempo.
Oi! Você já teve alguma experiência inesquecível em viagens?
Com certeza! Uma vez, eu fiz uma trilha incrível em uma montanha e pude ver uma vista deslumbrante do topo. E você?
Eu tive a oportunidade de mergulhar em um recife de coral e explorar a vida marinha. Foi uma experiência surreal.
Bom dia! O que você tem planejado para o fim de semana?
Olá! Estou pensando em sair para uma trilha e curtir a natureza. E você?
Eu pretendo relaxar em casa e assistir a alguns filmes. Talvez seja uma boa oportunidade para descansar.
Oi! Você já experimentou algum esporte radical?
Sim, eu fiz paraquedismo uma vez. Foi uma experiência incrível! E você?
Ainda não, mas estou experimentando o bungee jump. Parece emocionante.
Ei, você tem algum plano de viagem dos sonhos?
Com certeza! Eu adoraria visitar o Japão e conhecer sua cultura única. E você?
Tenho o desejo de explorar as paisagens deslumbrantes da Nova Zelândia. É um lugar incrível.
Olá! O que você gosta de fazer nas suas horas livres?
Eu gosto de ler livros e expandir meus conhecimentos. E você?
Eu gosto de cozinhar novas receitas e experimentar diferentes sabores. É uma paixão minha.
Ei, qual é a sua música favorita de todos os tempos?
É difícil escolher apenas uma, mas eu diria que "Bohemian Rhapsody" do Queen é uma das minhas favoritas. E você?
Eu sou um grande fã de "Imagine" de John Lennon. Acho que é uma música muito inspiradora.
Oi! Você já fez algum trabalho voluntário?
Sim, eu já me envolvi em um abrigo de animais. Foi uma experiência gratificante. E você?
Eu participei de um programa de alfabetização para crianças carentes. Foi muito bom poder ajudar.
Ei, qual é o seu prato favorito?
Eu adoro comida italiana, especialmente uma boa lasanha. E você?
Sou um fã de comida tailandesa. Um bom curry apimentado é o meu prato favorito.
Olá! Você já teve algum momento de superação pessoal que gostaria de compartilhar?
Certa vez, eu enfrentei meu medo de falar em público e fiz uma apresentação importante. Foi um grande passo para mim. E você?
Eu superei minha timidez ao entrar em um grupo de teatro. Foi transformar a aprender a me expressar no palco.
Ei, você já teve algum encontro romântico dourado?
Uma vez, eu planejei um jantar à luz de velas na praia. Foi um momento muito especial. E você?
 Tive um encontro em um parque de diversões e passamos o dia
Ei, você sabe por que o livro foi ao médico?
Não, por quê?
Porque ele tinha muitas histórias para contar!
Oi! Qual é o animal mais antigo do mundo?
Não faço ideia, qual é?
A zebra, porque está sempre nas listas de antiguidade!
Você já ouviu falar do restaurante no espaço?
Não, me conta! Personagem A: A comida é ótima, mas não tem atmosfera!
Sabe por que o livro não fez exercícios?
Não, por quê?
Porque ele prefere ser uma história de ficção!
Qual é o cúmulo da paciência?
Não sei, qual é?
Ir pescar e ficar esperando a boa vontade do peixe de morder o anzol!
O que aconteceu com o ladrão que roubou um calendário?
Não faço ideia, o que aconteceu?
Ele pegou 12 meses de prisão!
Você conhece a piada do pão?
Não, qual é?
Ah, é uma piada meio "massante". Melhor deixar para lá...
Sabe por que a matemática foi para a terapia?
Por quê?
Porque tinha muitos problemas para resolver!
Qual é o animal mais rico?
Não faço ideia, qual é?
O porco, porque ele está cheio de "dinheiro"!
O que o livro de receitas disse para a farinha?
Não sei, o que disse?
"Nos amassamos muito bem!"
Ei, você está acompanhando algum evento esportivo recentemente?
Sim, tenho assistido alguns jogos de futebol. E você? Personagem A: Eu tenho acompanhado a temporada de basquete. É sempre emocionante ver os tempos competindo.
Legal! Qual é o seu time favorito de futebol?
Sou torcedor do Barcelona. Admiro o estilo de jogo e a habilidade dos jogadores.
Interessante! Eu sou fã do Manchester United. Acompanho o clube há anos e sempre torço por eles.
Você pratica algum esporte também?
Sim, sou esportivo por tênis. Jogo regularmente com amigos nas finais de semana.
Que legal! Eu costumava praticar natação quando era mais jovem. É um esporte que me traz muita tranquilidade.
Compreendo. A natação é uma ótima atividade para relaxar e também oferece muitos benefícios para a saúde.
Você já teve a oportunidade de assistir a algum evento esportivo ao vivo?
Sim, já assista a alguns jogos de futebol e tênis ao vivo. A atmosfera nos estádios é incrível e a emoção é palpável.
Concordo completamente! Assistir a um jogo ao vivo é uma experiência única. A energia dos torcedores é contagiante.
Falando nisso, você já participou de algum jogo ou competição esportiva?
Sim, participei de alguns torneios de futebol amador com amigos. Foi divertido e desafiador ao mesmo tempo.
Isso é ótimo! Participar de competições esportivas é uma forma empolgante de testar suas habilidades e se divertir.
Definitivamente. O esporte tem esse poder de unir as pessoas, proporcionar emoções e criar memórias inesquecíveis.
Com certeza! É incrível como o esporte transcende barreiras e conecta pessoas de diferentes origens e culturas
Olá! Você está envolvido na gestão de algum negócio atualmente?
Sim, sou o gerente de operações de uma empresa de tecnologia. E você, está envolvido em alguma área de gestão?
Sim, sou empreendedor e estou à frente de uma startup no setor de e-commerce. Estamos em fase de crescimento.
Ótimo! Lidar com o crescimento de uma empresa pode ser desafiador. Como você tem enfrentado esse processo?
Tem sido um desafio estimulante. Estamos focados em estabelecer uma estratégia de expansão, otimizando nossos processos internos e buscando novas oportunidades de mercado.
Excelente! Ter uma estratégia sólida é fundamental para o crescimento sustentável. Além disso, a melhoria contínua dos processos é essencial para a eficiência operacional.
Concordo plenamente. Estamos constantemente revisando e aprimorando nossos processos para garantir que estejamos operando de forma eficiente e entregando valor aos nossos clientes.
Além disso, como líder, é importante ter uma equipe engajada e esclarecida com os objetivos da empresa. Como você tem lidado com a gestão de pessoas?
A gestão de pessoas é um aspecto fundamental. Investimos no desenvolvimento da nossa equipe, fornecendo treinamentos e incentivando um ambiente colaborativo. Valorizamos a comunicação aberta e a meritocracia.
Isso é muito importante. Uma equipe motivada e engajada contribui diretamente para o sucesso de um negócio. Como você lida com os desafios e toma decisões estratégicas?
Tomar decisões estratégicas requer análise cuidadosa dos dados disponíveis, avaliação de pensamentos e consideração das tendências do mercado. Também busco a opinião de especialistas e líderes da equipe para tomar decisões decisivas.
É uma abordagem inteligente. Ouvir diferentes perspectivas e ter acesso a informações relevantes ajuda a tomar decisões mais embasadas. Além disso, é importante ter flexibilidade para se adaptar às mudanças do mercado.
Exatamente. A agilidade e a capacidade de adaptação são fundamentais no mundo dos negócios. Estamos sempre monitorando o ambiente externo e ajustando nossa estratégia conforme necessário.
Parece que você está no caminho certo. A gestão de negócios exige um equilíbrio entre planejamento planejado, execução eficiente e capacidade de adaptação. Desejo sucesso contínuo para você e sua startup.
Muito obrigado! Desejo o mesmo para você e sua empresa. A gestão de negócios é desafiadora, mas também traz grandes oportunidades de crescimento e profissional.
Olá! Como está sua família? Você tem filhos? Personagem B: Olá! Minha família está muito bem, obrigado. Sim, tenho dois filhos. E você, tem filhos também?
Sim, tenho uma filha e um filho. Eles são a alegria da minha vida e trazem muita felicidade para nossa família.
É maravilhoso ter filhos, não é? Eles nos ensinam tanto e nos fazem ver o mundo de uma maneira diferente.
Com certeza! Eles têm uma maneira única de nos fazer respeitar as coisas simples da vida e nos lembrar da importância do amor e do cuidado.
Concordo plenamente. Acredito que a família é um alicerce sólido em nossas vidas. É onde encontramos apoio, compreensão e um sentimento de pertencimento.
Exatamente! A família é um porto seguro em tempos difíceis e também um lugar para compartilhar momentos felizes e criar memórias duradouras.
Além disso, a criação dos filhos também nos desafia a sermos melhores pessoas. Aprendemos a ser mais pacientes, empáticos e responsáveis.
Com certeza! A paternidade/maternidade nos transforma e nos ajuda a crescer emocionalmente. É uma jornada de aprendizado constante.
Você tem alguma dica ou conselho para lidar com os desafios da criação dos filhos?
Cada família é única e enfrenta desafios diferentes, mas acredito que a comunicação aberta e o amor incondicional são fundamentais. Também é importante estabelecer limites saudáveis ​​e promover o desenvolvimento emocional e intelectual das crianças.
Concordo completamente. Acredito que dar um bom exemplo, dedicar tempo de qualidade e incentivar a autonomia são aspectos importantes da criação dos filhos.
Além disso, é essencial lembrar-se de aproveitar cada momento com os filhos, pois o tempo passa rápido demais.
Absolutamente! Os momentos que passamos com nossos filhos são preciosos e devemos aproveitá-los ao máximo.
Olá! Como vai sua saúde? Você tem cuidado bem de si mesmo? Personagem B: Olá! Minha saúde está indo bem, obrigado. Sim, tenho me esforçado para cuidar de mim mesmo e adotar hábitos saudáveis. E você, como tem sido sua jornada em relação à saúde?
Fico feliz em saber que sua saúde está bem! Tenho tentado priorizar minha saúde também, mantendo uma dieta equilibrada e praticando exercícios regularmente.
É ótimo saber que você está se cuidando. Uma alimentação saudável e a prática de exercícios são pilares importantes para uma vida saudável. Além disso, você tem check-ups médicos regulares realizados?
Sim, tenho ido ao médico regularmente para fazer exames e verificar minha saúde geral. Acredito que a prevenção é fundamental para detectar qualquer problema nas iniciais.
Com certeza! Os check-ups regulares são essenciais para prevenir doenças e garantir que estamos no caminho certo para uma boa saúde. Além disso, você tem cuidado da sua saúde mental?
Sim, tenho procurado equilibrar minha saúde mental também. Tenho técnicas de relaxamento, como meditação e ioga, e dedicado tempo para atividades que me proporcionam prazer e bem-estar.
Isso é muito importante. A saúde mental é tão crucial quanto a saúde física. É fundamental cuidar das nossas emoções, gerenciar o estresse e buscar apoio quando necessário.
Concordo plenamente. O equilíbrio entre a saúde física e mental é essencial para um estilo de vida saudável. Além disso, você tem algum conselho para manter a motivação e a disciplina?
Manter a motivação e a disciplina pode ser um desafio, mas é importante encontrar o que funciona para você. Definir metas realistas, encontrar atividades físicas e hábitos alimentares que você goste e ter o apoio de pessoas próximas pode ajudar a manter a motivação.
São ótimas dicas! Encontrar prazer nas escolhas saudáveis ​​é fundamental para manter o comprometimento a longo prazo. A saúde é um investimento valioso em nossa qualidade de vida.
Exatamente! Cuidar da nossa saúde é um investimento que colheremos os frutos no futuro. É importante lembrar que pequenas mudanças podem ter um impacto significativo na nossa saúde geral.
Com certeza! A saúde é um bem precioso que deve ser superior e priorizar em nossas vidas. Desejo a você uma jornada contínua de saúde e bem-estar.
Muito obrigado! Desejo o mesmo para você. Vamos continuar nos cuidando e incentivando outros a fazerem o mesmo.
Olá! Você gosta de viajar? Já fez alguma viagem recentemente? Personagem B: Olá! Sim, sou apaixonado por viajar! Recentemente, tive a oportunidade de fazer uma viagem incrível para a Tailândia. Foi uma experiência inesquecível.
Que incrível! A Tailândia é conhecida por suas praias deslumbrantes e cultura rica. O que mais te marcou nessa viagem?
Com certeza, as praias foram deslumbrantes! Mas o que mais me marcou foi a hospitalidade das pessoas e a riqueza dos templos e palácios. Foi uma imersão cultural fascinante.
Adoro conhecer novas culturas e experimentar comidas diferentes durante as viagens. Houve algum prato típico que você experimentou e gostou muito?
Sim! Experimentei o famoso Pad Thai e me apaixonei pelo sabor. Também provei pratos de rua deliciosos, como o caril de coco. A culinária tailandesa é uma verdadeira festa para o paladar.
Fico animado só de ouvir sobre essas experiências gastronômicas! Você já tem algum destino em mente para sua próxima viagem?
Estou planejando visitar o Japão em breve. Sempre fui fascinado pela cultura japonesa, pela arquitetura tradicional e pela culinária única. Mal posso esperar para explorar Tóquio e Kyoto.
O Japão é um destino incrível! Tenho certeza de que você vai adorar. Não se esqueça de visitar os templos, os jardins de cerejeiras e experimentar o autêntico sushi!
Anotei todas as dicas! Estou realmente empolgado com essa viagem. E você, tem algum destino dos sonhos que deseja conhecer?
Sim, meu sonho é visitar a Islândia. As paisagens naturais deslumbrantes, as geleiras e as auroras boreais sempre me encantaram. Espero realizar essa viagem em breve.
A Islândia é um destino fascinante! Tenho certeza de que você terá uma experiência única. Não se esqueça de visitar a famosa Lagoa Azul e explorar as paisagens selvagens.
Com certeza! Obrigado pelas dicas. Viajar é realmente uma forma maravilhosa de explorar o mundo, conhecer novas pessoas e criar memórias inesquecíveis.
Concordo plenamente. As viagens nos enriquecem de maneiras que nenhum outro investimento pode fazer. Desejo a você muitas aventuras emocionantes em suas futuras viagens!
Olá! Você tem algum animal de preservação? Eu adoro animais de estimação!
Olá! Sim, tenho um cachorro. Ele é um verdadeiro companheiro e traz muita alegria para minha vida. E você, tem algum animal de preservação?
Sim, tenho um gato. Ele é uma verdadeira bola de pelos e sempre enche a casa de diversão. Os animais de tentar realmente trazem uma energia especial, não é?
Com certeza! Os animais de sustentação têm uma maneira única de nos alegrar e nos fazer sentir amados. É incrível como eles se tornam parte da família.
Concordo plenamente. Eles nos ensinam sobre lealdade, amor incondicional e nos protegem as coisas simples da vida.
Além disso, ter um animal de vantagem pode ser benéfico para nossa saúde. Eles nos incentivam a praticar exercícios, sofrem o estresse e nos ajudam a criar rotinas treinadas.
Exatamente! Meu gato adora brincar e correr pela casa, o que me motiva a me comandar também. E você, como você cuida do seu cachorro?
Eu o levo para passear todos os dias e garantir que ele tenha uma dieta balanceada. Além disso, também reserva um tempo para brincar com ele e oferece o cuidado e atenção que ele precisa.
É maravilhoso ver como nossos animais de conquista nos retribuem todo o amor e cuidado que damos a eles. Eles realmente têm um lugar especial em nossos corações.
Sem dúvida! Eles são membros valiosos da família. Você já teve alguma experiência comeu ou comeu com seu gato?
Sim, uma vez ele subiu em cima do armário e ficou miando até que eu o resgatei. Foi uma cena divertida! Os gatos sempre nos surpreendem com suas travessuras.
Eles têm personalidades únicas, não é? Meu cachorro adora pegar seus brinquedos e trazê-los para que eu brinque com ele. É uma fofura!
Sim, os animais de realmente realmente trazem muita alegria e amor para nossas vidas. Eles são verdadeiros amigos leais.
Com certeza! Sou grato por ter meu cachorro ao meu lado. Ele é meu companheiro fiel em todas as horas.
Olá! Estou lendo o livro "O Monge e o Executivo" e fiquei fascinado pelos conceitos de liderança apresentados nele. Você já leu o livro ou tem alguma experiência prática com liderança?
Olá! Sim, li o livro e realmente me fez refletir sobre minha abordagem como líder. Acredito que a liderança verdadeira vai além de cargas e títulos. Envolva uma habilidade de inspirar, inspirar e servir aos outros. O que mais chamou sua atenção no livro?
Concordo plenamente. Achei interessante o conceito de liderança servidora, onde o líder está disposto a colocar as necessidades dos outros em primeiro lugar. Acredito que um líder eficaz deve ser capaz de se conectar com sua equipe e criar um ambiente de confiança e respeito mútuo.
Absolutamente! A liderança servidora implica em colocar o bem-estar e o crescimento dos membros da equipe como prioridade. Ao focar em desenvolver e capacitar os outros, o líder fortalecedor a equipe como um todo. Isso resulta em um ambiente de trabalho mais positivo e produtivo.
Concordo plenamente. Além disso, o livro também fala sobre a importância da humildade e da autoridade moral na liderança. O líder deve ser alguém que inspira confiança e respeito por meio de suas ações e valores.
Exatamente! A autoridade moral é conquistada através da integridade e negociação entre o que o líder fala e o que ele faz. É fundamental que o líder seja um exemplo a ser seguido, agindo de acordo com seus princípios e valores.
Isso mesmo! Outro ponto interessante do livro é a importância da escuta ativa. Um líder eficaz deve ser capaz de ouvir as ideias, preocupações e opiniões de sua equipe, buscando entender suas necessidades e promover um ambiente inclusivo.
Com certeza! A escuta ativa é uma habilidade valiosa para um líder, pois demonstra respeito e valorização das contribuições de cada membro da equipe. Ao ouvir atentamente, o líder pode tomar decisões mais difíceis e criar um senso de pertencimento na equipe.
Além disso, o livro também ressalta a importância do autoconhecimento para a liderança. É fundamental que o líder conheça suas próprias virtudes, limitações e áreas de desenvolvimento, buscando constantemente aprimorar suas habilidades.
Com certeza! O autoconhecimento é a base para o desenvolvimento pessoal e profissional. Um líder que está em constante busca por crescimento e aprendizado é capaz de se adaptar às mudanças e liderar com maior eficácia.
Concordo plenamente. Ser um líder eficaz requer um compromisso contínuo com o aprendizado e o crescimento pessoal. É um processo constante de aprimoramento e desenvolvimento de habilidades.
Olá! Você já leu o livro "O Monge e o Executivo"? Ele traz reflexões interessantes sobre liderança e valores pessoais.
Olá! Sim, eu li e achei o livro muito inspirador. Uma das lições que mais me impactou foi a importância de liderar com empatia e compaixão.
Concordo plenamente. No livro, o personagem principal aprende que a verdadeira liderança está enraizada na habilidade de servir e se importar com as pessoas ao seu redor, em vez de apenas buscar o poder e o status.
Exatamente! Acredite que um líder autêntico é aquele que se preocupa em desenvolver e capacitar sua equipe, criando um ambiente de confiança e respeito mútuo.
Sem dúvida. O líder que valoriza as pessoas como seres humanos, ouvindo suas ideias, reconhecendo suas contribuições e fornecendo suporte, fortalecendo relacionamentos sólidos e inspirando o melhor de cada indivíduo.
E não podemos esquecer a importância da autorresponsabilidade como líder. O livro nos lembra que devemos assumir a responsabilidade por nossas ações e decisões, buscando constantemente o aprendizado e o crescimento pessoal.
Com certeza. Um líder responsável não culpa os outros ou as circunstâncias pelos resultados, mas busca soluções e aprendizados mesmo diante dos desafios.
Outro aspecto interessante se encaixa no livro é a importância de ter um propósito maior. Um líder deve se conectar com seus valores e princípios, buscando contribuir para o bem-estar da equipe e da sociedade como um todo.
Concordo totalmente. Quando um líder está alinhado com seu propósito e idade de acordo com seus valores, ele consegue inspirar e motivar os outros a seguirem uma visão comum.
Além disso, a humildade é uma característica fundamental para um líder eficaz. Reconhecer que não tem todas as respostas e estar aberto ao aprendizado contínuo é essencial para promover um ambiente de crescimento e inovação.
Sim, a humildade permite que um líder ouça atentamente, aprenda com os outros e admita seus erros. Isso fortalece a confiança e o respeito dentro da equipe.
Definitivamente. O livro nos lembra que a liderança vai além da carga ou título. É uma jornada de autodescoberta, onde o líder se esforça para desenvolver suas habilidades, influenciar positivamente as pessoas e criar um legado significativo.
Concordo plenamente. O livro "O Monge e o Executivo" nos convida a repensar nossa abordagem à liderança, destacando a importância de cultivar relacionamentos genuínos, agir com integridade e buscar o crescimento pessoal e profissional.
Com certeza. Vamos aplicar esses conceitos em nossa jornada de liderança, lembrando sempre que o verdadeiro poder de um líder está em seu caráter, em sua capacidade de influenciar positivamente as vidas das pessoas ao seu redor.
Olá! Você já explorou um pouco de filosofia? É um assunto fascinante que nos convida a questionar e refletir sobre a vida.
Olá! Sim, estou bastante interessado em filosofia. É incrível como ela nos ajuda a entender melhor o mundo ao nosso redor e nós mesmos. Você tem alguma corrente filosófica favorita?
É difícil escolher apenas uma corrente, pois cada uma traz perspectivas únicas. No entanto, a filosofia estoica sempre me atraiu. Sua ênfase na virtude, na aceitação do que não podemos controlar e no desenvolvimento pessoal é inspiradora.
Concordo. Os estoicos nos ensinam a encontrar serenidade e equilíbrio diante dos desafios da vida. Outra corrente que me interessa é o existencialismo, que nos convida a refletir sobre o sentido da existência e a liberdade de escolha.
O existencialismo certamente nos leva a questionar o propósito e a importância de nossas ações. Também admiro o pensamento de filósofos como Sócrates, que enfatizava a importância do autoconhecimento e do questionamento constante.
Sim, o método socrático de questionamento nos incentiva a buscar a verdade e buscar respostas mais profundas. Ele nos lembra que o conhecimento começa com a humildade de admitir que não sabe tudo.
Além disso, a filosofia nos desafia a refletir sobre questões éticas e morais. É através dessa reflexão que podemos desenvolver uma visão mais clara sobre o que é certo e errado em nossas vidas.
Sem dúvida. A ética e a moralidade são temas fundamentais na filosofia. Elas nos convidam a refletir sobre como devemos agir e viver em sociedade, buscando um equilíbrio entre o bem individual e o bem comum.
E não podemos esquecer a filosofia oriental, como o budismo e o taoísmo, que nos trazem ensinamentos valiosos sobre a busca da paz interior, o desapego e a harmonia com a natureza.
Com certeza. Essas filosofias nos convidam a olhar para dentro de nós mesmos e encontrar um estado de equilíbrio e serenidade. Elas nos ensinam a viver o momento presente e aceitam a impermanência da vida.
A filosofia é realmente uma fonte inesgotável de sabedoria e questionamento. Ela nos desafia a expandir nossos horizontes e pensar de forma mais profunda sobre a vida e o mundo que nos cerca.
Compartilhar essas reflexões filosóficas é enriquecedor. Nos convida a explorar diferentes perspectivas e ter conversas conversas. A filosofia nos lembra que a busca pelo conhecimento e pela compreensão é uma jornada contínua.
Você já ouviu uma piada do pão?
Não, qual é?
Ah, é melhor não... É meio "massante"!
(k,k,k,k,k) Essa foi boa! Agora tenho uma para você: por que o livro de matemática não se dá bem com o livro de história?
Não sei, por quê?
Porque o livro de matemática sempre quer colocar tudo em números, enquanto o livro de história prefere contar as coisas em palavras!
(risos) Muito boa! Adorei a rivalidade literária entre os livros!
É engraçado imaginar os livros discutindo sobre suas compulsivas. É bom ter um pouco de humor para alegrar o dia!
  ]
    

# Crie um treinador para o chatbot
trainer = ListTrainer(chatbot)

# Treine o chatbot com o corpus de perguntas e respostas pré-cadastradas
trainer.train(conversa)
# Train based on english greetings corpus
#trainer.train("chatterbot.corpus.portuguese.greetings")

# Train based on the english conversations corpus
#trainer.train("chatterbot.corpus.portuguese.conversations")

# Função principal do chatbot
def chat():
    print("Olá! Sou um chatbot treinado. Você pode começar a digitar suas perguntas ou digitar 'sair' para encerrar.")

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() == "sair":
            print("ChatBot: Até logo!")
            break

        resposta = chatbot.get_response(pergunta)
        print("ChatBot:", resposta)

# Executar o chatbot
chat()
