
def tratamento_acao(*dados):
    
    if dados[2] <= dados[1]:
        mensagem = f'A Cotação de {dados[0]} está na máxima do dia! '
        mensagem_valor = f'Está cotada nesse momento à {dados[1]}'
        return f'{mensagem}, {mensagem_valor}'



    elif dados[3] >= dados[1]:
        mensagem = f'A Cotação de {dados[0]} está na mínima do dia! '
        mensagem_valor = f'Está cotada nesse momento à {dados[1]}'
        return f'{mensagem}, {mensagem_valor}'

    else:
        return 'Tudo nos conformes'
