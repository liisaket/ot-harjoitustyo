from tkinter import ttk, constants, StringVar
from tkinter.tkk import Combobox
from services.diary_service import diary_service


class NewEntryView:
    def __init__(self, root, handle_logout, handle_show_main_page_view):
        self._root = root
        self._handle_show_main_page_view = handle_show_main_page_view
        self._handle_logout = handle_logout
        self._user = diary_service.get_current_user()
        self._frame = None
        self._create_entry = None

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
    
    def _handle_create_entry(self):
        entry_content = self._create_entry.get()

        if entry_content:
            diary_service.create_entry(entry_content)
    
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
            text=f"Notes:"
        )
        
        choices = ["happy", "euphoric", "calm", "sad", "angry", "tired"]
        variable = StringVar()
        variable.set("happy")
        
        c_box = Combobox(self._root, values=choices, textvariable=variable, state="readonly")
        c_box.pack()
        
        self._create_entry = ttk.Entry(master=self._frame)

        new_label.grid(row=1, column=0, padx=5, pady=5, sticky=constants.W)
        feeling_label.grid(row=2, column=0, padx=5, pady=5, sticky=constants.W)
        notes_label.grid(row=3, column=0, padx=5, pady=5, sticky=constants.W)

        self._create_entry.grid(
            row=3,
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

        save_entry_button.grid(row=5, column=0, padx=5,
                               pady=5, sticky=constants.EW)
        go_back_button.grid(row=6, column=0, padx=5,
                            pady=5, sticky=constants.EW)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_footer()
        self._initialize_header()

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._frame.grid_columnconfigure(1, weight=0)
