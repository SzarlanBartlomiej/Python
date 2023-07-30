def generuj_liste_zadan(dane_tabeli):
    # Stwórz listę zadań i opcjonalnie listę priorytetów
    lista_zadan = []
    lista_priorytetow = []
    for zadanie, priorytet in dane_tabeli:
        lista_zadan.append(zadanie)
        if priorytet.isdigit():
            lista_priorytetow.append(int(priorytet))
        else:
            lista_priorytetow.append(0)  # Domyślny priorytet, jeśli nie podano lub nie jest liczbą

    # Sortowanie zadań na podstawie priorytetu (jeśli istnieje)
    if any(lista_priorytetow):
        lista_zadan = [zadanie for _, zadanie in sorted(zip(lista_priorytetow, lista_zadan), reverse=True)]

    return lista_zadan

def dodaj_zadanie(dane_tabeli):
    zadanie = input("Podaj nazwę zadania: ")
    priorytet = input("Podaj priorytet zadania (opcjonalnie): ")

    dane_tabeli.append((zadanie, priorytet))
    return dane_tabeli

# Dane tabeli (zadania i opcjonalnie priorytety)
dane_tabeli = [
    ("Zadanie 1", "3"),
    ("Zadanie 2", "1"),
    ("Zadanie 3", "5"),
    ("Zadanie 4", "2"),
    ("Zadanie 5", "4"),
]

# Przykład użycia funkcji generuj_liste_zadan
lista_zadan = generuj_liste_zadan(dane_tabeli)

# Wyświetlenie listy zadań
print("Lista zadań:")
for i, zadanie in enumerate(lista_zadan, 1):
    print(f"{i}. {zadanie}")

# Dodanie nowego zadania
dane_tabeli = dodaj_zadanie(dane_tabeli)

# Ponowne wygenerowanie listy zadań po dodaniu nowego zadania
lista_zadan = generuj_liste_zadan(dane_tabeli)

# Wyświetlenie zaktualizowanej listy zadań
print("\nZaktualizowana lista zadań:")
for i, zadanie in enumerate(lista_zadan, 1):
    print(f"{i}. {zadanie}")
