pip install pyinstaller
pip install pyyaml
pip install xmltodict
import sys
import argparse
import json
import yaml
import xml.etree.ElementTree as ET


def parse_args():
    parser = argparse.ArgumentParser(description='Narzędzie do konwersji danych')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego')
    args = parser.parse_args()
    return args.input_file, args.output_file

if __name__ == "__main__":
    input_file, output_file = parse_args()
    print(f'Plik wejściowy: {input_file}, Plik wyjściowy: {output_file}')

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

def wczytaj_xml(sciezka_pliku):
    try:
        drzewo = ET.parse(sciezka_pliku)
        korzen = drzewo.getroot()
        print("Plik XML został poprawnie wczytany.")
        return korzen
    except ET.ParseError as e:
        print(f"Błąd dekodowania XML: {e}")
    except FileNotFoundError as e:
        print(f"Plik nie został znaleziony: {e}")
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")

sciezka_pliku = 'sciezka/pliku.xml'
korzen = wczytaj_xml(sciezka_pliku)
if korzen is not None:
    print("Korzeń XML:", korzen.tag)

def zapisz_do_xml(dane, sciezka_pliku):
    korzen = ET.Element("root")

    # dodawanie danych do korzenia
    for klucz, wartosc in dane.items():
        element = ET.SubElement(korzen, klucz)
        element.text = str(wartosc)

    # utowrzeie drzewa XML
    drzewo = ET.ElementTree(korzen)

    try:
        with open(sciezka_pliku, 'wb') as plik:
            drzewo.write(plik, encoding='utf-8', xml_declaration=True)
        print("Dane zostały zapisane do pliku XML.")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisywania do pliku: {e}")

dane = {
    "imie": "Kamil",
    "nazwisko": "Chybala",
    "wiek": 20,
    "miasto": "Bielsko-Biala"
}

sciezka_pliku = 'sciezka/pliku.xml'
zapisz_do_xml(dane, sciezka_pliku)
