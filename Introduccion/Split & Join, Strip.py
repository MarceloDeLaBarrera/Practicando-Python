from datetime import datetime
import re
# String a splitear/cortar

problems = "I, have, a, big, problem"
print(problems)


# Se corta un string indicando el caracter de corte, y se guarda cada corte dentro de una lista
p = problems.split(", ")
print(p)

# Sintaxis para unir los elementos de una lista en un string. Lo que va entre comillas seria el "como" se uniran
joined = "-".join(p)
print(joined)

# Strip elimina los caracteres que esten al comienzo y final de la cadena. Ej:
txt = " hola "
print(txt.strip(" "))

dictionary = {}
emptylist = []
lineas = [['juan', 'perez', 12], [
    'ramon', 'canasta', 23], ['jose', 'dominguez', 25]]
num = 0

for i in range(3):
    dictionary['nombre'] = lineas[num][0]
    dictionary['apellido'] = lineas[num][1]
    dictionary['edad'] = lineas[num][2]
    num += 1
    emptylist.append(dictionary.copy())

print(emptylist)

start = ["X0", "X2", "X4"]
string = "EURUSDX2"
start_nemos = [
    "EURUSDX0",
    "EURUSDX2",
    "EURUSDX4",
    "USDCLPX0",
    "USDCLPX2",
    "USDCLPX4",
    "USDJPYX0",
    "USDJPYX2",
    "USDJPYX4",
]

print(string)
string = [
    string.replace(element, "")
    for element in start
    if (element in string)
][0]
print(string)


def filtered_currency(currency, sub_string_options):
    last_two_chars = currency[-2:]

    if last_two_chars in sub_string_options:
        currency = currency.replace(last_two_chars, "")

    return currency


print(filtered_currency("usdX0", start))


def is_ticket_registered_on_sf():
    ticket_message = ""
    tickets = ["'1111111'", "'3232'", "'33333333'",]
    tickets = [
        {
            'ID': 'dsds',
            'Ticket': 'dsdsdsddd',
            'URL': 'dsdsdsdsds'
        },
        {
            'ID': 'dsdasdas',
            'Ticket': '123123',
            'URL': 'dsdsdsdsds'
        },
        {
            'ID': 'dsdasdas',
            'Ticket': '1231244443',
            'URL': 'dsdsdsdsds'
        },
    ]

    for ticket in tickets:
        ticket_message += ticket['Ticket'] + ", "

    return ticket_message


lists = []
print(is_ticket_registered_on_sf())

if lists:
    print("aaaaaa")
else:
    print("bbbbbbbbb")

tickets = [12312, ""]
print(tickets)
# print(", ".join(tickets))

ticketsin = [
    {
        'ID': '312312',
        'Ticket': 32332,
        'URL': 'ddddddddddd'
    },
    {
        'ID': '32312321',
        'Ticket': 244323,
        'URL': 'ffffffff'
    }
]

dictio = {
    'ID': '312312',
    'Ticket': 32332,
    'URL': 'ddddddddddd'
}
new_list = list(dictio.keys())
newew = []
newew += new_list
print(newew)
print("jasjdasjdjas")

tickets = ""
for ticket in ticketsin:
    print(ticket['Ticket'], "ssssssssssssssssss")
    tickets += f"{ticket['Ticket']}, "
print(tickets)
print("aaa")
print(", ".join([str(ticket['Ticket']) for ticket in ticketsin]))


new_text = 'Representante Legal / Beneficiario Final'
new_text = new_text.replace(" ","").lower().replace("representantelegal","representant").replace("beneficiariofinal", "beneficiary").split("/")
print(new_text)


new_text = 'Representante Legal / Beneficiario Final'

# new_text = re.sub("\\s+", "", new_text)
# print(new_text)

new_new = re.sub(r'(representantelegal)|(beneficiariofinal)', lambda x: {'representantelegal': 'representant', 'beneficiariofinal': 'beneficiary'}[x.group(0)], new_text.lower().replace(" ", "")).split("/")
print(new_new)

varNone = "dd"

thisVar = varNone or "pepe"
print(thisVar)



date = '2023-01-04'

inserted_date = datetime.strptime(date, '%Y-%m-%d')
print(inserted_date)
