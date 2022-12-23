from tkinter import ttk, constants
from services.diary_service import diary_service


class MainPageView:
    """Luokka sovelluksen etusivua varten."""

    def __init__(self, root, handle_logout, handle_show_new_entry_view, handle_show_past_entries_view):
        """Luokan konstruktori. Luo uuden näkymän.

        Args:
            root: TKinter-elementti, jonka sisään näkymä alustetaan.
            handle_logout:
                Kutsuttava arvo, jota kutsutaan, kun käyttäjä kirjautuu ulos.
            handle_show_new_entry_view:
                Kutsuttava arvo, jota kutsutaan, kun siirrytään luomaan uutta postausta.
            handle_show_past_entries_view:
                Kutsuttava arvo, jota kutsutaan, kun siirrytään omien postauksien sivulle.
        """

        self._root = root
        self._handle_show_new_entry_view = handle_show_new_entry_view
        self._handle_show_past_entries_view = handle_show_past_entries_view
        self._handle_logout = handle_logout
        self._user = diary_service.get_current_user()
        self._frame = None

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

        new_entry_button = ttk.Button(
            master=self._frame,
            text="Make an entry",
            command=self._handle_show_new_entry_view
        )

        past_entries_button = ttk.Button(
            master=self._frame,
            text="Past entries",
            command=self._handle_show_past_entries_view
        )

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        new_entry_button.grid(row=2, column=0, padx=5,
                              pady=5, sticky=constants.EW)
        past_entries_button.grid(
            row=3, column=0, padx=5, pady=5, sticky=constants.EW)

        self._initialize_header()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
