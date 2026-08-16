# -*- coding: utf-8 -*-
"""Content for 'Mapa do Coração' — a parenting guide on common childhood
behavioral challenges, with a Christian framing. All text is original."""

COLORS = {
    "sage":  {"bg": "#5f8d6e", "soft": "#eef5f0", "text": "#3d6249"},
    "clay":  {"bg": "#c76f4c", "soft": "#fbeee7", "text": "#9a4a2c"},
    "gold":  {"bg": "#c99a3e", "soft": "#faf3e2", "text": "#8a6415"},
    "rose":  {"bg": "#c07b8b", "soft": "#fbedf0", "text": "#8f4657"},
    "teal":  {"bg": "#4f8a8b", "soft": "#eaf4f4", "text": "#2f5b5c"},
}
COLOR_CYCLE = ["sage", "clay", "gold", "rose", "teal"]

TOPICS = [
    dict(icon="😤", title="Birras e Explosões de Raiva",
        what="A birra costuma aparecer quando a criança sente uma emoção grande demais para "
             "o tamanho do seu vocabulário e do seu autocontrole ainda em formação. Gritos, "
             "choro no chão, chutes — não é “manha” ou manipulação: é a forma que ela "
             "encontrou de expressar frustração, cansaço ou um “não” que não queria ouvir.",
        why="O cérebro infantil ainda está desenvolvendo a área responsável por regular "
            "emoções fortes. Fome, sono atrasado, mudanças de rotina e a simples "
            "incapacidade de comunicar o que sente costumam ser os gatilhos mais comuns.",
        verse="“Não provoqueis à ira vossos filhos, mas criai-os na disciplina e "
              "admoestação do Senhor.” — baseado em Efésios 6:4",
        reflection="Deus não pede que sejamos pais perfeitos e sempre calmos, mas pede que "
                   "criemos um ambiente onde o filho se sinta seguro para sentir — e aprender "
                   "a lidar com o que sente.",
        tips=[
            "Mantenha a calma antes de tentar acalmar seu filho — sua tranquilidade é contagiante.",
            "Nomeie o sentimento: “Eu vejo que você está muito bravo agora.”",
            "Espere a tempestade passar antes de conversar sobre o que aconteceu.",
            "Combine, num momento calmo, um sinal ou palavra que ajude a criança a pedir uma pausa.",
        ],
        prayer="Senhor, me dá paciência para acolher as emoções grandes do meu filho com "
               "calma, e sabedoria para ensiná-lo, aos poucos, a lidar com elas. Amém."),
    dict(icon="🙅", title="Teimosia e Desobediência",
        what="A criança teimosa não está necessariamente “aprontando” — muitas vezes ela "
             "está testando limites, exercitando sua própria vontade e descobrindo até onde "
             "pode ir. É uma fase importante de afirmação de identidade, mesmo quando cansa "
             "os pais.",
        why="Entre os 2 e os 7 anos, é normal e esperado que a criança comece a testar "
            "regras para entender o mundo ao seu redor. Regras inconsistentes (que valem num "
            "dia e não valem no outro) costumam intensificar a teimosia.",
        verse="“Instrui a criança no caminho em que deve andar, e, ainda quando for velho, "
              "não se desviará dele.” — baseado em Provérbios 22:6",
        reflection="Firmeza e amor não são opostos — são parceiros. Regras claras, ditas com "
                   "carinho e mantidas com consistência, ajudam a criança a se sentir segura, "
                   "não controlada.",
        tips=[
            "Dê poucas regras, mas cumpra todas elas com consistência.",
            "Ofereça escolhas dentro de limites: “Você prefere escovar os dentes antes ou "
            "depois do pijama?”",
            "Evite grandes discussões — explique uma vez, com calma, e sustente a decisão.",
            "Elogie especificamente quando ela obedecer, reforçando o comportamento bom.",
        ],
        prayer="Deus, me ajuda a ser firme com amor, e a lembrar que educar não é vencer uma "
               "queda de braço, mas guiar um coração. Amém."),
    dict(icon="👧👦", title="Ciúmes Entre Irmãos",
        what="A chegada de um irmão, ou simplesmente a divisão da atenção dos pais, pode "
             "despertar ciúmes reais e intensos. A criança pode regredir em comportamentos "
             "(voltar a fazer xixi na cama, pedir mamadeira) ou demonstrar agressividade com "
             "o irmão.",
        why="Para uma criança pequena, amor ainda parece um recurso limitado — ela não "
            "entende, de forma intuitiva, que o amor dos pais não “diminui” quando é "
            "dividido. Isso gera insegurança e competição.",
        verse="“O amor é paciente, o amor é bondoso.” — baseado em 1 Coríntios 13:4",
        reflection="Assim como Deus ama cada um dos Seus filhos de forma completa e "
                   "individual, sem “dividir” o amor entre eles, podemos mostrar aos nossos "
                   "filhos que o amor de um pai por cada filho é inteiro, não fracionado.",
        tips=[
            "Reserve um tempinho individual e exclusivo com cada filho, mesmo que curto.",
            "Evite comparações (“seu irmão já sabe fazer isso”).",
            "Valide o sentimento: “Eu entendo que é difícil dividir a atenção.”",
            "Envolva o mais velho em pequenas tarefas de cuidado, para se sentir parte, não substituído.",
        ],
        prayer="Senhor, ajuda-me a fazer cada um dos meus filhos sentir que é amado de forma "
               "completa e única. Amém."),
    dict(icon="🤥", title="Mentiras e Meias-Verdades",
        what="Por volta dos 3-4 anos, a criança começa a entender que pode dizer algo "
             "diferente da realidade — e isso é, na verdade, um marco do desenvolvimento "
             "cognitivo. Com o tempo, ela aprende quando e por que mentir, geralmente para "
             "evitar problemas ou punições.",
        why="O medo de uma reação exagerada dos pais costuma ser o principal motivo por trás "
            "das mentiras infantis. Quando dizer a verdade parece perigoso demais, a mentira "
            "vira um escudo.",
        verse="“Não mintais uns aos outros.” — baseado em Colossenses 3:9",
        reflection="Criar um ambiente onde a verdade é mais segura do que a mentira — mesmo "
                   "quando a verdade é difícil de ouvir — é um dos maiores presentes que "
                   "podemos dar ao caráter de um filho.",
        tips=[
            "Reaja com calma quando a verdade for revelada, mesmo que seja algo grave.",
            "Elogie a honestidade explicitamente: “Obrigado por me contar a verdade.”",
            "Evite “armadilhas” (perguntar algo que você já sabe a resposta só para testar).",
            "Modele a honestidade você mesmo, inclusive em pequenas coisas do dia a dia.",
        ],
        prayer="Deus, me ajuda a construir uma relação de confiança com meu filho, onde a "
               "verdade sempre encontre um lugar seguro. Amém."),
    dict(icon="😨", title="Medos e Ansiedade Infantil",
        what="Medo do escuro, de monstros, de ficar sozinho, de errar — os medos infantis "
             "mudam com a idade, mas são reais e merecem ser levados a sério, mesmo quando "
             "parecem, para um adulto, pequenos ou irracionais.",
        why="A imaginação infantil é muito ativa, e o cérebro ainda está aprendendo a "
            "distinguir entre perigo real e imaginado. Mudanças na rotina, notícias "
            "assustadoras ou brigas em casa também podem aumentar a ansiedade.",
        verse="“Não tenhas medo, porque eu sou contigo.” — baseado em Isaías 41:10",
        reflection="Podemos ensinar aos filhos que é normal sentir medo, e que Deus está com "
                   "eles em cada situação assustadora — o objetivo não é eliminar todo medo, "
                   "mas ensinar a enfrentá-lo com apoio.",
        tips=[
            "Nunca ridicularize o medo, mesmo que pareça bobo para você.",
            "Crie pequenos rituais de segurança (luz noturna, um ursinho, uma oração antes de dormir).",
            "Ensine a respirar fundo e nomear o medo em voz alta.",
            "Exponha a criança aos poucos e com apoio, nunca de forma forçada ou repentina.",
        ],
        prayer="Senhor, acalma o coração do meu filho nos momentos de medo, e me ajuda a ser "
               "um porto seguro para ele. Amém."),
    dict(icon="📚", title="Dificuldade de Concentração",
        what="Criança que não para quieta, que muda de atividade a todo momento, que parece "
             "não ouvir quando é chamada — em muitos casos, isso é apenas um traço normal da "
             "infância, especialmente em crianças pequenas ou muito estimuladas.",
        why="O tempo de atenção sustentada cresce gradualmente com a idade. Excesso de "
            "estímulos (telas, brinquedos demais, rotina agitada) e falta de sono adequado "
            "também prejudicam bastante a concentração.",
        verse="“Tudo tem o seu tempo determinado.” — baseado em Eclesiastes 3:1",
        reflection="Respeitar o tempo e o ritmo de cada criança, sem comparar com outras, é "
                   "uma forma de honrar como Deus formou cada uma de forma única.",
        tips=[
            "Divida tarefas em passos pequenos e claros, um de cada vez.",
            "Reduza estímulos ao redor na hora de fazer uma atividade (TV desligada, ambiente calmo).",
            "Use temporizadores visuais para tornar o tempo de foco mais concreto.",
            "Garanta uma boa noite de sono — ela impacta diretamente a atenção do dia seguinte.",
        ],
        prayer="Deus, me ajuda a ter paciência com o ritmo do meu filho, e a criar um "
               "ambiente que favoreça sua concentração. Amém."),
    dict(icon="📱", title="Uso Excessivo de Telas",
        what="Tablets, celulares e TV fazem parte do dia a dia de quase toda família hoje. O "
             "desafio não é a tela em si, mas o tempo, o conteúdo e o que deixa de acontecer "
             "(brincar, conversar, ler) quando a tela toma conta do tempo livre da criança.",
        why="Telas oferecem estímulo e recompensa imediatos, o que é naturalmente atraente "
            "para qualquer cérebro, ainda mais um em desenvolvimento. Sem limites claros, "
            "elas tendem a ocupar cada vez mais espaço.",
        verse="“Tudo me é lícito, mas nem tudo convém.” — baseado em 1 Coríntios 6:12",
        reflection="Assim como em muitas áreas da vida, o equilíbrio é o caminho — telas não "
                   "são o inimigo, mas merecem um lugar bem definido na rotina, ao lado de "
                   "outras atividades importantes.",
        tips=[
            "Defina horários claros de tela, e mantenha-os visíveis (num quadro, por exemplo).",
            "Prefira conteúdos educativos e assista/acompanhe junto quando possível.",
            "Crie momentos “sem tela” em família, como as refeições.",
            "Ofereça alternativas atrativas: livros, brincadeiras ao ar livre, jogos em família.",
        ],
        prayer="Senhor, me dá sabedoria para equilibrar a tecnologia na vida do meu filho, "
               "sem que ela ocupe o lugar de coisas mais importantes. Amém."),
    dict(icon="🙈", title="Timidez e Dificuldade Social",
        what="Algumas crianças demoram mais para se soltar em ambientes novos, preferem "
             "observar antes de participar, ou ficam quietas perto de pessoas que não "
             "conhecem bem. Isso não é, por si só, um problema — é um traço de temperamento.",
        why="A timidez tem forte componente de personalidade, mas pode ser intensificada por "
            "excesso de cobrança (“vai lá, cumprimenta”) ou por comparações com crianças mais "
            "extrovertidas.",
        verse="“Cada um tem de Deus o seu próprio dom.” — baseado em 1 Coríntios 7:7",
        reflection="Deus criou personalidades diferentes de propósito — a criança mais "
                   "quieta e observadora tem tanto valor quanto a mais falante, e não precisa "
                   "ser “consertada”.",
        tips=[
            "Evite rótulos (“ele é tímido”) na frente da criança — isso pode reforçar o comportamento.",
            "Prepare-a com antecedência para situações sociais novas, explicando o que vai acontecer.",
            "Permita que observe antes de participar, sem forçar interação.",
            "Elogie pequenos passos de coragem social, sem exagerar ou pressionar por mais.",
        ],
        prayer="Deus, obrigado por criar meu filho do jeito que ele é. Me ajuda a valorizar "
               "seu jeitinho único, sem tentar mudá-lo. Amém."),
    dict(icon="👊", title="Agressividade com Outras Crianças",
        what="Morder, bater, empurrar — comportamentos agressivos são comuns especialmente "
             "em crianças pequenas que ainda não têm palavras suficientes para expressar "
             "frustração, e podem continuar, em menor grau, em crianças maiores sob estresse.",
        why="A agressividade costuma ser a forma mais rápida e imediata que a criança "
            "encontra para resolver um conflito quando ainda não aprendeu (ou não conseguiu "
            "acessar, no calor do momento) formas mais elaboradas de comunicação.",
        verse="“Sede bondosos uns para com os outros, compassivos, perdoando-vos uns aos "
              "outros.” — baseado em Efésios 4:32",
        reflection="Ensinar um filho a lidar com raiva sem agressão é ensinar, na prática, o "
                   "que significa amar o próximo mesmo quando estamos frustrados.",
        tips=[
            "Intervenha imediatamente e com calma, sem gritar ou bater de volta.",
            "Nomeie a emoção e ofereça uma alternativa: “Você está bravo, mas não pode bater. "
            "Pode dizer ‘pare’ bem alto.”",
            "Ensine e pratique, em momentos calmos, formas de pedir algo ou expressar raiva com palavras.",
            "Seja consistente nas consequências, sempre com respeito, nunca com humilhação.",
        ],
        prayer="Senhor, ensina meu filho a expressar sua raiva sem machucar, e me dá "
               "paciência para ensiná-lo com gentileza. Amém."),
    dict(icon="🧸", title="Dificuldade em Compartilhar",
        what="Para uma criança pequena, seus brinquedos são extensões de si mesma — dividir "
             "pode parecer, literalmente, perder uma parte de si. Isso é uma fase normal do "
             "desenvolvimento, não “egoísmo” no sentido adulto da palavra.",
        why="O conceito de posse e a capacidade de considerar o ponto de vista do outro "
            "amadurecem com o tempo. Antes dos 3-4 anos, a maioria das crianças ainda tem "
            "dificuldade real de entender por que deveria dividir algo que é “seu”.",
        verse="“Há mais felicidade em dar do que em receber.” — baseado em Atos 20:35",
        reflection="Ensinar a generosidade é um processo, não um evento único — cada pequena "
                   "prática de dividir vai construindo, aos poucos, um coração generoso.",
        tips=[
            "Não force a divisão imediata de um brinquedo favorito — negocie um tempo de espera.",
            "Elogie especificamente quando a criança compartilhar por conta própria.",
            "Modele a generosidade dividindo suas próprias coisas na frente dela.",
            "Use um temporizador para “revezar” brinquedos disputados de forma justa e previsível.",
        ],
        prayer="Deus, ajuda meu filho a descobrir a alegria de dividir, e me ajuda a ensinar "
               "isso com paciência e exemplo. Amém."),
    dict(icon="🌙", title="Resistência à Hora de Dormir",
        what="Pedidos de “mais uma história”, idas ao banheiro, medo do escuro, ou "
             "simplesmente não querer parar de brincar — a hora de dormir é, para muitas "
             "famílias, um dos momentos mais desafiadores do dia.",
        why="Crianças muitas vezes resistem ao sono porque não querem “perder” o tempo com a "
            "família, ou porque a transição do dia agitado para o silêncio da noite é "
            "difícil sem uma rotina que sinalize esse momento com antecedência.",
        verse="“Em paz também me deitarei e dormirei, porque só tu, Senhor, me fazes habitar "
              "em segurança.” — baseado em Salmos 4:8",
        reflection="Criar uma rotina de boa noite calma e previsível ensina à criança que "
                   "dormir não é um castigo, mas um momento de paz e cuidado.",
        tips=[
            "Mantenha um horário consistente, todos os dias, inclusive nos fins de semana.",
            "Crie uma sequência fixa: banho, pijama, história, oração, luz apagada.",
            "Desligue telas pelo menos uma hora antes de dormir.",
            "Reserve um “tempo de conexão” antes da cama, para que a criança não sinta que "
            "está perdendo tempo com você.",
        ],
        prayer="Senhor, obrigado por cuidar do meu filho enquanto ele dorme. Ajuda-nos a "
               "criar noites tranquilas e cheias de paz. Amém."),
    dict(icon="🥦", title="Seletividade Alimentar",
        what="Recusar legumes, comer sempre a mesma coisa, fazer careta para alimentos "
             "novos — a seletividade alimentar é extremamente comum na infância e, na "
             "maioria das vezes, é uma fase, não um problema permanente.",
        why="É biologicamente normal que crianças pequenas sejam cautelosas com alimentos "
            "novos — é um mecanismo antigo de proteção contra possíveis venenos. Pressão "
            "excessiva na hora da refeição costuma piorar a seletividade, não melhorar.",
        verse="“Quer, pois, comais quer bebais, ou façais outra coisa qualquer, fazei tudo "
              "para glória de Deus.” — baseado em 1 Coríntios 10:31",
        reflection="Refeições em família podem ser momentos de conexão e gratidão, não de "
                   "batalha — o clima ao redor da mesa importa tanto quanto o prato em si.",
        tips=[
            "Ofereça o alimento novo várias vezes, sem forçar, e sem grandes comentários.",
            "Coma junto o que quer que a criança coma — o exemplo pesa mais que a explicação.",
            "Evite recompensas ou castigos ligados à comida (“só sobremesa se comer tudo”).",
            "Mantenha as refeições em horário regular e num ambiente tranquilo, sem pressa.",
        ],
        prayer="Deus, obrigado pelo alimento de cada dia. Ajuda-me a ter paciência com o "
               "tempo do meu filho de experimentar coisas novas. Amém."),
    dict(icon="🧦", title="Falta de Responsabilidade",
        what="Esquecer tarefas, deixar brinquedos espalhados, não cuidar dos próprios "
             "pertences — a responsabilidade é uma habilidade que se constrói aos poucos, "
             "com prática e oportunidade, não algo que a criança já nasce sabendo.",
        why="O cérebro responsável por planejamento e organização é uma das últimas áreas a "
            "amadurecer, continuando seu desenvolvimento até a vida adulta jovem. Esperar "
            "responsabilidade adulta de uma criança pequena gera frustração para os dois lados.",
        verse="“Fiel no pouco, fiel no muito.” — baseado em Lucas 16:10",
        reflection="Dar pequenas responsabilidades, do tamanho da criança, é uma forma "
                   "prática de ensinar o valor bíblico da fidelidade nas pequenas coisas.",
        tips=[
            "Dê tarefas do tamanho certo para a idade, com instruções simples e específicas.",
            "Use listas visuais (com desenhos, para os menores) em vez de só instruções verbais.",
            "Celebre o esforço, não só o resultado perfeito.",
            "Seja consistente: a mesma tarefa, no mesmo momento do dia, cria hábito com o tempo.",
        ],
        prayer="Senhor, ajuda meu filho a crescer em responsabilidade, um pequeno passo de "
               "cada vez, e me dá paciência nesse processo. Amém."),
    dict(icon="🤗", title="Apego Excessivo aos Pais",
        what="Chorar quando os pais saem, recusar ficar com outras pessoas, precisar de "
             "contato físico constante — o apego forte é, na maioria das vezes, sinal de um "
             "vínculo saudável, mesmo quando cansa os pais.",
        why="Até certa idade, a criança ainda não desenvolveu totalmente a noção de "
            "permanência do objeto emocional — ela precisa aprender, com repetição, que os "
            "pais sempre voltam, mesmo quando saem de perto.",
        verse="“Não te deixarei, nem te desampararei.” — baseado em Hebreus 13:5",
        reflection="Assim como Deus promete nunca nos abandonar, podemos ajudar nossos "
                   "filhos a internalizar essa mesma segurança através de despedidas "
                   "previsíveis e retornos confiáveis.",
        tips=[
            "Crie um ritual curto e consistente de despedida — evite despedidas longas e ansiosas.",
            "Nunca saia escondido, mesmo que pareça mais fácil no momento.",
            "Reforce verbalmente: “Eu sempre volto para buscar você.”",
            "Aumente gradualmente o tempo de separação, começando com curtos períodos de confiança.",
        ],
        prayer="Deus, ajuda meu filho a se sentir seguro mesmo quando estamos separados, "
               "sabendo que o amor continua mesmo à distância. Amém."),
    dict(icon="😒", title="Respostas Mal-Educadas",
        what="Respostas atravessadas, tom de voz alterado, “não quero” gritado — esse tipo "
             "de comportamento costuma aparecer quando a criança está testando limites de "
             "comunicação, ou simplesmente imitando o que ouve ao redor.",
        why="Crianças aprendem padrões de comunicação observando os adultos e outras "
            "crianças ao seu redor. Cansaço, frustração acumulada e falta de vocabulário "
            "para se expressar de forma educada também contribuem bastante.",
        verse="“A resposta branda desvia o furor.” — baseado em Provérbios 15:1",
        reflection="Ensinar respeito na fala é, antes de tudo, modelar respeito na fala — "
                   "nossos filhos aprendem o tom que usamos tanto quanto as palavras que "
                   "dizemos.",
        tips=[
            "Não reaja com o mesmo tom — responda com calma, mesmo firme.",
            "Nomeie o comportamento sem atacar o caráter: “Esse tom não é respeitoso” em vez "
            "de “Você é mal-educado”.",
            "Ensine, num momento calmo, uma forma melhor de dizer a mesma coisa.",
            "Elogie quando a criança se corrigir sozinha ou pedir desculpas.",
        ],
        prayer="Senhor, coloca guarda em minha própria boca, para que eu ensine meu filho a "
               "falar com respeito pelo exemplo que dou. Amém."),
]

