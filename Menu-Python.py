#--------------COMEÇO DA FUNÇÃO VOLUMEFEIJOADA----------#
def volumeFeijoada():
    while True:
        try:
            print('Menu Volume Feijoada')
            volumeF = int(input('Entre com a quantidade que deseja(ml):\n'
                                '>>'))
            if 300 <= volumeF <= 5000:
                return volumeF * 0.08
            else:
                print('Não aceitamos porções menores que 300ml ou maiores que 5l. Tente novamente!')
        except ValueError:
            print('Foi inserido um valor não númerico')
            continue

#-------------------FIMDAFUNÇÃOVOLUMEFEIJOADA----------#
#--------------COMEÇO DA FUNÇÃO OPÇÃOFEIJOADA----------#
def opcaoFeijoada():
    while True:
        print('Menu Volume Feijoada')
        opcaoF=input('Entre com a opção de Feijoada:\n'
                    'b- Básica (Feijão + paiol + costelinha)\n'
                    'p- Premium (Feijão + paiol + costelinha + partes de porco)\n'
                    's- Suprema (Feijão + paiol + costelinha + partes de porco + charque + calabresa + bacon)\n'
                    '>>')
        if opcaoF == 'b':
            return 1.0
        elif opcaoF == 'p':
            return 1.25
        elif opcaoF == 's':
            return 1.50
        else:
            print('Você não digitou uma opção válida')
            continue
#-------------------FIMDAFUNÇÃO OPÇÃOFEIJOADA----------#
#--------------COMEÇO DA FUNÇÃO ACOMPANHAMENTO FEIJOADA----------#
def acompanhamentoFeijoada():

    subtotal = 0
    while True:
        acompanhamentoF=int(input('Deseja mais algum acompanhamento:\n'
                              '0- não desejo mais acompahamentos (encerrar pedido)\n'
                              '1- 200g de arroz\n'
                              '2- 150g de farofa especial\n'
                              '3- 100g de couve cozida\n'
                              '4- 1 laranja descascada\n'
                              '>>'))
        if acompanhamentoF == 0:
            return subtotal
        elif acompanhamentoF == 1:
            subtotal = subtotal + 5
            continue
        elif acompanhamentoF == 2:
            subtotal = subtotal + 6
            continue
        elif acompanhamentoF == 3:
            subtotal = subtotal + 7
            continue
        elif acompanhamentoF == 4:
            subtotal = subtotal + 3
            continue
        else:
            print('Opção Inválida')
            continue
        return subtotal



#-------------------FIMDAFUNÇÃOACOMPANHAMENTO FEIJOADA----------#
#------------------COMEÇO DA MAIN-------------------------
print('Bem-vindo ao Programa de Feijoada do Ricardo Douglas da Silva Mariz')
volume = volumeFeijoada()
opcao = opcaoFeijoada()
acompanhamento = acompanhamentoFeijoada()
total = (volume * opcao) + acompanhamento
print('O valor a ser pago é (R$): {} (volume = {} * opção = {} + acompanhamento = {})'.format(total,volume,opcao,acompanhamento))

#------------------FIM DA MAIN-----------------------