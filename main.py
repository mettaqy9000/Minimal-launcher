import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class MinimalLauncherApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.header_label = Label(
            text="Focus Mode Active\nChoose mindfully.", 
            font_size='24sp', 
            halign='center',
            color=(1, 1, 1, 1)
        )
        layout.add_widget(self.header_label)
        
        self.search_input = TextInput(
            text='',
            hint_text='Search Apps...',
            font_size='18sp',
            multiline=False,
            padding_x=10,
            padding_y=10,
            size_hint_y=None,
            height=60,
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1)
        )
        self.search_input.bind(on_text_validate=self.on_search)
        layout.add_widget(self.search_input)
        
        essential_apps = ["Phone", "Messages", "Browser", "Notes"]
        for app_name in essential_apps:
            btn = Button(
                text=app_name,
                font_size='18sp',
                background_color=(0, 0, 0, 0),
                color=(0.7, 0.7, 0.7, 1)
            )
            btn.bind(on_press=self.open_app_handler)
            layout.add_widget(btn)
            
        return layout

    def on_start(self):
        Window.clearcolor = (0, 0, 0, 1)

    def open_app_handler(self, instance):
        self.header_label.text = f"Opening {instance.text}..."

    def on_search(self, instance):
        search_query = self.search_input.text
        if search_query:
            self.header_label.text = f"Searching for '{search_query}'..."
        else:
            self.header_label.text = "Focus Mode Active\nChoose mindfully."
        self.search_input.text = ""

if __name__ == '__main__':
    MinimalLauncherApp().run()
