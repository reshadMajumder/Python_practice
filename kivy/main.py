from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class KeyboardApp(App):
    def build(self):
        # Main layout container
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # TextInput field to show typed text
        self.text_input = TextInput(
            multiline=False,
            font_size=24,
            size_hint=(1, 0.2),
            hint_text="Type here..."
        )
        main_layout.add_widget(self.text_input)

        # Layout for the keyboard
        keyboard_layout = BoxLayout(orientation='vertical', spacing=5)

        # Define the keys for the keyboard
        keys = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Shift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Backspace'],
            ['123', 'Space', 'Enter']
        ]

        # Create rows of keys
        for row in keys:
            row_layout = BoxLayout()
            for key in row:
                btn = Button(
                    text=key,
                    font_size=20,
                    size_hint=(1, 1)
                )
                # Bind button presses to their respective functions
                if key == 'Space':
                    btn.bind(on_press=lambda x: self.add_key(' '))
                elif key == 'Backspace':
                    btn.bind(on_press=lambda x: self.backspace())
                elif key == 'Enter':
                    btn.bind(on_press=lambda x: self.enter())
                elif key == 'Shift':
                    btn.bind(on_press=lambda x: self.toggle_shift())
                elif key == '123':
                    btn.bind(on_press=lambda x: self.show_numbers())
                else:
                    btn.bind(on_press=lambda x, k=key: self.add_key(k))
                row_layout.add_widget(btn)
            keyboard_layout.add_widget(row_layout)

        main_layout.add_widget(keyboard_layout)
        return main_layout

    def add_key(self, key):
        """Add a key to the text input."""
        if hasattr(self, 'is_shift_active') and self.is_shift_active:
            key = key.upper()
        else:
            key = key.lower()
        self.text_input.text += key

    def backspace(self):
        """Remove the last character."""
        self.text_input.text = self.text_input.text[:-1]

    def enter(self):
        """Simulate an Enter key."""
        self.text_input.text += '\n'

    def toggle_shift(self):
        """Toggle the shift key for uppercase."""
        if not hasattr(self, 'is_shift_active'):
            self.is_shift_active = False
        self.is_shift_active = not self.is_shift_active

    def show_numbers(self):
        """Show a number keyboard (placeholder)."""
        self.text_input.text += "[123 Keyboard]"

if __name__ == '__main__':
    KeyboardApp().run()
