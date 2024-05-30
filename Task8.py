import tkinter as tk
from tkinter import messagebox, filedialog
import xml.etree.ElementTree as ET

def zapisz_do_xml(dane, sciezka_do_pliku):
    korzen = ET.Element("root")

    for klucz, wartosc in dane.items():
        element = ET.SubElement(korzen, klucz)
        element.text = str(wartosc)

    drzewo = ET.ElementTree(korzen)

    try:
        with open(sciezka_do_pliku, 'wb') as plik:
            drzewo.write(plik, encoding='utf-8', xml_declaration=True)
        messagebox.showinfo("Sukces", "Dane zostały zapisane do pliku XML.")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd podczas zapisywania do pliku: {e}")

def wczytaj_i_zweryfikuj_xml(sciezka_do_pliku):
    try:
        drzewo = ET.parse(sciezka_do_pliku)
        korzen = drzewo.getroot()
        messagebox.showinfo("Sukces", "Plik XML został poprawnie wczytany.")
        return korzen
    except ET.ParseError as e:
        messagebox.showerror("Błąd dekodowania XML", f"Błąd dekodowania XML: {e}")
    except FileNotFoundError as e:
        messagebox.showerror("Błąd", f"Plik nie został znaleziony: {e}")
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił nieoczekiwany błąd: {e}")
    return None

def zapisz():
    dane = {
        "imie": entry_imie.get(),
        "nazwisko": entry_nazwisko.get(),
        "wiek": entry_wiek.get(),
        "miasto": entry_miasto.get()
    }
    sciezka_do_pliku = filedialog.asksaveasfilename(defaultextension=".xml", filetypes=[("XML files", "*.xml")])
    if sciezka_do_pliku:
        zapisz_do_xml(dane, sciezka_do_pliku)

def wczytaj():
    sciezka_do_pliku = filedialog.askopenfilename(filetypes=[("XML files", "*.xml")])
    if sciezka_do_pliku:
        korzen = wczytaj_i_zweryfikuj_xml(sciezka_do_pliku)
        if korzen is not None:
            entry_imie.delete(0, tk.END)
            entry_nazwisko.delete(0, tk.END)
            entry_wiek.delete(0, tk.END)
            entry_miasto.delete(0, tk.END)

            entry_imie.insert(0, korzen.find('imie').text if korzen.find('imie') is not None else '')
            entry_nazwisko.insert(0, korzen.find('nazwisko').text if korzen.find('nazwisko') is not None else '')
            entry_wiek.insert(0, korzen.find('wiek').text if korzen.find('wiek') is not None else '')
            entry_miasto.insert(0, korzen.find('miasto').text if korzen.find('miasto') is not None else '')

root = tk.Tk()
root.title("XML Data Manager")

# Etykiety i pola tekstowe
tk.Label(root, text="Imię:").grid(row=0, column=0)
entry_imie = tk.Entry(root)
entry_imie.grid(row=0, column=1)

tk.Label(root, text="Nazwisko:").grid(row=1, column=0)
entry_nazwisko = tk.Entry(root)
entry_nazwisko.grid(row=1, column=1)

tk.Label(root, text="Wiek:").grid(row=2, column=0)
entry_wiek = tk.Entry(root)
entry_wiek.grid(row=2, column=1)

tk.Label(root, text="Miasto:").grid(row=3, column=0)
entry_miasto = tk.Entry(root)
entry_miasto.grid(row=3, column=1)

tk.Button(root, text="Zapisz do XML", command=zapisz).grid(row=4, column=0)
tk.Button(root, text="Wczytaj z XML", command=wczytaj).grid(row=4, column=1)

root.mainloop()
