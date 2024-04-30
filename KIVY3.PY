from kivy.app import App     
from kivy.uix.button import Button
from kivy.app import App  
from kivy.uix.button import Button

class MinhaApp(App):
  def build(self):
           return Button(text='Clique Aqui', background_color= get_color_from_hex ("#3498db"))
  
if __name__ == "__main__":
     MinhaApp().run()

def botao_pressionado(instance):
    print("Botão pressionado!")

class MinhaApp (App):    
    def build (self):
        btn = Button(text= 'Clique aqui')
        btn.bind(on_press=botao_pressionado)
        return btn  
    
if __name__ == "__main__":
    MinhaApp().run()   
