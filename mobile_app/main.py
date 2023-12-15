from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CoughCounter(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.count = 0
        self.label = Label(text='Cough Count: 0')
        self.add_widget(self.label)
        self.button = Button(text='Count Cough')
        self.button.bind(on_press=self.increment_count)
        self.add_widget(self.button)

    def increment_count(self, instance):
        self.count += 1
        self.label.text = f'Cough Count: {self.count}'
        # TODO: Implement data sending to server

class TheCoughApp(App):
    def build(self):
        return CoughCounter()

if __name__ == '__main__':
    TheCoughApp().run()
