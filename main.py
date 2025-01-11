from customtkinter import CTk, CTkButton, set_widget_scaling
from keyboard import add_hotkey, remove_hotkey, _hotkeys
from asyncio import run
from Frames.Checkbox_Frame import CheckboxFrame
import threading

class App(CTk):
    def __init__(self):
        super().__init__()

        # Параметры Окна
        self.title("my app")
        self.geometry("400x700")
        set_widget_scaling(1.25)

        # Параметры фрейма флажков
        self.checkbox_frame = CheckboxFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")
        self.active_hotkeys = []
        self.active_hotkeys = []
        self.hotkeys_lock = threading.Lock()


        # Параметры кнопки Применить
        self.button = CTkButton(self, text="Применить", command=self.button_callback)
        self.button.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        # Параметры сетки окна
        self.grid_columnconfigure(0, weight=1)


    def button_callback(self):
        for yes, checkbox in self.checkbox_frame.get():
            if checkbox.get("hot_key"):
                hotkey = checkbox["hot_key"]
                if yes == 1:
                    with self.hotkeys_lock:
                        if hotkey not in self.active_hotkeys:
                            add_hotkey(hotkey, checkbox["function"])
                            self.active_hotkeys.append(hotkey)
                elif yes == 0:
                    with self.hotkeys_lock:
                        if hotkey in self.active_hotkeys:
                            if hotkey in _hotkeys:
                                self.active_hotkeys.remove(hotkey)
                                remove_hotkey(hotkey)
                            


if __name__ == "__main__":
    app = App()
    run(app.mainloop())
