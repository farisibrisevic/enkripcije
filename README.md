# Enkripcija
Probavanje i igranje sa "enkripcijama" u Pythonu. Nijedan od "algoritama" nije zvaničan, niti se koristi u prave svrhe. Cilj ovih kodova jest shvatanje kako algoritmi za enkripciju rade, kako rade ključevi, i učenje nekih od osnovnih kriptografskih načela.

<h2>enkripcija.py: </h2> Glavna svrha ovog koda jeste shvatanje različitih vrsta algoritama enkripcije, kao i shvatanje da što je "miješanje" komplikovanije, komplikovanija je i enkripcija. Unutar ovoga imamo tri stavke: 

- Jednostavna enkripcija: pomjera  ASCII vrijednost za +1. Ako je ASCII vrijednost slova "A" 65, enkriptovana vrijednost će biti 66, odnosno "B". Jednostavan i nesiguran algoritam, na principu Cezarove šifre.
- Komplikovana enkripcija: pomjera ASCII vrijednost za +3, pa od te vrijednosti oduzima 26. Malo sigurnije i složenije, ali i dalje nesigurno obzirom da se koristi fiksno pomjeranje. Brute force lahko može proći kroz ovo.
- Random ekripcija: program sam od sebe generiše neku enkripciju. Što komplikovanija šifra/poruka, kompikovanija enkripcija.


<h2>cesar_sifra.py: </h2> U suštini, kombinacija Cezarove šifre i enkripcije. Korisnik unosi poruku, a zatim unosi neki "ključ" ili "key" za enkripciju. Taj ključ ustvari pomjera slova unaprijed za tu vrijednost. Ako se unese pravilan ključ, ispisat će se pravilna, odnosno ispravna poruka. Ako se ne unese pravilan ključ, ispisat će se neka druga, netačna poruka.
  <h3>cesar_sifra.py (V2): </h3> Omogućena enkripcija simbola ("()=/ itd) i brojeva. Urađen malo bolji "UI", odnosno program više je user-friendly 🙄 (i dalje je u terminalu...)

  <h2>hashiranje.py: </h2> Dobro poznata funkcija. Koristi se SHA-256 algoritam. Svaka hash vrijednost je fiksne dužine i nemoguće ili veoma teško je vratiti u originalnu formu. Cilj hashiranja jeste da i svaka manja promjena u ulaznoj vrijednosti generiše potpuno drugačiju hash vrijednost.
