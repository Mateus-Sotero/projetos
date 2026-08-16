# -*- coding: utf-8 -*-
"""Generates ebook-mapa-biblico-kids.html — a standalone, print-ready children's
Bible ebook. Run, then render to PDF with Playwright (see render.js)."""

COLORS = {
    "teal":   {"bg": "#0d9488", "bgsoft": "#e6f7f5", "text": "#0d9488"},
    "coral":  {"bg": "#fb7185", "bgsoft": "#feeef0", "text": "#e11d48"},
    "orange": {"bg": "#fb923c", "bgsoft": "#fff3e8", "text": "#c2410c"},
    "sky":    {"bg": "#38bdf8", "bgsoft": "#e8f8ff", "text": "#0284c7"},
    "purple": {"bg": "#a78bfa", "bgsoft": "#f2edfe", "text": "#7c3aed"},
    "gold":   {"bg": "#f5b942", "bgsoft": "#fff8e6", "text": "#b45309"},
    "grass":  {"bg": "#4ade80", "bgsoft": "#eafcf1", "text": "#15803d"},
}

OT_STORIES = [
    dict(icon="🌎", color="sky", ref="Gênesis 1 e 2", title="A Criação do Mundo",
        story="No começo, não existia nada — só Deus. E Deus, com Sua palavra poderosa "
              "e cheia de amor, começou a criar! No primeiro dia fez a luz. Depois, o céu, "
              "os mares, a terra e as plantas. Criou o sol, a lua e as estrelas. Encheu os "
              "mares de peixes e o céu de pássaros. Fez os animais da terra, cada um do seu "
              "jeitinho. E, por último, o melhor de tudo: Deus criou o ser humano — homem e "
              "mulher — à Sua imagem, pra cuidar do mundo e viver perto d'Ele. No sétimo dia, "
              "Deus descansou e olhou pra tudo o que tinha feito. Estava tudo muito bom!",
        lesson="Deus criou cada coisinha do mundo com cuidado e capricho — e criou você "
               "também, do jeitinho que é, porque tem um propósito especial pra sua vida.",
        verse="“No princípio, Deus criou os céus e a terra.” — baseado em Gênesis 1:1",
        question="Qual parte da criação de Deus você acha mais linda: o céu estrelado, o "
                  "mar, as montanhas ou os animais? Por quê?",
        prayer="Obrigado, Deus, por criar um mundo tão lindo e cheio de cores. Obrigado por "
               "me criar também, do jeitinho que sou. Ajuda-me a cuidar bem de tudo que Você "
               "fez. Amém.",
        fact="A palavra “Gênesis” significa “origem” ou “começo” — por isso o primeiro livro da Bíblia tem esse nome!"),
    dict(icon="🍎", color="coral", ref="Gênesis 2 e 3", title="Adão e Eva no Jardim",
        story="Deus colocou Adão e Eva num jardim maravilhoso chamado Éden, cheio de "
              "árvores frutíferas, rios e animais. Lá, eles podiam comer de todas as árvores, "
              "menos de uma: a árvore do conhecimento do bem e do mal. Deus pediu que não "
              "comessem dela, pra protegê-los. Mas uma serpente enganou Eva, dizendo que a "
              "fruta era boa e que Deus estava escondendo algo. Eva comeu e deu também a "
              "Adão. Naquele momento, eles sentiram vergonha e medo pela primeira vez, e "
              "tiveram que deixar o jardim. Mesmo assim, Deus não abandonou os dois: Ele "
              "continuou cuidando deles e prometeu que, um dia, enviaria alguém para "
              "consertar o que tinha se quebrado.",
        lesson="Nossas escolhas têm consequências, mas mesmo quando erramos, Deus não para "
               "de nos amar — Ele sempre nos dá uma nova chance.",
        verse="“Deus fez roupas de peles para Adão e sua mulher, e os vestiu.” — "
              "baseado em Gênesis 3:21",
        question="Já aconteceu de você fazer algo errado e ter medo de contar pra alguém? "
                  "O que você acha que devemos fazer quando erramos?",
        prayer="Deus, obrigado porque mesmo quando eu erro, Você continua me amando. "
               "Ajuda-me a ter coragem de pedir perdão e a fazer escolhas melhores. Amém.",
        fact="Os nomes “Adão” e “Eva” vêm do hebraico e significam algo como “homem/terra” e “que dá vida”."),
    dict(icon="🚢", color="teal", ref="Gênesis 6 a 9", title="Noé e a Grande Arca",
        story="Depois de muito tempo, o mundo ficou cheio de maldade, e isso deixou Deus "
              "triste. Mas havia um homem chamado Noé que amava e obedecia a Deus. Deus "
              "pediu que Noé construísse um barco enorme, uma arca, porque ia mandar uma "
              "grande chuva para lavar o mundo. Noé obedeceu, mesmo sem entender tudo e "
              "mesmo com as pessoas rindo dele. Ele construiu a arca e levou sua família e "
              "um casal de cada animal para dentro. Choveu por 40 dias e 40 noites! Quando a "
              "água baixou, Noé soltou uma pomba, que voltou trazendo um ramo de oliveira — "
              "sinal de que a terra estava seca de novo. Deus fez um arco-íris no céu como "
              "promessa de que nunca mais destruiria a terra com um dilúvio.",
        lesson="Obedecer a Deus às vezes parece estranho ou difícil, principalmente quando "
               "ninguém mais está fazendo o mesmo — mas Deus sempre recompensa quem confia "
               "n'Ele.",
        verse="“E Deus disse: este é o sinal da aliança... porei o meu arco-íris nas "
              "nuvens.” — baseado em Gênesis 9:12-13",
        question="Já teve que fazer a coisa certa mesmo quando os outros amigos estavam "
                  "fazendo diferente? Como você se sentiu?",
        prayer="Senhor, me ajuda a ser corajoso como Noé e a obedecer a Você mesmo quando "
               "for difícil. Obrigado pela promessa do arco-íris. Amém.",
        fact="A arca de Noé era enorme: media cerca de 133 metros de comprimento — quase o tamanho de um campo e meio de futebol!"),
    dict(icon="⭐", color="gold", ref="Gênesis 12 a 22", title="Abraão, o Amigo de Deus",
        story="Deus chamou um homem chamado Abraão e disse: “Saia da sua terra e vá "
              "para o lugar que eu vou te mostrar. Vou te abençoar e fazer de você uma "
              "grande nação!” Abraão não sabia exatamente para onde estava indo, mas "
              "confiou em Deus e partiu com sua esposa Sara. Passaram-se muitos anos, e "
              "Abraão e Sara ainda não tinham filhos — mas Deus tinha prometido que teriam "
              "um. Quando já eram bem idosos, nasceu Isaque, o filho da promessa! Deus "
              "cumpriu exatamente o que tinha dito, porque as promessas de Deus nunca "
              "falham, mesmo que demorem.",
        lesson="Fé é confiar em Deus mesmo quando não conseguimos ver o caminho todo — Deus "
               "sempre cumpre o que promete, no tempo certo.",
        verse="“Abraão creu no Senhor, e isso lhe foi creditado como justiça.” — "
              "baseado em Gênesis 15:6",
        question="Você já teve que esperar bastante por algo que queria muito? Como foi "
                  "essa espera?",
        prayer="Deus, ensina-me a confiar em Você como Abraão confiou, mesmo quando eu não "
               "entender tudo o que está acontecendo. Amém.",
        fact="Abraão é chamado de “pai da fé” e é uma figura importante não só para os cristãos, mas também para judeus e muçulmanos."),
    dict(icon="🌈", color="purple", ref="Gênesis 37 a 45", title="José e o Sonho que Virou Realidade",
        story="José era filho de Jacó e tinha um sonho especial: um dia, sua família se "
              "curvaria diante dele. Seus irmãos ficaram com ciúmes e o venderam como "
              "escravo para o Egito! Lá, mesmo passando por injustiças e até indo preso "
              "sem culpa, José continuou confiando em Deus. Com o tempo, Deus deu a José a "
              "capacidade de entender sonhos, e ele foi levado até o próprio rei do Egito, o "
              "Faraó. José interpretou um sonho que avisava sobre 7 anos de fartura seguidos "
              "de 7 anos de fome, e o Faraó o colocou como governador para organizar tudo! "
              "Anos depois, seus irmãos foram ao Egito buscar comida durante a fome e "
              "encontraram José — que, ao invés de se vingar, os perdoou e disse: “Vocês "
              "pensaram em me fazer mal, mas Deus transformou tudo em bem.”",
        lesson="Mesmo quando as pessoas são injustas com a gente, Deus pode transformar as "
               "coisas mais difíceis em algo bom — e perdoar liberta nosso coração.",
        verse="“Vocês pensaram em me fazer mal, mas Deus tornou isso em bem.” — "
              "baseado em Gênesis 50:20",
        question="Alguma vez alguém foi injusto com você? O que você acha que ajuda a "
                  "perdoar essa pessoa?",
        prayer="Senhor, assim como José, me ajuda a confiar em Você mesmo nas dificuldades, "
               "e me ensina a perdoar quem me machuca. Amém.",
        fact="A túnica especial que José ganhou do pai era um sinal de status — provavelmente tinha mangas compridas e cores variadas."),
    dict(icon="🔥", color="orange", ref="Êxodo 3", title="Moisés e a Sarça Ardente",
        story="Muito tempo depois, o povo de Deus (os israelitas) virou escravo no Egito. "
              "Um bebê chamado Moisés foi salvo das águas do rio Nilo e cresceu no palácio "
              "do Faraó. Anos depois, já adulto, Moisés estava cuidando de ovelhas no "
              "deserto quando viu algo incrível: uma sarça (um arbusto) pegando fogo, mas "
              "sem se queimar! Dali, Deus falou com ele: “Moisés, vá até o Faraó e diga: "
              "deixe o meu povo ir!” Moisés ficou com medo e disse que não sabia falar "
              "direito, mas Deus prometeu estar com ele. Moisés obedeceu, e Deus usou ele "
              "para libertar todo o povo de Israel da escravidão.",
        lesson="Deus não escolhe só os mais fortes ou mais talentosos — Ele escolhe pessoas "
               "comuns, como você, para fazer coisas extraordinárias.",
        verse="“Vai, pois; e eu serei com a tua boca.” — baseado em Êxodo 4:12",
        question="Se Deus te chamasse hoje para fazer algo importante, o que você acha que "
                  "sentiria?",
        prayer="Deus, assim como fez com Moisés, me dá coragem para fazer o que Você pedir, "
               "mesmo quando eu tiver medo. Amém.",
        fact="O nome “Moisés” significa algo como “tirado das águas”, porque ele foi resgatado do rio Nilo quando era bebê."),
    dict(icon="🌊", color="sky", ref="Êxodo 14", title="A Travessia do Mar Vermelho",
        story="Depois de libertar o povo de Israel, Moisés os guiava pelo deserto rumo à "
              "terra prometida. Mas o Faraó se arrependeu de deixá-los ir e mandou seu "
              "exército atrás deles! O povo ficou preso: na frente, o Mar Vermelho; atrás, "
              "os cavalos e carros do exército egípcio se aproximando. Todos ficaram com "
              "muito medo, mas Moisés disse: “Não tenham medo, fiquem parados e vejam a "
              "salvação do Senhor!” Deus mandou um vento forte que abriu um caminho seco "
              "no meio do mar, com água em pé dos dois lados! O povo atravessou em "
              "segurança, e quando o exército egípcio tentou seguir, as águas voltaram ao "
              "normal.",
        lesson="Quando parece que não há saída, Deus pode abrir um caminho onde a gente "
               "nunca imaginou que existiria um.",
        verse="“O Senhor lutará por vocês; fiquem apenas quietos.” — baseado em "
              "Êxodo 14:14",
        question="Você já se sentiu “encurralado”, sem saída para um problema? O "
                  "que essa história ensina sobre confiar em Deus nesses momentos?",
        prayer="Senhor, quando eu não enxergar saída, ajuda-me a lembrar que Você pode abrir "
               "caminhos incríveis. Eu confio em Você. Amém.",
        fact="Até hoje, o povo judeu relembra essa travessia na festa da Páscoa (Pessach), uma das celebrações mais importantes do calendário judaico."),
    dict(icon="📜", color="teal", ref="Êxodo 20", title="Os Dez Mandamentos",
        story="Depois de atravessar o mar, o povo chegou ao monte Sinai. Ali, Deus chamou "
              "Moisés para subir a montanha e lhe deu dez regras importantes, escritas em "
              "tábuas de pedra, para ajudar o povo a viver bem e em paz: amar somente a "
              "Deus, não adorar ídolos, respeitar o nome de Deus, descansar um dia por "
              "semana, honrar pai e mãe, não matar, não trair, não roubar, não mentir e não "
              "cobiçar o que é dos outros. Essas regras não eram para prender o povo, mas "
              "para protegê-lo e ensiná-lo a amar a Deus e ao próximo.",
        lesson="As regras de Deus não existem para nos limitar, mas porque Ele nos ama e "
               "quer o melhor para nossa vida e para quem está ao nosso redor.",
        verse="“Ama o Senhor, teu Deus... e ama o teu próximo como a ti mesmo.” — "
              "baseado em Mateus 22:37-39",
        question="Qual desses mandamentos você acha mais fácil de seguir? E qual é mais "
                  "difícil?",
        prayer="Deus, obrigado por Suas regras que cuidam de mim. Me ajuda a segui-las com "
               "amor, e não só por obrigação. Amém.",
        fact="As tábuas com os Dez Mandamentos eram guardadas dentro de uma caixa muito especial, chamada Arca da Aliança."),
    dict(icon="🎺", color="gold", ref="Josué 6", title="Josué e os Muros de Jericó",
        story="Depois que Moisés morreu, Josué se tornou o novo líder do povo de Israel, e "
              "eles finalmente chegaram perto da terra prometida! Mas na frente havia uma "
              "cidade cercada por muralhas altíssimas: Jericó. Deus deu um plano bem "
              "diferente: o povo devia marchar ao redor da cidade uma vez por dia, durante "
              "seis dias, em silêncio. No sétimo dia, deviam marchar sete vezes, e depois "
              "gritar bem alto enquanto os sacerdotes tocavam trombetas. Parecia um plano "
              "estranho para vencer uma guerra! Mas o povo obedeceu exatamente como Deus "
              "mandou — e, no momento do grito, as muralhas de Jericó desabaram!",
        lesson="Às vezes o plano de Deus parece estranho ou sem sentido para nós, mas quando "
               "confiamos e obedecemos, vemos coisas incríveis acontecerem.",
        verse="“Pela fé, caíram os muros de Jericó, depois de rodeados sete dias.” "
              "— baseado em Hebreus 11:30",
        question="Você já teve que confiar em um plano que não fazia muito sentido pra "
                  "você? Como foi?",
        prayer="Senhor, me ajuda a confiar nos Seus planos, mesmo quando eu não entendo tudo "
               "direito. Amém.",
        fact="Jericó é considerada uma das cidades habitadas mais antigas do mundo — arqueólogos ainda estudam suas muralhas hoje em dia."),
    dict(icon="🪨", color="coral", ref="1 Samuel 17", title="Davi e Golias",
        story="O exército de Israel estava com muito medo de um gigante filisteu chamado "
              "Golias, que desafiava qualquer um a lutar com ele. Ninguém tinha coragem de "
              "enfrentá-lo — ele era enorme e assustador! Mas um jovem pastor de ovelhas "
              "chamado Davi, que tinha ido visitar seus irmãos no acampamento, disse que ia "
              "enfrentar o gigante, confiando em Deus. Todos acharam loucura: Davi era só "
              "um garoto, sem armadura, e o gigante tinha espada e lança enormes! Mas Davi "
              "pegou sua funda e cinco pedrinhas do riacho e disse: “Você vem contra mim "
              "com espada, mas eu venho em nome do Senhor!” Davi acertou uma pedrinha "
              "bem na testa de Golias, e o gigante caiu!",
        lesson="Deus é maior do que qualquer “gigante” na nossa vida — um medo, uma "
               "dificuldade grande — e Ele pode usar até os que parecem pequenos e fracos "
               "para fazer coisas grandes.",
        verse="“O Senhor, que me livrou das garras do leão e do urso, ele me livrará da "
              "mão deste filisteu.” — baseado em 1 Samuel 17:37",
        question="Qual é o seu “gigante” hoje — algo que te dá medo ou parece "
                  "grande demais? Como Davi enfrentou o dele?",
        prayer="Deus, me dá a coragem de Davi para enfrentar meus medos, sabendo que Você "
               "está do meu lado. Amém.",
        fact="Segundo o relato bíblico, Golias tinha quase 3 metros de altura! Mesmo assim, uma pedrinha guiada por fé foi suficiente."),
    dict(icon="🦁", color="orange", ref="Daniel 6", title="Daniel na Cova dos Leões",
        story="Daniel era um homem que amava muito a Deus e orava três vezes por dia, "
              "mesmo morando em um reino estrangeiro. Alguns homens que tinham inveja de "
              "Daniel convenceram o rei a criar uma lei proibindo orar a qualquer deus além "
              "dele por trinta dias, e quem desobedecesse seria jogado numa cova cheia de "
              "leões! Daniel soube da lei, mas continuou orando a Deus normalmente, com a "
              "janela aberta, sem se esconder. Ele foi pego e jogado na cova dos leões. Mas "
              "Deus enviou um anjo que fechou a boca dos leões, e Daniel passou a noite "
              "inteira sem se machucar! Na manhã seguinte, o rei ficou maravilhado e passou "
              "a honrar o Deus de Daniel.",
        lesson="Manter a fé, mesmo quando é arriscado ou dá medo, mostra pra todo mundo o "
               "quanto confiamos em Deus — e Ele cuida de quem é fiel a Ele.",
        verse="“O meu Deus enviou o seu anjo, e fechou a boca dos leões.” — "
              "baseado em Daniel 6:22",
        question="Você continuaria orando mesmo se alguém tentasse te impedir? Por que a "
                  "fé de Daniel era tão forte?",
        prayer="Senhor, me ajuda a ser fiel a Você como Daniel foi, mesmo quando for difícil "
               "ou eu tiver medo. Amém.",
        fact="Daniel viveu na Babilônia, uma das cidades mais avançadas do mundo antigo, e mesmo assim nunca deixou de adorar a Deus."),
    dict(icon="🐋", color="sky", ref="Jonas 1 a 3", title="Jonas e o Grande Peixe",
        story="Deus pediu que o profeta Jonas fosse até a cidade de Nínive avisar que as "
              "pessoas precisavam mudar de vida. Mas Jonas não queria ir — ele fugiu na "
              "direção contrária, pegando um navio! Deus mandou uma tempestade tão forte "
              "que os marinheiros ficaram desesperados. Jonas contou que estava fugindo de "
              "Deus e pediu para ser jogado ao mar, para que a tempestade parasse. Assim que "
              "caiu na água, um grande peixe o engoliu, e Jonas ficou três dias e três "
              "noites dentro dele! Lá dentro, Jonas orou e pediu perdão a Deus. O peixe o "
              "cuspiu na praia, e dessa vez Jonas foi até Nínive, como Deus tinha pedido "
              "desde o começo.",
        lesson="Quando fugimos do que Deus pede, as coisas ficam mais difíceis — mas mesmo "
               "assim, Deus não desiste de nós e nos dá uma nova chance.",
        verse="“E veio a palavra do Senhor a Jonas, pela segunda vez.” — baseado "
              "em Jonas 3:1",
        question="Já tentou “fugir” de fazer algo que sabia que era certo? O que "
                  "aconteceu no final?",
        prayer="Deus, obrigado porque mesmo quando eu fujo do que é certo, Você me dá outra "
               "chance. Me ajuda a obedecer da primeira vez. Amém.",
        fact="Nínive, a cidade para onde Jonas foi enviado, era a capital do Império Assírio — uma das maiores cidades do mundo antigo."),
]

