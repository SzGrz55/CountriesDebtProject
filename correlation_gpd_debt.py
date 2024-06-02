"""
KORELACJA
Ta część programu odpowiada za obliczenie korelacji Pearsona pomiędzy kolejno: długiem prywatnym i dynamiką wzrostu PKB, oraz długiem publicznym i dynamiką wzrostu PKB.
Otrzymane wyniki zostaną wypisane w konsoli (następnie zostaną również umieszczone w ramach legend wykresów).
"""
def correlation(public_debt, gdp_growth, gdp, private_debt):
    # Korelacja między długiem prywatnym a dynamiką wzrostu PKB
    correlation_private_gdp = private_debt['value'].corr(gdp_growth['value']) #obliczenie korelacji Pearsona i zapisanie do zmiennej correlation_private_gdp

    # Korelacja między długiem publicznym a dynamiką wzrostu PKB
    correlation_public_gdp = public_debt['value'].corr(gdp_growth['value']) #obliczenie korelacji Pearsona i zapisanie do zmiennej correlation_public_gdp

    # Wypisanie wyników
    print("Korelacja między długiem prywatnym a % wzrostem PKB:", correlation_private_gdp)
    print("Korelacja między długiem publicznym a % wzrostem PKB:", correlation_public_gdp)

    return correlation_private_gdp, correlation_public_gdp #zwrócenie wartości korelacji