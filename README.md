# JSD-Tim7 - jsd za kreiranje recepata

<img src="https://marketplace.canva.com/EAFNsV8XtFc/1/0/1067w/canva-white-modern-recipe-card-g0ij-n11PwM.jpg" width="400" height="550"/>

Recipe DSL je projekat u kojem ćemo razviti jezik specifičan za domen koji omogućava jednostavno kreiranje kulinarskih recepata i pritom pruža standardizovan format za njihovo definisanje. Njegov cilj je digitalizacija postojećih recepata u pisanom formatu. Prednost kod korišćenja ovog jezika naspram klasične web aplikacije jeste brzina i jednostavnost kod generisanja recepata. Kada korisnik izgeneriše jedan recept, za svaki naredni će samo morati da izmeni vrednosti na ulazu, što je brže nego odraditi to isto putem korisničkog interfejsa. Pored toga, preglednije je unošenje novih recepata, jer se svi nalaze u istom fajlu, pa se lako može videti šta se nalazi u nekom od prethodnih recepata. Takođe, korisnik može dosta brže da unese više recepata odjednom. Naš jezik ima strukturu sličnu ručno napisanim receptima (na papiru), te omogućava intuitivniju digitalizaciju.

Izlaz programa je generisana HTML/PDF stranica sa receptom. 

## Uputstvo za pokretanje
Projekat se može instalirati u virtualno okruženje na sledeći način:

```
python -m venv venv
source venv/bin/activate
pip install git+https://github.com/Munja200/JSD-Tim7.git
```

Nakon toga aplikacija se može pokrenuti uz pomoć komande ```rcp-run [putanja .rcp datoteke]```, ili samo putem komande ```rcp-run```, u tom slučaju će se izgenerisati recept na osnovu ugrađenog primera.

## Koraci u definisanju

* Definisanje osnovnih informacija - ime recepta, opis vrste jela, vreme pripreme...
* Lista sastojaka - nabrajanje liste sastojaka sa količinom
* Uputstva za spremanje - opisuju se koraci za pripremanje jela sa navedenim sastojcima
* Nutritivne vrednosti - opciono se mogu navesti nutritivne vrednosti sastojaka
* Saveti - mogu se podeliti saveti i varijacije za unapređenje recepta
* Alergeni

## Primer
```
Namirnice: 
  Ime namirnice: Banane;
  Nutritivna vrednost: 5 kcal na 1 KG;

  Ime namirnice: Brašno;
  Nutritivna vrednost: 30 kcal na 100 G;
  Alergeni: 
    1. Gluten;

Recepti:
  Ime: Banana hleb;
  URL do slike jela: "https://marketplace.canva.com/EAFNsV8XtFc/1/0/1067w/canva-white-modern-recipe-card-g0ij-n11PwM.jpg";
  Opis jela: pecivo sa bananom;
  Vrsta jela: Pecivo;
  Vreme pripreme: 0:30;
  Lista sastojaka:
    1. banane, 1 KG;
    2. brašno, 500 g;

  Uputstvo za spremanje:
    1. Izmiksati banane;
    2. Pomešati sa brašnom;
    3. Ispeći;
  
  Saveti: 
    1. Operi posudje pre spremanja;

```
