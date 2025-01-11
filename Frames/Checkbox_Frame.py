from customtkinter import CTkFrame, CTkCheckBox, set_widget_scaling
from config import functions


class CheckboxFrame(CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)

        self.chekboxes = []
        self.functions = functions

        for i in self.functions.items():
            print(i)
            chekbox = CTkCheckBox(self, text=i[0])
            self.chekboxes.append(chekbox)

        for index, checkbox in enumerate(self.chekboxes):
            checkbox.grid(
                row=index,
                column=0,
                padx=10,
                pady=10,
                sticky="nsew",
            )

    def get(self):
        checked_checkboxes = []

        for checkbox in self.chekboxes:
            checkbox_config = self.functions.get(checkbox.cget("text"), None)
            checked_checkboxes.append([checkbox.get(), checkbox_config])

        return checked_checkboxes
