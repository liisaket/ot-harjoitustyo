import tkinter as tk
from ui.ui import UI

def main():
    window = tk.Tk()
    window.title("Mood-Tracker")
    window.eval("tk::PlaceWindow . center")
    frame1 = tk.Frame(window, width=500, height=300, bg="alice blue")
    frame1.grid(row=0, column=0)

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()