import json

def wczytaj_json(sciezka_do_pliku):
    try:
        with open(sciezka_do_pliku, 'r', encoding='utf-8') as plik:
            dane = json.load(plik)
        print("Plik JSON został poprawnie wczytany.")
        return dane
    except json.JSONDecodeError as e:
        print(f"Błąd dekodowania JSON: {e}")
    except FileNotFoundError as e:
        print(f"Plik nie został znaleziony: {e}")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

sciezka_pliku = 'sciezka/pliku.json'
dane = wczytaj_json(sciezka_pliku)
if dane:
    print("Dane:", dane)
