print("Hej hur gammal e du")
age = input()
age = int(age)

if age <= 14:
    print("Då ska du a en barnbiljet kostar det 16kr")

elif age <=20:
    print("Då ska du he en ungdomsbiljetkostar det 20kr")

elif age <=64:
    print("Då ska du ha en ordinariebiljet då kostar det 27kr")

elif age >=65:
    print("Då ska du ha en Seniorbiljet för 21kr")