NT_STORIES = [
    dict(icon="⭐", color="gold", ref="Lucas 2", title="O Nascimento de Jesus",
        story="Depois de muitos e muitos anos esperando a promessa de Deus, chegou a hora! "
              "Um anjo apareceu para uma jovem chamada Maria e disse que ela teria um filho "
              "especial, chamado Jesus, o Filho de Deus. Maria e José viajaram até Belém, "
              "mas não havia lugar na hospedaria, então Jesus nasceu num estábulo simples, "
              "e foi colocado numa manjedoura (a caixinha onde os animais comiam). No céu, "
              "uma estrela brilhante apareceu, e anjos anunciaram a boa notícia a alguns "
              "pastores que cuidavam de ovelhas: “Hoje nasceu o Salvador!” Sábios de "
              "terras distantes seguiram a estrela e trouxeram presentes especiais para o "
              "bebê Jesus.",
        lesson="Deus escolheu vir ao mundo do jeito mais simples e humilde possível, "
               "mostrando que Ele se importa com todo mundo, não só com os mais ricos ou "
               "importantes.",
        verse="“Hoje, na cidade de Davi, nasceu o Salvador, que é Cristo, o "
              "Senhor.” — baseado em Lucas 2:11",
        question="Por que você acha que Deus escolheu um estábulo simples, e não um "
                  "palácio, para o nascimento de Jesus?",
        prayer="Obrigado, Jesus, por vir ao mundo por amor a mim. Que eu tenha um coração "
               "simples e agradecido como os pastores. Amém.",
        fact="Os pastores foram os primeiros a saber do nascimento de Jesus — pessoas simples, e não reis ou pessoas importantes!"),
    dict(icon="🕊️", color="sky", ref="Mateus 3", title="O Batismo de Jesus",
        story="Quando Jesus já era adulto, foi até o rio Jordão, onde João Batista batizava "
              "as pessoas que queriam mudar de vida e se aproximar de Deus. João ficou "
              "surpreso quando Jesus pediu para ser batizado, porque Jesus nunca tinha "
              "pecado — Ele não precisava disso! Mas Jesus quis mostrar o caminho certo "
              "para todos nós. Quando Jesus saiu da água, o céu se abriu, o Espírito Santo "
              "desceu como uma pomba sobre Ele, e uma voz do céu disse: “Este é o meu "
              "Filho amado, em quem me agrado!”",
        lesson="Jesus, mesmo sendo perfeito, quis nos mostrar o caminho, do início ao fim — "
               "isso nos ensina a seguir o exemplo d'Ele em tudo o que fazemos.",
        verse="“Este é o meu Filho amado, em quem me agrado.” — baseado em Mateus "
              "3:17",
        question="O que você acha que significa “seguir o exemplo de Jesus” no seu "
                  "dia a dia?",
        prayer="Jesus, quero seguir Seu exemplo em tudo o que eu fizer. Obrigado por me "
               "mostrar o caminho certo. Amém.",
        fact="“Batizar” significa “mergulhar” ou “imergir” — por isso o batismo costumava ser feito em rios, como o Jordão."),
    dict(icon="🎣", color="teal", ref="Mateus 4", title="Jesus Escolhe os Discípulos",
        story="Andando pela beira do mar da Galileia, Jesus viu dois irmãos pescadores, "
              "Pedro e André, jogando suas redes na água. Jesus os chamou: “Venham "
              "comigo, e eu farei de vocês pescadores de pessoas!” Na mesma hora, eles "
              "largaram as redes e o seguiram. Um pouco mais adiante, Jesus chamou outros "
              "dois irmãos, Tiago e João, que também deixaram tudo para segui-lo. Ao longo "
              "do tempo, Jesus escolheu doze discípulos — pessoas comuns, como pescadores e "
              "cobradores de impostos — para aprenderem com Ele e depois contarem a boa "
              "notícia para o mundo inteiro.",
        lesson="Jesus não escolhe as pessoas mais famosas ou perfeitas — Ele chama gente "
               "comum, como você, para fazer parte da Sua grande história.",
        verse="“Venham após mim, e eu os farei pescadores de homens.” — baseado em "
              "Mateus 4:19",
        question="Se Jesus te chamasse pessoalmente hoje para segui-lo, o que você faria?",
        prayer="Jesus, obrigado por me chamar para fazer parte da Sua família. Quero Te "
               "seguir todos os dias da minha vida. Amém.",
        fact="Dos doze discípulos de Jesus, pelo menos quatro — Pedro, André, Tiago e João — eram pescadores de profissão."),
    dict(icon="🍞", color="orange", ref="Mateus 14", title="A Multiplicação dos Pães e Peixes",
        story="Uma tarde, mais de cinco mil pessoas seguiram Jesus até um lugar deserto "
              "para ouvi-lo ensinar e ver os milagres que Ele fazia. Quando ficou tarde, os "
              "discípulos disseram que era melhor mandar as pessoas embora para comprarem "
              "comida, porque não havia nada ali. Jesus respondeu: “Vocês mesmos deem "
              "de comer a eles!” Um menino tinha apenas cinco pães e dois peixinhos, e "
              "os entregou a Jesus. Jesus abençoou aquela pouquinha comida, e — para a "
              "surpresa de todos — deu para todo mundo comer, e ainda sobrou! Doze cestos "
              "cheios de sobras, para mais de cinco mil pessoas!",
        lesson="Quando entregamos o pouco que temos nas mãos de Jesus, mesmo que pareça "
               "insuficiente, Ele pode multiplicar e fazer muito mais do que imaginamos.",
        verse="“Trouxeram-lhe os cinco pães e os dois peixes... e todos comeram e se "
              "fartaram.” — baseado em Mateus 14:19-20",
        question="Você tem algo pequeno — um talento, um brinquedo, um gesto de carinho — "
                  "que poderia compartilhar com alguém hoje?",
        prayer="Jesus, ensina-me a compartilhar o que eu tenho, confiando que Você pode "
               "fazer muito com o pouco que eu ofereço. Amém.",
        fact="Esse é um dos poucos milagres de Jesus contado nos quatro Evangelhos: Mateus, Marcos, Lucas e João!"),
    dict(icon="⛵", color="sky", ref="Marcos 4", title="Jesus Acalma a Tempestade",
        story="Depois de um longo dia ensinando, Jesus e os discípulos entraram num barco "
              "para atravessar o mar da Galileia. Jesus estava tão cansado que adormeceu "
              "logo na popa do barco. De repente, uma tempestade forte se levantou, com "
              "ondas enormes que ameaçavam afundar o barco! Os discípulos ficaram "
              "apavorados e acordaram Jesus, gritando: “Mestre, não te importas que "
              "estamos morrendo?” Jesus se levantou, olhou para o vento e o mar, e "
              "disse apenas: “Acalme-se!” E, na mesma hora, tudo ficou completamente "
              "calmo. Os discípulos ficaram admirados: “Até o vento e o mar lhe "
              "obedecem!”",
        lesson="Mesmo nas “tempestades” da nossa vida — medos, problemas, "
               "dificuldades — Jesus está no barco com a gente, e Ele tem o poder de trazer "
               "paz.",
        verse="“Acalma-te, emudece! E o vento cessou, e fez-se grande "
              "bonança.” — baseado em Marcos 4:39",
        question="O que você faz quando sente medo ou está passando por um momento "
                  "difícil?",
        prayer="Jesus, quando eu passar por tempestades, me lembra que Você está comigo e "
               "pode trazer paz ao meu coração. Amém.",
        fact="O mar da Galileia é, na verdade, um grande lago de água doce, conhecido por tempestades repentinas e muito fortes."),
    dict(icon="🏠", color="coral", ref="Lucas 15", title="A Parábola do Filho Pródigo",
        story="Jesus contou a história de um pai com dois filhos. O filho mais novo pediu "
              "sua parte da herança e foi embora para um país distante, onde gastou tudo "
              "vivendo de forma descontrolada. Quando o dinheiro acabou, veio uma grande "
              "fome, e ele ficou tão pobre que passou a cuidar de porcos e até teve vontade "
              "de comer a comida deles! Foi aí que ele pensou: “Vou voltar para casa do "
              "meu pai e pedir perdão.” Enquanto ele ainda estava longe, o pai o viu "
              "chegando, correu ao encontro dele, o abraçou e organizou uma grande festa, "
              "dizendo: “Meu filho estava morto e voltou a viver; estava perdido e foi "
              "encontrado!”",
        lesson="Não importa o quanto a gente se afaste ou erre, o coração de Deus está "
               "sempre pronto para nos receber de volta com amor, sem cobranças.",
        verse="“Enquanto ainda estava longe, seu pai o viu e, cheio de compaixão, "
              "correu, abraçou-o.” — baseado em Lucas 15:20",
        question="Como você se sente sabendo que Deus sempre te recebe de volta, não "
                  "importa o que aconteça?",
        prayer="Pai, obrigado porque Seus braços estão sempre abertos para mim. Me ajuda a "
               "voltar para perto de Você sempre que eu me afastar. Amém.",
        fact="Essa é uma parábola — uma história inventada por Jesus para ensinar uma lição. Ele contava muitas histórias assim!"),
    dict(icon="❤️", color="purple", ref="Lucas 10", title="A Parábola do Bom Samaritano",
        story="Um mestre da lei perguntou a Jesus: “Quem é o meu próximo?” Jesus "
              "respondeu com uma história: um homem estava viajando quando foi atacado por "
              "ladrões, que bateram nele, roubaram tudo e o deixaram quase morto na estrada. "
              "Um sacerdote passou por ali e desviou para o outro lado. Depois, um levita "
              "(ajudante do templo) fez a mesma coisa. Mas um samaritano — alguém que, "
              "naquela época, era mal visto pelos judeus — parou, cuidou dos ferimentos do "
              "homem, o levou numa pousada e pagou tudo o que ele precisava para se "
              "recuperar. Jesus perguntou: “Qual dos três foi o próximo daquele "
              "homem?” A resposta era clara: aquele que teve compaixão.",
        lesson="Amar o próximo é cuidar de quem precisa, mesmo que essa pessoa seja "
               "diferente de nós ou que ninguém mais esteja ajudando.",
        verse="“Vá, e faça a mesma coisa.” — baseado em Lucas 10:37",
        question="Você conhece alguém que precisa de ajuda ou de um gesto de carinho hoje? "
                  "O que você pode fazer?",
        prayer="Jesus, me ensina a ter um coração cheio de compaixão, pronto para ajudar "
               "quem precisa, do jeito que o bom samaritano fez. Amém.",
        fact="Na época de Jesus, judeus e samaritanos geralmente não se davam bem — por isso a atitude do samaritano surpreendeu tanto quem ouviu."),
    dict(icon="🍇", color="purple", ref="Mateus 26", title="A Última Ceia",
        story="Antes da festa da Páscoa, Jesus se reuniu com Seus doze discípulos para uma "
              "última refeição especial. Durante o jantar, Jesus fez algo surpreendente: se "
              "levantou, pegou uma bacia com água e começou a lavar os pés dos discípulos — "
              "uma tarefa que normalmente era feita pelos servos! Ele queria ensinar que "
              "amar de verdade é servir uns aos outros, sem orgulho. Depois, Jesus pegou o "
              "pão, abençoou e disse: “Isto é o meu corpo, entregue por vocês.” "
              "Depois pegou o cálice de vinho e disse: “Isto é o meu sangue, derramado "
              "por vocês.” Ele estava se preparando para dar a vida por todos nós, por "
              "amor.",
        lesson="Jesus nos ensinou, com atitudes e não só com palavras, que servir com amor é "
               "o caminho mais bonito de viver.",
        verse="“Assim como eu vos amei, que também vos ameis uns aos "
              "outros.” — baseado em João 13:34",
        question="Você consegue pensar em uma forma de servir alguém da sua casa esta "
                  "semana, como Jesus fez com os discípulos?",
        prayer="Jesus, me ensina a servir com amor, sem esperar nada em troca, assim como "
               "Você fez por mim. Amém.",
        fact="Até hoje, muitas igrejas relembram a Última Ceia por meio de uma celebração chamada Santa Ceia ou Eucaristia."),
    dict(icon="✝️", color="gold", ref="Mateus 27 e 28", title="A Crucificação e a Ressurreição",
        story="Jesus foi preso injustamente, julgado e condenado a morrer numa cruz — "
              "mesmo nunca tendo feito nada de errado. Ele fez isso por amor, para pagar "
              "pelos erros de todas as pessoas do mundo, para sempre. Foi um dia muito "
              "triste: Jesus morreu e foi colocado num túmulo, com uma pedra enorme na "
              "entrada. Mas essa não foi a última parte da história! No terceiro dia, "
              "domingo de manhã bem cedo, algumas mulheres foram até o túmulo e encontraram "
              "a pedra removida — e o túmulo vazio! Um anjo disse: “Ele não está aqui, "
              "ressuscitou, como tinha dito!” Jesus estava vivo outra vez, vencendo até "
              "a morte, e apareceu para muitas pessoas depois disso.",
        lesson="Jesus deu a Sua vida por amor a cada um de nós, e Sua ressurreição nos "
               "mostra que, com Deus, sempre existe esperança, mesmo depois dos momentos "
               "mais tristes.",
        verse="“Ele não está aqui; ressuscitou, como tinha dito.” — baseado em "
              "Mateus 28:6",
        question="Como você se sente sabendo que Jesus fez tudo isso por amor a você?",
        prayer="Jesus, obrigado por dar a Sua vida por mim e por vencer a morte. Quero viver "
               "cada dia agradecido por esse amor tão grande. Amém.",
        fact="A Páscoa cristã, celebrada até hoje no mundo todo, é justamente a comemoração da ressurreição de Jesus."),
    dict(icon="🔥", color="orange", ref="Atos 2", title="O Pentecostes e o Início da Igreja",
        story="Depois que Jesus ressuscitou, Ele ficou mais um tempo com os discípulos e "
              "depois subiu ao céu, prometendo enviar o Espírito Santo para ajudá-los. Dez "
              "dias depois, durante uma festa judaica chamada Pentecostes, os discípulos "
              "estavam todos reunidos quando, de repente, ouviram um som como um vento "
              "forte enchendo a casa toda, e algo parecido com línguas de fogo apareceu "
              "sobre a cabeça de cada um deles! Eles ficaram cheios do Espírito Santo e "
              "começaram a falar sobre Jesus com uma coragem que não tinham antes — tanta "
              "coragem que, naquele mesmo dia, milhares de pessoas decidiram seguir a Jesus "
              "também. Assim começou a Igreja, uma grande família espalhada pelo mundo "
              "todo.",
        lesson="Deus dá coragem e força para contarmos sobre o Seu amor a todas as pessoas "
               "ao nosso redor, mesmo quando temos medo ou vergonha.",
        verse="“E todos foram cheios do Espírito Santo.” — baseado em Atos 2:4",
        question="O que você conta para seus amigos sobre o quanto Deus te ama?",
        prayer="Espírito Santo, me enche de coragem para contar sobre o amor de Jesus para "
               "todas as pessoas que eu encontrar. Amém.",
        fact="A palavra “Pentecostes” vem do grego e significa “quinquagésimo dia” — 50 dias depois da Páscoa."),
]

