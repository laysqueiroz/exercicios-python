opcao = (int(input('Inserir dados? 0 - Não     1 - Sim ')))

while opcao == 1:
    nome = (str(input('Nome do aluno(a): ')))
    nota = (float(input('Nota final: ')))

    if 0 <= nota < 3:
        conceito = 'E'
    elif 3 <= nota < 5:
        conceito = 'D'
    elif 5 <= nota < 7:
        conceito = 'C'
    elif 7 <= nota < 9:
        conceito = 'B'
    elif 9 <= nota <= 10:
        conceito = 'A'
    else:
        print('Nota inválida.')
        exit()

    print('O aluno(a) {} tirou a nota {} e se enquadra no conceito {}.'.format(nome, nota, conceito))
    opcao = (int(input('Inserir dados? 0 - Não     1 - Sim ')))