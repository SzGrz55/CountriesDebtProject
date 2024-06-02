import statsmodels.api as sm #import biblioteki statsmodels do modelowania szeregów czasowych

"""
PROGNOZA
Ta część programu służy stworzeniu prognozy długu publicznego, długu prywatnego i PKB, używając metody ARIMA.
Użytkownik programu ma możliwość podania na ile lat ma być stworzona prognoza, aczkolwiek należy pamiętać, że przy dłuższych okresach będzie ona mniej wiarygodna. 
"""
def forecast(public_debt, gdp_growth, gdp, private_debt, step):
    #Ustawienie częstotliwości próbkowania na roczny dla trzech szeregów czasowych
    private_debt.index.freq = 'AS-JAN'
    public_debt.index.freq = 'AS-JAN'
    gdp.index.freq = 'AS-JAN'

    # Modelowanie dla długu prywatnego
    model_private = sm.tsa.ARIMA(private_debt, order=(2, 1, 0), enforce_stationarity=True) #tworzenie modelu szeregu czasowego dla długu prywatnego z użyciem metody ARIMA
    results_private = model_private.fit() #dostosowanie modelu dla danych i obliczenie wyników

    # Prognoza dla długu prywatnego
    forecast_private = results_private.forecast(steps=step) #prognozowanie wartości długu prywatnego na 10 następnych okresów (lat)

    # Modelowanie dla długu publicznego
    model_public = sm.tsa.ARIMA(public_debt, order=(2, 1, 0), enforce_stationarity=False) #tworzenie modelu szeregu czasowego dla długu publicznego z użyciem metody ARIMA
    results_public = model_public.fit() #dostosowanie modelu do danych i obliczenie wyników

    # Prognoza dla długu publicznego
    forecast_public = results_public.forecast(steps=step) #prognozowanie wartości długu publicznego na 10 następnych okresów (lat)

    # Modelowanie dla PKB
    model_gdp = sm.tsa.ARIMA(gdp, order=(2, 1, 0), enforce_stationarity=True) #tworzenie modelu szeregu czasowego dla PKB z użyciem metody ARIMA
    results_gdp = model_gdp.fit() #doposowanie modelu do danych i obliczenie wyników

    # Prognoza dla PKB
    forecast_gdp = results_gdp.forecast(steps=step) #prognozowanie wartości PKB na 10 następnych okresów (lat)

    return forecast_private, forecast_public, forecast_gdp #zwrócenie otrzymanych wartości prognóz
