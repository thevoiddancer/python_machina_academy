def dodaj_1(broj):
    return broj + 1

def dodaj_2(broj: int) -> int:
    return broj + 1

print(dodaj_2(7))
print(dodaj_2('7'))
