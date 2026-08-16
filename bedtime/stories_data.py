# -*- coding: utf-8 -*-
"""Story content for 'Histórias Para Dormir' — 50 original bedtime stories
(30 Bible retellings + 20 original values fables), each with a clear
beginning/middle/end and a closing moral. All prose is original."""

COLORS = {
    "gold":    {"bg": "#f5b942", "soft": "#fff8e6", "text": "#92400e"},
    "lavender":{"bg": "#a78bfa", "soft": "#f2edfe", "text": "#6d28d9"},
    "rose":    {"bg": "#fb7185", "soft": "#feeef0", "text": "#be123c"},
    "sky":     {"bg": "#7dd3fc", "soft": "#eaf8ff", "text": "#0369a1"},
    "mint":    {"bg": "#86efac", "soft": "#eefdf3", "text": "#15803d"},
}
COLOR_CYCLE = ["gold", "lavender", "rose", "sky", "mint"]

CLOSERS = [
    "E, com o coração tranquilo, todos foram dormir sabendo que Deus cuida de cada um.",
    "E naquela noite, o sono chegou leve e feliz, cheio de paz.",
    "E assim, em paz, todos fecharam os olhinhos e dormiram sorrindo.",
    "E o coração ficou quentinho de alegria até a hora de dormir.",
    "E, sob as estrelas, veio um sono calmo e uma noite tranquila.",
    "E todos dormiram bem, sabendo que o amor de Deus nunca dorme.",
    "E a noite chegou serena, com o coração leve e grato.",
    "E, com um sorriso no rosto, vieram os sonhos bons daquela noite.",
]

