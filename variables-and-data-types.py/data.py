# Let's start with a long time programming tradition and print "Hello World!" by typing it inside print() function. Replace "type here" with "Hello World!"

print("Hello World!")

# Now try to assign "Hello World!" to the variable my_text. You can assign "Hello World!" to the variable below on.

my_text="Hello World!"
print(my_text)

# There are many ways to concatenate different data pieces with Python's print() function. Here is one of them. Take a look! # Type a couple of different values inside the print function. Make sure they are separated by commas. 
 
question="How about you?"   
print(my_text, "I like games!", question)

# Below is a good example of mixing numbers and text inside the print() function. Assign a number to the variable: glass_of_water

glass_of_water = 8
print("I drank", glass_of_water, "glasses of water today.")

# Let's try to see what happens after assigning a new value to our variable. Place the variable: glass_of_water inside the print function and observe what happens.

glass_of_water=3
glass_of_water=glass_of_water + 1
print(glass_of_water)

# Let's check out a simple integer example. Assign an integer to the variable, then print it.

men_stepped_on_the_moon = -81
print(men_stepped_on_the_moon)

# Now a string example. Type a couple of words or a short sentence for your variable, then print it.

my_reason_for_coding = "I want to learn more about computers!"
print(my_reason_for_coding)

# Let's try to see what happens after assigning a new value to our variable. Assign a float with 2 decimals to the variable below. 

global_mean_sea_level_2018 = 21
 
#Type your code here.
global_mean_sea_level_2018 = 21.07
print(global_mean_sea_level_2018)

# Finally a boolean example. Assign True or False to the variable below then print it.

staying_alive = False 
print(staying_alive)

# Let's check out some exercises that will help you really understand the type() function and type conversions in Python. Using the type() function, assign the type of the variable to answer_1, then print it. 

men_stepped_on_the_moon=12

#Type your code here.
answer_1 = type(men_stepped_on_the_moon)
print(answer_1)

# Using the type() function, assign the type of the variable to answer_2, then print it.

my_reason_for_coding="intergalactic travel"

#Type your code here.
answer_2 = type(my_reason_for_coding)
print(answer_2)

# Using the type() function, assign the type of the variable to answer_3, then print it.

global_mean_sea_level_delta_2018=21.36

#Type your code here.
answer_3 = type(global_mean_sea_level_delta_2018)
print(answer_3)

# We will now print the type of boolean data. Later stages in programming, booleans become quite common. 

staying_alive=True

#Type your code here.
answer_4 = type(staying_alive)
print(answer_4)

# Now let's see some more exercises about converting data types. Let's now try to convert a string into an integer. my_grade variable is a string (because it's in quotes). Convert it to an integer.

my_grade="10"
answer_5 = int(my_grade)
print(answer_5)

# Can you convert a float into an integer. my_temp variable is a float (because it has decimals). Convert it to an integer.

my_temp=97.70
answer_6 = int(my_temp)
print(answer_6)

# Now let's convert a string into a float. shoe_price variable is a string (because it's in quotes). On line 9, convert it into a float.

shoe_price="69.99"
answer_7 = float(shoe_price)
print(answer_7)

# Finally, convert data into a string. GWP denotes the total economic activity created by the world population collectively in a year.

gross_world_product=84.84
gwp_str = str(gross_world_product)
answer_8="In 2018 gross product of the world (GWP) was " + gwp_str + " in trillion US dollars."
print(answer_8)

# Let's create an empty list and print its type.

gift_list = []
answer_9 = type(gift_list)
print(answer_9)

# Now, we will create an empty dictionary and print its type.

grocery_items = {}
answer_10 = type(grocery_items)
print(answer_10)

# Then we will create an empty tuple and print its type.

bucket_list = ()
answer_11 = type(bucket_list)
print(answer_11)

# Now let's see some more exercises about converting data types. Let's create a list with values in it.

gift_list = [1, 2, 3, 4, 5]
print(gift_list)

# Now let's create a dictionary with values in it.

grocery_list = {
    "bacon": 5.99,
    "eggs": 3.99,
    "croissants":7.99,
}
print(grocery_list)

# Finally, let's create a tuple with values in it. 

bucket_list = ("skydiving", "japan", "ride an elephant")
print(bucket_list)