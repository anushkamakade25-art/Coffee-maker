
import json

with open("kitchen.json", "r") as file:
    data = json.load(file)
    print(list(data.values()))
    print(data['coffee'])
price = 200   
while(data['coffee'] >= 4 and data['sugar'] >= 10 and 
       data['water'] >= 50 and data['milk'] >= 100 and 
       data['icecream'] >= 1): 
    if (data['coffee'] < 4 or data['sugar'] < 10 or
        data['water'] < 50 or data['milk'] < 100 or
        data['icecream'] < 1):
        print("Sorry, shop closed. No resources left")
        break

    num = int(input("How many coffee you want?:"))
    
    if data['coffee'] >= 4*num and data['sugar']>=10*num and data['water']>=50*num and data['milk']>=100*num and data['icecream']>=1*num:
        print(f"{num} coffee is available")
        bill = price * num
        print(f"here is your bill: {bill}")
        data['coffee'] -= 4 * num
        data['sugar'] -= 10 * num
        data['water'] -= 50 * num
        data['milk'] -= 100 * num
        data['icecream'] -= 1 * num
        with open("kitchen.json", "w") as file:
            json.dump(data, file, indent=4)        


        
    else:
        print("sorry, no coffee")
        
    
    



    


