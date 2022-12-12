# Mood-Tracker

Päiväkirjasovellus tunteiden seurantaan.

Sovelluksessa rekisteröitynyt käyttäjä voi tehdä postauksen päivän tunnetilasta ja kirjoittaa lisätietoja päivästään.

### Sovelluksen tämänhetkinen tilanne:

- Pystyy luomaan uuden käyttäjän ja kirjautua sisään
- Pystyy kirjautumaan ulos Logout-napista
- Löytyy etusivu ja napit postauksen luomissivulle ja vanhojen postauksien katsomiseen
- Pystyy luomaan uuden postauksen (valitaan päivän tunnetila ja voi kirjoittaa lisätietoja päivästään)
- Past entries-sivulla näkyy vain uusin postaus !!


## Dokumentaatio

- [Työaikakirjanpito](https://github.com/liisaket/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/liisaket/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Vaatimusmäärittely](https://github.com/liisaket/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/liisaket/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Käyttöohjeet

- Lataa projektin viikon 5 [releasen](https://github.com/liisaket/ot-harjoitustyo/releases/tag/viikko5) lähdekoodi: Releases -> Assets -> Source code
- Avaa ladattu zip-kansio ja pura se
- Siirry purettuun kansioon terminaalissa -> jatka ohjeita Asennus-kohdasta


## Asennus

1. Riippuvuudet asennetaan komennolla:

```bash
poetry install
```

2. Alustustoimenpiteet suoritetaan komennolla:

```bash
poetry run invoke build
```

3. Sovelluksen käynnistetään komennolla:

```bash
poetry run invoke start
```

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

Raportti ilmestyy _htmlcov_-hakemistoon.

### Pylint

Pylint-tarkastukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
