from tkinter import Tk, ttk, constants

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        heading_label = ttk.Label(master=self._root, text="Login")

        username_label = ttk.Label(master=self._root, text="Username")
        username_entry = ttk.Entry(master=self._root)

        password_label = ttk.Label(master=self._root, text="Password")
        password_entry = ttk.Entry(master=self._root)

        button = ttk.Button(master=self._root, text="Button")

        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=1)

window = Tk()
window.title("TkInter example")

ui = UI(window)
ui.start()

window.mainloop()
