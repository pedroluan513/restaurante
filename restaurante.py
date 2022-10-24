regiao = ''
refeicao = ''
CafeDaManha = ''
almoco = ''
janta = ''
CafeDaTarde = ''
sobremesa = ''
while regiao != '1' and regiao != 'NORDESTE' and regiao != '2' and regiao != 'SULDESTE' and regiao != '3' and regiao != 'SUL' and regiao != '4' and regiao != 'NORTE' and regiao != '5' and regiao != 'CENTRO-OESTE':
    regiao = str(input('''Escolha uma região do Brasil (Digite o número ou o nome da região)
[1]Nordeste
[2]Suldeste
[3]Sul
[4]Norte
[5]Centro-Oeste
Resposta: ''')).upper().strip()
##REGIÃO NORDESTE


    if (regiao == '1' or regiao == 'NORDESTE'):
        while refeicao != '1' and refeicao != 'CAFÉ DA MANHÃ' and refeicao != '2' and refeicao != 'ALMOÇO' and refeicao != '3' and refeicao != 'CAFÉ DA TARDE' and refeicao != '4' and refeicao != 'JANTA' and refeicao != '5' and refeicao != 'SOBREMESA':
            refeicao = str(input('''Escolha o tipo da refeição do Nordeste
[1]Café da manhã
[2]Almoço
[3]Café da tarde
[4]Janta
[5]Sobremesa
Resposta: ''')).upper().strip()
            if (refeicao == '1' or refeicao == 'CAFÉ DA MANHÃ'):
                while CafeDaManha != '1' and CafeDaManha != 'CUZCUZ' and CafeDaManha != '2' and CafeDaManha != 'TAPIOCA' and CafeDaManha != '3' and CafeDaManha != 'BANANA COZIDA' and CafeDaManha != '4' and CafeDaManha != 'MANDIOCA' and CafeDaManha != '5' and CafeDaManha != 'CURAU':
                    CafeDaManha = str(input('''Agora escolha um café da manhã típico do Nordeste
[1]CuzCuz
[2]Tapioca
[3]Banana cozida
[4]Mandioca
[5]Curau
Resposta: ''')).upper().strip()
                    if (CafeDaManha == '1' or CafeDaManha == 'CUZCUZ'):
                        print('Aqui está seu CuzCuz, bom apetite!')
                    elif (CafeDaManha == '2' or CafeDaManha == 'TAPIOCA'):
                        print('Aqui está sua Tapioca, bom apetite!')
                    elif (CafeDaManha == '3' or CafeDaManha == 'BANANA COZIDA'):
                        print('Aqui está sua Banana cozida, bom apetite!')
                    elif (CafeDaManha == '4' or CafeDaManha == 'MANDIOCA'):
                        print('Aqui está sua Mandioca, bom apetite!')
                    elif (CafeDaManha == '5' or CafeDaManha == 'CURAU'):
                        print('Aqui está seu Curau, bom apetite!')
                    else:
                        print('Não temos esse café da manhã :(, tente novamente.')
            elif (refeicao == '2' or refeicao == 'ALMOÇO'):
                while almoco != '1' and almoco != 'BAIÃO DE DOIS' and almoco != '2' and almoco != 'ACARAJÉ BAIANO' and almoco != '3' and almoco != 'CUZCUZ RECHEADO' and almoco != '4' and almoco != 'FEIJOADA' and almoco != '5' and almoco != 'CANJICA COM CARNE':
                    almoco = str(input('''Agora escolha um Almoço típico do Nordeste
[1]Baião de dois
[2]Acarajé baiano
[3]CuzCuz recheado
[4]Feijoada
[5]Canjica com carne
Resposta: ''')).upper().strip()
                    if (almoco == '1' or almoco == 'BAIÃO DE DOIS'):
                        print('Aqui está seu Baião, bom apetite!')
                    elif (almoco == '2' or almoco == 'ACARAJÉ BAIANO'):
                        print('Aqui está seu Acarajé, bom apetite!')
                    elif (almoco == '3' or almoco == 'CUZCUZ RECHEADO'):
                        print('Aqui está seu CuzCuz recheado, bom apetite!')
                    elif (almoco == '4' or almoco == 'FEIJOADA'):
                        print('Aqui está sua Feijoada, bom apetite!')
                    elif (almoco == '5' or almoco == 'CANJICA COM CARNE'):
                        print('Aqui está sua Canjica com carne, bom apetite!')
                    else:
                        print('Não temos esse Almoço :(, tente novamente.')
            elif (refeicao == '3' or refeicao == 'CAFÉ DA TARDE'):
                while CafeDaTarde != '1' and CafeDaTarde != 'TAPIOCA' and CafeDaTarde != '2' and CafeDaTarde != 'ARROZ DE CUJÁ' and CafeDaTarde != '3' and CafeDaTarde != 'MOQUECA' and CafeDaTarde != '4' and CafeDaTarde != 'BUXADA' and CafeDaTarde != '5' and CafeDaTarde != 'CARANGUEJADA':
                    CafeDaTarde = str(input('''Agora escolha um Almoço típico do Nordeste
[1]Tapioca
[2]Arroz de Cujá
[3]Moqueca
[4]Buxada
[5]Caranguejada
Resposta: ''')).upper().strip()
                    if (CafeDaTarde == '1' or CafeDaTarde == 'TAPIOCA'):
                        print('Aqui está sua Tapioca, bom apetite!')
                    elif (CafeDaTarde == '2' or CafeDaTarde == 'ARROZ DE CUJÁ'):
                        print('Aqui está seu Arroz de cujá, bom apetite!')
                    elif (CafeDaTarde == '3' or CafeDaTarde == 'MOQUECA'):
                        print('Aqui está sua Moqueca, bom apetite!')
                    elif (CafeDaTarde == '4' or CafeDaTarde == 'BUXADA'):
                        print('Aqui está sua Buxada, bom apetite!')
                    elif (CafeDaTarde == '5' or CafeDaTarde == 'CARANGUEJADA'):
                        print('Aqui está sua Caranguejada, bom apetite!')
                    else:
                        print('Não temos esse Café da tarde aqui :(, tente novamente.')
            elif (refeicao == '4' or refeicao == 'JANTA'):
                while janta != '1' and janta != 'VATAPÁ' and janta != '2' and janta != 'CARURU' and janta != '3' and janta != 'CARANGUEIJO' and janta != '4' and janta != 'CARNE DE SOL' and janta != '5' and janta != 'PANELADA':
                    janta = str(input('''Agora escolha uma Janta típica do Nordeste
[1]Vatapá
[2]Caruru
[3]Caranguejo
[4]Carne de sol
[5]Panelada
Resposta: ''')).upper().strip()
                    if (janta == '1' or janta == 'VATAPÁ'):
                        print('Aqui está seu Vatapá, bom apetite!')
                    elif (janta == '2' or janta == 'CARURU'):
                        print('Aqui está seu Caruru, bom apetite!')
                    elif (janta == '3' or janta == 'CARANGUEIJO'):
                        print('Aqui está seu Carangueijo, bom apetite!')
                    elif (janta == '4' or janta == 'CARNE DE SOL'):
                        print('Aqui está sua Carne de sol, bom apetite!')
                    elif (janta == '5' or janta == 'PANELADA'):
                        print('Aqui está sua Panelada, bom apetite!')
                    else:
                        print('Não temos essa Janta aqui :(, tente novamente.')
            elif (refeicao == '5' or refeicao == 'SOBREMESA'):
                while sobremesa != '1' and sobremesa != 'COCADA' and sobremesa != '2' and sobremesa != 'BOLO DE ROLO' and sobremesa != '3' and sobremesa != 'PAMONHA DOCE' and sobremesa != '4' and sobremesa != 'MUGUNZÁ' and sobremesa != '5' and sobremesa != 'RAPADURA':
                    sobremesa = str(input('''Agora escolha um Almoço típico do Nordeste
[1]Cocada
[2]Bolo de rolo
[3]Pamonha doce
[4]Mugunzá
[5]Rapadura
Resposta: ''')).upper().strip()
                    if (sobremesa == '1' or sobremesa == 'COCADA'):
                        print('Aqui está sua Cocada, bom apetite!')
                    elif (sobremesa == '2' or sobremesa == 'BOLO DE ROLO'):
                        print('Aqui está seu Acarajé, bom apetite!')
                    elif (sobremesa == '3' or sobremesa == 'PAMONHA DOCE'):
                        print('Aqui está sua Pamonha doce, bom apetite!')
                    elif (sobremesa == '4' or sobremesa == 'MUGUNZÁ'):
                        print('Aqui está sua Mugunzá, bom apetite!')
                    elif (sobremesa == '5' or sobremesa == 'RAPADURA'):
                        print('Aqui está sua Rapadura, bom apetite!')
                    else:
                        print('Não temos essA Sobremesa aqui :(, tente novamente.')
