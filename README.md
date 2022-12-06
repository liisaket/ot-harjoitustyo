# Mood-Tracker

Päiväkirjasovellus tunteiden seurantaan.

Sovelluksessa rekisteröitynyt käyttäjä voi tehdä postauksen päivän tunnetilasta ja kirjoittaa lisätietoja päivästään.

### Sovelluksen tämänhetkinen tilanne:
- Pystyy luomaan uuden käyttäjän ja kirjautua sisään
- Pystyy kirjautumaan ulos Logout-napista
- Etusivulla Make an entry-nappi: pääsee sivulle, jossa luodaan uusi postaus (ei vielä toiminnassa); Go back -> takaisin etusivulle, Save entry -> tallenna postaus (ei vielä tee mitään)
- Etusivulla Past entries-nappi: pääsee sivulle, jossa näkyy kaikki omat postaukset


## Dokumentaatio

- [Työaikakirjanpito](https://github.com/liisaket/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/liisaket/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Vaatimusmäärittely](https://github.com/liisaket/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/liisaket/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Riippuvuudet voi asentaa komennolla:

```bash
poetry install
```

2. Alustustoimenpiteet voi suorittaa komennolla:

```bash
poetry run invoke build
```

3. Sovelluksen voi käynnistää komennolla:

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
