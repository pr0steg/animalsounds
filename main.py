from kivy.app import App
from kivy.base import runTouchApp
from kivy.core.audio import SoundLoader
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

import os.path

Window.set_title('Animal Sounds')


class Sounds(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        pass


class SoundsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        Window.size = (320, 640)
        size = dp(100)
        Window.add_widget(
            Image(
                source="images/bg.jpg",
                keep_ratio=False,
                allow_stretch=True))

        layout = GridLayout(cols=3,
                            spacing=10,
                            size_hint_y=None,
                            padding=[1, 1, 1, 1],
                            )
        layout.bind(minimum_height=layout.setter('height'))

        for i in range(64):
            img_src = i + 1
            if os.path.exists(f"animals/pic/{img_src}.jpg"):
                btn = Button(text=str(i + 1),
                             size_hint=(None, None),
                             size=(size, size),
                             font_size='0dp',
                             color=(0, 0, 1, 1),
                             border=(10, 10, 10, 10),
                             bold=True,
                             background_normal=f"animals/pic/{img_src}.jpg")

                btn.bind(on_press=self.callback)
            else:
                btn = Button(text=str(i + 1),
                             size_hint=(None, None),
                             size=(size, size),
                             font_size='0dp',
                             color=(0, 0, 1, 1),
                             bold=True,
                             background_normal="images/0.png")
            layout.add_widget(btn)

        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout)
        runTouchApp(root)
        return Sounds()

    @staticmethod
    def callback(btn):
        sound_num = btn.text
        sound = SoundLoader.load(f'animals/sound/{sound_num}.mp3')

        if sound:
            sound.play()


if __name__ == '__main__':
    SoundsApp().run()
