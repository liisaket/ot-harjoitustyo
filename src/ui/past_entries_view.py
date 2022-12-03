from tkinter import ttk, constants
from services.diary_service import diary_service


class PastEntriesView:
    def __init__(self, root, handle_logout, handle_show_main_page_view):
        self._root = root
        self._handle_show_main_page_view = handle_show_main_page_view
        self._handle_logout = handle_logout
        self._user = diary_service.get_current_user()
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
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
        
        go_back_button.grid(row=6, column=0, padx=5, pady=5, sticky=constants.EW)
        
        self._frame.grid_columnconfigure(0, weight=1, minsize=400)

        self._initialize_header()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
