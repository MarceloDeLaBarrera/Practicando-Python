def prefix_herarchy(list, query):
    number_of_coincidences = []
    counter = 0

    for i in range(len(query)):
        counter = 0
        for j in range(len(list)):
            if list[j].lower().startswith(query[i].lower()):
                if list[j].lower() != query[i].lower():
                    counter += 1
        number_of_coincidences.append(counter)

    return number_of_coincidences


print(prefix_herarchy(["Martin", "Pedro", "Maria",
      "Martina", "Marina", "Mongo", "mariano", "marTiTa"], ["Mart", "Mar", "Mong"]))


def count_word(array, word):
    number_of_coincidences = 0
    length = len(array)

    for i in array:
        if word.lower() == i.lower():
            number_of_coincidences += 1

    return number_of_coincidences, length


print(count_word(["perro", "gato", "mama", "perro", "perro"], "PerRo"))
print(count_word(["ab", "a"], "a"))
