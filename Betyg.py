while True:
    max_poäng = float(input("Hej! Skriv mängd betyg i procent 0-100:"))

    poäng = float(input("Skriv mängd poäng:"))

    procent = (poäng/max_poäng) * 100

    print(f"Du fick{procent:.1f}%")

    if procent < 50:
        print("Ditt betyg är F")

    elif procent < 60:
        print("Ditt betyg är E")

    elif procent < 70:
        print("Dittbetyg är D")

    elif procent < 80:
        print("Ditt bedyg är C")
        
    elif procent < 90:
        print("Ditt bedyg är B")

    elif procent < 100:
        print("Ditt betyg är A")