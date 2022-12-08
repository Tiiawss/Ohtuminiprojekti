# Käyttöohje

## Lataaminen

Lataa ohjelma githubista komennolla

```bash
git clone https://github.com/Tiiawss/Ohtuminiprojekti.git
```

## Konfiguraatio

### Lähdeviittaustyypit

Ohjelman ![src](../src) kansiosta löytyy tiedosto ![cite_tyoes.toml](../src/cite_types.toml). Tällä tiedostolla pystyy määrittelemään sovelluksen käyttämät tiedostotyypit seuraavasti

```
[Book] # Lähdeviittauksen nimi
author = ["Kirjailijan nimi","True"] 

Ensin bibtex nimitys, 
listan ensimmäisenä Sovelluksen titteli viitteelle 
ja viimeisenä Pakollinen vai ei, aseta "True" jos on, muuten ""
```

**HUOM!** Sovelluksessa on jo käytössä _date_ ja _tagit_ kentät, eli niitä ei voi käyttää.

### Tietokanta

Sovelluskäyttää MongoDB tietokantaa. Tämän käyttöä varten tulee luoda [MongoDB](https://www.mongodb.com) tietokanta ja tämän secret key pitää asettaa ![src](../src) kansioon tiedostoon _secrects.env_.

## Ohjelman käynnistäminen

Ennen ensimmäistä suorituskertaa asenna riippuvuudet suorittamalla ohjelman juurihakemistossa
```bash
poetry install
```

Tämän jälkeen on mahdollista käynnistää sovellus suorittamalla juurihakemistossa komento

```bash
poetry run invoke start
```

## Sivustolle siirtyminen

Kun ohjelma on käynnissä, on sitä mahdollista käyttää paikallisesti. Sovelluksen käyttäminen onnistuu siirtymällä nettiselaimessa sivustolle
[http://127.0.0.1:5000](http://127.0.0.1:5000)

Ohjelma on myös internetissä osoitteessa [https://quiet-night-8665.fly.dev/](https://quiet-night-8665.fly.dev/)

## Lähteen lisääminen

Lähteen lisääminen onnistuu painamalla aloitussivulta _Lisää tästä_ -nappia, joka siirtää sovelluksen lähteen lisäys sivulle.

Lähteen lisäyksessä ensimmäisenä on viitetyypin valinta. Kaikki viitetyypit on määritelty ![cite_tyoes.toml](../src/cite_types.toml) tiedostossa. Viitetyypin valitseminen vaihtaa täytettävät kentät kyseisen lähdeviiteen kentikiksi.

Viitetyypillä on kolmea erilaista kenttää seuraavassa järjestyksessä:

- Pakolliset kentät

- Vapaaehtoiset kentät

- Tagit

Kaikki pakolliset kentät tulee olla täytettynä lähteen lisäämistä varten.

Kenttien täyttämisen jälkeen painamalla _Lisää_ -nappia lähde lisätään lähdeluetteloon

## Lähteiden tarkastelu ihmisluettavassa muodossa

Painamalla aloitussivulta _Katso kaikki_ -nappia, siirtyy ohjelma sivulle, jossa on mahdollista tarkastalle lisättyjä lähteitä luettelomuodossa

Sivulla on lueteltu kaikki lähteet seuraavassa muodossa:

- Lähteen viiteavain

- Lähdeviiteen arvot

- Lähdeviitteen tagit

## Lähteistä bibtexin muodostamisen

Painamalla aloitussivulla _Muodosta BibTex_ -nappia, siirtyy ohjelma sivustolle, jossa on lisätyt lähteet BibTex-tiedosto muodossa
