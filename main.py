import nltk
from nltk.chat.util import Chat, reflections


reflections_pt = {
    'eu': 'você',
    'eu sou': 'você é',
    'eu era': 'você era',
    'eu iria': 'você iria',
    'eu irei': 'você irá',
    'meu': 'seu',
    'você': 'eu',
    'você é': 'eu sou',
    'você era': 'eu era',
    'você iria': 'eu iria',
    'você irá': 'eu irei',
    'seu': 'meu'
}

pares = [
        [
         r'oi|olá|opa',
         ['olá!', 'como vai?', 'tudo bem?']
        ],
        [
         r'(.*)Qual é o seu Nome?',
         ['Meu nome é Urbe!']
        ],
        [
         r'(.*)idade',
         ['Sou um Robô filha da puta!']
        ],
        [
         r'meu nome é(.*)',
         ['E ai %1, como vc ta?']
        ],
        [
         r'quit',
         ['vlw Chefe!', 'Até!', 'Inté!']
        ]
]

print('Olá sou o Bot!')
chat = Chat(pares, reflections_pt)
chat.converse()
