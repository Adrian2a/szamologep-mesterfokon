
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.összeadás")
print("2.kivonás")
print("3.szorzás")
print("4.osztás")
print("5. type 'NEM AKAROK' to exit")

while True:
  
    choice = input("tiéd a választás, Neo(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("írja be az ELSŐ számot: "))
            num2 = float(input("majd a másodikat: "))
        except ValueError:
            print("számot írj légyszi.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice =='5':
            print("akkor szia báttya")
    next_calculation = input("Ez az utolsó esélyed. Ezután nincs visszaút. Ha beveszed a kék pirulát, a történet véget ér, felébredsz az ágyadban, és azt hiszel, amit hinni akarsz. Ha beveszed a piros pirulát, Csodaországban maradsz, és én megmutatom, milyen mély a nyúlüreg.? (Piros tabletta/kék tabletta): ")
    if next_calculation == "kék tabletta"  :
      break
    else:
        print("bro elírtad😭💀")