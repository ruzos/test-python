
print("Podaj kwotę do wypłacenia")
x = input()
x = int(x)
print(x)

banknoty = [10,20,50,100,200, 500]
print(banknoty)
print(type(banknoty))
print(banknoty[0])

banknoty.append(1000)
print(banknoty)
x = banknoty.count(10)
print(x)

banknoty.remove(1000)
print(banknoty)

banknoty = (10,20,50,100,200,500)
print(banknoty)
print(type(banknoty))

person = {"wiek" : 20, "imie":"Ania","nazwisko":"kowalska"}
print(person)
print(type(person))


