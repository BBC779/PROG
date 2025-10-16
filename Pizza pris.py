
BASE_PRICE = 70

pizza = []

ingredients = [
    ("Tomatsås", 20),
    ("Ost", 25),
    ("Skinka", 15)
]


print("Välkommen till pizzabagaren 4000")
while True:
    print("Vad vill du göra?")
    print("1. Visa Möjliga Ingredienser")
    print("2. Lägga till en ingrediens")
    print("3. Ta bort en ingrediens")
    print("4. Visa Pizza")
    print("5. Räkna ut pris")
    print("q. Stänga av")

    choice = input()

    if choice == "1":
        print(ingredients)

    elif choice == "2":
        print("Vad ska du ha på pizza")
        for i,item in enumerate(ingredients):
            print(i, item[0])

        pos = input()
        pos = int(pos)
        pizza.append(ingredients[pos][0])
        
    elif choice == "3":
        print("Vad ska du ha bort")
        print("Du har", pizza,"på")
        namn = input()
        if namn in pizza:
            pizza.remove(namn)

    elif choice == "4":
        print("Din pizza har", pizza)

    elif choice == "5":
        total = 0
        for ingredient in pizza:
            for ingredients2 in ingredients:
                if ingredient == ingredients2[0]:
                    total += ingredients2[1]

        total += BASE_PRICE
        print("Din totala är", total)

    elif choice == "q":
        print("Stänger...")
        break
    else:
        print("Ogiltigt Svar")
    

    input("\nTryck enter för att fortsätta...")