QUIZ = [
    ("Quem construiu uma arca enorme para escapar do dilúvio?", ["Abraão", "Noé", "Moisés", "Davi"], 1),
    ("Qual jovem pastor enfrentou o gigante Golias com uma funda e uma pedrinha?", ["José", "Daniel", "Davi", "Jonas"], 2),
    ("Em que cidade Jesus nasceu?", ["Jerusalém", "Nazaré", "Belém", "Jericó"], 2),
    ("Quantos mandamentos Deus deu a Moisés no monte Sinai?", ["Cinco", "Sete", "Dez", "Doze"], 2),
    ("Quem foi jogado na cova dos leões por continuar orando a Deus?", ["Jonas", "Daniel", "José", "Josué"], 1),
    ("O que aconteceu com as muralhas de Jericó depois que o povo marchou e gritou?", ["Ficaram mais fortes", "Não mudou nada", "Desabaram", "Viraram ouro"], 2),
    ("Quantos pães e peixes o menino entregou a Jesus antes da multiplicação?", ["2 pães e 5 peixes", "5 pães e 2 peixes", "10 pães e 10 peixes", "Só 1 peixe"], 1),
    ("Na parábola do bom samaritano, quem ajudou o homem ferido na estrada?", ["O sacerdote", "O levita", "O samaritano", "Um soldado"], 2),
    ("O que aconteceu no terceiro dia depois que Jesus morreu na cruz?", ["Ele apareceu como anjo", "O túmulo continuou fechado", "Ele ressuscitou", "Nada mudou"], 2),
    ("No Pentecostes, o que os discípulos receberam para ter coragem de falar de Jesus?", ["Um livro novo", "O Espírito Santo", "Uma espada", "Um mapa"], 1),
]

