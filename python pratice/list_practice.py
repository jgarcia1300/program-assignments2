cities = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
print(cities)

horror_movies = ["chucky", "friday the 13th", "nightmare on elm street", "halloween", "scream", "donnie darko", "texas chainsaw", "conjuring", "hellraiser", "it"]
print(horror_movies)

print(cities[-3], cities[2], cities[-5])
print(horror_movies[0], horror_movies[-3], horror_movies[-6])

first_four_cities = cities[0:4]
print(first_four_cities)

last_four_horror_movies = horror_movies[-5:-1]
print(last_four_horror_movies)

cities[0] = "San Fransisco"
cities[2] = "Brooklyn"
cities[-3] = "Hollywood"
cities[-5] = "Tampa"
print(cities)

cities.append("Oakland")
cities.extend(["New York City" , "Los Angeles"])
cities.insert(0, "Miami")
print(cities)

del cities[0]
cities.pop(-1)
cities.remove("Tampa")
print(cities)

