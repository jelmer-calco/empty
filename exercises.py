"""
Python vervolgopdrachten - van basis naar verdieping

Deze opdrachten bouwen verder op:
- variabelen
- strings
- arithmetic
- lists
- dictionaries
- if-statements
- loops
- functiess

Onderwerpen in volgorde:
1) Input en interactie
2) Meer met strings
3) Lists en dictionaries combineren
4) While-loops
5) Functies serieuzer gebruiken
6) Fouten herkennen en voorkomen
7) Tekstbestanden lezen en schrijven
8) Eenvoudige algoritmes op tekst

Werkwijze:
1. Lees per onderdeel eerst de theorie in de comments.
2. Maak daarna de opdracht.
3. Run het bestand regelmatig en test met verschillende inputs.
4. Vul alleen de TODO's in. Laat de rest staan.

Tip:
Gebruik print() om tussendoor te controleren wat je code doet.
"""
print (f"exercises.py is running ")


# ============================================================
# 1) Input en interactie
# ============================================================
"""
Theorie (kort)
Met input() kun je de gebruiker iets laten typen.
Wat een gebruiker invoert, wordt standaard opgeslagen als tekst (string).

Voorbeeld:
naam = input("Wat is je naam? ")
print(f"Hallo {naam}")

Opdracht 1
Vraag de gebruiker om:
- naam
- leeftijd

Print daarna:
- een begroeting
- of iemand volwassen is (18 of ouder) of niet

Ondersteuning
- Gebruik input() voor naam en leeftijd
- Let op: leeftijd moet je omzetten naar een int
- Gebruik if / else

Hints
- leeftijd = int(input("Hoe oud ben je? "))
- if leeftijd >= 18:
"""

def opdracht_1():
    print("\n--- Opdracht 1: Input en interactie ---")

    # TODO: vraag om naam
    naam = ""

    # TODO: vraag om leeftijd en zet om naar int
    leeftijd = 0

    # TODO: print een begroeting
    # TODO: print of iemand volwassen is of niet
    pass


# ============================================================
# 2) Meer met strings
# ============================================================
"""
Theorie (kort)
Strings kun je bewerken met handige functies:
- .lower()  -> alles naar kleine letters
- .upper()  -> alles naar hoofdletters
- .replace() -> vervangt tekst
- .split() -> maakt van een zin een list met woorden
- .strip() -> haalt spaties aan het begin en einde weg

Opdracht 2
Gebruik de string hieronder en doe het volgende:
- maak alles lowercase
- vervang alle komma's en punten door niets
- split de tekst in losse woorden
- print het aantal woorden

Ondersteuning
Werk stap voor stap:
1. begin met de originele tekst
2. maak de tekst lowercase
3. haal leestekens weg
4. gebruik split()

Hints
- tekst = tekst.lower()
- tekst = tekst.replace(",", "")
- woorden = tekst.split()
- len(woorden)
"""

def opdracht_2():
    print("\n--- Opdracht 2: Meer met strings ---")

    tekst = "Python is Leuk, krachtig en flexibel. Python is ook populair."

    # TODO: maak lowercase
    # TODO: verwijder komma's en punten
    # TODO: split de tekst in woorden
    woorden = []

    # TODO: print de woordenlijst
    # TODO: print het aantal woorden
    pass


# ============================================================
# 3) Lists en dictionaries combineren
# ============================================================
"""
Theorie (kort)
Een list gebruik je voor een rij waarden.
Een dictionary gebruik je voor key-value pairs.

Je kunt bijvoorbeeld twee lists combineren tot één dictionary.

Voorbeeld:
namen = ["anna", "bas", "carlos"]
scores = [8, 6, 9]

resultaat = {}
for naam, score in zip(namen, scores):
    resultaat[naam] = score

Opdracht 3
Gebruik de lists hieronder en maak een dictionary met:
- naam als key
- cijfer als value

Print daarna voor elke student:
- de naam
- het cijfer

Ondersteuning
- Gebruik zip()
- Gebruik een lege dictionary
- Loop daarna met .items() door de dictionary

Hints
- for naam, cijfer in zip(namen, cijfers):
- resultaten[naam] = cijfer
- for naam, cijfer in resultaten.items():
"""

def opdracht_3():
    print("\n--- Opdracht 3: Lists en dictionaries combineren ---")

    namen = ["Alice", "Bob", "Charlie", "Dylan"]
    cijfers = [8, 5, 7, 9]

    resultaten = {}

    # TODO: vul de dictionary
    # TODO: print alle naam-cijfer paren
    pass


# ============================================================
# 4) While-loops
# ============================================================
"""
Theorie (kort)
Een while-loop blijft doorgaan zolang een voorwaarde waar is.
Dat is handig als je niet weet hoe vaak iets moet herhalen.

Opdracht 4
Maak een programma dat:
- steeds een woord vraagt aan de gebruiker
- elk woord opslaat in een list
- stopt als de gebruiker 'stop' typt
- daarna alle ingevoerde woorden print

Belangrijk
- Het woord 'stop' mag niet in de list komen

Ondersteuning
- Begin met een lege list
- Gebruik een while-loop
- Voeg woorden toe met .append()

Hints
- woorden = []
- invoer = ""
- while invoer != "stop":
- if invoer != "stop":
"""

def opdracht_4():
    print("\n--- Opdracht 4: While-loops ---")

    # TODO: maak een lege list
    woorden = []

    # TODO: maak een variabele voor invoer
    invoer = ""

    # TODO: vraag steeds om een woord totdat iemand 'stop' typt
    while invoer != "stop":
        pass

    print("\nIngevoerde woorden:")
    # TODO: print alle woorden met een for-loop
    pass


