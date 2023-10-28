while True:
    try:
    
        liczba1str: str = input("Wprowadź liczbę, którą chcesz podzielić: ")
        if liczba1 == "q":
            break
        liczba1: float = float(liczba1str)
        liczba2 = float(input("Wprowadź liczbę, przez którą chcesz podzielić: "))
        # Próba dzielenia i wyświetlenie wyniku
        wynik = liczba1 / liczba2
        print(f"Wynik: {wynik}")
        break
    except ZeroDivisionError:
        print("Błąd: Nie można dzielić przez zero! Spróbuj jeszcze raz.")
    except ValueError:
        print("Błąd: Wprowadzono nieprawidłową wartość! Upewnij się, że wprowadzasz liczby.")
        continue
    except Exception as e:
        print(f"Wystąpił nieoczekiwany błąd: {e}")
    break   
