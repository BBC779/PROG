shop = {

}

sales = {

}

print("Välkommen till ikea lagring")
print('Inloggad som Butiksägare')
while True:
    print("Vad vill du göra?")
    print("1. Visa alla varor")
    print("2. Lägg till en ny vara")
    print("3. Ändra priset på vara")
    print("4. Fylla på vara")
    print("5. Sälja en vara")
    print("6. Visa total intäkter")
    print("q. Stänga av")

    choice = input()

    if choice == "1":
        if len(shop) == 0:
            print("Det finns inga produkter i lagret just nu.")
        else:
            print("Namn, Mängd, Pris")
            for name, data in shop.items():
                print(f"{name}\t{data['mängd']}\t{data['pris']}kr")

    elif choice == "2":
        name = input("Vilken vara vill du lägga till? ")
        if name in shop:
            print("Den hära varan finns redan.")
        else:
            price = int(input("Ange pris: "))
            amount = int(input("Ange mängd: "))
            shop[name] = {"pris": price, "mängd": amount}
            print(f"{name} har lagts till!")

    elif choice == "3":
        name = input("Vilken vara vill du ändra priset på? ")
        if name in shop:
            new_price = int(input("Nytt pris: "))
            shop[name]["pris"] = new_price
            print("Priset har uppdaterats!")
        else:
            print("Dena vara finns inte i lagret.")

    elif choice == "4":
        name = input("Vilken vara vill du fylla på? ")
        if name in shop:
            add_amount = int(input("Hur många ska fyllas på? "))
            shop[name]["mängd"] += add_amount
            print("Lagret har uppdaterats!")
        else:
            print("Den hära varan finns inte i butiken.")

    elif choice == "5":
        name = input("Vilken vara vill du sälja? ")
        if name not in shop:
            print("Varan du försöker sälja finns ej i lager.")
        else:
            amount = int(input("Hur många såldes? "))
            if amount > shop[name]["mängd"]:
                print("Det finns ej mängd!")
            else:
                shop[name]["mängd"] -= amount
                revenue = shop[name]["pris"] * amount

                if name not in sales:
                    sales[name] = 0
                sales[name] += revenue

                print(f"Du sålde {amount} st {name}. Intäkt: {revenue}kr")

                if shop[name]["mängd"] == 0:
                    del shop[name]

    elif choice == "6":
        print("Lista över intäkter:")
        total = 0
        for item, money in sales.items():
            print(f"{item}: {money}kr")
            total += money
        print(f"Totala intäkter: {total}kr")

    elif choice == "q":
        print("Avslutar programmet...")
        break

    else:
        print("Error")

    input("Tryck ENTER för att fortsätta...")
