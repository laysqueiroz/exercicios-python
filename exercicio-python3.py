import random
doadores = []

def cadastro_doador(nome, doacao):
    doadores.extend(((nome + ' ') * int(doacao // 10)).split())
    return

def sorteio_ganhador():
    random.shuffle(doadores)
    print(f'Lista embaralhada de doadores: {doadores} ')
    return random.choice(doadores)

opcao = int(input('Deseja cadastrar doador(a)? 0 - Não     1 - Sim '))

while opcao == 1:
    doador = input('Nome do doador(a): ')
    valor = float(input('Valor de doação: '))

    while len(doador) == 0 or valor < 10:
        print('O nome é obrigatório e o valor mínimo para doação é de R$ 10,00.')
        doador = input('Nome do doador(a): ')
        valor = float(input('Valor de doação: '))

    cadastro_doador(doador, valor)

    opcao = int(input('Deseja cadastrar doador(a)? 0 - Não     1 - Sim '))

if len(doadores) > 0:
    print(f'Lista de doadores para sorteio: {doadores}')
    print(f'O(a) vencedor(a) foi: {sorteio_ganhador()}')