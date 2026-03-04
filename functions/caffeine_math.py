def caffeine_remaining(dose_mg, hours_since, half_life_h):
    """
    Berechnet den verbleibenden Koffeinwert im Körper.

    Formel:
    Rest = Dosis * 0.5^(Zeit / Halbwertszeit)
    """

    if half_life_h <= 0:
        return 0.0

    return dose_mg * (0.5 ** (hours_since / half_life_h))