DRAW_PROMPTS = [
    dict(color="teal", title="Desenhe a Arca de Noé",
         prompt="Como você imagina a arca de Noé por dentro? Desenhe os animais entrando, "
                "dois a dois, e não esqueça da pomba com o ramo de oliveira!"),
    dict(color="gold", title="Desenhe o Nascimento de Jesus",
         prompt="Desenhe o estábulo onde Jesus nasceu, com Maria, José, os pastores e a "
                "estrela brilhando lá no céu."),
    dict(color="coral", title="Desenhe Você e Jesus",
         prompt="Imagine que Jesus está pertinho de você agora. O que vocês estariam "
                "fazendo juntos? Desenhe essa cena!"),
]

# ---------------------------------------------------------------------------
# HTML rendering
# ---------------------------------------------------------------------------

def esc(s):
    return s

def story_page(idx, total, section_label, s):
    c = COLORS[s["color"]]
    return f"""
<section class="page story-page" style="--accent:{c['bg']}; --accent-soft:{c['bgsoft']}; --accent-text:{c['text']}">
  <div class="story-deco tl">✦</div>
  <div class="story-deco br">✦</div>
  <header class="story-head">
    <div class="story-badge">{s['icon']}</div>
    <div class="story-head-text">
      <span class="story-kicker">{section_label} · História {idx} de {total}</span>
      <h2>{s['title']}</h2>
      <span class="story-ref">📍 {s['ref']}</span>
    </div>
  </header>
  <p class="story-body">{s['story']}</p>
  <div class="story-grid">
    <div class="callout lesson">
      <span class="callout-tag">💡 Lição de hoje</span>
      <p>{s['lesson']}</p>
    </div>
    <div class="callout verse">
      <span class="callout-tag">📖 Versículo pra guardar</span>
      <p>{s['verse']}</p>
    </div>
  </div>
  <div class="story-grid">
    <div class="callout question">
      <span class="callout-tag">🤔 Vamos pensar</span>
      <p>{s['question']}</p>
    </div>
    <div class="callout prayer">
      <span class="callout-tag">🙏 Oração</span>
      <p>{s['prayer']}</p>
    </div>
  </div>
  <div class="callout fact">
    <span class="callout-tag">🌟 Você sabia?</span>
    <p>{s['fact']}</p>
  </div>
  <div class="story-stripe">{(s['icon'] + ' ') * 14}</div>
  <div class="page-foot">Mapa Bíblico Kids</div>
</section>"""


