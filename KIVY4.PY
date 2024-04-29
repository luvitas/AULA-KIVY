from kivy.app import App  
from kivy.uix.checkbox import CheckBox

class MinhaApp(App):
    def build (self):
        return CheckBox(active=false)
    
if __name__ == "___main___":
    MinhaApp().run()    