import yaml

def wczytaj_yml(sciezka_do_pliku):
    try:
        with open(sciezka_do_pliku, 'r', encoding='utf-8') as plik:
            dane = yaml.safe_load(plik)
        print("Plik YAML został poprawnie wczytany.")
        return dane
    except yaml.YAMLError as e:
        print(f"Błąd dekodowania YAML: {e}")
    except FileNotFoundError as e:
        print(f"Plik nie został znaleziony: {e}")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

sciezka_pliku = 'sciezka/pliku.yml'
dane = wczytaj_yml(sciezka_pliku)
if dane:
    print("Dane:", dane)
