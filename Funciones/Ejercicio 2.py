# Determinar si año es bisiesto o no

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    # Devuelve True por años bisiestos.
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

    # Tambien se puede retornar todo en una linea asi:
    # return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    # Retorna numero de dias en ese mes de ese año.

    if not 1 <= month <= 12:
        return "Invalid Month"

    elif month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month]


print(days_in_month(2020, 2))
