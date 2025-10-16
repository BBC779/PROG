
while True:
    print("Skriv in ett nummer")

    nummer_1 = input()

    try:
        nummer_1 = int (nummer_1)
        break
    except ValueError:
        print("Nej! Det där var inte ett nummer")