def divider_page(title, subtitle, emoji, color):
    c = COLORS[color]
    return f"""
<section class="page divider-page" style="--accent:{c['bg']}">
  <div class="divider-shape s1"></div>
  <div class="divider-shape s2"></div>
  <div class="divider-shape s3"></div>
  <div class="divider-emoji">{emoji}</div>
  <h1>{title}</h1>
  <p>{subtitle}</p>
</section>"""


def _quiz_rows(items, start):
    letters = ["A", "B", "C", "D"]
    rows = []
    for offset, (q, opts, correct) in enumerate(items):
        i = start + offset
        opt_html = "".join(
            f'<li><span class="opt-letter">{letters[j]}</span>{o}</li>'
            for j, o in enumerate(opts)
        )
        rows.append(f'<li class="quiz-q"><p class="quiz-q-text">{i}. {q}</p>'
                     f'<ul class="quiz-opts">{opt_html}</ul></li>')
    return "".join(rows)


def quiz_pages():
    half = len(QUIZ) // 2
    first, second = QUIZ[:half], QUIZ[half:]
    page1 = f"""
<section class="page quiz-page">
  <header class="section-head" style="--accent:{COLORS['purple']['bg']}">
    <span class="section-kicker">🎉 Hora de brincar e aprender</span>
    <h1>Quiz: Você é Craque na Bíblia?</h1>
    <p>Marque com um círculo a resposta certa em cada pergunta. O gabarito está na
    próxima página!</p>
  </header>
  <ol class="quiz-list">{_quiz_rows(first, 1)}</ol>
  <div class="page-foot">Mapa Bíblico Kids</div>
</section>"""
    answer_key = " · ".join(
        f"{i+1}-{['A','B','C','D'][c]}" for i, (_, _, c) in enumerate(QUIZ)
    )
    page2 = f"""
<section class="page quiz-page">
  <header class="section-head" style="--accent:{COLORS['purple']['bg']}">
    <span class="section-kicker">🎉 continuando o quiz</span>
    <h1>Mais Perguntas Pra Você!</h1>
  </header>
  <ol class="quiz-list" start="{half + 1}">{_quiz_rows(second, half + 1)}</ol>
  <div class="answer-key">🔑 Gabarito: {answer_key}</div>
  <div class="page-foot">Mapa Bíblico Kids</div>
</section>"""
    return page1 + page2


