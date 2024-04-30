from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical" , padding=20)
        slider= Slider (min=0, max=100, value=50, step=1)
        slider.bind(value=self.autalizar_label)
        self.label = Label (text= " Valor do slider:  {}". format(int(slider.value))")
        layout.add_widget(slider)
        layout.add_widget(self.label)

        return layout
    def atualizar_label(self,instace,valor):
        self.label.text ="Valor do Slider: {}". format(int(valor))
        #samara araujo 3a
