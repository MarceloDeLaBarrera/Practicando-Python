def six_digits(n):
    cm = n//100000
    dm = n % 100000 // 10000
    m = n % 10000 // 1000
    c = n % 1000 // 100
    d = n % 100 // 10
    u = n % 10
    print(cm)
    print(dm)
    print(m)
    print(c)
    print(d)
    print(u)
    return cm+dm+m+c+d+u


print(six_digits(293721))


def five_digits(n):
    dm = n//10000
    m = n % 10000 // 1000
    c = n % 1000 // 100
    d = n % 100 // 10
    u = n % 10
    print(dm)
    print(m)
    print(c)
    print(d)
    print(u)
    return m+c+d+u+dm


# print(five_digits(29372))


def four_digits(n):
    m = n // 1000
    c = n % 1000 // 100
    d = n % 100 // 10
    u = n % 10
    print(m)
    print(c)
    print(d)
    print(u)
    return m+c+d+u


# print(four_digits(9874))

def three_digits(n):
    c = n//100
    m = n % 100 // 10
    x = n % 10
    print(c)
    print(m)
    print(x)
    return c+m+x

# print(three_digits(234))


def two_digits(n):
    m = n//10
    x = n % 10
    return m + x


# print(two_digits(28))

def suma(n):
    sum = 0
    for i in str(n)[::-1]:
        sum += int(i)
    return sum


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


print(suma(5432342))
