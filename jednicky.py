### Spocitej pocet jednicek v zadanem cisle
def pocet_jednicek(cislo):
    pocet = 0
    while cislo >0:
        zbytek = cislo %10
        if zbytek == 1:
            pocet = pocet +1
        cislo = cislo // 10
    return pocet

cislo= int(input('isert numeber:'))
pocet = pocet_jednicek(cislo)

print ("pocet jednicek v cisle {} je {}.".format(cislo,pocet))
