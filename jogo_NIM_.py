
def partida():

    n = int(input("Quantas peças? \n"))
    m = int(input("Limite de peças por jogada? \n"))
    vezDoPc = False

    if n % (m+1) == 0:
       print("Voçê começa! \n")
    else:
        print("Computador começa! \n")
        vezDoPc = True

    while n > 0:
        if vezDoPc:
            computadorRemove = computador_escolhe_jogada(n, m)
            n = n - computadorRemove
            if computadorRemove == 1:
                print("O computador tirou uma peça \n")
            else:
                print("O computador tirou", computadorRemove, " peças \n")
            
            vezDoPc = False
        else:
            jogadorRemove = usuario_escolhe_jogada(n, m)
            n = n - jogadorRemove
            if jogadorRemove == 1:
                print("Voçê tirou uma peça \n")
            else:
                print("Voçê tirou", jogadorRemove," peças \n")
            vezDoPc = True
        if n == 1:
            print("Agora resta um peça no tabuleiro. \n")
        else:
            if n != 0:
                print("Agora restam", n, "peças no tabuleiro. \n")
    print("Fim do jogo! O computador ganhou!")
        
def usuario_escolhe_jogada(n, m):

    jogadaValida = False

    while not jogadaValida == 0:
        jogadorRemove = int(input("Quantas peças irá tirar? "))

        if jogadorRemove > m or jogadorRemove < 1:
            print("Oops! Jogada inválida! \n")
        else:
            jogadaValida = True

    return jogadorRemove

def computador_escolhe_jogada(n, m):
    computadorRemove = 1

    while computadorRemove != m:
        if (n - computadorRemove) % (m+1) == 0:
            return computadorRemove
        
        else:
            computadorRemove += 1
    
    return computadorRemove

def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print("**** Rodada", numeroRodada," ****\n")
        partida()
        numeroRodada += 1
    print("Placar: Voçê 0 x 3 Computador \n")





print("Bem-vindo ao jogo do NIM! Escolha: \n")
print("1 - para jogar uma partida isolada")
tipoDePartida = int(input("2 - para jogar um campeonato \n"))
if tipoDePartida == 2:
    print("Voçê escolheu um campeonato! \n")
    campeonato()
else:
    if tipoDePartida == 1:
        partida()

