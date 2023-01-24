import json

# json.dumps permite convertir un objeto en formato json.
# json.loads permite convertir un archivo o data json en formato python/diccionario.
# json.load permite recuperar info de un archivo.
# json.dump permite enviar info hacia un archivo.

diccionario = {
    "Personas": [
        {
            "Nombre": "Juan",
            "Edad": 24
        },
        {
            "Nombre": "Pedro",
            "Edad": 45
        }
    ]
}

string = "Mi mama me mima"

# Carga de diccionario a archivo Json. Forma1 (modo write):
with open("Prueba1_IntroUso_JsonconPython.json", "w") as archivo:
    json.dump(diccionario, archivo, indent=2)

# Leer desde archivo json. (Modo read)
with open("Prueba1_IntroUso_JsonconPython.json", "r") as archivo:
    datos = json.load(archivo)
print(type(datos))

for persona in datos["Personas"]:
    print(persona["Nombre"])

from datetime import datetime

date= '19-02-2022'

try:
    data_object= datetime.strptime(date, "%d-%m-%Y")
    print('es valida')
    data_string = datetime.strftime(data_object, "%Y-%m-%d")
    print(data_string)
except ValueError:
    print('no lo es')


import re
dictionary = {'blabla1': 123, 'blabla32': 1232, 'ashjhdask': 12312, 'blabla': 4343}

empty_list = []
for key,value in dictionary.items():
    if 'blabla' in key:
        empty_list.append(key)

print(int(''.join(filter(str.isdigit, 'test3246'))))
for i in empty_list:
    # if filter(str.isdigit, i):
    #     bankID = int(''.join(filter(str.isdigit, i)))
    #     print(bankID)
    bankID= ''.join(re.findall('\d+', i))
    if bankID is not '':
        print(int(bankID))


sf_account = {

        'Numero_Cuenta_Bancaria1__c': 'pepe_123',
        'Nombre_Banco1__c': '6872168',
        'Tipo_de_cuenta_1__c': '42342',
        'CCI_1__c': '423423',


        'Numero_Cuenta_Bancaria3__c': 'pepe_323',
        'Nombre_Banco3__c': '6872168',
        'Tipo_de_cuenta_3__c': '42342',
        'CCI_3__c': '423423',


        'Numero_Cuenta_Bancaria5__c': '12312',
        'Nombre_Banco5__c': 'dasdas',
        'Tipo_de_cuenta_5__c': '12312',
        'CCI_5__c': '423423',


        'Numero_Cuenta_Bancaria2__c': 'dsadas',
        'Nombre_Banco2__c': 'dadsa',
        'Tipo_de_cuenta_2__c': 'dsadasdas',
        'CCI_2__c': '43432',


        'Numero_Cuenta_Bancaria20__c': None,
        'Nombre_Banco20__c': None,
        'Tipo_de_cuenta_20__c': None,
        'CCI_20__c': None,


        'Numero_Cuenta_Bancaria15__c': 'pepe_123',
        'Nombre_Banco15__c': '6872168',
        'Tipo_de_cuenta_15__c': '42342',
        'CCI_15__c': '423423',

}

nueva_lista = []
for key, value in sf_account.items():
        if 'Nombre_Banco' in key:
            bankID = ''.join(re.findall('\d+', key))
            if bankID is not '':
                bankID = int(bankID)
                nueva_lista.append(
                {   'registerID': bankID,
                    'account_number': sf_account[f'Numero_Cuenta_Bancaria{bankID}__c'],
                    'bank_name': value,
                    'account_type': sf_account[f'Tipo_de_cuenta_{bankID}__c'],
                    'cci': sf_account[f'CCI_{bankID}__c'],
                }
                )

print(nueva_lista)

values= ['account_number', 'bank_name', 'account_type', 'cci']
for i in range(len(nueva_lista)):
    lista = list(nueva_lista[i].values())
    print(lista)
    del lista[0]
    print(lista)
    if lista.count(None) == len(lista):
        print(nueva_lista[i]['registerID'],'blabla')
    else:
        print(nueva_lista[i].values())

# def equal_dicts(d1, d2, ignore_keys):
#     ignored = set(ignore_keys)
#     for k1, v1 in d1.items():
#         if k1 not in ignored and (k1 not in d2 or d2[k1] != v1):
#             return False
#     for k2, v2 in d2.items():
#         if k2 not in ignored and k2 not in d1:
#             return False
#     return True

# other_dict= {
#     'account_number': 'pepe_123',
#     'bank_name': '6872168',
#     'account_type': '42342',
#     'cci': '423423',
# }

# print(other_dict)
# print(nueva_lista[0])
# print(equal_dicts(nueva_lista[0], other_dict, ['registerID']))

import datetime as dt
date = dt.datetime.strftime(dt.date.today(),"%d-%m-%Y")
date = dt.datetime.strptime(date, "%d-%m-%Y").date()
print(type(date))

new_date= dt.datetime.strptime(
    dt.datetime.strftime(
        dt.date.today(),"%d-%m-%Y"
    ),
    "%d-%m-%Y"
).date()

print(new_date)

def function0():
    amount="1234"
    function1(amount=amount)
    print(amount, type(amount))
    print("Blabalbla")

def function1(amount):
    boolean= False
    amount = int(amount)
    return boolean

print(function0())

dictionaryy = {'pepe': 'pepito', 'ramon': 'ramoncito'}
dict_json = json.dumps(dictionaryy)
print(dictionaryy)
print(dict_json)
