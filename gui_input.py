import tkinter as tk # import biblioteki tkinter jako tk
from tkinter import ttk # import widżetów tkinter z modułu ttk
from src.forecast_gdp_debt import forecast # import funkcji forecast
from src.load_csv_data import load_data # import funkcji load_data
from src.plot_forecast_correlation import plot # import funkcji plot
from src.correlation_gpd_debt import correlation # import funkcji correlation

"""
Ta część programu odpowiada za interfejs graficzny programu i odczytanie wyboru użytkownika odnośnie kraju oraz długości prognozy. 
Funkcja get_data oprócz przypisania wartości kroku i kraju, wywołuje również funkcje prognozy, korelacji, wczytania danych z plików csv, oraz funkcję rysowania wykresu.
Dzięki temu w pliku main.py wystarczy wyowołać funkcję get_data. 
"""

def get_data():
    if not window.closed and step_entry.get(): # jeśli okno nie jest zamknięte i pole kroku nie jest puste
        step = int(step_entry.get()) # przypisanie wartości z pola kroku do zmiennej step (jako typ int)
        country = country_combobox.get() # przypisanie wartości z pola wyboru kraju do zmiennej country

        public_debt, gdp_growth, gdp, private_debt = load_data(country) # wczytanie danych z plików csv
        forecast_private, forecast_public, forecast_gdp = forecast(public_debt, gdp_growth, gdp, private_debt, step) # prognozowanie PKB, długu publicznego i prywatnego
        correlation_private_gdp, correlation_public_gdp = correlation(public_debt, gdp_growth, gdp, private_debt) # obliczenie wartości korelacji

        # Wywołanie funkcji plot z wynikiem prognoz oraz argumentami wejściowymi
        plot(public_debt, gdp_growth, gdp, private_debt, correlation_private_gdp, correlation_public_gdp, forecast_private, forecast_public, forecast_gdp)
        window.closed = True # ustawienie atrybutu closed po zamknięciu okna na True, ażeby przerwać działanie programu w tle
        window.destroy() # zamknięcie okna


# Tworzenie okna
window = tk.Tk() # utworzenie obiektu reprezentującego okno
window.title("Prognozowanie wskaźników gospodarczych") # nadanie tytułu oknu
window.geometry("300x150") # ustawienie rozmiaru okna na 300x150 pikseli
window.closed = False # ustawienie atrybutu closed na wartość False, co znaczy, że jest otwarte i użytkownik może z niego skorzystać


# Tworzenie etykiety i pola do wpisania wartości kroku
step_label = ttk.Label(window, text="Krok (lata):") # utworzenie etykiety "Krok"
step_label.grid(column=0, row=0, padx=5, pady=5) # umieszczenie etykiety w oknie
step_entry = ttk.Entry(window) # otworzenie pola do wpisania wartości kroku
step_entry.grid(column=1, row=0, padx=5, pady=5) # umieszcznie pola do wpisania wartości kroku, w oknie

# Tworzenie etykiety i pola wyboru kraju
country_label = ttk.Label(window, text="Kraj:") # utworzenie etkiety "Kraj"
country_label.grid(column=0, row=1, padx=5, pady=5) # umieszczenie etykiety w oknie
country_combobox = ttk.Combobox(window, values=["USA", "Japonia", "UK"]) # utworzenie comboboxa do wyboru kraju
country_combobox.current(0) # ustawienie wartości domyślnej na pierwszą opcję (USA)
country_combobox.grid(column=1, row=1, padx=5, pady=5) # umieszczenie comboboxa do wybru kraju, w oknie

# Tworzenie przycisku do uruchomienia programu
run_button = ttk.Button(window, text="Uruchom", command=get_data) # utworzenie przycisku wywołującego funkcję get_data
run_button.grid(column=0, row=2, columnspan=2, padx=5, pady=5) # umieszczenie przycisku w oknie

# Uruchomienie pętli zdarzeń, dzięki której aplikacja będzie działała i reagowała na interakcję użytkownika
window.mainloop()

