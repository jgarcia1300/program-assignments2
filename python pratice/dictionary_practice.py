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

print(food)
print(games)
print(call_of_duty_price)

shoes = {"Jordan 13": 1 , "Yeezy": 8 , "Foamposite": 10 , "Air Max": 5 , "SB Dunk": 20}
print(shoes)

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
print(shoes)

food["eggs"] = 1.79
food["bacon"] = 1.89
food["soda"] = 1.39
print(food)

games["bloons"] = 20.00
games["Gmod"] = 10.00
games["DBD"] = 20.00
print(games)

shoes["Jordan 11"] = 12
shoes["Vans"] = 4
shoes["Pumas"] = 6
print(shoes)

del food["bacon"]
del food["soda"] 
print(food)

del games["Gmod"] 
del games["DBD"] 
print(games)

del shoes["Vans"] 
del shoes["Pumas"] 
print(shoes)
