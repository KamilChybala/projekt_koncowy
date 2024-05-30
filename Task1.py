import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='Narzędzie do konwersji danych')
    parser.add_argument('input_file', type=str, help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', type=str, help='Ścieżka do pliku wyjściowego')
    args = parser.parse_args()
    return args.input_file, args.output_file

if __name__ == "__main__":
    input_file, output_file = parse_args()
    print(f'Plik wejściowy: {input_file}, Plik wyjściowy: {output_file}')
