from tkinter import ttk, constants, StringVar
from services.diary_service import diary_service


class PastEntriesList:
    """Luokka postauksien listaamiseen."""
    
    def __init__(self, root, entries, handle_delete_entry):
        """Luokan konstruktori. Luo uuden näkymän.
        
        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            entries: Lista Entry-olioita, jotka näkymässä näytetään.
            handle_delete_entry:
                Kutsuttava arvo, jota kutsutaan, kun postaus poistetaan.
        """
        
        self._root = root
        self._entries = entries
        self._handle_delete_entry = handle_delete_entry
        self._frame = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _initialize_entry_item(self, entry):
        new_line = "\n"
        item_frame = ttk.Frame(master=self._frame)
        label = ttk.Label(
            master=item_frame,
            text=f"Date: {entry.date}{new_line}Emotion: {entry.emotion}{new_line}Notes: {entry.content}"
        )
        
        
        delete_entry_button = ttk.Button(
            master=item_frame,
            text="Delete",
            command=lambda: self._handle_delete_entry(entry.id)
        )

        label.grid(row=4, column=0, padx=5, pady=5, sticky=constants.SW)
        
        delete_entry_button.grid(
            row=4,
            column=1,
            padx=5,
            pady=5,
            sticky=constants.EW
        )

        item_frame.grid_columnconfigure(0, weight=1)
        item_frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        for entry in self._entries:
            self._initialize_entry_item(entry)


class PastEntriesView:
    """Luokka omien postauksien listaamiseen ja näyttämiseen."""
    
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
        self._entries_frame = None
        self._entries_view = None
        self._frame = None
        self._message_variable = None
        self._message_label = None

        self._initialize()

    def pack(self):
        """Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän."""
        self._frame.destroy()

    def _logout_handler(self):
        diary_service.logout()
        self._handle_logout()
    
    def _handle_delete_entry(self, entry_id):
        diary_service.delete_entry(entry_id)
        self._initialize_message("green")
        self._show_message("Entry deleted.")
        self._initialize_entries()
    
    def _show_message(self, message):
        self._message_variable.set(message)
        self._message_label.grid()

    def _hide_message(self):
        self._message_label.grid_remove()
        
    def _initialize_message(self, color):
        self._message_variable = StringVar(self._frame)

        self._message_label = ttk.Label(
            master=self._frame,
            textvariable=self._message_variable,
            foreground=color
        )

        self._message_label.grid(row=4, padx=5, pady=5, sticky=constants.S)

    def _initialize_entries(self):
        if self._entries_view:
            self._entries_view.destroy()

        entries = diary_service.get_entries()
        
        if len(entries) == 0:
            self._initialize_message(None)
            self._show_message("No entries (yet).")

        self._entries_view = PastEntriesList(
            self._entries_frame,
            entries,
            self._handle_delete_entry
        )

        self._entries_view.pack()

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

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._entries_frame = ttk.Frame(master=self._frame)

        past_label = ttk.Label(
            master=self._frame,
            text=f"Past entries:"
        )

        past_label.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)

        go_back_button = ttk.Button(
            master=self._frame,
            text="Go back",
            command=self._handle_show_main_page_view
        )

        go_back_button.grid(row=6, column=0, padx=5,
                            pady=5, sticky=constants.EW)

        self._initialize_entries()
        self._initialize_header()

        self._entries_frame.grid(row=4, column=0, sticky=constants.EW)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
