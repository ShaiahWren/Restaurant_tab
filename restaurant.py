menu = {    
    "Brunch": {        
        "Steak and Eggs": 16.99,        
        "Three Egg Breakfast": 8.99,        
        "Eggs Benedict": 11.99,        
        "Biscuit and Gravy": 7.99,        
        "Chicken Fingers": 10.99,        
        "Chicken Wrap": 8.99,        
        "Steak Salad": 1.99    },    
    "Drinks": {        
        "Soft Drink": 1.99,        
        "Coffee": 1.99,        
        "Orange Juice": 0.99,        
        "Milk": 0.55,        
        "Water": 0.00    
    }      
}

menu["Brunch"]["Steak Salad"] = 15.99
# print(menu["Brunch"]["Steak Salad"])

menu["Specials"] = {"Soup of the Day" : 8.99, "Catch of the Day" : 14.99, "Chef Special": 15.99}
# print(menu["Specials"])

menu["Brunch"]["Three Egg Breakfast"] = {"Without Bacon" : 8.99, "With Bacon" : 9.99}
# print(menu["Brunch"]["Three Egg Breakfast"])

## RECEIPT

## menu items and price
def price(list_brunch, list_specials, list_drinks):
    running_total = 0
    for item in list_brunch:
        price = menu["Brunch"][item]
        print_item(item, menu["Brunch"][item]) 
        running_total += price
    for item in list_specials:
        price = menu["Specials"][item]
        print_item(item, menu["Specials"][item])
        running_total += price
    for item in list_drinks:
        price = menu["Drinks"][item]
        print_item(item, menu["Drinks"][item])
        running_total += price
    print()
    print(f"{'':<10} Price:  ${running_total:>5.2f}")
    print(f"{'':<10} Taxes:  ${(running_total * 0.07):>5.2f}")
    print(f"{'':<10} Total:  ${(running_total*1.07):>5.2f}")
    print()
    tip(running_total * 1.07)


## string formatting for price and item
def print_item(item, price):
    print(f"{item :<20}   $   {price:>5}")

### tip function
def tip(total):
    print("**Suggested Tip**")
    for t in range(25, 10, -5):
        print(f"Tip {t}: {total * t/100:>5.2f}")


price(["Eggs Benedict", "Biscuit and Gravy", "Steak and Eggs"], [], ["Coffee", "Coffee", "Soft Drink"])


