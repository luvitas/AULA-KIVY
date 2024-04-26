from kivy.app import APP
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class RotuloApp(APP):
    def build(self):
        layout = BoxLayout(orientation='vertical ')
        self.lab1 = Label(
             text= 'SENAI',  color=[1, 0, 0, 1],
             front_size=40, bold=True
    )   
       
         
