import yaml

def zapisz_do_yml(dane, sciezka_pliku):
    try:
        with open(sciezka_pliku, 'w', encoding='utf-8') as plik:
            yaml.dump(dane, plik, allow_unicode=True, default_flow_style=False, indent=4)
        print("Dane zostały zapisane do pliku YAML.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")


dane = {
    "imie": "Kamil",
    "nazwisko": "Chybala",
    "wiek": 20,
    "miasto": "Bielsko-Biala"
}


sciezka_pliku = 'sciezka/pliku.yml'
zapisz_do_yml(dane, sciezka_pliku)
