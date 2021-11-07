cities = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]


horror_movies = ["chucky", "friday the 13th", "nightmare on elm street", "halloween", "scream", "donnie darko", "texas chainsaw", "conjuring", "hellraiser", "it"]




first_four_cities = cities[0:4]


last_four_horror_movies = horror_movies[-5:-1]


cities[0] = "San Fransisco"
cities[2] = "Brooklyn"
cities[-3] = "Hollywood"
cities[-5] = "Tampa"


cities.append("Oakland")
cities.extend(["New York City" , "Los Angeles"])
cities.insert(0, "Miami")


del cities[0]
cities.pop(-1)
cities.remove("Tampa")

def print_city(list):
    for el in list:
        print(el)
    return "All Cities Printed"
print(print_city(cities))

def reorganize_list(list):
    counter = 0
    while counter < len(list):
        item1 = list[counter]
        item2 = list[counter + 1]
        if len(item1) >= len(item2):
            counter += 1
            continue 
        elif counter + 1 == len(list) - 1:
            break 
        else:
            list.remove(item1)
            list.append(item1)
            counter += 1
    return list
print(reorganize_list(cities))

def sort_list(list):
    return sorted(list)
print(sort_list(horror_movies))
