import xml.etree.ElementTree as ET

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
