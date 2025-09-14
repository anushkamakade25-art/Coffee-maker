import json

with open("kitchen.json", "r") as file:
    data = json.load(file)
    print(list(data.values()))

price = 200   

while (data['coffee'] >= 4 and data['sugar'] >= 10 and 
       data['water'] >= 50 and data['milk'] >= 100 and 
       data['icecream'] >= 1): 
    
    if (data['coffee'] < 4 or data['sugar'] < 10 or
        data['water'] < 50 or data['milk'] < 100 or
        data['icecream'] < 1):
        print("Shop closed. No resources left.")
        break

    num = int(input("How many coffees do you want?: ")) 

    possible = 0 
    while (data['coffee'] >= 4*(possible+1) and
           data['sugar'] >= 10*(possible+1) and
           data['water'] >= 50*(possible+1) and
           data['milk'] >= 100*(possible+1) and
           data['icecream'] >= 1*(possible+1)):
        possible += 1

    if num <= possible:
        print(f"{num} coffee is available")
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
        if possible > 0:
            print(f"Sorry, {num} coffees cannot be made right now.")
            choice = input(f"We have only {possible} coffee(s) at this moment. Do you want it? (yes/no): ").strip().lower()
            
            if choice == "yes":
                print("Please wait, we are processing your order")
                bill = price * possible
                print(f"Here is your bill: {bill}")

                # update stock
                data['coffee'] -= 4 * possible
                data['sugar'] -= 10 * possible
                data['water'] -= 50 * possible
                data['milk'] -= 100 * possible
                data['icecream'] -= 1 * possible

                with open("kitchen.json", "w") as file:
                    json.dump(data, file, indent=4) 
            else:
                print("Okay, order cancelled.")
        else:
            print("Sorry, no coffee can be made right now.")
