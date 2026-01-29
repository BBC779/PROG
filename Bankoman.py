saldo = 1000

print((f"Du har {saldo} kr."))

insättning = int(input("Hur mycket vill du sätta in?"))
saldo += insättning

print(f"Ditt nya saldo är {saldo} kr.")

uttag = int(input("Hur mycket vill du ta ut?"))
saldo -= uttag

print(f"Ditt nyare saldo är {saldo} kr.")