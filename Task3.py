import json

def zapisz_do_json(dane, sciezka_pliku):
    try:
        with open(sciezka_pliku, 'w', encoding='utf-8') as plik:
            json.dump(dane, plik, ensure_ascii=False, indent=4)
        print("Dane zostały zapisane do pliku JSON.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")

dane = {
    "imie": "Kamil",
    "nazwisko": "Chybala",
    "wiek": 20,
    "miasto": "Bielsko-Biala"
}


sciezka_pliku = 'sciezka/pliku.json'
zapisz_do_json(dane, sciezka_pliku)
