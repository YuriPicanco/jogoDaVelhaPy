def imprimeTabuleiro(jogo):
    for column, row in enumerate(jogo):
        print('|'.join(row))
        if(column<len(row)-1):
            print('- '*5)