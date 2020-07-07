version = '1.0.0 Beta'

def intro():
    mensagem = f'Assistente - Version {version}/ by: Saimon Ribeiro'
    print('-'* len(mensagem) + f'\n{mensagem}\n'+ '-'* len(mensagem))
lista_erros=[
        'Não intendi Nada',
        'Repete por favor',
        'Fala direito'
]

conversas = {
    'Olá':'Opa! e ai?',
    'sim e você?':'Tudo bem!'
}
comandos = {
    'desligar':'desligando',
    'reiniciar':'reiniciando'
}

def verifica_nome(user_name):
    if user_name.startswith('Meu nome é'):
        user_name = user_name.replace('Meu nome é','')
    if user_name.startswith('Eu me chamo'):
        user_name = user_name.replace('Eu me chamo','')
    if user_name.startswith('Eu sou o'):
        user_name = user_name.replace('Eu sou o','')
    if user_name.startswith('Eu sou a'):
        user_name = user_name.replace('Eu sou a','')

    return user_name


def verifica_nome_existe(nome):
    dados = open('dados/nomes.txt','r')
    nome_list = dados.readlines()

    if not nome_list:
        vazio = open('dados/nomes.txt','r')
        conteudo = vazio.readlines()
        conteudo.append(f'{nome}')
        vazio = open('dados/nomes.txt','w')
        vazio.writelines(conteudo)
        vazio.close()

        return f'Olá {nome} prazer em te conhecer'

    for linha in nome_list:
        if linha == nome:
            return f'Olá {nome}'

    vazio = open('dados/nomes.txt','r')
    conteudo = vazio.readlines()
    conteudo.append(f'\n{nome}')
    vazio = open('dados/nomes.txt','w')
    vazio.writelines(conteudo)
    vazio.close()

    return f'Olá! {nome}, Sou sua assistente virtual'


def name_list():
    try:
        nomes = open('dados/nomes.txt','r')
        nomes.close()

    except FileNotFoundError:
        nomes = open('dados/nomes.txt','w')
        nomes.close()
