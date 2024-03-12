def marcaJogo(jogo, marca):
    while (True):
        row = input("Esolha uma linha para jogar")
        column = input("Esolha uma coluna para jogar")

        if(jogo[int(row)-1][int(column)-1] == '  '):
            jogo[int(row)-1][int(column)-1] = marca
            break
        else:
            print("Esse Campo já está ocupado. Jogue de novo")
    return jogo