def draw_page(d):
    c = COLORS[d["color"]]
    return f"""
<section class="page draw-page" style="--accent:{c['bg']}; --accent-soft:{c['bgsoft']}">
  <span class="section-kicker">🎨 Hora de criar</span>
  <h1>{d['title']}</h1>
  <p class="draw-prompt">{d['prompt']}</p>
  <div class="draw-frame">
    <span class="draw-frame-corner tl"></span>
    <span class="draw-frame-corner tr"></span>
    <span class="draw-frame-corner bl"></span>
    <span class="draw-frame-corner br"></span>
  </div>
  <div class="page-foot">Mapa Bíblico Kids</div>
</section>"""


COVER_PAGE = """
<section class="page cover-page">
  <div class="cover-shape c1"></div>
  <div class="cover-shape c2"></div>
  <div class="cover-shape c3"></div>
  <div class="cover-shape c4"></div>
  <div class="cover-stars">✦ ⋆ ✦ ⋆ ✦ ⋆ ✦ ⋆ ✦</div>
  <div class="cover-badge">📖✨</div>
  <span class="cover-kicker">um livro para crianças exploradoras da Bíblia</span>
  <h1 class="cover-title">Mapa Bíblico<br>Kids</h1>
  <p class="cover-subtitle">Da Criação à Igreja: 22 histórias, lições, versículos,<br>
     perguntas, orações e atividades para viver a Palavra de Deus</p>
  <div class="cover-icons">🌍 🐑 ⭐ 🕊️ ✝️ 🔥</div>
  <span class="cover-brand">Mapa Bíblico Kids</span>
</section>"""


LETTER_PAGE = """
<section class="page letter-page">
  <span class="section-kicker" style="--accent:#0d9488">💌 uma cartinha especial</span>
  <h1>Para os Pais, Padrinhos e Professores</h1>
  <p>Que alegria ter você e sua criança começando essa jornada! Este e-book foi feito
  com muito carinho para apresentar a Bíblia inteira de um jeito simples, ilustrado e
  gostoso de aprender — da Criação até o nascimento da Igreja.</p>
  <p>Cada história vem acompanhada de quatro ferramentas para ajudar a transformar
  leitura em aprendizado de verdade:</p>
  <ul class="letter-list">
    <li><span class="letter-ic" style="background:#0d9488">💡</span>
        <b>Lição de hoje</b> — o valor ou princípio central da história.</li>
    <li><span class="letter-ic" style="background:#38bdf8">📖</span>
        <b>Versículo pra guardar</b> — uma referência bíblica para memorizar juntos.</li>
    <li><span class="letter-ic" style="background:#fb923c">🤔</span>
        <b>Vamos pensar</b> — uma pergunta para conversar em família.</li>
    <li><span class="letter-ic" style="background:#a78bfa">🙏</span>
        <b>Oração</b> — uma oração curtinha, do jeitinho de uma criança.</li>
  </ul>
  <p>Sugerimos ler uma história por dia, em voz alta, e depois conversar juntos sobre
  a pergunta e fazer a oração de mãos dadas. No final, tem quiz, atividades de desenho
  e um certificado para comemorar a conquista!</p>
  <p class="letter-sign">Com carinho,<br><b>Equipe Mapa Bíblico Kids</b></p>
  <div class="page-stripe">💌 📖 💜 📖 💌 📖 💜 📖 💌 📖 💜 </div>
  <div class="page-foot">Mapa Bíblico Kids</div>
</section>"""


HOWTO_PAGE = """
<section class="page howto-page">
  <span class="section-kicker" style="--accent:#fb7185">🧭 como usar este livro</span>
  <h1>Sua Aventura Tem 4 Passos</h1>
  <div class="howto-grid">
    <div class="howto-card" style="--accent:#0d9488">
      <span class="howto-num">1</span>
      <span class="howto-ic">📖</span>
      <h3>Leia a história</h3>
      <p>Cada capítulo conta uma história da Bíblia de um jeito simples e gostoso.</p>
    </div>
    <div class="howto-card" style="--accent:#fb923c">
      <span class="howto-num">2</span>
      <span class="howto-ic">💡</span>
      <h3>Descubra a lição</h3>
      <p>Veja o que essa história ensina para a nossa vida hoje.</p>
    </div>
    <div class="howto-card" style="--accent:#38bdf8">
      <span class="howto-num">3</span>
      <span class="howto-ic">🤔</span>
      <h3>Converse e ore</h3>
      <p>Responda a pergunta com a família e faça a oraçãozinha juntos.</p>
    </div>
    <div class="howto-card" style="--accent:#a78bfa">
      <span class="howto-num">4</span>
      <span class="howto-ic">🎉</span>
      <h3>Brinque e aprenda</h3>
      <p>No final, teste o que aprendeu no quiz e desenhe suas cenas favoritas!</p>
    </div>
  </div>
  <div class="page-stripe">🧭 ✨ 🎈 🧭 ✨ 🎈 🧭 ✨ 🎈 🧭 ✨ </div>
  <div class="page-foot">Mapa Bíblico Kids</div>
</section>"""


def toc_page():
    ot_items = "".join(f'<li><span class="toc-ic">{s["icon"]}</span>{s["title"]}</li>' for s in OT_STORIES)
    nt_items = "".join(f'<li><span class="toc-ic">{s["icon"]}</span>{s["title"]}</li>' for s in NT_STORIES)
    return f"""
<section class="page toc-page">
  <span class="section-kicker" style="--accent:#f5b942">🗺️ sumário</span>
  <h1>O Que Você Vai Encontrar</h1>
  <div class="toc-columns">
    <div class="toc-col">
      <h3 style="color:#0d9488">🏺 Antigo Testamento</h3>
      <ul class="toc-list">{ot_items}</ul>
    </div>
    <div class="toc-col">
      <h3 style="color:#7c3aed">✝️ Novo Testamento</h3>
      <ul class="toc-list">{nt_items}</ul>
      <h3 style="color:#e11d48; margin-top:18px">🎉 Hora de Brincar</h3>
      <ul class="toc-list">
        <li><span class="toc-ic">❓</span>Quiz bíblico</li>
        <li><span class="toc-ic">🎨</span>Atividades de desenho</li>
        <li><span class="toc-ic">🏆</span>Certificado</li>
      </ul>
    </div>
  </div>
  <div class="page-stripe">🗺️ ⭐ 📚 🗺️ ⭐ 📚 🗺️ ⭐ 📚 🗺️ </div>
  <div class="page-foot">Mapa Bíblico Kids</div>
</section>"""


PANORAMA_PAGE = """
<section class="page panorama-page">
  <span class="section-kicker" style="--accent:#0d9488">🗺️ panorama geral</span>
  <h1>A Bíblia é Uma Historia Só!</h1>
  <p>A Bíblia tem 66 livros, escritos ao longo de muitos e muitos anos — mas todos eles
  contam uma única grande história: a de um Deus que ama o mundo e quer estar perto das
  pessoas que Ele criou. Ela se divide em duas grandes partes:</p>
  <div class="panorama-split">
    <div class="panorama-half" style="--accent:#0d9488">
      <span class="panorama-num">39</span>
      <h3>Antigo Testamento</h3>
      <p>Conta desde a Criação do mundo até a preparação para a chegada de Jesus:
      os primeiros povos, as promessas de Deus a Abraão, a libertação do Egito, os reis,
      os profetas e a longa espera pelo Salvador prometido.</p>
    </div>
    <div class="panorama-half" style="--accent:#a78bfa">
      <span class="panorama-num">27</span>
      <h3>Novo Testamento</h3>
      <p>Conta a vida de Jesus — Seu nascimento, ensinamentos, milagres, morte e
      ressurreição — e o começo da Igreja, quando Seus seguidores levaram essa boa
      notícia para o mundo inteiro.</p>
    </div>
  </div>
  <h2 class="panorama-timeline-title">✨ Linha do Tempo Resumida</h2>
  <div class="timeline">
    <div class="timeline-item"><span class="timeline-dot" style="background:#0d9488"></span>
      <b>Criação</b><span>Deus cria o mundo e as primeiras pessoas</span></div>
    <div class="timeline-item"><span class="timeline-dot" style="background:#38bdf8"></span>
      <b>Patriarcas</b><span>Abraão, Isaque, Jacó e José</span></div>
    <div class="timeline-item"><span class="timeline-dot" style="background:#fb923c"></span>
      <b>Êxodo</b><span>Moisés liberta o povo da escravidão no Egito</span></div>
    <div class="timeline-item"><span class="timeline-dot" style="background:#f5b942"></span>
      <b>Reis e Profetas</b><span>Davi, Salomão e os profetas anunciam o Salvador</span></div>
    <div class="timeline-item"><span class="timeline-dot" style="background:#fb7185"></span>
      <b>Jesus</b><span>O Filho de Deus nasce, ensina, morre e ressuscita</span></div>
    <div class="timeline-item"><span class="timeline-dot" style="background:#a78bfa"></span>
      <b>A Igreja</b><span>Os discípulos espalham a boa notícia pelo mundo</span></div>
  </div>
  <p class="panorama-highlight">💜 Do primeiro ao último livro, existe um fio condutor: <b>Jesus é o
  centro de tudo</b>, o herói dessa grande história de amor.</p>
  <div class="page-stripe">🗺️ ⏳ ✨ 🗺️ ⏳ ✨ 🗺️ ⏳ ✨ 🗺️ </div>
  <div class="page-foot">Mapa Bíblico Kids</div>
</section>"""


