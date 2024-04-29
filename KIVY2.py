from kivy.app import App
from kivy.uix.label import Label 
from kivy.utils import get_color_from_hex

class MyApp(App):
    def build (self):
        return Label(text= "Olá SENAI", font_size=100, font_name='Arial', color=get_color_from_hex("#FF5733"))
halign='left' , # alinha o texto à esquerda 
valign= 'top' , # alinha o texto no topo
size_hint=(None,None), # Desativa o ajuste automático do tamanho
size=(150,50), # Define o tamanho do rótulon
text_size=(150,None) # Define a largura máxima do texto

if __name__ == '__main__':
    MyApp().run()    