##REGIÃO SULDESTE


    elif (regiao == '2' or regiao == 'SULDESTE'):
        while refeicao != '1' and refeicao != 'CAFÉ DA MANHÃ' and refeicao != '2' and refeicao != 'ALMOÇO' and refeicao != '3' and refeicao != 'CAFÉ DA TARDE' and refeicao != '4' and refeicao != 'JANTA' and refeicao != '5' and refeicao != 'SOBREMESA':
            refeicao = str(input('''Escolha o tipo da refeição do Suldeste
[1]Café da manhã
[2]Almoço
[3]Café da tarde
[4]Janta
[5]Sobremesa
Resposta: ''')).upper().strip()
            if (refeicao == '1' or refeicao == 'CAFÉ DA MANHÃ'):
                print('Agora escolha os cafés da manhã típicos do Suldeste')
            elif (refeicao == '2' or refeicao == 'ALMOÇO'):
                print('Agora escolha os almoços típicos do Suldeste')
            elif (refeicao == '3' or refeicao == 'CAFÉ DA TARDE'):
                print('Agora escolha os cafés da tarde típicos do Suldeste')
            elif (refeicao == '4' or refeicao == 'JANTA'):
                print('Agora escolha as jantas típicas do Suldeste')
            elif (refeicao == '5' or refeicao == 'SOBREMESA'):
                print('Agora escolha as sobremesas típicas do Suldeste')
            else:
                print('Você escreveu algo errado, tente novamente.')
