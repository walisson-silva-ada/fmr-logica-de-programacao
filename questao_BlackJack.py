from random import randint

#Função principal
def jogo_blackjack():
    numero_participantes = int(input('Quantos participantes? '))
    jogadores = {}
    for i in range(numero_participantes):
        nome = input(f'Digite o nome do {i+1}º participante: ')
        jogadores[nome] = {'pontos': 0, 'ativo': True}

    #loop do jogo
    for jogador in jogadores.keys():
        baralho = criar_baralho() #baralho completo para cada jogador
        jogada(jogador, jogadores, baralho)
    
    print(jogadores)
    lista_vencedores = verifica_vencedor(jogadores)
    print(f'O(s) vencedor(es): {lista_vencedores}')

#Função para criar baralho
def criar_baralho():
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q','K']
    naipes = ['copas', 'espadas', 'ouros', 'paus']
    baralho = []
    for naipe in naipes:
        for valor in valores:
            baralho.append(valor + ' de ' + naipe)
    return baralho

#Função para a jogada
def jogada(nome_jogador, dict_jogadores, baralho):
    jogador_atual = dict_jogadores[nome_jogador]
    while jogador_atual['ativo']:
        if jogador_atual['pontos'] < 21:
            continuar = input(f'{nome_jogador}, Quer comprar uma carta? [S/N] ').upper().strip()
            if continuar == 'S':
                jogador_atual['pontos'] += sorteio(baralho)
                print('{} tem {} pontos'.format(nome_jogador,jogador_atual['pontos']))
            else:
                jogador_atual['ativo'] = False
                print('{}, você encerrou sua jogada com {} pontos'.format(nome_jogador,jogador_atual['pontos']))
        else:
            jogador_atual['ativo'] = False

#Função o sorteio
def sorteio(baralho):
    carta = baralho[randint(0, len(baralho) - 1)] #sorteia uma carta
    print(carta)
    baralho.remove(carta)
    if carta[:1] == 'A': #compara apenas a posicao 0 (valor)
        return int(1)
    elif carta[:1] in ('J', 'Q','K'):
        return int(10)
    else:
        return int(carta[:1])

#Função verificação
def verifica_vencedor(dict_jogadores):
    cont = 0
    maior = 0
    vencedor = []
    for nome_jogador in dict_jogadores:
        jogador = dict_jogadores[nome_jogador]
        if jogador['pontos'] <= 21:
            if cont == 0:
                maior = jogador['pontos']
                vencedor = nome_jogador
            else:
                if jogador['pontos'] > maior:
                    maior = jogador['pontos']
                    vencedor = nome_jogador
                elif  jogador['pontos'] == maior:
                    vencedor.append(nome_jogador)
            cont += 1
    return vencedor        

jogo_blackjack()
