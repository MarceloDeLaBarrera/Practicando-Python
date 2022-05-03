a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]

# a.sort()
#aordenada= sorted(a)
# print(a)

# for element in a:
#    b.append(element**2)
# print(b)


def comp(a, b):
    if a and b:
        return sorted([i**2 for i in a]) == sorted(b)


print(comp(a, b))
