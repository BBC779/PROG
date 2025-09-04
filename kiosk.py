glass = 20
varmkorv = 15
lask = 15
godis = 10

print("Produkter och priser:")
print("glass - 20 kr")
print("varmkorv - 15 kr")
print("läsk - 15 kr")
print("godis - 10 kr")

produkt = input("Välkommen lilla mannen, vad ska du köpa? ")
antal = int(input("Hur många vill du ha? "))

if produkt == "glass":
    pris = 20
elif produkt == "varmkorv":
    pris = 15
elif produkt == "läsk":
    pris = 15
elif produkt == "godis":
    pris = 10
else:
    pris = 0

total = pris * antal

if pris > 0:
    print("Det kommer att kosta", total, "kr lillis.")
else:
    print("Den produkten finns inte hära lilgrabben.")