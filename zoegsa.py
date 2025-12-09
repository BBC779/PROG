zoo = {
    "Savana": [
        {"art": "Lejon", "namn": "Simba", "happiness": 50, "age": 5},
        {"art": "Elefant", "namn": "Dumbo", "happiness": 70, "age": 12}
    ],
    "Regnskog": [
        {"art": "Apa", "namn": "Koko", "happiness": 60, "age": 7}
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
                print(djur["namn"], djur["art"], "Happiness:", djur["happiness"], "Age:", djur["age"])
        else:
            print("Området finns inte.")

    elif val == "2":
        område = input("Vilket område?: ")

        if område not in zoo:
            zoo[område] = []

        art = input("Art: ")
        namn = input("Namn: ")
        happiness = int(input("Happiness: "))
        age = int(input("Ålder: "))

        zoo[område].append({"art": art, "namn": namn, "happiness": happiness, "age": age})
        print("Djuret är tillagt.")

    elif val == "3":
        print("Områden:")
        for område in zoo:
            print(område)

        område = input("Välj område att hälsa på: ")

        if område in zoo:
            print("1. Mata\n2. Lek\n3. Städa")
            handling = input("Välj: ")

            if handling in ["1", "2", "3"]:
                for djur in zoo[område]:
                    djur["happiness"] += 10
                print("Djurens happiness ökade.")
            else:
                print("Fel val.")
        else:
            print("Området finns inte.")

    elif val == "4":
        alla = []
        for område in zoo:
            for djur in zoo[område]:
                alla.append(djur)

        if len(alla) == 0:
            print("Inga djur finns.")
        else:
            gladast = max(alla, key=lambda d: d["happiness"])
            aldst = max(alla, key=lambda d: d["age"])

            print("Antal djur:", len(alla))
            print("Gladast:", gladast["namn"], gladast["happiness"])
            print("Äldst:", aldst["namn"], aldst["age"])

    elif val == "5":
        print("Hejdå!")
        break

    else:
        print("Fel val!")
