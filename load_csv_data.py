import pandas as pd #import biblioteki pandas do obsługi danych tabelarycznych

"""
POBRANIE DANYCH
Ta część programu odpowiada za pobranie potrzebnych danych, argument 'country' to kraj wybrany przez użytkownika. Dane pochodzą ze strony Banku Światowego oraz FRED. 
"""
def load_data(country):
    # Pobranie danych o długu publicznym
    public_debt = pd.read_csv(f'data/{country}/public_debt.csv', parse_dates=['year'], index_col='year') #wczytanie danych, wskazanie na kolumnę 'rok' jako daty i indeks danych

    # Pobranie danych o dynamice wzrostu PKB
    gdp_growth = pd.read_csv(f'data/{country}/gdp_growth.csv', parse_dates=['year'], index_col='year') #wczytanie danych, wskazanie na kolumnę 'rok' jako daty i indeks danych

    # Pobranie danych o poziomie PKB
    gdp = pd.read_csv(f'data/{country}/gdp.csv', parse_dates=['year'], index_col='year') #wczytanie danych, wskazanie na kolumnę 'rok' jako daty i indeks danych

    # Pobranie danych o poziomie długu prywatnego
    private_debt = pd.read_csv(f'data/{country}/private_debt.csv', parse_dates=['year'], index_col='year') #wczytanie danych, wskazanie na kolumnę 'rok' jako daty i indeks

    return public_debt, gdp_growth, gdp, private_debt #zwrócenie zmiennych otrzymanych po wczytaniu plików