##REGIÃO SUL


    elif (regiao == '3' or regiao == 'SUL'):
        while refeicao != '1' and refeicao != 'CAFÉ DA MANHÃ' and refeicao != '2' and refeicao != 'ALMOÇO' and refeicao != '3' and refeicao != 'CAFÉ DA TARDE' and refeicao != '4' and refeicao != 'JANTA' and refeicao != '5' and refeicao != 'SOBREMESA':
            refeicao = str(input('''Escolha o tipo da refeição do Sul
[1]Café da manhã
[2]Almoço
[3]Café da tarde
[4]Janta
[5]Sobremesa
Resposta: ''')).upper().strip()
            if (refeicao == '1' or refeicao == 'CAFÉ DA MANHÃ'):
                print('Agora escolha os cafés da manhã típicos do Sul')
            elif (refeicao == '2' or refeicao == 'ALMOÇO'):
                print('Agora escolha os almoços típicos do Sul')
            elif (refeicao == '3' or refeicao == 'CAFÉ DA TARDE'):
                print('Agora escolha os cafés da tarde típicos do Sul')
            elif (refeicao == '4' or refeicao == 'JANTA'):
                print('Agora escolha as jantas típicas do Sul')
            elif (refeicao == '5' or refeicao == 'SOBREMESA'):
                print('Agora escolha as sobremesas típicas do Sul')
            else:
                print('Você escreveu algo errado, tente novamente.')
##REGIÃO NORTE


    elif (regiao == '4' or regiao == 'NORTE'):
        while refeicao != '1' and refeicao != 'CAFÉ DA MANHÃ' and refeicao != '2' and refeicao != 'ALMOÇO' and refeicao != '3' and refeicao != 'CAFÉ DA TARDE' and refeicao != '4' and refeicao != 'JANTA' and refeicao != '5' and refeicao != 'SOBREMESA':
            refeicao = str(input('''Escolha o tipo da refeição do Norte
[1]Café da manhã
[2]Almoço
[3]Café da tarde
[4]Janta
[5]Sobremesa
Resposta: ''')).upper().strip()
            if (refeicao == '1' or refeicao == 'CAFÉ DA MANHÃ'):
                print('Agora escolha os cafés da manhã típicos do Norte')
            elif (refeicao == '2' or refeicao == 'ALMOÇO'):
                print('Agora escolha os almoços típicos do Norte')
            elif (refeicao == '3' or refeicao == 'CAFÉ DA TARDE'):
                print('Agora escolha os cafés da tarde típicos do Norte')
            elif (refeicao == '4' or refeicao == 'JANTA'):
                print('Agora escolha as jantas típicas do Norte')
            elif (refeicao == '5' or refeicao == 'SOBREMESA'):
                print('Agora escolha as sobremesas típicas do Norte')
            else:
                print('Você escreveu algo errado, tente novamente.')
##REGIÃO CENTRO-OESTE


    elif (regiao == '5' or regiao == 'CENTRO-OESTE'):
        while refeicao != '1' and refeicao != 'CAFÉ DA MANHÃ' and refeicao != '2' and refeicao != 'ALMOÇO' and refeicao != '3' and refeicao != 'CAFÉ DA TARDE' and refeicao != '4' and refeicao != 'JANTA' and refeicao != '5' and refeicao != 'SOBREMESA':
            refeicao = str(input('''Escolha o tipo da refeição do Centro-Oeste
[1]Café da manhã
[2]Almoço
[3]Café da tarde
[4]Janta
[5]Sobremesa
Resposta: ''')).upper().strip()
            if (refeicao == '1' or refeicao == 'CAFÉ DA MANHÃ'):
                print('Agora escolha os cafés da manhã típicos do Centro-Oeste')
            elif (refeicao == '2' or refeicao == 'ALMOÇO'):
                print('Agora escolha os almoços típicos do Centro-Oeste')
            elif (refeicao == '3' or refeicao == 'CAFÉ DA TARDE'):
                print('Agora escolha os cafés da tarde típicos do Centro-Oeste')
            elif (refeicao == '4' or refeicao == 'JANTA'):
                print('Agora escolha as jantas típicas do Centro-Oeste')
            elif (refeicao == '5' or refeicao == 'SOBREMESA'):
                print('Agora escolha as sobremesas típicas do Centro-Oeste')
            else:
                print('Você escreveu algo errado, tente novamente.')