# ---------------------------------------------------------------------------
# 30 Bible story retellings — short, gentle, bedtime-appropriate
# ---------------------------------------------------------------------------
BIBLE_STORIES = [
    dict(icon="🌎", title="A Criação do Mundo", ref="baseado em Gênesis 1",
        story="No começo de tudo, só existia Deus. Com carinho, Ele começou a criar: a luz, o "
              "céu, os mares e a terra. Depois vieram o sol para aquecer os dias e a lua para "
              "iluminar as noites. Deus encheu os campos de flores, os mares de peixinhos "
              "coloridos e o céu de pássaros cantores. Por fim, criou o ser humano, para "
              "cuidar de tudo com amor. Ao olhar para o mundo pronto, Deus sorriu: estava tudo "
              "muito bom. E, no sétimo dia, Ele descansou, mostrando que até as noites de sono "
              "fazem parte de um plano cheio de amor.",
        moral="Tudo o que Deus faz, Ele faz com cuidado e amor — inclusive você."),
    dict(icon="🍃", title="Adão e Eva no Jardim", ref="baseado em Gênesis 2 e 3",
        story="Deus preparou um jardim lindo para Adão e Eva, cheio de árvores frutíferas e "
              "rios cristalinos. Eles podiam brincar e comer à vontade, menos de uma árvore "
              "especial que Deus pediu para não tocarem, para protegê-los. Um dia, encantados "
              "por uma conversa enganosa, os dois comeram do fruto proibido e sentiram, pela "
              "primeira vez, um friozinho de vergonha no coração. Mesmo assim, Deus não os "
              "abandonou: cuidou deles com ternura e prometeu que, um dia, tudo seria "
              "consertado com muito amor.",
        moral="Mesmo quando erramos, o amor de Deus por nós nunca diminui."),
    dict(icon="🚢", title="Noé e a Arca", ref="baseado em Gênesis 6 a 9",
        story="Noé era um homem bom que confiava em Deus. Um dia, Deus lhe pediu para "
              "construir um barco enorme, porque uma grande chuva estava chegando. Noé "
              "obedeceu, mesmo sem entender tudo, e reuniu sua família e os animais, dois a "
              "dois, dentro da arca. Choveu por muitos dias, mas todos ficaram seguros e "
              "quentinhos lá dentro. Quando a chuva parou, uma pomba trouxe um ramo verde, "
              "sinal de que a terra estava pronta de novo. No céu, surgiu um lindo arco-íris, "
              "a promessa de Deus de cuidar sempre do seu povo.",
        moral="Confiar em Deus, mesmo sem entender tudo, traz paz para o coração."),
    dict(icon="🏗️", title="A Torre de Babel", ref="baseado em Gênesis 11",
        story="Havia um tempo em que todas as pessoas falavam a mesma língua e viviam juntas "
              "numa cidade. Elas quiseram construir uma torre tão alta que chegasse ao céu, "
              "mais para se mostrar grandes do que para agradecer a Deus. Com carinho, Deus "
              "fez com que todos passassem a falar línguas diferentes, e as famílias se "
              "espalharam pelo mundo, cada uma com seu jeitinho de falar. Foi assim que "
              "surgiram os povos diferentes que existem até hoje, cada um especial à sua "
              "maneira.",
        moral="É bom ter sonhos grandes, mas o mais importante é ter um coração humilde."),
    dict(icon="✨", title="Abraão e as Estrelas", ref="baseado em Gênesis 15 e 22",
        story="Deus chamou Abraão para uma jornada especial e prometeu: “Você terá uma "
              "família tão grande quanto as estrelas do céu.” Certa noite, Deus levou "
              "Abraão para fora da tenda e disse: “Olhe para cima e tente contar as "
              "estrelas.” Abraão olhou maravilhado para tantas luzinhas brilhando e "
              "confiou na promessa, mesmo sem filhos ainda. Com o passar do tempo, nasceu "
              "Isaque, o filho tão esperado, e a promessa de Deus começou a se cumprir, "
              "estrelinha por estrelinha.",
        moral="As promessas de Deus podem demorar, mas elas sempre se cumprem."),
    dict(icon="🪣", title="Isaque e o Poço da Amizade", ref="baseado em Gênesis 26",
        story="Isaque, filho de Abraão, gostava de cavar poços de água para ajudar seu povo e "
              "os animais a matarem a sede. Algumas vezes, outros pastores brigavam por causa "
              "dos poços que ele cavava. Em vez de discutir, Isaque preferia se afastar em paz "
              "e cavar um novo poço em outro lugar. Com paciência e sem brigas, ele encontrou "
              "água em abundância, e no final, até aqueles que antes discutiam com ele vieram "
              "fazer as pazes.",
        moral="A paciência e a paz resolvem mais coisas do que a briga."),
    dict(icon="🪜", title="Jacó e a Escada Até o Céu", ref="baseado em Gênesis 28",
        story="Certa noite, Jacó estava viajando sozinho e usou uma pedra como travesseiro "
              "para dormir ao relento. Enquanto dormia, teve um sonho maravilhoso: uma escada "
              "enorme que ia da terra até o céu, com anjos subindo e descendo por ela. No "
              "topo, Deus prometeu estar sempre com ele, em cada passo de sua jornada. Jacó "
              "acordou maravilhado e entendeu que, mesmo sozinho no meio do caminho, nunca "
              "estivera realmente só.",
        moral="Mesmo quando parecemos sozinhos, Deus está sempre pertinho da gente."),
    dict(icon="🌈", title="José, o Sonhador", ref="baseado em Gênesis 37 a 45",
        story="José tinha sonhos especiais e uma túnica colorida que seu pai lhe deu de "
              "presente. Seus irmãos, com ciúmes, o venderam para longe, e José passou por "
              "muitas dificuldades numa terra estranha. Mesmo assim, ele continuou confiando "
              "em Deus e trabalhando com honestidade, até se tornar um homem importante no "
              "Egito. Anos depois, quando seus irmãos precisaram de ajuda, José os recebeu "
              "com um abraço e disse que os perdoava de coração, porque Deus tinha "
              "transformado tudo em algo bom.",
        moral="Perdoar quem nos machucou é um dos maiores presentes que podemos dar."),
    dict(icon="🌊", title="O Bebê Moisés no Rio", ref="baseado em Êxodo 2",
        story="Para proteger seu bebê, uma mamãe colocou o pequeno Moisés numa cestinha "
              "macia e o deixou flutuando entre os juncos do rio, com sua irmã vigiando de "
              "longe. Uma princesa encontrou o bebê chorando e, encantada, decidiu cuidar "
              "dele como filho. Assim, Moisés cresceu protegido e, mais tarde, tornou-se um "
              "grande líder que ajudou seu povo a ser livre. Tudo começou com o cuidado "
              "amoroso de uma mãe e a proteção de Deus sobre aquela cestinha no rio.",
        moral="Deus cuida dos pequenos detalhes, mesmo quando tudo parece incerto."),
    dict(icon="🔥", title="Moisés e a Sarça que Não se Queimava", ref="baseado em Êxodo 3",
        story="Enquanto cuidava de ovelhas no deserto, Moisés viu algo incrível: um arbusto "
              "pegando fogo, mas que não se queimava. Curioso, ele se aproximou, e ouviu a "
              "voz de Deus chamando seu nome com carinho. Deus pediu que Moisés ajudasse seu "
              "povo a sair da escravidão no Egito. Moisés ficou com medo, achando que não era "
              "capaz, mas Deus prometeu estar sempre ao seu lado. Com essa promessa no "
              "coração, Moisés seguiu em frente, corajoso.",
        moral="Deus não escolhe só os mais fortes, mas dá coragem a quem confia n'Ele."),
    dict(icon="🍞", title="O Maná do Céu", ref="baseado em Êxodo 16",
        story="Depois de deixarem o Egito, o povo caminhava pelo deserto e começou a sentir "
              "fome. Deus, com carinho, fez cair do céu um alimento especial toda manhã, "
              "parecido com pequenos flocos brancos e doces, chamado maná. Bastava colher o "
              "suficiente para aquele dia, porque no dia seguinte viria mais, fresquinho. "
              "Assim, ninguém passou fome na longa viagem, e todos aprenderam a confiar que "
              "Deus cuidaria de cada novo dia.",
        moral="Deus cuida de nós um dia de cada vez, sem precisarmos nos preocupar demais."),
    dict(icon="🌾", title="Rute, a Nora Fiel", ref="baseado em Rute 1 a 4",
        story="Rute amava muito sua sogra Noemi, mesmo depois de tempos difíceis na família. "
              "Quando Noemi decidiu voltar para sua terra natal, sozinha e triste, Rute "
              "disse: “Não vou te deixar, para onde você for, eu vou também.” As duas "
              "viajaram juntas, e Rute trabalhou com humildade recolhendo grãos nos campos "
              "para sustentar as duas. Sua bondade e lealdade tocaram o coração de um homem "
              "bom chamado Boaz, que cuidou delas com carinho, e a família de Rute foi "
              "abençoada para sempre.",
        moral="A lealdade e o amor pela família trazem bênçãos inesperadas."),
    dict(icon="👂", title="Ana e o Menino Samuel", ref="baseado em 1 Samuel 1 a 3",
        story="Ana desejava muito ter um filho e orou com todo o seu coração, prometendo "
              "dedicá-lo a Deus. Quando Samuel nasceu, ela cumpriu sua promessa com alegria, "
              "e o menino cresceu ajudando no templo. Certa noite, Samuel ouviu uma voz "
              "chamando seu nome, mas pensou que fosse o sacerdote Eli. Depois de chamá-lo "
              "três vezes, Eli entendeu: era Deus falando com o menino! Samuel respondeu com "
              "um coração disposto: “Fala, Senhor, que Teu servo está ouvindo.”",
        moral="Deus fala com quem tem um coração disposto a escutar."),
    dict(icon="🐑", title="Davi, o Pastorzinho Corajoso", ref="baseado em 1 Samuel 16 e 17",
        story="Davi era o mais novo entre seus irmãos e cuidava das ovelhas da família nos "
              "campos verdes. Mesmo sendo o mais novo, ele já tinha um coração corajoso: "
              "protegia o rebanho de animais perigosos com destreza e confiava sempre em "
              "Deus. Um dia, ele foi escolhido para uma tarefa muito maior, porque Deus não "
              "olha para o tamanho de alguém, mas para o tamanho do seu coração. Davi seguiu "
              "confiante, sabendo que quem cuida das ovelhinhas com amor também sabe cuidar "
              "de grandes desafios com coragem.",
        moral="Deus não olha o tamanho da pessoa, mas o tamanho da sua fé."),
    dict(icon="👑", title="Salomão e o Pedido Sábio", ref="baseado em 1 Reis 3",
        story="Quando Salomão se tornou rei, Deus apareceu em um sonho e disse: “Peça o "
              "que quiser, e eu te darei.” Ele poderia ter pedido riquezas ou fama, mas "
              "Salomão pediu algo diferente: um coração sábio para cuidar bem do seu povo. "
              "Deus ficou tão contente com esse pedido gentil que lhe deu sabedoria, e também "
              "riquezas e honra por cima. Com o tempo, Salomão se tornou conhecido em muitas "
              "terras por suas decisões justas e bondosas.",
        moral="Pedir sabedoria e um bom coração vale mais do que pedir riquezas."),
    dict(icon="🐦", title="Elias e os Corvos", ref="baseado em 1 Reis 17",
        story="Durante um tempo de seca no reino, Deus disse ao profeta Elias para se "
              "esconder perto de um riacho tranquilo. Ali, todas as manhãs e todas as "
              "tardes, corvos vinham voando e traziam pão e carne para ele comer, como Deus "
              "tinha combinado. Elias bebia da água fresquinha do riacho e descansava em "
              "paz, sabendo que estava sendo cuidado de um jeito muito especial, mesmo em "
              "tempos difíceis. Assim aprendeu que Deus sempre encontra um jeito de cuidar de "
              "quem confia n'Ele.",
        moral="Mesmo nos momentos difíceis, Deus encontra formas surpreendentes de cuidar da gente."),
    dict(icon="🫙", title="O Óleo que Não Acabava", ref="baseado em 2 Reis 4",
        story="Uma viúva estava muito preocupada, pois tinha apenas um potinho de óleo em "
              "casa. O profeta Eliseu pediu que ela juntasse o máximo de potes vazios que "
              "conseguisse com os vizinhos. Com fé, ela começou a despejar seu pouco óleo nos "
              "potes, e, para sua surpresa, o óleo não parava de sair, enchendo pote após "
              "pote! Só parou quando não havia mais nenhum vasilhame vazio para encher. Assim, "
              "ela vendeu o óleo e conseguiu cuidar de sua família com o que sobrou.",
        moral="Quando confiamos em Deus, o pouco que temos pode se tornar o suficiente."),
    dict(icon="👸", title="Ester, a Rainha Corajosa", ref="baseado em Ester 4 e 5",
        story="Ester se tornou rainha num reino distante, mas guardava em segredo que fazia "
              "parte do povo judeu. Quando soube que seu povo corria perigo, seu tio Mordecai "
              "pediu que ela fosse corajosa e pedisse ajuda ao rei. Ester ficou com medo, mas "
              "decidiu confiar em Deus e agir com coragem, mesmo sem saber como o rei "
              "reagiria. Com sabedoria e gentileza, ela falou com o rei no momento certo, e "
              "seu povo foi salvo graças à sua coragem.",
        moral="Às vezes, Deus nos coloca no lugar certo bem na hora certa para fazer o bem."),
    dict(icon="🦁", title="Daniel e os Leões Gentis", ref="baseado em Daniel 6",
        story="Daniel amava muito a Deus e orava todos os dias, mesmo sabendo que algumas "
              "pessoas não gostavam disso. Por causa de uma lei injusta, ele foi colocado numa "
              "cova cheia de leões, mas Daniel não teve medo, porque confiava em Deus com todo "
              "o coração. Durante a noite inteira, um anjo ficou ao lado de Daniel e os leões "
              "permaneceram calmos e gentis, sem machucá-lo. Na manhã seguinte, todos ficaram "
              "maravilhados ao ver Daniel são e salvo.",
        moral="A fé tranquila pode nos dar paz mesmo nos momentos mais assustadores."),
    dict(icon="🐋", title="Jonas e o Peixe Gigante", ref="baseado em Jonas 1 a 3",
        story="Deus pediu que Jonas fosse avisar uma cidade distante para mudar de "
              "comportamento, mas Jonas, com medo, fugiu para o lado contrário num navio. Uma "
              "tempestade forte surgiu, e Jonas acabou caindo no mar, onde um peixe enorme o "
              "engoliu gentilmente e o manteve seguro em sua barriga por três dias. Ali "
              "dentro, Jonas orou e pediu perdão a Deus. O peixe o levou até a praia, e Jonas, "
              "dessa vez, foi fazer o que Deus tinha pedido desde o início.",
        moral="Nunca é tarde para corrigir o caminho e fazer a coisa certa."),
    dict(icon="⭐", title="O Nascimento de Jesus", ref="baseado em Lucas 2",
        story="Numa noite muito especial, em Belém, nasceu um bebê chamado Jesus, num "
              "estábulo simples e aconchegante, cercado pelo cheiro de feno e o calor dos "
              "animais. Uma estrela brilhante apareceu bem no céu, mais brilhante que todas as "
              "outras, guiando quem quisesse encontrar aquele bebê especial. Pastores que "
              "cuidavam de ovelhas durante a noite foram avisados por anjos e correram para "
              "ver a boa notícia. Encontraram Maria, José e o pequeno Jesus dormindo "
              "tranquilamente na manjedoura, envolto em panos macios.",
        moral="As coisas mais preciosas costumam vir de um jeitinho simples e humilde."),
    dict(icon="🐑", title="Os Pastores e a Estrela", ref="baseado em Lucas 2",
        story="Enquanto cuidavam de suas ovelhas durante a noite, alguns pastores viram o céu "
              "se encher de luz e ouviram anjos anunciando: “Não tenham medo! Hoje nasceu "
              "um Salvador cheio de amor para todos.” Maravilhados, os pastores deixaram "
              "suas ovelhas por um momento e correram até Belém para ver aquele milagre com "
              "os próprios olhos. Ao encontrarem o bebê Jesus, ficaram cheios de alegria e "
              "saíram contando para todos a boa notícia que tinham visto naquela noite "
              "estrelada.",
        moral="As boas notícias merecem ser compartilhadas com um coração alegre."),
    dict(icon="🤲", title="Jesus e as Criancinhas", ref="baseado em Marcos 10",
        story="Certo dia, muitas famílias levaram seus filhinhos até Jesus, para que Ele os "
              "abençoasse com carinho. Alguns discípulos acharam que Jesus estava ocupado "
              "demais para as crianças e tentaram afastá-las gentilmente. Mas Jesus disse com "
              "um sorriso: “Deixem as criancinhas virem até mim, pois delas é o Reino dos "
              "Céus.” Ele pegou cada criança no colo, com muito carinho, e as abençoou uma "
              "por uma, mostrando que todas eram muito importantes e amadas por Deus.",
        moral="Cada criança é muito especial e amada aos olhos de Deus."),
    dict(icon="🐑", title="A Ovelhinha Perdida", ref="baseado em Lucas 15",
        story="Um pastor cuidava de cem ovelhinhas, mas percebeu que uma delas tinha se "
              "perdido, longe do rebanho. Mesmo tendo noventa e nove ovelhas seguras, ele não "
              "ficou tranquilo e saiu pelas montanhas, procurando com carinho até encontrar a "
              "pequena ovelha assustada. Quando a encontrou, colocou-a com cuidado em seus "
              "ombros e voltou feliz para casa, chamando os amigos para comemorar. Assim é o "
              "amor de Deus: Ele sempre vai atrás de quem se perde, com muita alegria ao "
              "encontrá-lo de volta.",
        moral="Deus se alegra profundamente cada vez que alguém encontra o caminho de volta."),
    dict(icon="🌱", title="O Grão de Mostarda", ref="baseado em Mateus 13",
        story="Jesus gostava de contar histórias simples para ensinar coisas importantes. "
              "Certa vez, Ele comparou o Reino de Deus a uma pequena sementinha de mostarda, a "
              "menor de todas as sementes do jardim. Quando plantada com cuidado na terra, "
              "essa sementinha crescia e se tornava uma árvore grande, forte o bastante para "
              "os passarinhos fazerem seus ninhos entre os galhos. Assim, Jesus mostrou que "
              "coisas pequenas, cuidadas com fé e paciência, podem crescer e se tornar algo "
              "muito grande e bonito.",
        moral="Pequenos atos de fé podem crescer e se tornar algo maravilhoso."),
    dict(icon="🩹", title="O Bom Samaritano", ref="baseado em Lucas 10",
        story="Um viajante foi ferido no caminho e ficou deitado, precisando de ajuda. Duas "
              "pessoas passaram por ali, mas seguiram em frente, sem parar para socorrê-lo. "
              "Então chegou um samaritano, alguém de um povo diferente, que parou "
              "imediatamente ao ver o homem machucado. Com cuidado, ele limpou os "
              "ferimentos, o levou para um lugar seguro e pagou para que fosse bem cuidado até "
              "se recuperar. Jesus contou essa história para ensinar que ser um bom vizinho é "
              "cuidar de quem precisa, não importa de onde a pessoa venha.",
        moral="Amar o próximo é parar e ajudar quem precisa, sem olhar diferenças."),
    dict(icon="🏠", title="O Filho Que Voltou Para Casa", ref="baseado em Lucas 15",
        story="Um jovem pediu sua parte da herança ao pai e foi viver longe, gastando tudo "
              "sem pensar no amanhã. Quando o dinheiro acabou, ele passou fome e sentiu muita "
              "saudade de casa. Envergonhado, decidiu voltar, mesmo sem saber como seria "
              "recebido. Para sua surpresa, o pai o viu chegando de longe e correu para "
              "abraçá-lo com lágrimas de alegria, sem nenhuma cobrança. Fez uma bela festa "
              "para comemorar, porque o filho que estava perdido, finalmente, tinha voltado "
              "para casa.",
        moral="O amor de um pai — e o amor de Deus — está sempre pronto para nos receber de volta."),
    dict(icon="⛵", title="Jesus Acalma a Tempestade", ref="baseado em Marcos 4",
        story="Depois de um dia cheio de ensinamentos, Jesus e seus amigos entraram num barco "
              "para atravessar o lago. Jesus, cansado, adormeceu tranquilamente na popa do "
              "barco. De repente, uma tempestade forte surgiu, balançando o barco de um lado "
              "para o outro. Assustados, os amigos acordaram Jesus, que se levantou e disse "
              "calmamente ao vento e às ondas: “Fiquem quietos.” Na mesma hora, tudo se "
              "acalmou, e um silêncio de paz tomou conta do lago outra vez.",
        moral="Mesmo nas tempestades da vida, a paz de Deus pode acalmar nosso coração."),
    dict(icon="🍞", title="A Multiplicação dos Pães", ref="baseado em Mateus 14",
        story="Uma multidão seguiu Jesus até um lugar tranquilo para ouvi-lo falar, e quando "
              "a noite se aproximou, todos estavam com fome. Um menino generoso ofereceu os "
              "poucos pães e peixinhos que tinha guardado para si. Jesus pegou aquela "
              "pequena oferta, agradeceu a Deus por ela e começou a distribuir para todos — e, "
              "para a surpresa de todos, a comida nunca acabava! Milhares de pessoas comeram "
              "até ficarem satisfeitas, e ainda sobrou muito mais do que tinham no começo.",
        moral="Quando compartilhamos o pouco que temos com um coração generoso, ele pode se multiplicar."),
    dict(icon="🌳", title="Zaqueu, o Homem Baixinho", ref="baseado em Lucas 19",
        story="Zaqueu era um homem baixinho que queria muito ver Jesus passando pela cidade, "
              "mas a multidão era grande demais. Com criatividade, ele subiu numa árvore para "
              "conseguir enxergar por cima de todos. Jesus, ao passar, olhou para cima, "
              "sorriu e disse: “Zaqueu, desça, hoje vou visitar sua casa!” Zaqueu ficou "
              "tão feliz e transformado por essa atenção carinhosa que decidiu, ali mesmo, "
              "ser uma pessoa mais generosa e gentil com todos ao seu redor.",
        moral="Um pouco de atenção e amor pode transformar completamente um coração."),
]