CLOSING_PAGE = """
<section class="page closing-page">
  <div class="cover-shape c1"></div>
  <div class="cover-shape c2"></div>
  <div class="closing-emoji">🎉📖💜</div>
  <h1>Parabéns por Chegar até Aqui!</h1>
  <p>Você agora conhece as histórias mais importantes da Bíblia, do começo ao fim.
  Continue lendo, conversando e orando — a Palavra de Deus é um tesouro para a vida
  inteira!</p>
  <span class="cover-brand">Mapa Bíblico Kids</span>
  <p class="closing-copy">Mapa Bíblico Kids © 2026 — Todos os direitos reservados</p>
</section>"""


def certificate_page():
    return """
<section class="page certificate-page">
  <div class="certificate-border">
    <span class="cert-ic">🏆</span>
    <span class="cert-kicker">certificado de conclusão</span>
    <h1>Eu Conheço a Bíblia!</h1>
    <p class="cert-text">Certificamos que</p>
    <div class="cert-line"></div>
    <p class="cert-text">leu e aprendeu as 22 histórias do <b>Mapa Bíblico Kids</b>,
    do Antigo ao Novo Testamento, e descobriu que Jesus é o centro de tudo!</p>
    <div class="cert-footer">
      <div><div class="cert-line small"></div><span>data</span></div>
      <div class="cert-seal">⭐</div>
      <div><div class="cert-line small"></div><span>assinatura</span></div>
    </div>
  </div>
</section>"""


