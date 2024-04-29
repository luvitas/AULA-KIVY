from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label

class MinhaApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical" , padding=20)
        slider= Slider (min=0, max=100, value=50, step=1)
        slider.bind(value=self.autalizar_label)
        self.label = Label (text= " Valor do slider:")