# ---------------------------------------------------------------------------
# 20 original values fables — fully invented characters and plots
# ---------------------------------------------------------------------------
FABLE_STORIES = [
    dict(icon="⭐", title="A Estrelinha que Queria Brilhar Sozinha",
        story="No alto do céu, havia uma estrelinha pequena chamada Luma, que sonhava em "
              "brilhar mais forte do que todas as outras. Uma noite, ela se afastou das "
              "amigas, achando que sozinha brilharia mais. Mas, longe das outras estrelas, "
              "Luma percebeu que sua luz parecia fraquinha e solitária no meio da escuridão. "
              "Ela voltou correndo para perto das amigas, e juntas, formaram um céu "
              "deslumbrante, cada uma brilhando à sua maneira, mas muito mais lindas em "
              "conjunto do que sozinhas.",
        moral="Somos mais fortes e brilhamos mais quando estamos juntos, ajudando uns aos outros."),
    dict(icon="🐦", title="O Passarinho que Aprendeu a Confiar",
        story="Um passarinho chamado Pipo tinha muito medo de voar longe do ninho, achando "
              "que ia se perder no caminho. Sua mãe explicou, com carinho, que Deus cuidava "
              "de cada passarinho, guiando seu voo mesmo quando o caminho parecia incerto. "
              "Num dia de sol, Pipo criou coragem e abriu suas asinhas, voando mais longe do "
              "que jamais tinha ido. No caminho, encontrou frutinhas deliciosas e um lindo "
              "riacho, e percebeu que, confiando, o mundo se tornava um lugar cheio de coisas "
              "boas para descobrir.",
        moral="Confiar em Deus nos dá coragem para explorar coisas novas sem medo."),
    dict(icon="🐑", title="A Ovelha que Voltou pro Rebanho",
        story="Uma ovelhinha curiosa chamada Nina resolveu explorar sozinha um campo distante, "
              "sem avisar ao pastor. Ao anoitecer, ela percebeu que estava longe demais e não "
              "conseguia encontrar o caminho de volta, e ficou com muito medo da escuridão. "
              "O pastor, preocupado, saiu à sua procura com uma lanterna, chamando seu nome "
              "com carinho pelos campos. Ao ouvir a voz familiar, Nina correu em direção à "
              "luz, e o pastor a levou de volta, aquecida e segura, para junto do rebanho.",
        moral="Seguir perto de quem cuida da gente evita muitos sustos pelo caminho."),
    dict(icon="🍞", title="O Menino que Compartilhou seu Pão",
        story="Tiago tinha o único pedaço de pão da turma na hora do lanche, e viu um "
              "coleguinha novo, sentado sozinho, sem nada para comer. Ele hesitou por um "
              "momento, pensando em guardar tudo só para si, mas seu coração o convenceu a "
              "repartir. Dividiu o pão em duas partes e sentou-se ao lado do menino, "
              "conversando e rindo juntos durante o lanche. No fim do dia, Tiago percebeu que "
              "tinha ganhado não só um amigo novo, mas uma alegria muito maior do que se "
              "tivesse comido o pão sozinho.",
        moral="Compartilhar o pouco que temos multiplica a alegria em nosso coração."),
    dict(icon="🦋", title="A Borboleta e a Oração da Manhã",
        story="Toda manhã, uma borboletinha chamada Flor pousava numa flor diferente do "
              "jardim e agradecia a Deus por mais um dia de sol e cores. As outras "
              "borboletas achavam estranho parar para agradecer, preferindo apenas voar sem "
              "pensar em mais nada. Um dia, uma tempestade repentina assustou todas as "
              "borboletas do jardim, mas Flor, com o coração em paz por sua gratidão diária, "
              "encontrou um abrigo tranquilo debaixo de uma folha grande. Ali, ela esperou "
              "calmamente a chuva passar, sabendo que Deus estava cuidando dela.",
        moral="Começar o dia agradecendo enche o coração de paz para qualquer situação."),
    dict(icon="🐴", title="O Pastorzinho Honesto",
        story="Beto era um pastorzinho que cuidava de um pequeno rebanho na fazenda de seu "
              "avô. Um dia, sem querer, ele deixou o portão aberto e duas ovelhas fugiram "
              "para o campo vizinho. Com medo de ser repreendido, Beto pensou em esconder o "
              "que tinha acontecido, mas decidiu contar a verdade ao avô, mesmo com receio. "
              "Seu avô, ao invés de ficar bravo, agradeceu a honestidade do neto e os dois "
              "foram juntos buscar as ovelhinhas, rindo e conversando pelo caminho.",
        moral="Dizer a verdade, mesmo quando é difícil, fortalece a confiança entre as pessoas."),
    dict(icon="🌻", title="A Sementinha Paciente",
        story="Uma sementinha foi plantada num canto do jardim e ficou ansiosa para crescer "
              "rapidamente e virar uma flor grande. Todos os dias, ela tentava espiar para "
              "fora da terra antes da hora, mas só encontrava escuridão e teve que esperar "
              "mais um pouco. Com paciência, ela recebeu água, sol e cuidado, até que, "
              "finalmente, no tempo certo, brotou como uma linda flor amarela, brilhando ao "
              "sol da manhã. Ela entendeu que cada coisa boa tem seu próprio tempo de "
              "acontecer.",
        moral="As coisas boas da vida acontecem no tempo certo, e vale a pena esperar com paciência."),
    dict(icon="🐞", title="O Anjo da Guarda de Joaninha",
        story="Joaninha, a pequena inseto de bolinhas vermelhas, tinha medo de atravessar "
              "sozinha o jardim grande até a horta do outro lado. Sua avó lhe contou que "
              "Deus colocava um anjinho da guarda para cuidar de cada bichinho em sua "
              "jornada, mesmo quando ela não conseguia vê-lo. Com essa lembrança no coração, "
              "Joaninha criou coragem e voou devagarinho, sentindo-se protegida em cada folha "
              "que pousava. Ao chegar são e salva do outro lado, ela sorriu, sabendo que "
              "nunca estivera realmente sozinha.",
        moral="Mesmo sem ver, podemos sentir que Deus está cuidando de nós em cada passo."),
    dict(icon="🌙", title="A Lua que Emprestou Sua Luz",
        story="Numa noite muito escura, a Lua percebeu que uma coruja pequena estava perdida "
              "na floresta, sem conseguir enxergar o caminho de casa. Mesmo cansada depois de "
              "um longo dia escondida atrás das nuvens, a Lua decidiu brilhar com toda sua "
              "força para iluminar o caminho da corujinha. Aos poucos, a coruja encontrou a "
              "árvore de seu ninho e agradeceu, piscando os olhinhos para o céu. A Lua, "
              "satisfeita por ter ajudado, brilhou ainda mais bonita aquela noite.",
        moral="Ajudar alguém a encontrar o caminho é um dos gestos mais bonitos que existem."),
    dict(icon="🐰", title="O Coelhinho que Perdoou o Amigo",
        story="Marrom, um coelhinho brincalhão, ficou muito triste quando seu amigo esquilo "
              "acidentalmente destruiu seu jardim de cenouras durante uma brincadeira. No "
              "começo, Marrom pensou em nunca mais falar com ele, mas viu como o esquilo "
              "estava arrependido e triste pelo que tinha feito. Com um coração generoso, "
              "Marrom decidiu perdoá-lo, e os dois passaram a tarde plantando novas "
              "sementinhas de cenoura juntos. No final, o jardim ficou ainda mais bonito do "
              "que antes, regado com risadas e amizade renovada.",
        moral="Perdoar um amigo pode deixar a amizade ainda mais forte do que era antes."),
    dict(icon="🐜", title="A Formiguinha Agradecida",
        story="Uma formiguinha chamada Fé trabalhava o dia inteiro carregando alimentos para "
              "o formigueiro, sempre cantarolando baixinho de tão feliz. Suas amigas "
              "perguntaram por que ela estava sempre tão alegre, mesmo com tanto trabalho "
              "pela frente. Fé respondeu que, a cada folhinha que carregava, ela agradecia a "
              "Deus por ter força, amigas e um lar aconchegante para voltar. Contagiadas pela "
              "sua alegria, as outras formiguinhas também começaram a agradecer, e o "
              "formigueiro inteiro ficou mais leve e feliz.",
        moral="A gratidão transforma até as tarefas mais simples em momentos de alegria."),
    dict(icon="🕯️", title="O Menino e a Vela da Esperança",
        story="Durante uma noite de tempestade, faltou luz na casa de Pedro, e o menino "
              "ficou com muito medo do escuro. Sua mãe acendeu uma velinha pequena e disse: "
              "“Mesmo a luz mais fraquinha consegue afastar uma escuridão bem grande.” "
              "Pedro observou a chama tremular, e aos poucos foi se acalmando, imaginando que "
              "a esperança funcionava do mesmo jeito: por menor que fosse, sempre trazia luz "
              "para os momentos difíceis. Naquela noite, ele aprendeu a nunca deixar sua "
              "esperança se apagar.",
        moral="Mesmo uma pequena esperança pode iluminar os momentos mais escuros."),
    dict(icon="🌱", title="As Duas Sementes no Jardim",
        story="No mesmo canteiro, foram plantadas duas sementinhas: uma orgulhosa, que "
              "achava que cresceria mais alta e bonita que todas as outras plantas, e outra "
              "humilde, que só queria crescer com gratidão. A sementinha orgulhosa cresceu "
              "rápido, mas seus galhos ficaram fracos por querer crescer alto demais, muito "
              "rápido. Já a sementinha humilde cresceu devagar, com raízes fortes e "
              "profundas, tornando-se uma planta resistente mesmo nos dias de vento forte. "
              "No final, a humildade se mostrou a base mais firme para crescer bem.",
        moral="Crescer com humildade nos dá raízes mais fortes para enfrentar as dificuldades."),
    dict(icon="🐟", title="O Peixinho Dourado e o Rio da Bondade",
        story="Um peixinho dourado chamado Raio adorava nadar pelo rio, ajudando outros "
              "peixinhos a encontrar caminhos seguros entre as pedras. Um dia, encontrou um "
              "peixinho pequeno e assustado, preso numa poça isolada depois que o rio baixou. "
              "Mesmo sem conhecê-lo, Raio nadou de um lado para o outro até encontrar uma "
              "passagem de água que reconectava a poça ao rio principal. O peixinho pequeno, "
              "livre novamente, agradeceu, e os dois se tornaram grandes amigos, nadando "
              "juntos pelo resto do dia.",
        moral="Um gesto de bondade pode transformar completamente o dia de alguém."),
    dict(icon="🐑", title="A Ovelha Negra que Encontrou seu Lugar",
        story="Preta era uma ovelhinha diferente das demais, com sua lã escura em meio a um "
              "rebanho todo branquinho. No começo, ela se sentia triste, achando que não se "
              "encaixava e ficando sempre um pouco afastada das outras. Mas o pastor sempre a "
              "tratava com o mesmo carinho, e aos poucos, as outras ovelhas perceberam que "
              "Preta era divertida, corajosa e uma ótima amiga. Com o tempo, ela se tornou "
              "querida por todos, entendendo que ser diferente não a fazia menos especial.",
        moral="Cada um é especial do seu próprio jeitinho, e isso deve ser celebrado."),
    dict(icon="🧸", title="O Ursinho que Aprendeu a Orar",
        story="Todas as noites, antes de dormir, o ursinho Mel ficava um pouquinho "
              "preocupado com as coisas do dia seguinte. Sua mamãe ursa lhe ensinou a fazer "
              "uma oraçãozinha simples antes de fechar os olhos, agradecendo pelo dia e "
              "pedindo um sono tranquilo. No começo, Mel achou estranho conversar com Deus "
              "sem vê-lo, mas logo sentiu seu coração ficar mais leve e calmo depois de "
              "orar. Desde então, a oraçãozinha da noite virou sua parte preferida antes de "
              "dormir.",
        moral="Conversar com Deus antes de dormir traz paz e tranquilidade para o coração."),
    dict(icon="🌟", title="A Estrela Guia da Menina Perdida",
        story="Durante um passeio noturno em acampamento, a pequena Alice se distraiu "
              "olhando as flores e acabou se afastando do grupo, ficando sozinha na trilha. "
              "Com o coração acelerado, ela se lembrou do que seu pai tinha ensinado: "
              "procurar a estrela mais brilhante do céu e caminhar em direção à luz das "
              "fogueiras. Respirando fundo, Alice seguiu a estrela e logo avistou o brilho "
              "alaranjado da fogueira do acampamento ao longe. Correu para os braços de seu "
              "pai, aliviada, aprendendo que manter a calma sempre ajuda a encontrar o "
              "caminho.",
        moral="Mesmo perdidos, com calma e um pouco de fé, sempre encontramos o caminho de volta."),
    dict(icon="🌳", title="O Passarinho e a Árvore Generosa",
        story="Uma árvore grande e frondosa oferecia seus galhos para os passarinhos "
              "construírem seus ninhos e suas frutas para eles se alimentarem. Um passarinho "
              "chamado Vento, agradecido, perguntou por que a árvore dava tanto sem pedir "
              "nada em troca. A árvore respondeu, balançando suas folhas: “A alegria de "
              "ver vocês felizes já é a minha recompensa.” Vento entendeu a lição e, "
              "daquele dia em diante, passou a compartilhar suas sementinhas com os outros "
              "passarinhos da floresta, do mesmo jeitinho generoso.",
        moral="Dar sem esperar nada em troca é uma das formas mais bonitas de amar."),
    dict(icon="☁️", title="A Nuvem que Aprendeu a Deixar Chover",
        story="Uma nuvem fofinha chamada Bruma guardava toda sua água com medo de que, se "
              "chovesse, ela desapareceria no céu. Mas ao ver os campos secos e as "
              "florzinhas murchando sem água, seu coração ficou apertado de tristeza. Com "
              "coragem, Bruma decidiu confiar e deixou a chuva cair, mesmo com medo do que "
              "aconteceria depois. Ao invés de desaparecer, ela se sentiu leve e feliz, "
              "vendo o jardim inteiro florescer graças à sua generosidade.",
        moral="Soltar o que guardamos com medo pode trazer bênçãos que nem imaginávamos."),
    dict(icon="🐦", title="O Sonho da Pequena Andorinha",
        story="Uma andorinha bem pequena, chamada Aurora, sonhava em voar até terras muito "
              "distantes, mas suas asinhas ainda pareciam fracas demais para uma viagem tão "
              "longa. Muitos pássaros mais velhos disseram que ela era jovem demais para "
              "tentar, e Aurora quase desistiu do seu sonho. Mas, treinando um pouquinho a "
              "cada dia e confiando na força que Deus tinha colocado nela, suas asinhas foram "
              "ficando cada vez mais fortes. Quando chegou a hora, Aurora alçou voo com toda a "
              "sua turma, realizando o sonho que um dia pareceu impossível.",
        moral="Com fé, coragem e um pouco de treino todo dia, sonhos grandes se tornam possíveis."),
]

ALL_STORIES = BIBLE_STORIES + FABLE_STORIES
assert len(ALL_STORIES) == 50, len(ALL_STORIES)
