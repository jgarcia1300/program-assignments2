food = {"chicken":1.59 , "beef":1.99 , "cheese":1.00 , "milk":2.50}

games = {"cod":60.00 , "ow":20.00 , "apex":0.00 , "beatsaber":30.00}

chicken_price =  food["chicken"] 
beef_price = food["beef"] 
cheese_price = food["cheese"] 
milk_price = food["milk"]

call_of_duty_price = games["cod"] 
overwatch_price = games["ow"]
apex_price = games["apex"] 
beatsaber_price = games["beatsaber"] 


shoes = {"Jordan 13": 1 , "Yeezy": 8 , "Foamposite": 10 , "Air Max": 5 , "SB Dunk": 20}


shoes["SB Dunk"] -= 2
shoes["Yeezy"] += 1
shoes["Yeezy"] += 7
shoes["SB Dunk"] += 7
shoes["Jordan 13"] += 7
shoes["Foamposite"] += 7
shoes["Air Max"] += 7
shoes["Yeezy"] -= 3
shoes["SB Dunk"] -= 3
shoes["Jordan 13"] -= 3
shoes["Foamposite"] -= 3
shoes["Air Max"] -= 3


food["eggs"] = 1.79
food["bacon"] = 1.89
food["soda"] = 1.39


games["bloons"] = 20.00
games["Gmod"] = 10.00
games["DBD"] = 20.00

shoes["Jordan 11"] = 12
shoes["Vans"] = 4
shoes["Pumas"] = 6


del food["bacon"]
del food["soda"] 


del games["Gmod"] 
del games["DBD"] 


del shoes["Vans"] 
del shoes["Pumas"] 

def total_price(food_item, food_item2): 
    total = food[food_item] + food[food_item2] 
    return total 

print(total_price("beef", "cheese"))    

def price_difference(food_item, food_item2):
     difference = food[food_item] - food[food_item2]
     return abs(difference)

print(price_difference("beef", "cheese"))

print(shoes)

def shoe_restock(shoe, num):
    shoes[shoe] *= num 
    return shoes 

print(shoe_restock("Yeezy", 3))

def clearance_sale(shoe, num):
    shoes[shoe] /= num
    return shoes
print(clearance_sale("SB Dunk", 2))

def game_search(dict):
    largest = 0
    game = ''
    for key in dict.keys():
        if dict[key] > largest:
            largest = dict[key]
            game = key
    return (game, largest)
print(game_search(games))
             