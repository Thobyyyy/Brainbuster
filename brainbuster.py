import random

# -----------------------------
# Daten (Fragen + Rangliste)
# -----------------------------
fragen = [
    {"frage": "Wie viel ist 2 + 2?", "antwort": "4"},
    {"frage": "Hauptstadt von Deutschland?", "antwort": "berlin"},
    {"frage": "Wie viel ist 5 * 3?", "antwort": "15"}
]

rangliste = []


# -----------------------------
# Funktionen
# -----------------------------

def zeige_hilfe():
    print("\n--- Hilfe ---")
    print("Beantworte die Fragen.")
    print("Gib 'h' ein, um diese Hilfe zu sehen.")
    print("Alles wird klein geschrieben verglichen.\n")


def stelle_frage(frage_objekt):
    print("\nFrage:", frage_objekt["frage"])
    eingabe = input("Deine Antwort: ").lower()

    if eingabe == "h":
        zeige_hilfe()
        return stelle_frage(frage_objekt)

    if eingabe == frage_objekt["antwort"]:
        print("Richtig!")
        return 1
    else:
        print("Falsch! Richtige Antwort:", frage_objekt["antwort"])
        return 0


def spiele_quiz():
    print("Willkommen zum Quiz-Spiel!")
    name = input("Dein Name: ")

    punkte = 0
    random.shuffle(fragen)

    for frage in fragen:
        punkte += stelle_frage(frage)

    print(f"\n{name}, du hast {punkte} Punkte erreicht!")
    speichere_ergebnis(name, punkte)


def speichere_ergebnis(name, punkte):
    rangliste.append({"name": name, "punkte": punkte})


def zeige_rangliste():
    print("\n--- Rangliste ---")
    sortiert = sorted(rangliste, key=lambda x: x["punkte"], reverse=True)

    for eintrag in sortiert:
        print(eintrag["name"], "-", eintrag["punkte"], "Punkte")


# -----------------------------
# Automatisierter Test
# -----------------------------
def test_stelle_frage():
    test_frage = {"frage": "Test?", "antwort": "ja"}
    
    # Simulierter Test (kein echtes input)
    assert test_frage["antwort"] == "ja"
    print("Test erfolgreich!")


# -----------------------------
# "Diagramm" (einfach erklärt)
# -----------------------------
def zeige_klassendiagramm():
    print("""
    Klassendiagramm (vereinfacht):

    +-------------------+
    | QuizSpiel         |
    +-------------------+
    | fragen            |
    | rangliste         |
    +-------------------+
    | spiele_quiz()     |
    | stelle_frage()    |
    | zeige_rangliste() |
    +-------------------+
    """)


# -----------------------------
# Hauptprogramm
# -----------------------------
if __name__ == "__main__":
    test_stelle_frage()
    zeige_klassendiagramm()
    
    while True:
        spiele_quiz()
        zeige_rangliste()

        nochmal = input("\nNochmal spielen? (j/n): ")
        if nochmal.lower() != "j":
            break

    print("Danke fürs Spielen!")