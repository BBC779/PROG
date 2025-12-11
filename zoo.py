zoo = {
    "Savana": [
        {"art": "Lejon", "namn": "Simba", "Glädje": 50, "Ålder": 5},
        {"art": "Elefant", "namn": "Dumbo", "Glädje": 70, "Ålder": 12}
    ],
    "Regnskog": [
        {"art": "Apa", "namn": "kalle", "Glädje": 60, "Ålder": 7}
    ]
}

while True:
    print("\n1. Visa område")
    print("2. Lägg till djur")
    print("3. Hälsa på djuren")
    print("4. Visa rapport")
    print("5. Avsluta")

    val = input("Välj alternativ: ")

    if val == "1":
        print("Områden:")
        for område in zoo:
            print(område)

        område = input("Välj område: ")

        if område in zoo:
            for djur in zoo[område]:
                print(djur["namn"], djur["art"], "Glädje:", djur["Glädje"], "Ålder:", djur["Ålder"])
        else:
            print("Området finns ej.")

    elif val == "2":
        område = input("Vilket område?: ")

        if område not in zoo:
            zoo[område] = []

        art = input("Art: ")
        namn = input("Namn: ")
        gjädje = int(input("Glädje: "))
        ålder = int(input("Ålder: "))

        zoo[område].append({"art": art, "namn": namn, "Glädje": gjädje, "Ålder": ålder})
        print("Djuret har .")

    elif val == "3":
        print("Områden:")
        for område in zoo:
            print(område)

        område = input("Vart vill du hälsa på: ")

        if område in zoo:
            print("1. Mata\n2. Lek\n3. Städa")
            handling = input("Välj: ")

            if handling in ["1", "2", "3"]:
                for djur in zoo[område]:
                    djur["Glädje"] += 10
                print("Djurens Glädje ökade.")
            else:
                print("Error.")
        else:
            print("Området finns ej.")

    elif val == "4":
        alla = []
        for område in zoo:
            for djur in zoo[område]:
                alla.append(djur)

        if len(alla) == 0:
            print("Inga djur finns.")
        else:
            gladast = max(alla, key=lambda d: d["Glädje"])
            aldst = max(alla, key=lambda d: d["Ålder"])

            print("Antal djur:", len(alla))
            print("Gladast:", gladast["namn"], gladast["Glädje"])
            print("Äldst:", aldst["namn"], aldst["Ålder"])

    elif val == "5":
        print("Hejdå!")
        break

    else:
        print("Error")
