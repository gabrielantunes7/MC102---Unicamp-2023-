print("Este é um sistema que irá te ajudar a escolher a sua próxima Distribuição Linux. Responda a algumas poucas perguntas para ter uma recomendação.")

caminho = 0
resposta_1 = input("Seu SO anterior era Linux? (0) Não (1) Sim ")

if resposta_1 == '0':
    resposta_2 = input("Seu SO anterior era um MacOS? (0) Não (1) Sim ")

    if resposta_2 == '0':
        caminho = 2
        opcoes = 'Ubuntu Mate, Ubuntu Mint, Kubuntu e Manjaro.'

    else:
        caminho = 2
        opcoes = 'ElementaryOS e ApricityOS.'

else:
    resposta_2 = input(
        "É programador/desenvolvedor ou de áreas semelhantes? (0) Não (1) Sim (2) Sim, realizo testes e invasão de sistemas ")

    if resposta_2 == '0':
        caminho = 3
        opcoes = 'Ubunto Mint e Fedora.'

    elif resposta_2 == '1':
        resposta_3 = input(
            "Gostaria de algo pronto para o uso ao invés de ficar configurando o SO? (0) Não (1) Sim ")

        if resposta_3 == '0':
            resposta_4 = input("Já utilizou Arch Linux? (0) Não (1) Sim ")

            if resposta_4 == '0':
                caminho = 3
                opcoes = 'Antergos e Arch Linux.'

            else:
                caminho = 1
                opcoes = 'Gentoo, CentOS e Slackware.'

        else:
            resposta_4 = input(
                "Já utilizou Debian ou Ubuntu? (0) Não (1) Sim ")

            if resposta_4 == '0':
                caminho = 3
                opcoes = 'OpenSUSE, Ubuntu Mate, Ubuntu Mint e Ubuntu.'

            else:
                caminho = 1
                opcoes = 'Manjaro e ApricityOS.'

    else:
        caminho = 3
        opcoes = 'Kali Linux e Black Arch.'

if caminho == 1:
    print("Suas escolhas te levaram a um caminho repleto de desafios, para você recomendamos as distribuições:", opcoes)

elif caminho == 2:
    print("Você passará pelo caminho daqueles que decidiram abandonar sua zona de conforto, as distribuições recomendadas são:", opcoes)

elif caminho == 3:
    print("Ao trilhar esse caminho, um novo guru do Linux irá surgir, as distribuições que servirão de base para seu aprendizado são:", opcoes)

else:
    print("Opção inválida, recomece o questionário.")