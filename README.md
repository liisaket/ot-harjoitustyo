# Mood-Tracker

Päiväkirjasovellus tunteiden seurantaan.

Sovelluksessa rekisteröitynyt käyttäjä voi tehdä postauksen päivän tunnetilasta ja kirjoittaa lisätietoja päivästään.

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
