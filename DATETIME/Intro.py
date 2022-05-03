
import datetime as dt
import calendar as calend

# Fecha Dia actual
today = dt.date.today()
monthday = dt.date.today()
print(today)

# Fecha y hora actual
print(dt.datetime.today())

# Capturar el numero de dia, mes o año de dia actual. weekday= dia de la semana ( 0 a 6).
today.day, today.month, today.year, today.weekday()+1,

# Asignar fecha a una variable YYYY-MM-DD. MES Y DIA SIN ANTEPONER 0 CUANDO ES DEL 1 AL 9.
birthday = dt.date(1992, 8, 8)
print(birthday)

# Cantidad de dias entre dos fechas
days_since_birthday = (today - birthday).days
print(days_since_birthday)


# Almacenar una cantidad de dias determinadas para agregarlos o restarlos a una fecha puntual.
tdelta = dt.timedelta(days=10)
print(today + tdelta)

# Asignar Hora a una variable, formato: Hour,minute,second,microsecond.
print(dt.time(7, 2, 0, 0))

# Almacenar una cantidad de horas determinadas para agregarlos o restarlos a una hora puntual, como ahora.
hour_delta = dt.timedelta(hours=10)
print(dt.datetime.today()+hour_delta)
print(dt.datetime.now()+hour_delta)

# Formatear a string fechas. Si se cambian de minuscula a mayus, cambia formato. strftime--> str f= formating time
print(today.strftime("%B %d, %Y"))
print(dt.datetime.today().strftime("%d/%m/%y   %H:%M:%S"))
print(dt.datetime.strptime("September 27, 2021 06:13:00", "%B %d, %Y %H:%M:%S"))

# Determinar si un año es bisiesto o no.
print(calend.isleap(2020))

# Imprimir todo un calendario de un mes determinado
print(calend.month(2020, 12, 4))
