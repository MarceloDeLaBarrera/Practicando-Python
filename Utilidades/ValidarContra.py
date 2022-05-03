import string

contraseña = "chu4palaqA,d"


def validador(contra):
    if 6 < len(contra) < 12:
        if any([c.isdigit() for c in contra]):
            if any([c.islower() for c in contra]):
                if any([c.isupper() for c in contra]):
                    if any([True if c in string.punctuation else False for c in contra]):
                        print("Contraseña establecida correctamernte")

                    else:
                        print("La contraseña debe tener algun caracter especial")
                else:
                    print("La contraseña debe contener al menos una mayuscula")
            else:
                print("La contraseña debe contener al menos una minuscula")
        else:
            print("La contraseña debe contener al menos un numero")
    else:
        print("La contraseña debe tener un largo entre 6 y 12 caracteres")


def validador2(contra):
    if 6 > len(contra) > 12:
        print("La contraseña debe tener un largo entre 6 y 12 caracteres")
    elif not any([c.isdigit() for c in contra]):
        print("La contraseña debe contener al menos un numero")
    elif not any([c.islower() for c in contra]):
        print("La contraseña debe contener al menos una minuscula")
    elif not any([c.isupper() for c in contra]):
        print("La contraseña debe contener al menos una mayuscula")
    elif not any([True if c in string.punctuation else False for c in contra]):
        print("La contraseña debe tener algun caracter especial")
    else:
        print("Contraseña establecida correctamernte")


validador2(contraseña)
