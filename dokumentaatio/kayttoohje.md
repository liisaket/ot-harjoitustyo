# Käyttöohje

- Lataa projektin viimeisimmän [releasen](https://github.com/liisaket/ot-harjoitustyo/releases) lähdekoodi: Releases -> Assets > Source code
- Avaa ladattu zip-kansio ja pura se
- Siirry purettuun kansioon terminaalissa

## Sovelluksen käynnistäminen

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Kirjautuminen

Sisäänkirjautumissivu tulee näkyviin sovelluksen käynnistämisen yhteydessä.

*kuva*

Sisäänkirjaudutaan kirjoittamalla olemassaoleva käyttäjätunnus ja sen salasana syötekenttiin, ja painamalla "Login"-nappia. Jos sisäänkirjautuminen epäonnistuu, tulee esiin virheilmoitus epäpätevästä käyttäjätunnuksesta tai salasanasta.

## Uuden käyttäjän luominen

Sisäänkirjautumissivulta pääsee luomaan uuden käyttäjän painamalla "Create user"-nappia.

*kuva*

Uusi käyttäjä luodaan kirjoittajamalla pätevä käyttäjätunnus ja salasana syötekenttiin ja painamalla "Create"-nappia. Jos käyttäjän luominen onnistuu, siirrytään sovelluksen etusivulle. Muussa tapauksessa tulee esiin virheilmoitus epäpätevästä käyttäjätunnuksesta.

Takaisin sisäänkirjautumissivulle pääsee painamalla "Login"-nappia.

## Etusivu

Kun sisään on kirjauduttu, tulee näkyviin sovelluksen etusivu.

*kuva*

Oma käyttäjätunnus näkyy vasemassa yläkulmassa. Oikean yläkulman "Logout"-napista pääsee uloskirjautumaan.

Uutta postausta pääsee luomaan "Make an entry"-napista.

Vanhoja postauksia pääsee katsomaan "Past entries"-napista. *kesken*

## Postauksen luominen

Kun etusivulla painetaan "Make an entry"-nappia, siirrytään uuden postauksen luomissivulle.

*kuva*

Valikosta valitaan päivän tunnetilaa kuvaava adjektiivi (happy, euphoric, calm, sad, angry, tired).

Syötekenttään voi kirjoittaa lisätietoja päivästään.

"Save an entry"-nappi tallentaa postauksen.

"Go back"-napista pääsee takaisin etusivulle.

## Vanhat postaukset

Kun etusivulla painetaan "Past entries"-nappia, siirrytään sivulle, jossa näkee käyttäjän postaukset. *kesken*

## Komentorivikomennot

### Testaus

Testit voi suorittaa komennolla:

```bash
poetry run invoke test
```

### Testikattavuusraportti

Testikattavuusraportin voi suorittaa komennolla:

```bash
poetry run invoke coverage-report
```

Raportti ilmestyy _htmlcov_-hakemistoon (tiedosto _index.hmtl_).

### Pylint

Pylint-tarkastukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
