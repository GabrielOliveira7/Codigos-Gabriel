guinchos = ['Guincho 1 (para veículos simples)', 'Guincho 2 (para veículos de porte médio)', 'Guincho 3 (para veículos de 5 a 10 toneladas)', 'Guincho 4 (para veículos de 10 a 20 toneladas)']
solicitacoes = []

while True:
    print('----- Auto Help Porto -----')
    print('1 - Solicitar Suporte')
    print('2 - Verificar Solicitações')
    print('3 - Cancelar Solicitação')
    print('4 - Catálogo de Guinchos')
    print('0 - Encerrar Atendimento')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        print('Catálogo de guinchos disponíveis:')
        for i, guincho in enumerate(guinchos):
            print(f'{i+1} - {guincho}')
        
        numero = input('Digite o número do guincho desejado: ')

        if numero.isdigit() and int(numero) <= len(guinchos):
            guincho = guinchos[int(numero)-1]
            guinchos.remove(guincho)
            solicitacoes.append(guincho)
            print(f'Solicitação de guincho {guincho} realizada com sucesso!')
        else:
            print('Número de guincho inválido!')

    elif escolha == '2':
        if solicitacoes:
            print('Solicitações de guincho:')
            for i, guincho in enumerate(solicitacoes):
                print(f'{i+1} - {guincho}')
        else:
            print('Não há solicitações de guincho!')

    elif escolha == '3':
        if solicitacoes:
            print('Solicitações de guincho:')
            for i, guincho in enumerate(solicitacoes):
                print(f'{i+1} - {guincho}')

            numero = input('Digite o número da solicitação a ser cancelada: ')

            if numero.isdigit() and int(numero) <= len(solicitacoes):
                guincho = solicitacoes[int(numero)-1]
                solicitacoes.remove(guincho)
                guinchos.append(guincho)
                print(f'Solicitação de guincho {guincho} cancelada com sucesso!')
            else:
                print('Número de solicitação inválido!')
        else:
            print('Não há solicitações de guincho!')

    elif escolha == '4':
        print('Catálogo de guinchos disponíveis:')
        for guincho in guinchos:
            print(guincho)

    elif escolha == '5':
        if solicitacoes:
            print('Última solicitação de guincho:')
            print(solicitacoes[-1])
        else:
            print('Não há solicitações de guincho!')

    elif escolha == '6':
        if guinchos:
            print('Quantidade de guinchos disponíveis:')
            print(len(guinchos))
        else:
            print('Não há guinchos disponíveis!')

    elif escolha == '0':
        print('Atendimento encerrado!')
        break

    else:
        print('Opção inválida. Tente novamente.')


# ==========================================================================================





