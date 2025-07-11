#Calculator Gorget
print("Welcome do Calculator!!")
bill = float(input("What was the total bill? R$ "))
porcent = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

bill_with_people = bill *(1+porcent/100)/people
final = round(bill_with_people,2)
print(f"Each person should pay: R$ {final}")