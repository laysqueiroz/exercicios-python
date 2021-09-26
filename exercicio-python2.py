nome = (input('Nome: '))
sobrenome = (input('Sobrenome: '))
ru = (input('Digite os dois últimos dígitos do seu RU: '))

def criarEmail(nome, sobrenome, ru):
    email = nome[0].lower() + sobrenome.lower() + ru + '@algoritmos.com.br'
    print('Sra. {} {}, seu e-mail é {}'.format(nome, sobrenome, email))

criarEmail(nome, sobrenome, ru)