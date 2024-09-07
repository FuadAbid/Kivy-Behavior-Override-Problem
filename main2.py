from kivy.app import App
from kivy.lang.builder import Builder
import New_folder

KV = '''
Screen:
    canvas.before:
        Color:
            rgba: .1, .1, .1, 1
        Rectangle:
            size: self.size

    FCard:
        bg_color: .2, .2, .2, 1
        size_hint: .5, None
        height: dp(50)
        pos_hint: {'center_x': .5, 'center_y': .5}

        # FLabel:
        #     text: 'Test'

        FButton:
            text: 'Hello World'
            size_hint: None, None
            size: 150, 50
            x: 350
            pos_hint: {'center_y': .5}
            bg_color: 'red'
            shadow_size: dp(8)
            on_press:
                self.bg_color = 'blue'
                self.shadow_size = dp(16)
            on_release:
                self.bg_color = 'red'
                self.shadow_size = dp(8)
'''

class Example(App):
    def build(self):
        return Builder.load_string(KV)
    
Example().run()