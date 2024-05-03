from kivy.app import App     
from kivy.uix.video import Video


class MinhaApp(App):
    def build(sef):
        return Video(source='caminho/para/seu/video.mp4')
    
if __name__ == "__main__":
    MinhaApp().run( )    