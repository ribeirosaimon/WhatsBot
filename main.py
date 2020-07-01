from chatterbot import Chatbot
from chatterbot.trainers import ListTrainer
import win32com.client
import speech_recognition as sr
import os

bot = Chatbot('Urbe',read_only=True)
bot.set_trainer(ListTrainer)
bot.train(['opa!','Olá!','Beleza?','sim e vc?','Tambem estou bem!'])
