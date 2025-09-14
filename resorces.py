import json

with open("kitchen.json", "r") as file:
    data = json.load(file)
    print(list(data.values()))

def getNumberOfCoffee():
    possible = 0 
    while (data['coffee'] >= 4*(possible+1) and
           data['sugar'] >= 10*(possible+1) and
           data['water'] >= 50*(possible+1) and
           data['milk'] >= 100*(possible+1) and
           data['icecream'] >= 1*(possible+1)):
        possible += 1
    return possible

price = 200   

while (data['coffee'] >= 4 and data['sugar'] >= 10 and 
       data['water'] >= 50 and data['milk'] >= 100 and 
       data['icecream'] >= 1): 
    
    available = getNumberOfCoffee()  
    if available == 0:
        print("Shop closed. No resources left.")
        break

    num = int(input("How many coffees do you want?: ")) 
    
    if num <= available:
        print(f"{num} coffee(s) is available")
        bill = price * num
        print(f"Here is your bill: {bill}")
       
        data['coffee'] -= 4 * num
        data['sugar'] -= 10 * num
        data['water'] -= 50 * num
        data['milk'] -= 100 * num
        data['icecream'] -= 1 * num

        with open("kitchen.json", "w") as file:
            json.dump(data, file, indent=4)

    else:
        print(f"Sorry, {num} coffees cannot be made right now.")
        choice = input(f"We have only {available} coffee(s) at this moment. Do you want it? (yes/no): ").strip().lower()
        
        if choice == "yes":
            print("Please wait, we are processing your order")
            bill = price * available
            print(f"Here is your bill: {bill}")

            data['coffee'] -= 4 * available
            data['sugar'] -= 10 * available
            data['water'] -= 50 * available
            data['milk'] -= 100 * available
            data['icecream'] -= 1 * available

            with open("kitchen.json", "w") as file:
                json.dump(data, file, indent=4) 
        else:
            print("Okay, order cancelled.")
