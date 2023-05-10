import requests
import json

while True:
    num_jogadores = input("Quantos jogadores vão jogar? (1-4): ")
    if num_jogadores.isdigit() and 1 <= int(num_jogadores) <= 4:
        num_jogadores = int(num_jogadores)
        break
    else:
        print("Por favor, insira um número entre 1 e 4.")
        
valor = input('Insira o valor da carta: ').upper()


dicionario_naipes = {
    'COPAS': 'HEARTS',
    'PAUS': 'CLUBS',
    'ESPADAS': 'SPADES',
    'OUROS': 'DIAMONDS',
    'HEARTS': 'COPAS',
    'CLUBS': 'PAUS',
    'SPADES': 'ESPADAS',
    'DIAMONDS': 'OUROS'
}

naipe = input('informe o naipe desejado: ').upper()
    
response_baralho = requests.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')

baralho = response_baralho.json()
deck_id = baralho['deck_id']

while True:
    response_carta = requests.get(f'https://deckofcadsapi.com/api/deck/{deck_id}/draw/?count=1')
    carta = response_carta.json()['cards'][0]
    cartas_no_baralho = response_carta.json()['remaining']
    
    if carta['value'] == valor and carta['suit'] == dicionario_naipes[naipe]:
        print('\n\nEncontrei sua carta!')
        
        codigo = carta['code']
        with open('carta.json','w') as arquivo_carta:
            json.dump(carta, arquivo_carta)
            
            break
    else:
        valor_encontrado = carta['value']
        naipe_encontrado = dicionario_naipes[carta['suit']]
        print(f'Carta encontrada: {valor_encontrado} de {naipe_encontrado}')
        print(f'Cartas restantes no baralho: {cartas_no_baralho}\n')
                                                     