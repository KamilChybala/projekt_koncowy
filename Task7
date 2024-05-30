import xml.etree.ElementTree as ET

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
