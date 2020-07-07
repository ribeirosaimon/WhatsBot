import speech_recognition as sr
import pyttsx3
from config import *
from random import choice


reproducao = pyttsx3.init()

def saiSom(resposta):
    reproducao.say(resposta)
    reproducao.runAndWait()


def assistente():
    while True:
        resposta_erro_aleatoria = choice(lista_erros)
        rec = sr.Recognizer()
        with sr.Microphone() as s:
            rec.adjust_for_ambient_noise(s)
        while True:
            try:
                audio = rec.listen(s)
                user_name = rec.recognize_google(audio, language='pt')
                user_name = verifica_nome(user_name)
                name_list()
                apresentacao = f'{verifica_nome_existe(user_name)}'
                print(apresentacao)
                saiSom(apresentacao)
                brute_user_name = user_name
                user_name = user_name.split(' ')
                user_name = user_name[0]
                break
            except sr.UnknownValueError:
                saiSom(resposta_erro_aleatoria)
    print('='*len(apresentacao))
    print('Olá! Bom Dia!')
    while True:
        try:
            audio = rec.listen(s)
            entrada = rec.recognize_google(audio, language='pt')
            print (f'{user_name}: {entrada}')

            resposta = conversas[entrada]
            print(f'Assistente: {resposta}')

            saiSom(f'{resposta}')
        except sr.UnknownValueError:
            saiSom(resposta_erro_aleatoria)


if __name__ == '__main__':
    intro()
    saiSom('Iniciando')
    assistente()