CSS = """
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@500;600;700;800&family=Nunito:wght@400;600;700;800&display=swap');

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: 'Nunito', sans-serif;
  color: #374151;
  line-height: 1.55;
  background: #e9ecef;
}
h1, h2, h3 { font-family: 'Baloo 2', cursive; color: #134e4a; margin: 0 0 10px; line-height: 1.2; }
p { margin: 0 0 10px; }
ul, ol { margin: 0; }

.page {
  position: relative;
  width: 210mm;
  min-height: 297mm;
  margin: 0 auto;
  background: #fffaf3;
  padding: 20mm 18mm;
  overflow: hidden;
  page-break-after: always;
}

.page-foot {
  position: absolute;
  bottom: 10mm;
  left: 0; right: 0;
  text-align: center;
  font-size: 10px;
  letter-spacing: .5px;
  color: #b3b0a8;
  font-weight: 700;
  text-transform: uppercase;
}

/* ---------- Cover ---------- */
.cover-page {
  background: linear-gradient(160deg, #0d9488 0%, #0f766e 45%, #134e4a 100%);
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  gap: 14px;
}
.cover-shape { position: absolute; border-radius: 50%; opacity: .18; }
.c1 { width: 260px; height: 260px; background: #fb923c; top: -80px; left: -80px; }
.c2 { width: 200px; height: 200px; background: #fb7185; bottom: -60px; right: -60px; }
.c3 { width: 140px; height: 140px; background: #f5b942; bottom: 60px; left: -50px; }
.c4 { width: 100px; height: 100px; background: #a78bfa; top: 90px; right: -30px; }
.cover-stars { letter-spacing: 8px; font-size: 14px; opacity: .8; }
.cover-badge {
  font-size: 54px; background: rgba(255,255,255,.15); border: 3px solid rgba(255,255,255,.4);
  width: 120px; height: 120px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
}
.cover-kicker { text-transform: uppercase; letter-spacing: 2px; font-size: 12px; font-weight: 700; opacity: .85; }
.cover-title { font-size: 64px; color: #fff; margin: 6px 0; }
.cover-subtitle { font-size: 16px; max-width: 480px; opacity: .92; }
.cover-icons { font-size: 26px; letter-spacing: 10px; margin-top: 12px; }
.cover-brand {
  margin-top: 22px; font-family: 'Baloo 2', cursive; font-size: 15px;
  background: rgba(255,255,255,.15); padding: 6px 22px; border-radius: 50px;
}

/* ---------- Section kicker (generic label pill) ---------- */
.section-kicker {
  display: inline-flex; align-items: center; gap: 6px;
  background: var(--accent, #0d9488); color: #fff;
  font-weight: 800; font-size: 11px; letter-spacing: 1px; text-transform: uppercase;
  padding: 6px 16px; border-radius: 50px; margin-bottom: 14px;
}
.section-head { text-align: center; margin-bottom: 8px; }
.section-head p { max-width: 480px; margin: 0 auto; color: #6b7280; }

/* ---------- Letter page ---------- */
.letter-page h1 { font-size: 32px; }
.letter-page p { font-size: 15.5px; line-height: 1.7; }
.letter-list { list-style: none; padding: 0; margin: 18px 0; }
.letter-list li {
  display: flex; align-items: flex-start; gap: 14px;
  margin-bottom: 16px; font-size: 15.5px; line-height: 1.6;
}
.letter-ic {
  flex: 0 0 auto; width: 36px; height: 36px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  color: #fff; font-size: 17px;
}
.letter-sign { margin-top: 24px; font-style: italic; color: #134e4a; font-size: 15.5px; }

/* ---------- How to use ---------- */
.howto-page h1 { font-size: 32px; }
.howto-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 24px; }
.howto-card {
  background: #fff; border: 2px solid #eee;
  border-top: 6px solid var(--accent); border-radius: 18px; padding: 26px;
  position: relative;
}
.howto-num {
  position: absolute; top: -16px; right: 18px;
  background: var(--accent); color: #fff; font-family: 'Baloo 2', cursive;
  width: 34px; height: 34px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center; font-size: 17px;
}
.howto-ic { font-size: 34px; display: block; margin-bottom: 10px; }
.howto-card h3 { font-size: 19px; margin-bottom: 8px; }
.howto-card p { font-size: 14.5px; color: #6b7280; margin: 0; line-height: 1.55; }

/* ---------- TOC ---------- */
.toc-page h1 { font-size: 32px; }
.toc-columns { display: grid; grid-template-columns: 1fr 1fr; gap: 36px; margin-top: 18px; }
.toc-col h3 { font-size: 18px; margin-bottom: 12px; }
.toc-list { list-style: none; padding: 0; }
.toc-list li {
  display: flex; align-items: center; gap: 12px;
  font-size: 14.5px; font-weight: 700; color: #374151;
  padding: 10px 0; border-bottom: 1px dashed #e5e7eb;
}
.toc-ic { font-size: 18px; }

/* ---------- Panorama ---------- */
.panorama-page h1 { font-size: 32px; }
.panorama-page > p { font-size: 15.5px; line-height: 1.7; }
.panorama-split { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin: 20px 0; }
.panorama-half {
  background: #fff; border: 2px solid #eee; border-top: 6px solid var(--accent);
  border-radius: 18px; padding: 22px;
}
.panorama-num { font-family: 'Baloo 2', cursive; font-size: 40px; color: var(--accent); }
.panorama-half h3 { font-size: 19px; margin: 6px 0 10px; }
.panorama-half p { font-size: 14.5px; color: #6b7280; margin: 0; line-height: 1.6; }
.panorama-timeline-title { font-size: 22px; margin-top: 14px; }
.timeline {
  display: flex; flex-direction: column; gap: 14px; margin: 16px 0;
  border-left: 3px dashed #ddd6fe; padding-left: 20px;
}
.timeline-item { display: flex; align-items: baseline; gap: 10px; font-size: 14.5px; }
.timeline-dot {
  width: 12px; height: 12px; border-radius: 50%; margin-left: -26px; margin-right: 6px;
  border: 2px solid #fff; box-shadow: 0 0 0 2px #eee;
}
.timeline-item b { color: #134e4a; min-width: 130px; display: inline-block; }
.timeline-item span { color: #6b7280; }
.panorama-highlight {
  background: #f3f0ff; border: 1.5px solid #ddd6fe; border-radius: 16px;
  padding: 18px 22px; font-size: 15.5px; margin-top: 18px; line-height: 1.6;
}

/* ---------- Story pages ---------- */
.story-page { background: #fffaf3; display: flex; flex-direction: column; }
.story-deco { position: absolute; font-size: 40px; color: var(--accent-soft); opacity: .9; }
.story-deco.tl { top: 10mm; left: -4mm; }
.story-deco.br { bottom: 16mm; right: -4mm; }
.story-head { display: flex; align-items: center; gap: 16px; margin-bottom: 16px; }
.story-badge {
  flex: 0 0 auto; width: 76px; height: 76px; border-radius: 50%;
  background: var(--accent); display: flex; align-items: center; justify-content: center;
  font-size: 38px; box-shadow: 0 5px 0 rgba(0,0,0,.08);
}
.story-kicker {
  display: block; text-transform: uppercase; letter-spacing: 1px; font-size: 11px;
  font-weight: 800; color: var(--accent-text);
}
.story-head-text h2 { font-size: 26px; margin: 3px 0; }
.story-ref { font-size: 12.5px; color: #9ca3af; font-weight: 700; }
.story-body {
  font-size: 15px; color: #374151; background: #fff;
  border-radius: 16px; padding: 20px 22px; border: 1.5px solid #f1ede4;
  margin-bottom: 14px; line-height: 1.6;
}
.story-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 12px; }
.callout {
  border-radius: 14px; padding: 14px 16px; font-size: 13px;
  border: 1.5px solid var(--accent-soft); background: var(--accent-soft);
  line-height: 1.5;
}
.callout-tag {
  display: block; font-weight: 800; font-size: 11.5px; margin-bottom: 5px;
  color: var(--accent-text);
}
.callout p { margin: 0; color: #374151; }
.callout.fact {
  background: #fff8e6; border-color: #fde3a7; margin-bottom: 0;
  font-size: 13px;
}
.callout.fact .callout-tag { color: #b45309; }
.story-stripe {
  margin-top: auto; padding-top: 14px;
  text-align: center; font-size: 24px; letter-spacing: 12px;
  opacity: .16; white-space: nowrap; overflow: hidden;
}
.page-stripe {
  position: absolute; bottom: 26mm; left: 0; right: 0;
  text-align: center; font-size: 30px; letter-spacing: 16px;
  opacity: .14; white-space: nowrap; overflow: hidden;
}

/* ---------- Section dividers ---------- */
.divider-page {
  background: var(--accent);
  color: #fff; display: flex; flex-direction: column;
  align-items: center; justify-content: center; text-align: center;
}
.divider-shape { position: absolute; border-radius: 50%; background: rgba(255,255,255,.14); }
.divider-shape.s1 { width: 220px; height: 220px; top: -60px; right: -60px; }
.divider-shape.s2 { width: 140px; height: 140px; bottom: -40px; left: -40px; }
.divider-shape.s3 { width: 90px; height: 90px; bottom: 100px; right: 40px; }
.divider-emoji { font-size: 60px; margin-bottom: 10px; }
.divider-page h1 { color: #fff; font-size: 40px; }
.divider-page p { max-width: 420px; opacity: .9; font-size: 15px; }

/* ---------- Quiz ---------- */
.quiz-list { list-style: none; padding: 0; margin-top: 16px; }
.quiz-q { margin-bottom: 16px; }
.quiz-q-text { font-weight: 800; color: #134e4a; font-size: 14px; margin-bottom: 6px; }
.quiz-opts { list-style: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 6px; }
.quiz-opts li {
  display: flex; align-items: center; gap: 8px; font-size: 13px;
  background: #fff; border: 1.5px solid #ede9fe; border-radius: 10px; padding: 8px 12px;
}
.opt-letter {
  width: 22px; height: 22px; border-radius: 50%; background: #a78bfa; color: #fff;
  font-size: 11px; font-weight: 800; display: flex; align-items: center; justify-content: center;
  flex: 0 0 auto;
}
.answer-key {
  margin-top: 18px; background: #134e4a; color: #fff; border-radius: 12px;
  padding: 12px 18px; font-size: 12px; font-weight: 700; text-align: center;
  letter-spacing: .4px;
}

/* ---------- Draw page ---------- */
.draw-page { text-align: center; }
.draw-page h1 { font-size: 30px; }
.draw-prompt { max-width: 460px; margin: 0 auto 20px; font-size: 15px; color: #6b7280; }
.draw-frame {
  position: relative; height: 190mm; border: 3px dashed var(--accent);
  border-radius: 20px; background: var(--accent-soft);
}
.draw-frame-corner { position: absolute; font-size: 20px; }
.draw-frame-corner.tl { top: 10px; left: 14px; }
.draw-frame-corner.tr { top: 10px; right: 14px; }
.draw-frame-corner.bl { bottom: 10px; left: 14px; }
.draw-frame-corner.br { bottom: 10px; right: 14px; }
.draw-frame-corner::before { content: '✦'; color: var(--accent); }

/* ---------- Certificate ---------- */
.certificate-page {
  display: flex; align-items: center; justify-content: center;
  background: radial-gradient(circle at top, #fff8e6, #fffaf3 60%);
}
.certificate-border {
  border: 4px double #f5b942; border-radius: 24px;
  padding: 44px 40px; text-align: center; width: 100%;
}
.cert-ic { font-size: 46px; display: block; margin-bottom: 6px; }
.cert-kicker {
  text-transform: uppercase; letter-spacing: 2px; font-size: 12px; font-weight: 800;
  color: #b45309;
}
.certificate-border h1 { font-size: 32px; margin: 10px 0 18px; }
.cert-text { font-size: 15px; color: #374151; }
.cert-line { border-bottom: 2px solid #d6cfc0; width: 70%; margin: 10px auto 20px; height: 30px; }
.cert-line.small { width: 160px; height: 20px; margin: 0 0 6px; }
.cert-footer {
  display: flex; justify-content: space-between; align-items: center;
  margin-top: 36px; font-size: 11px; color: #9ca3af; text-transform: uppercase; letter-spacing: 1px;
}
.cert-seal { font-size: 34px; }

/* ---------- Closing ---------- */
.closing-page {
  background: linear-gradient(160deg, #134e4a 0%, #0d9488 100%);
  color: #fff; display: flex; flex-direction: column; align-items: center;
  justify-content: center; text-align: center;
}
.closing-emoji { font-size: 40px; margin-bottom: 12px; letter-spacing: 10px; }
.closing-page h1 { color: #fff; font-size: 30px; max-width: 480px; }
.closing-page p { max-width: 440px; opacity: .92; }
.closing-copy { margin-top: 26px; font-size: 11px; opacity: .7; }
"""


def build():
    parts = [COVER_PAGE, LETTER_PAGE, HOWTO_PAGE, toc_page(), PANORAMA_PAGE]
    parts.append(divider_page("Antigo Testamento", "Da Criação do mundo até a longa espera pelo Salvador prometido — 12 histórias inesquecíveis.", "🏺", "teal"))
    for i, s in enumerate(OT_STORIES, start=1):
        parts.append(story_page(i, len(OT_STORIES), "Antigo Testamento", s))
    parts.append(divider_page("Novo Testamento", "A vida de Jesus e o início da Igreja — 10 histórias que mudaram o mundo para sempre.", "✝️", "purple"))
    for i, s in enumerate(NT_STORIES, start=1):
        parts.append(story_page(i, len(NT_STORIES), "Novo Testamento", s))
    parts.append(divider_page("Hora de Brincar e Aprender", "Quiz, desenhos e um certificado especial para comemorar tudo o que você aprendeu!", "🎉", "coral"))
    parts.append(quiz_pages())
    for d in DRAW_PROMPTS:
        parts.append(draw_page(d))
    parts.append(certificate_page())
    parts.append(CLOSING_PAGE)

    html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8" />
<title>Mapa Bíblico Kids — E-book</title>
<style>{CSS}</style>
</head>
<body>
{''.join(parts)}
</body>
</html>"""
    return html


if __name__ == "__main__":
    out = build()
    with open("ebook-mapa-biblico-kids.html", "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote", len(out), "bytes")
