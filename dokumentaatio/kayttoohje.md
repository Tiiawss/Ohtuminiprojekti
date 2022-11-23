# Käyttöohje

## Lataaminen

Lataa ohjelma githubista komennolla

```bash
git clone https://github.com/Tiiawss/Ohtuminiprojekti.git
```

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

## Lähteen lisääminen

Lähteen lisääminen onnistuu painamalla aloitussivulta _Lisää tästä_ -nappia, joka siirtää sovelluksen lähteen lisäys sivulle.

Lähteen lisäyksessä on neljä eri kenttää:

- Kirjailijan nimi

- Kirjan nimi

- Kirjan julkaisuvuosi

- Kirjan julkaisija

Kaikki kentät tulee olla täytettynä lähteen lisäämistä varten.

Kenttien täyttämisen jälkeen painamalla _Lisää_ -nappia lähde lisätään lähdeluetteloon

## Lähteiden tarkastelu ihmisluettavassa muodossa

Painamalla aloitussivulta _Katso kaikki_ -nappia, siirtyy ohjelma sivulle, jossa on mahdollista tarkastalle lisättyjä lähteitä luettelomuodossa

Sivulla on lueteltu kaikki lähteet seuraavassa muodossa:

- Lähteen viiteavain

- Kirjailija

- Kirjan nimi

- Julkaisuvuosi

- Julkaisija

## Lähteistä bibtexin muodostamisen

Painamalla aloitussivulla _Muodosta BibTex_ -nappia, siirtyy ohjelma sivustolle, jossa on lisätyt lähteet BibTex-tiedosto muodossa
