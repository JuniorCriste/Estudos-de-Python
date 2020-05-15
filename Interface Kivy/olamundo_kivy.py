from kivy.app import App
from kivy.uix.button import Button

class Tela(App):
       def build(self):
           return Button(text='Ola Mundo', font_size=70)


Tela().run()
