# Arkkitehtuurikuvaus

## Rakenne

![pakkausrakenne](./kuvat/pakkausrakenne.png)

- Käyttöliittymä: [ui](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/ui)
- Sovelluslogiikka: [services](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/services)
- Tietojen pysyväistallennus: [repositories](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/repositories)
- Luokat datan käsittelyyn: [entities](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/entities)

## Käyttöliittymä

Viisi näkymää:
- Kirjautuminen
- Uuden käyttäjän luominen
- Sovelluksen etusivu
- Uuden postauksen luominen
- Omat postaukset

Jokainen näkymä on oma luokkansa. Luokka [UI](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/ui/ui.py) hoitaa näkymien näyttämisen.

## Sovelluslogiikka

Sovelluksen luokat datan käsittelyyn:

- [User](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/entities/user.py): kuvaa yksittäistä käyttäjää (käyttäjätunnus ja salasana)
- [Entry](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/entities/entry.py): kuvaa käyttäjän yksittäistä postausta (id, päivämäärä, tunnetila, lisätiedot)

```mermaid
 classDiagram
      Entry "*" --> "1" User
      class User{
          username
          password
      }
      class Entry{
          id
          date
          emotion
          content
      }
```

Luokka, joka vastaa sovelluksen toiminnoista:

- [DiaryService](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/services/diary_service.py)

Esimerkkejä DiaryService:n toiminnoista:

- ```login(username, password)```
- ```create_entry(content, emotion)```
- ```get_entries()```

DiaryService on yhteydessä luokkiin:

- [UserRepository](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/repositories/user_repository.py): vastaa käyttäjiin liittyvistä tietokantaoperaatioista
- [EntryRepository](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/repositories/entry_repository.py): vastaa postauksiin liittyvistä tietokantaoperaatioista

Pakkauskaavio ohjelmiston rakenteesta:

![Pakkausrakenne](./kuvat/arkkitehtuuri-rakenne.png)

## Tietojen pysyväistallennus

Luokat, jotka vastaavat tietojen tallentamisesta:

- [UserRepository](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/repositories/user_repository.py): vastaa käyttäjiin liittyvistä tietokantaoperaatioista (tallentaa SQLite-tietokantaan)
- [EntryRepository](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/repositories/entry_repository.py): vastaa postauksiin liittyvistä tietokantaoperaatioista (tallentaa CSV-tiedostoon)

Konfiguraatiotiedosto [.env](https://github.com/liisaket/ot-harjoitustyo/blob/master/.env) määrittelee tiedostojen nimet datan tallennusta varten.

Käyttäjät tallennetaan SQLite-tietokantaan tauluun ```users``` arvoilla ```username``` ja ```password```. Taulu alustetaan [initialize_database.py](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/initialize_database.py)-tiedostossa.

Sovellus tallentaa postauksien tiedot CSV-tiedostoon muodossa:

```
578e834c-127a-4eb1-9b18-079b170543b3;13-12-2022 16:00;Great day;happy;testi
```

1. Postauksen id
2. Postauksen päivämäärä ja kellonaika (pv-kk-vvvv hh:mm)
3. Päivän lisätiedot/muistiinpanot
4. Päivän tunnetila
5. Postauksen omaava käyttäjä

## Päätoiminnallisuudet ja toimintalogiikka

### Sisäänkirjautuminen

Kun käyttäjä kirjoittaa kirjautumisnäkymässä käyttäjätunnuksensa ja salasanan, ja klikkaa "Login"-nappia, tapahtuu seuraavaa:

![Kaavio1](./kuvat/loginkaavio.png)

- Napin painallukseen reagoi [tapahtumankäsittelijä](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/ui/login_view.py#L20), joka kutsuu sovelluslogiikan ```DiaryService``` metodia [login](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/services/diary_service.py#L46), jolle annetaan parametreiksi juuri syötetyt käyttäjätunnus ja salasana. 
- ```Login```-metodi kutsuu käyttäjistä vastaavan luokan ```UserRepository``` funktiota [find_by_username](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/repositories/user_repository.py#L46), jonka avulla tarkastetaan, onko käyttäjätunnus olemassa.
  - Jos käyttäjätunnus löytyy, funktio palauttaa kyseisen käyttäjän User-oliona.
  - Muuten funktio palauttaisi None, johon sovelluslogiikan metodi reagoisi nostattamalla ```InvalidCredentialsError```-virhetilanteen.
- Kun käyttäjätunnus on löytynyt, sovelluslogiikan metodi vertaa syötettyä salasanaa ja käyttäjän tallennettua salasanaa; jos ne täsmäävät, kirjautuminen onnistuu.
- Sitten käyttöliittymä päivittää näkymäksi sovelluksen etusivun, eli ```Main Page```.

### Uuden postauksen luominen

Kun käyttäjä on siirtynyt uuden postauksen luomissivulle, valinnut päivän tunnetilan ja kirjoittanut lisätietoja päivästään, sekä klikannut "Save entry"-nappia tallentaakseen postauksen, tapahtuu seuraavaa:

![Kaavio2](./kuvat/save_entry.png)

- [Tapahtumankäsittelijä](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/ui/new_entry_view.py#L73) reagoi napin painallukseen kutsumalla sovelluslogiikan ```DiaryService``` metodia [create_entry](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/services/diary_service.py#L107), jolle annetaan parametreiksi käyttäjän valitsema tunnetila (emotion), sekä hänen kirjoittamat lisätiedot päivästään (content).
- Metodi luo uuden [Entry](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/services/diary_service.py#L117)-olion postauksesta, jolle annetaan parametreiksi tunnetila, lisätiedot, sekä postauksen tehnyt käyttäjä.
- Tuo Entry-olio annetaan postauksista vastaavan luokan ```EntryRepository``` funktiolle [create](https://github.com/liisaket/ot-harjoitustyo/blob/master/src/repositories/entry_repository.py#L46), joka tallentaa postauksen CSV-tiedostoon. Funktio palauttaa tallennetun Entry-olion.
- Kun postaus on tallennettu, käyttöliittymä kutsuu omia metodeitaan ```_initialize_message("green")``` ja ```_show_message("Entry saved.")```. Näkymä päivittyy ja käyttäjä näkee vihreällä kirjoitetun ilmoituksen postauksen onnistuneesta tallentumisesta.
