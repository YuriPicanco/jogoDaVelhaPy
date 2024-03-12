from verificaJogo import verificaJogo
from tabuleiro import imprimeTabuleiro
from marcaJogo import marcaJogo

def jogoDaVelha():
    jogador1 = True 
    jogo = [
        ['  ', '  ', '  '],
        ['  ', '  ', '  '],
        ['  ', '  ', '  ']
    ]
    
    while (not verificaJogo(jogo)):
        imprimeTabuleiro(jogo)

        if(jogador1):
            print("É a vez do jogador X")
            jogo = marcaJogo(jogo, " X")
        else:
            print("É a vez do jogador O")
            jogo = marcaJogo(jogo, " O")
        jogador1 = not jogador1
