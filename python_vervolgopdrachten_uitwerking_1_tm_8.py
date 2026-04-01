"""
UITWERKING - Python vervolgopdrachten 1 t/m 8

Deze uitwerking hoort bij het opdrachtenblad.
Per opdracht vind je:
- een werkende oplossing
- extra uitleg in comments
- dezelfde opbouw als in het opdrachtenblad

Let op:
Bij opdrachten met input() kun je het beste één opdracht tegelijk testen
door onderaan alleen die functie aan te zetten.
"""

# ============================================================
# 1) Input en interactie
# ============================================================
"""
Uitleg
Met input() vraag je iets aan de gebruiker.
De uitkomst van input() is altijd een string.
Daarom moet je leeftijd omzetten naar een int als je ermee wilt rekenen
of vergelijken.

Stap voor stap:
1. Vraag om naam
2. Vraag om leeftijd
3. Zet leeftijd om naar int
4. Print een begroeting
5. Gebruik if / else om te bepalen of iemand volwassen is
"""
print ("test")

def opdracht_1():
    print("\n--- Opdracht 1: Input en interactie ---")

    naam = input("Wat is je naam? ")
    leeftijd = int(input("Hoe oud ben je? "))

    print(f"Hallo {naam}!")

    if leeftijd >= 18:
        print("Je bent volwassen.")
    else:
        print("Je bent nog niet volwassen.")

opdracht_1()


# ============================================================
# 2) Meer met strings
# ============================================================
"""
Uitleg
Hier bewerken we tekst stap voor stap.

Originele tekst:
"Python is Leuk, krachtig en flexibel. Python is ook populair."

We willen:
1. alles lowercase maken
2. komma's en punten verwijderen
3. de tekst splitsen in losse woorden
4. tellen hoeveel woorden er zijn

Waarom?
Dit is een basisvorm van tekstverwerking. Zulke stappen zie je ook terug
in tekstanalyse en eenvoudige taalmodellen.
"""

def opdracht_2():
    print("\n--- Opdracht 2: Meer met strings ---")

    tekst = "Python is Leuk, krachtig en flexibel. Python is ook populair."

    tekst = tekst.lower()
    tekst = tekst.replace(",", "")
    tekst = tekst.replace(".", "")
    woorden = tekst.split()

    print("Woordenlijst:")
    print(woorden)

    print("Aantal woorden:")
    print(len(woorden))


# ============================================================
# 3) Lists en dictionaries combineren
# ============================================================
"""
Uitleg
We hebben twee lists:
- één met namen
- één met cijfers

Met zip() kun je die twee lists tegelijk doorlopen.
Zo kun je een dictionary maken waarin elke naam gekoppeld wordt
aan het juiste cijfer.

Daarna gebruiken we .items() om alle key-value pairs te printen.
"""

def opdracht_3():
    print("\n--- Opdracht 3: Lists en dictionaries combineren ---")

    namen = ["Alice", "Bob", "Charlie", "Dylan"]
    cijfers = [8, 5, 7, 9]

    resultaten = {}

    for naam, cijfer in zip(namen, cijfers):
        resultaten[naam] = cijfer

    print("Resultaten dictionary:")
    print(resultaten)

    print("\nOverzicht:")
    for naam, cijfer in resultaten.items():
        print(f"{naam} heeft een {cijfer}")


# ============================================================
# 4) While-loops
# ============================================================
"""
Uitleg
Een while-loop is handig als je niet weet hoe vaak iets herhaald moet worden.

Hier blijven we woorden vragen totdat de gebruiker 'stop' typt.

Belangrijk:
- 'stop' mag niet in de lijst komen
- daarom controleren we eerst of de invoer niet gelijk is aan 'stop'
- daarna voegen we het pas toe

Na de while-loop printen we alle ingevoerde woorden met een for-loop.
"""

def opdracht_4():
    print("\n--- Opdracht 4: While-loops ---")

    woorden = []
    invoer = ""

    while invoer != "stop":
        invoer = input("Typ een woord (of 'stop' om te stoppen): ")

        if invoer != "stop":
            woorden.append(invoer)

    print("\nIngevoerde woorden:")
    for woord in woorden:
        print(woord)


# ============================================================
# 5) Functies serieuzer gebruiken
# ============================================================
"""
Uitleg
We maken hier twee functies met één duidelijke taak.

1. clean_text(tekst)
   Deze functie maakt tekst lowercase en verwijdert leestekens.

2. count_words(tekst)
   Deze functie splitst tekst in woorden en telt hoeveel woorden er zijn.

Door dit in functies te zetten:
- hoef je code niet te herhalen
- wordt je programma overzichtelijker
- kun je de functies later opnieuw gebruiken
"""

def clean_text(tekst):
    tekst = tekst.lower()
    tekst = tekst.replace(",", "")
    tekst = tekst.replace(".", "")
    return tekst

def count_words(tekst):
    woorden = tekst.split()
    return len(woorden)

