class User:
    """Yksittäistä käyttäjää kuvaava luokka.

    Attributes:
        username: Merkkijonoarvo, joka kuvaa käyttäjätunnusta.
        password: Merkkijonoarvo, joka kuvaa salasanaa.
    """

    def __init__(self, username, password):
        """Luokan konstruktori. Luo uuden käyttäjän.

        Args:
            username: Merkkijonoarvo, joka kuvaa käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa salasanaa.
        """

        self.username = username
        self.password = password