TOPICS += [
    dict(icon="😢", title="Choro Fácil e Sensibilidade Emocional",
        what="Algumas crianças choram por qualquer contrariedade — um brinquedo que não "
             "funciona, uma palavra mais dura, uma mudança de planos. Isso não significa "
             "fraqueza, mas geralmente um temperamento mais sensível, que sente tudo de "
             "forma mais intensa.",
        why="Crianças sensíveis processam estímulos emocionais com mais intensidade e, "
            "muitas vezes, ainda não têm ferramentas para lidar com essa intensidade. Elas "
            "não estão “exagerando” — para elas, aquilo realmente é grande.",
        verse="“Bem-aventurados os mansos, porque eles herdarão a terra.” — baseado em "
              "Mateus 5:5",
        reflection="A sensibilidade não é um defeito a ser corrigido — pode ser, com o tempo, "
                   "transformada em empatia e profundidade de caráter, se for acolhida com "
                   "paciência.",
        tips=[
            "Evite frases como “não é nada disso” ou “para de chorar por bobagem”.",
            "Valide o sentimento antes de tentar resolver o problema: “Eu vejo que isso te machucou.”",
            "Ensine, aos poucos, palavras para nomear emoções específicas, além de “triste” ou “bravo”.",
            "Celebre a sensibilidade como um dom, mostrando exemplos de empatia que ela já demonstra.",
        ],
        prayer="Senhor, ajuda-me a acolher o coração sensível do meu filho com paciência, "
               "vendo nele um dom e não um problema. Amém."),
    dict(icon="🧦", title="Bagunça e Desorganização do Quarto",
        what="Roupas no chão, brinquedos espalhados, cama nunca feita — a desorganização é "
             "uma das queixas mais comuns dos pais, e também uma das que mais gera atrito no "
             "dia a dia em casa.",
        why="Organização é uma habilidade executiva que se desenvolve com o tempo e a "
            "prática, e não é intuitiva para a maioria das crianças. Sem um sistema simples "
            "e visual, é comum que elas simplesmente não saibam por onde começar.",
        verse="“Mas todas as coisas se façam decentemente e com ordem.” — baseado em "
              "1 Coríntios 14:40",
        reflection="Ensinar ordem não é sobre perfeccionismo, mas sobre ajudar a criança a "
                   "construir hábitos que, no futuro, trarão mais paz e autonomia para a vida "
                   "dela.",
        tips=[
            "Simplifique: menos brinquedos acessíveis por vez facilita a arrumação.",
            "Use caixas ou cestos rotulados com desenhos, para facilitar a organização visual.",
            "Transforme a arrumação num momento leve, com música ou um desafio de tempo.",
            "Arrume junto nas primeiras vezes, ensinando o passo a passo antes de esperar autonomia.",
        ],
        prayer="Deus, me dá criatividade e paciência para ensinar meu filho a cuidar do que "
               "tem, um pequeno hábito de cada vez. Amém."),
    dict(icon="🚫", title="Dificuldade em Aceitar um “Não”",
        what="Chorar, insistir, negociar sem parar depois de ouvir um “não” — para "
             "muitas crianças, aceitar um limite é uma das habilidades mais difíceis de "
             "desenvolver, especialmente quando o desejo é muito forte.",
        why="A capacidade de tolerar frustração amadurece aos poucos, e cada “não” bem "
            "sustentado pelos pais é, na prática, um treino para essa habilidade tão "
            "importante para a vida adulta.",
        verse="“Porque o Senhor corrige a quem ama, assim como o pai corrige o filho a quem "
              "quer bem.” — baseado em Provérbios 3:12",
        reflection="Um “não” consistente, dito com amor, é uma das formas mais claras "
                   "de mostrar à criança que ela pode confiar na palavra dos pais — hoje e no "
                   "futuro.",
        tips=[
            "Diga “não” com poucas palavras, sem longas justificativas ou debates.",
            "Mantenha a decisão mesmo diante do choro — ceder ocasionalmente ensina a insistir mais.",
            "Ofereça uma alternativa dentro do “não”: “Não pode isso agora, mas pode aquilo.”",
            "Reconheça o esforço quando a criança aceitar um limite, mesmo que a contragosto.",
        ],
        prayer="Senhor, me dá firmeza para sustentar os limites necessários, mesmo quando é "
               "difícil ver meu filho frustrado. Amém."),
]

