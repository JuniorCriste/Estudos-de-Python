#coding=utf-8

from kivy.app import App
from kivy.uix.button import Button

class Tela(App):
       def build(self):
           return Button(text='Olá Mundo!', font_size=70)


Tela().run()

#codigo by: Junior Criste | Canal Informaticode | www.informaticode.com | @informaticode | @juniorcriste
