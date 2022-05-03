def palindromo(word):
    word = word.lower()
    if "".join(word.split()) == "".join(word.split())[::-1]:
        print("Es un palindromo")
        print("".join(word.split()))
    else:
        print("No es un palindromo")

# split separa en lista cada palabra y .join une todas las palabras quitando los espacios, al unir sin especificar un caracter de union.


palindromo("Isaac no ronca asi")
palindromo("No Traces en Ese Carton")
palindromo("chupala")
