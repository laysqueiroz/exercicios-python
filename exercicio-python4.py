lista = []

def cadastro_de_produto(produto_para_cadastro: dict):
    lista.append(produto_para_cadastro)
    return

opcao = int(input('Cadastrar produto? 0 - Não     1 - Sim '))
while opcao == 1:
    novo_produto = {}

    novo_produto['codigo'] = int(input('Digite o código do produto: '))

    if novo_produto['codigo'] == 0:
        break

    novo_produto['estoque'] = int(input('Digite a quantidade em estoque: '))
    novo_produto['minimo'] = int(input('Digite a quantidade mínima do estoque: '))

    cadastro_de_produto(novo_produto)
    opcao = int(input('Cadastrar produto? 0 - Não     1 - Sim '))

if len(lista) > 0:
    print('Lista de produtos por código em ordem crescente:')
    print("Código".center(10), end='')
    print("Estoque".center(10), end='')
    print("Mínimo".center(10))

    for produto in sorted(lista, key=lambda item: item['codigo']):
        print(str(produto['codigo']).center(10), end='')
        print(str(produto['estoque']).center(10), end='')
        print(str(produto['minimo']).center(10))
else:
    exit()