assert len(TOPICS) == 18, len(TOPICS)

FAQ = [
    ("É errado impor limites e regras para meu filho?",
     "Não — limites claros e consistentes são um ato de amor, não de rigidez. Eles dão à "
     "criança um senso de segurança e previsibilidade. O segredo está em como aplicamos "
     "esses limites: com firmeza, mas sempre com respeito e carinho."),
    ("Devo dar bronca na frente de outras pessoas?",
     "Sempre que possível, corrija em particular. Correções públicas costumam gerar mais "
     "vergonha do que aprendizado, e podem prejudicar a autoestima da criança sem "
     "necessariamente melhorar o comportamento."),
    ("Orar com meu filho realmente ajuda no comportamento dele?",
     "A oração em família não é uma “fórmula mágica”, mas cria um ambiente de conexão, "
     "calma e valores compartilhados que, com o tempo, fortalece o vínculo e a "
     "receptividade da criança aos ensinamentos dos pais."),
    ("Com que idade devo começar a dar responsabilidades ao meu filho?",
     "Desde muito cedo! Mesmo crianças de 2 e 3 anos podem guardar brinquedos simples ou "
     "ajudar a colocar a mesa. O importante é ajustar a tarefa à capacidade real da idade."),
    ("É normal meu filho ter fases de comportamento difícil sem motivo aparente?",
     "Sim, muito normal. Crescimento, mudanças na rotina, novas habilidades sendo "
     "desenvolvidas e até fatores como sono e alimentação podem gerar fases mais desafiadoras "
     "sem uma causa única e óbvia."),
    ("Quando devo procurar ajuda profissional?",
     "Se um comportamento for muito intenso, persistente por vários meses, ou atrapalhar "
     "significativamente a vida familiar, escolar ou social da criança, vale a pena buscar "
     "orientação de um pediatra ou psicólogo infantil — pedir ajuda é um ato de cuidado, não "
     "de fracasso."),
]

QUICK_REFERENCE = [(t["icon"], t["title"], t["tips"][0]) for t in TOPICS]
