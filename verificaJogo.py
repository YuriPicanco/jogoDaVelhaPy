def verificaJogo(jogo):
    for i in range(len(jogo)):
        #Verifica na horizontal
        if(jogo[i][0] != "  " and jogo[i][0] == jogo[i][1] and jogo[i][1] == jogo[i][2]):
            print(f"VITÓRIA DO JOGADOR{jogo[i][0]}")
            return True

        #Verifica na vertical
        if(jogo[0][i] != "  " and jogo[0][i] == jogo[1][i] and jogo[1][i] == jogo[2][i]):
                    print(f"VITÓRIA DO JOGADOR{jogo[0][i]}")
                    
    #Verifica na Diagonal
    if(jogo[0][0] != "  " and jogo[0][0] == jogo[1][1] and jogo[1][1] == jogo[2][2]):
        print(f"VITÓRIA DO JOGADOR{jogo[0][0]}")
        return True

    if(jogo[0][2] != "  " and jogo[0][2] == jogo[1][1] and jogo[1][1] == jogo[2][0]):
        print(f"VITÓRIA DO JOGADOR{jogo[0][0]}")
        return True
        
    return False
    


    