def opdracht_5():
    print("\n--- Opdracht 5: Functies serieuzer gebruiken ---")

    tekst = "Vandaag regent het. Morgen misschien ook, maar hopelijk niet."

    opgeschoonde_tekst = clean_text(tekst)
    aantal_woorden = count_words(opgeschoonde_tekst)

    print("Opgeschoonde tekst:")
    print(opgeschoonde_tekst)

    print("Aantal woorden:")
    print(aantal_woorden)


# ============================================================
# 6) Fouten herkennen en voorkomen
# ============================================================
"""
Uitleg
Niet alle gebruikers voeren geldige input in.
Als iemand bijvoorbeeld 'hallo' intypt terwijl jij een getal verwacht,
dan geeft int(...) normaal een fout.

Met try / except kun je dat netjes opvangen.

Werking:
- in try zet je code die fout kan gaan
- in except zet je wat er moet gebeuren als dat misgaat
"""

def opdracht_6():
    print("\n--- Opdracht 6: Fouten herkennen en voorkomen ---")

    try:
        getal = int(input("Geef een getal: "))
        print(f"Het dubbele is: {getal * 2}")
    except:
        print("Fout: je hebt geen geldig geheel getal ingevoerd.")


# ============================================================
# 7) Tekstbestanden lezen en schrijven
# ============================================================
"""
Uitleg
Met bestanden kun je gegevens bewaren buiten je Python-programma.

We doen hier vier dingen:
1. schrijven naar een bestand
2. lezen uit een bestand
3. de inhoud printen
4. de inhoud in hoofdletters opslaan in een nieuw bestand

'with open(...) as bestand:' is de veiligste standaardmanier om
met bestanden te werken.
"""

def opdracht_7():
    print("\n--- Opdracht 7: Tekstbestanden lezen en schrijven ---")

    with open("input_tekst.txt", "w", encoding="utf-8") as bestand:
        bestand.write("Python is handig voor tekstanalyse en automatisering.")

    with open("input_tekst.txt", "r", encoding="utf-8") as bestand:
        inhoud = bestand.read()

    print("Inhoud van input_tekst.txt:")
    print(inhoud)

    with open("output_tekst.txt", "w", encoding="utf-8") as bestand:
        bestand.write(inhoud.upper())

    print("\nDe inhoud is ook opgeslagen in hoofdletters in output_tekst.txt")


# ============================================================
# 8) Eenvoudige algoritmes op tekst
# ============================================================
"""
Uitleg
Dit is een eenvoudige vorm van tekstanalyse.

We doen het in stappen:
1. tekst lowercase maken
2. punten en komma's verwijderen
3. tekst splitsen in woorden
4. tellen hoe vaak elk woord voorkomt
5. zoeken welk woord het vaakst voorkomt

Voor het tellen gebruiken we een dictionary:
- key = woord
- value = aantal keer dat het woord voorkomt

Dat ziet er zo uit:
if woord in telling:
    telling[woord] += 1
else:
    telling[woord] = 1

Daarna zoeken we handmatig het hoogste aantal.
"""

def opdracht_8():
    print("\n--- Opdracht 8: Eenvoudige algoritmes op tekst ---")

    tekst = "de kat slaapt, de hond blaft. de kat rent en de hond rent."

    tekst = tekst.lower()
    tekst = tekst.replace(",", "")
    tekst = tekst.replace(".", "")

    woorden = tekst.split()

    telling = {}

    for woord in woorden:
        if woord in telling:
            telling[woord] += 1
        else:
            telling[woord] = 1

    meest_voorkomend_woord = ""
    hoogste_aantal = 0

    for woord, aantal in telling.items():
        if aantal > hoogste_aantal:
            hoogste_aantal = aantal
            meest_voorkomend_woord = woord

    print("Woordfrequenties:")
    print(telling)

    print("\nMeest voorkomende woord:")
    print(meest_voorkomend_woord)

    print("Aantal keer:")
    print(hoogste_aantal)


# ============================================================
# EXTRA DIDACTISCHE TIPS
# ============================================================
"""
Tips voor leerlingen:
- Test opdrachten met verschillende input
- Voeg extra print() regels toe als je wilt zien wat er tussendoor gebeurt
- Lees foutmeldingen goed; vaak staat daar precies wat er misgaat

Tips voor docenten:
- Laat studenten eerst voorspellen wat code doet vóór ze het runnen
- Laat ze fouten expres maken en uitleggen waarom iets misgaat
- Laat ze bij opdracht 8 eventueel uitbreiden naar:
  - unieke woorden
  - gemiddelde woordlengte
  - alfabetisch printen
"""


# ============================================================
# UITVOEREN
# ============================================================
"""
Haal het # weg bij de opdracht die je wilt testen.
Bij opdrachten met input is het handig er steeds maar één tegelijk te runnen.
"""

# opdracht_1()
# opdracht_2()
# opdracht_3()
# opdracht_4()
# opdracht_5()
# opdracht_6()
# opdracht_7()
# opdracht_8()
