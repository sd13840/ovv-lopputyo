# Ohjelmointivälineet ja versionhallinta IC250107-3004

## Lopputyö

Tässä lopputyössä tein pienen Python-ohjelman, jonka avulla harjoittelin Gitin käyttöä terminaalissa.

## Ohjelman kuvaus

Ohjelma kysyy ensin käytettävän kielen ja sen jälkeen käyttäjän nimen. Ohjelma tulostaa tervehdyksen ja päivänjatkotoivotuksen joko suomeksi tai englanniksi.

Jos kielivalinnaksi annetaan jotain muuta kuin `fi` tai `en`, ohjelma ilmoittaa tuntemattomasta kielivalinnasta.

## Käyttö

Ohjelma käynnistetään terminaalissa komennolla:

`python app.py`

## Gitin käyttö projektissa

Projektin aikana käytin Gitin peruskomentojen lisäksi myös kurssilla harjoiteltuja jatkotoimintoja.

Käytin haaroja eri ominaisuuksien tekemiseen ja yhdistin niitä takaisin main-haaraan. Yksi haara yhdistettiin GitHubissa Pull Requestin kautta.

Harjoittelin myös `git stash` ja `git stash pop` -komentoja kesken olevan muutoksen tallentamiseen.

Tein tarkoituksella virheellisen commitin ja peruin sen `git revert` -komennolla.

`git reset --hard` -komennolla poistin yhden commitin hetkeksi historiasta ja palautin sen `git reflog` -komennon avulla.

`git cherry-pick` -komennolla siirsin yhden commitin toisesta haarasta main-haaraan.

Harjoittelin myös `git rebase` -komentoa siirtämällä feature-haaran uusimman main-haaran päälle ennen yhdistämistä.

Projektissa tehtiin myös tarkoituksella merge-konflikti. Konflikti syntyi, kun samoja tervehdysrivejä muutettiin eri tavalla kahdessa haarassa. Ratkaisin konfliktin muokkaamalla tiedoston haluttuun muotoon ja jatkamalla mergeä.

Lisäksi lisäsin `.gitignore`-tiedoston, jolla `debug.log` jätetään versionhallinnan ulkopuolelle.

## Mitä opin

Projektin aikana Gitin peruskäyttö alkoi tuntua huomattavasti selkeämmältä. Varsinkin working directoryn, staging-alueen ja commitin välinen ero tuli paremmin ymmärrettyä.

Aikaisemmin esimerkiksi rebase, cherry-pick ja reflog olivat aika epäselviä, mutta niiden käyttäminen käytännössä auttoi ymmärtämään mitä ne oikeasti tekevät.

Merge-konfliktin ratkaiseminen oli myös hyödyllinen harjoitus, koska siinä näki konkreettisesti mitä tapahtuu, kun kahta eri versiota samasta tiedostosta yritetään yhdistää.
