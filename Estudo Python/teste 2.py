
guinchos = ['Guincho 1 (para veículos simples)', 'Guincho 2 (para veículos de porte médio)', 'Guincho 3 (para veículos de 5 a 10 toneladas)', 'Guincho 4 (para veículos de 10 a 20 toneladas)']
solicitacoes = []

def solicitar_guincho():
    print('--- Solicitar Suporte ---')
    print('Preencha os dados abaixo:')
    print('Catálogo de guinchos disponíveis:')
    for i, guincho in enumerate(guinchos):
        print(f'{i+1} - {guincho}')
    
    while True:
        numero = input('Digite o número do guincho desejado: ')

        if numero.isdigit() and int(numero) <= len(guinchos):
            guincho = guinchos[int(numero)-1]
            guinchos.remove(guincho)
            solicitacoes.append(guincho)
            print(f'Solicitação de guincho {guincho} realizada com sucesso!')
            break
        else:
            print('Ops, parece que você digitou um valor errado ou ja soliçitou esse guincho, tente novamente!.')

def verificar_solicitacoes():
    print('--- Verificar Solicitações ---')
    if solicitacoes:
        print('Solicitações de guincho:')
        for i, guincho in enumerate(solicitacoes):
            print(f'{i+1} - {guincho}')
    else:
        print('Não há solicitações de guincho!')

def cancelar_solicitacao():
    print('--- Cancelar Solicitação ---')
    if solicitacoes:
        print('Solicitações de guincho:')
        for i, guincho in enumerate(solicitacoes):
            print(f'{i+1} - {guincho}')

        while True:
            numero = input('Digite o número da solicitação a ser cancelada: ')

            if numero.isdigit() and int(numero) <= len(solicitacoes):
                guincho = solicitacoes[int(numero)-1]
                solicitacoes.remove(guincho)
                guinchos.append(guincho)
                print(f'Solicitação de guincho {guincho} cancelada com sucesso!')
                break
            else:
                print('Número de solicitação inválido! Por favor, digite um número válido.')
    else:
        print('Não há solicitações de guincho!')

def exibir_ultima_solicitacao():
    print('--- Exibir Última Solicitação ---')
    if solicitacoes:
        print('Última solicitação de guincho:')
        print(solicitacoes[-1])
    else:
        print('Não há solicitações de guincho!')

def exibir_quantidade_guinchos_disponiveis():
    print('--- Exibir Quantidade de Guinchos Disponíveis ---')
    if guinchos:
        print('Quantidade de guinchos disponíveis:', len(guinchos))
    else:
        print('Não há guinchos disponíveis!')

while True:
    print('----- Auto Help Porto -----')
    print('1 - Solicitar Suporte')
    print('2 - Verificar Solicitações')
    print('3 - Cancelar Solicitação')
    print('4 - Catálogo de Guinchos')
    print('5 - Exibir Última Solicitação')
    print('6 - Exibir Quantidade de Guinchos Disponíveis')
    print('0 - Encerrar Atendimento')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        solicitar_guincho()

    elif escolha == '2':
        verificar_solicitacoes()

    elif escolha == '3':
        cancelar_solicitacao()

    elif escolha == '4':
        print('--- Catálogo de Guinchos ---')
        for guincho in guinchos:
            print(guincho)

    elif escolha == '5':
        exibir_ultima_solicitacao()

    elif escolha == '6':
        exibir_quantidade_guinchos_disponiveis()

    elif escolha == '0':
        print('Atendimento encerrado!')
        break

    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')




