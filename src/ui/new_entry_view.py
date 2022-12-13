from tkinter import ttk, constants, Tk, StringVar
from tkinter.ttk import Combobox
from services.diary_service import diary_service


class NewEntryView:
    """Luokka uuden postauksen luomista varten."""
    
    def __init__(self, root, handle_logout, handle_show_main_page_view):
        """Luokan konstruktori. Luo uuden näkymän.
        
        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_logout:
                Kutsuttava arvo, jota kutsutaan, kun käyttäjä kirjautuu ulos.
            handle_show_main_page_view:
                Kutsuttava arvo, jota kutsutaan, kun siirrytään etusivulle.
        """
        
        self._root = root
        self._handle_show_main_page_view = handle_show_main_page_view
        self._handle_logout = handle_logout
        self._user = diary_service.get_current_user()
        self._frame = None
        self._notes = None
        self._emotion = None
        self._message_variable = None
        self._message_label = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()
    
    def _show_message(self, message):
        self._message_variable.set(message)
        self._message_label.grid()

    def _hide_message(self):
        self._message_label.grid_remove()

    def _logout_handler(self):
        diary_service.logout()
        self._handle_logout()

    def _initialize_header(self):
        user_label = ttk.Label(
            master=self._frame,
            text=f"Logged in as {self._user.username}"
        )

        logout_button = ttk.Button(
            master=self._frame,
            text="Logout",
            command=self._logout_handler
        )

        user_label.grid(row=0, column=0, padx=5, pady=5, sticky=constants.W)

        logout_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

    def _handle_create_entry(self):
        content = self._notes.get()
        emotion = self._emotion.get()

        if content and emotion:
            diary_service.create_entry(content, emotion)
            self._initialize()
            self._show_message("Entry saved.")

    def _initialize_footer(self):
        new_label = ttk.Label(
            master=self._frame,
            text=f"New entry:"
        )

        feeling_label = ttk.Label(
            master=self._frame,
            text=f"How are you feeling today?"
        )

        notes_label = ttk.Label(
            master=self._frame,
            text=f"Notes on your day:"
        )

        new_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        feeling_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.W)
        notes_label.grid(row=4, column=0, padx=5, pady=5, sticky=constants.W)

        choices = ["happy", "euphoric", "calm", "sad", "angry", "tired"]
        variable = StringVar()

        self._emotion = ttk.Combobox(
            master=self._frame, values=choices, textvariable=variable, state="readonly")
        self._emotion.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)

        self._notes = ttk.Entry(master=self._frame)

        self._notes.grid(
            row=5,
            column=0,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        save_entry_button = ttk.Button(
            master=self._frame,
            text="Save entry",
            command=self._handle_create_entry
        )

        go_back_button = ttk.Button(
            master=self._frame,
            text="Go back",
            command=self._handle_show_main_page_view
        )

        save_entry_button.grid(row=6, column=0, padx=5,
                               pady=5, sticky=constants.EW)
        go_back_button.grid(row=7, column=0, padx=5,
                            pady=5, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        
        self._message_variable = StringVar(self._frame)

        self._message_label = ttk.Label(
            master=self._frame,
            textvariable=self._message_variable,
            foreground="green"
        )

        self._message_label.grid(padx=5, pady=5)

        self._initialize_footer()
        self._initialize_header()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