# ============================================================
# 5) Functies serieuzer gebruiken
# ============================================================
"""
Theorie (kort)
Functies helpen je om code op te delen in kleine, herbruikbare stukken.
Een goede functie doet meestal één duidelijke taak.

Opdracht 5
Maak twee functies:
1. clean_text(tekst)
   - maakt tekst lowercase
   - verwijdert komma's en punten
   - returnt de opgeschoonde tekst

2. count_words(tekst)
   - split de tekst in woorden
   - returnt het aantal woorden

Test je functies met de tekst hieronder.

Ondersteuning
- Gebruik return
- Roep de functies daarna aan
- Print de resultaten

Hints
- def clean_text(tekst):
- return tekst
- def count_words(tekst):
- woorden = tekst.split()
- return len(woorden)
"""

def clean_text(tekst):
    # TODO: maak lowercase
    # TODO: verwijder komma's en punten
    return tekst

def count_words(tekst):
    # TODO: split tekst in woorden
    # TODO: return het aantal woorden
    return 0

def opdracht_5():
    print("\n--- Opdracht 5: Functies serieuzer gebruiken ---")

    tekst = "Vandaag regent het. Morgen misschien ook, maar hopelijk niet."

    # TODO: gebruik clean_text
    # TODO: gebruik count_words
    # TODO: print de uitkomsten
    pass


# ============================================================
# 6) Fouten herkennen en voorkomen
# ============================================================
"""
Theorie (kort)
Gebruikers voeren niet altijd geldige input in.
Met try / except kun je voorkomen dat je programma crasht.

Voorbeeld:
try:
    getal = int(input("Geef een getal: "))
except:
    print("Dat was geen geldig getal.")

Opdracht 6
Vraag de gebruiker om een getal.
- Als het lukt: print het dubbele van dat getal
- Als het niet lukt: print een foutmelding

Ondersteuning
- Gebruik try / except
- Zet input om naar int

Hints
- try:
- except:
"""

def opdracht_6():
    print("\n--- Opdracht 6: Fouten herkennen en voorkomen ---")

    # TODO: vraag om een getal met input
    # TODO: gebruik try / except
    # TODO: print het dubbele of een foutmelding
    pass


# ============================================================
# 7) Tekstbestanden lezen en schrijven
# ============================================================
"""
Theorie (kort)
Met open() kun je bestanden lezen en schrijven.

Lezen:
with open("voorbeeld.txt", "r") as bestand:
    inhoud = bestand.read()

Schrijven:
with open("uitkomst.txt", "w") as bestand:
    bestand.write("Hallo")

Opdracht 7
Doe het volgende:
1. Maak een tekstbestand met de naam input_tekst.txt
2. Schrijf daar zelf een korte zin in
3. Lees daarna de inhoud van het bestand
4. Print de inhoud
5. Schrijf diezelfde inhoud in hoofdletters naar output_tekst.txt

Ondersteuning
- Gebruik "w" om te schrijven
- Gebruik "r" om te lezen
- Gebruik .upper() voor hoofdletters

Hints
- with open("input_tekst.txt", "w", encoding="utf-8") as bestand:
- with open("input_tekst.txt", "r", encoding="utf-8") as bestand:
"""

def opdracht_7():
    print("\n--- Opdracht 7: Tekstbestanden lezen en schrijven ---")

    # TODO: schrijf een korte zin naar input_tekst.txt
    # TODO: lees de inhoud van input_tekst.txt
    inhoud = ""

    # TODO: print de inhoud
    # TODO: schrijf de inhoud in hoofdletters naar output_tekst.txt
    pass


# ============================================================
# 8) Eenvoudige algoritmes op tekst
# ============================================================
"""
Theorie (kort)
Een simpel algoritme op tekst is bijvoorbeeld:
- tekst opschonen
- woorden splitsen
- tellen hoe vaak elk woord voorkomt

Dat lijkt al op de basis van tekstanalyse en taalmodellen.

Opdracht 8
Gebruik de tekst hieronder en maak een dictionary waarin:
- elk woord een key is
- de value aangeeft hoe vaak dat woord voorkomt

Print daarna:
- de hele dictionary
- het woord dat het vaakst voorkomt
- hoe vaak dat woord voorkomt

Ondersteuning
Werk in stappen:
1. maak de tekst lowercase
2. verwijder punten en komma's
3. split de tekst in woorden
4. tel elk woord in een dictionary

Hints
- if woord in telling:
      telling[woord] += 1
  else:
      telling[woord] = 1

Extra hint
Je kunt daarna met een loop zoeken naar het hoogste aantal.
"""

def opdracht_8():
    print("\n--- Opdracht 8: Eenvoudige algoritmes op tekst ---")

    tekst = "de kat slaapt, de hond blaft. de kat rent en de hond rent."

    # TODO: schoon de tekst op
    # TODO: split de tekst in woorden
    woorden = []

    telling = {}

    # TODO: tel hoe vaak elk woord voorkomt

    # TODO: zoek het woord met de hoogste frequentie
    meest_voorkomend_woord = ""
    hoogste_aantal = 0

    # TODO: print de dictionary
    # TODO: print het meest voorkomende woord en het aantal
    pass


# ============================================================
# UITVOEREN
# ============================================================
"""
Haal het # weg bij de opdracht die je wilt testen.
Werk van boven naar beneden.
"""

# opdracht_1()
# opdracht_2()
# opdracht_3()
# opdracht_4()
# opdracht_5()
# opdracht_6()
# opdracht_7()
# opdracht_8()
