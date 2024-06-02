import matplotlib.pyplot as plt #import biblioteki matplotlib do tworzenia wykresów

"""
WYKRESY
Ta część programu odpowiada za wykresy kolejno: długu prywatnego, długu publicznego i PKB USA.
Przy wykresach wyświetlone też będą otrzymane wcześniej wartości korelacji.
"""
def plot(public_debt, gdp_growth, gdp, private_debt, correlation_private_gdp, correlation_public_gdp, forecast_private, forecast_public, forecast_gdp):
    # Wyświetlenie wykresów
    fig, axs = plt.subplots(nrows=3, figsize=(15, 10)) #stworzenie trzech wykresów o wymiarach 15 na 10, w trzech wierszach
    fig.suptitle('Wskaźniki gospodarcze') #nadanie tytułu dla całego zestawu wykresów

    # Wykres dla długu prywatnego
    title_private = f"Korelacja długu prywatnego z dynamiką PKB: {correlation_private_gdp:.5f}" #otworzenie zmiennej, która będzie odpowiedzialna za wyświetlenie korelacji w legendzie wykresu
    axs[0].plot(private_debt.index, private_debt, label='Dług prywatny') #wykres dla wartości historycznych długu prywatnego
    axs[0].plot(forecast_private.index, forecast_private, label='Prognoza') #wykres prognozowanych wartości długu prywatnego
    axs[0].legend(title=title_private) #wyświetlenie legendy na wykresie, wraz z utworzoną wcześniej zmienną
    axs[0].set_title('Dług prywatny') #nadanie tytułu dla konkretnego wykresu
    axs[0].set_xlabel('Rok') #nadanie etykiety dla osi X wykresu
    axs[0].set_ylabel('Wartość (w tryliardach USD)') #nadanie etykiety dla osi Y wykresu

    # Wykres dla długu publicznego
    title_public = f"Korelacja długu publicznego z dynamiką PKB: {correlation_public_gdp:.5f}" #utworzenie zmiennej, która będzie odpowiedzialna za wyświetlenie korelacji w legendzie wykresu
    axs[1].plot(public_debt.index, public_debt, label='Dług publiczny') #wykres dla wartości historycznych długu publicznego
    axs[1].plot(forecast_public.index, forecast_public, label='Prognoza') #wykres prognozowanych wartości długu publicznego
    axs[1].legend(title=title_public) #wyświetlenie legendy na wykresie, wraz z utworzoną wcześniej zmienną
    axs[1].set_title('Dług publiczny') #nadannie tytułu dla konkretnego wykresu
    axs[1].set_xlabel('Rok') #nadanie etykiety dla osi X wykresu
    axs[1].set_ylabel('Wartość (w tryliardach USD)') #nadanie etykiety dla osi Y wykresu

    # Wykres dla PKB
    axs[2].plot(gdp.index, gdp, label='PKB') #wykres dla wartości historycznych PKB
    axs[2].plot(forecast_gdp.index, forecast_gdp, label='Prognoza') #wykres prognozowanych wartości PKB
    axs[2].legend() #wyświetlenie legendy na wykresie
    axs[2].set_title('PKB') #nadanie tytułu konkretnemu wykresowi
    axs[2].set_xlabel('Rok') #nadanie etykiety dla osi X wykresu
    axs[2].set_ylabel('Wartość (w tryliardach USD)') #nadanie etkiety dla osi Y wykresu

    plt.tight_layout() #zoptymalizowanie odstępów między wykresami
    plt.show() #wyświetlenie wykresów



