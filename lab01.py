def interestelar():
    print("Filme a assistir: Interestelar")

def jornada():
    print("Filme a assistir: Jornada nas Estrelas")

def empate():
    print("Empate, jogue de novo")

while(1):
    sheila = input("Digite a jogada de Sheila: ")
    reginaldo = input("Digite a jogada de Reginaldo: ")
    if sheila == 'Tesoura':
        if (reginaldo == 'Papel' or reginaldo == 'Lagarto'):
            interestelar()
            break

        elif (reginaldo == 'Spock' or reginaldo == 'Pedra'):
            jornada()
            break

        elif reginaldo == 'Tesoura':
            empate()
            continue

    elif sheila == 'Papel':
        if (reginaldo == 'Pedra' or reginaldo == 'Spock'):
            interestelar()
            break

        elif (reginaldo == 'Tesoura' or reginaldo == 'Lagarto'):
            jornada()
            break

        elif reginaldo == 'Papel':
            empate()
            continue

    elif sheila == 'Pedra':
        if (reginaldo == 'Lagarto' or reginaldo == 'Tesoura'):
            interestelar()
            break

        elif (reginaldo == 'Papel' or reginaldo == 'Spock'):
            jornada()
            break

        elif reginaldo == 'Pedra':
            empate()
            continue

    elif sheila == 'Lagarto':
        if (reginaldo == 'Spock' or reginaldo == 'Papel'):
            interestelar()
            break

        elif (reginaldo == 'Pedra' or reginaldo == 'Tesoura'):
            jornada()
            break

        elif reginaldo == 'Lagarto':
            empate()
            continue

    elif sheila == 'Spock':
        if (reginaldo == 'Tesoura' or reginaldo == 'Pedra'):
            interestelar()
            break

        elif (reginaldo == 'Lagarto' or reginaldo == 'Papel'):
            jornada()
            break

        elif reginaldo == 'Spock':
            empate()
            continue