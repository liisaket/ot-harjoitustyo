# Mood-Tracker

Mood-Tracker on päiväkirjasovellus omien tunteiden ja päivien seurantaan.

Sovelluksessa käyttäjä voi tehdä postauksen, jossa hän valitsee päivän tunnetilan ja kirjoittaa lisätietoja päivästään.

### Sovelluksen toiminnallisuudet

- Perustoiminnallisuudet eli pystyy luomaan uuden käyttäjän, sekä sisään- ja uloskirjautua
- Sovelluksella on etusivu, josta pääsee postauksen luomissivulle ja omien postauksien sivulle
- Käyttäjä pystyy luomaan uuden postauksen, jossa valitaan päivän tunnetila eri vaihtoehtoista, sekä kirjoitetaan lisätietoja omasta päivästä
- Käyttäjä pystyy tutkia tekemiään postauksia
- Käyttäjä pystyy poistamaan omia postauksia
- Ottaa huomioon virhetilanteet

## Dokumentaatio

- [Käyttöohjeet](https://github.com/liisaket/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Arkkitehtuurikuvaus](https://github.com/liisaket/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Vaatimusmäärittely](https://github.com/liisaket/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Testausdokumentti](https://github.com/liisaket/ot-harjoitustyo/blob/master/dokumentaatio/testaus.md)
- [Changelog](https://github.com/liisaket/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Työaikakirjanpito](https://github.com/liisaket/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

## Releases

- [Releases](https://github.com/liisaket/ot-harjoitustyo/releases)
- Uusin release on viikolta 6 (13.12.2022)

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
