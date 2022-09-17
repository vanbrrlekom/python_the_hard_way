#create a mapping of state to abbreviation
states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California":"CA",
    "New York": "NY",
    "Michigan": "MI"
}

#Creaes a basic set of states and cities within them

cities = {
    "CA": "San francisco",
    "MI": "Detroit",
    "FL": "Jacksonville",
}

#add some more cities

cities["NY"] = "New York",
cities["OR"] = "Portland"

#Print out citis
print("-" * 10)
print("NY state has: ", cities["NY"])
print("OR state has: ", cities["OR"])

#Print some states
print("-" * 10)
print("Michigan's abreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ", states["Florida"])

#Do it by using the state then cities dict
print("_"* 10)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

#print every state abbreviation
print("-"*10)
for state, abbrev in list(cities.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print("-"*10)
for abbrev, city in list(states.items()):
    print(f"{abbrev}, has the city {city}")


#Now do both at the same time
print("-"*10)
for state, abbrev in list(states.items( )):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("-"*10)
#safely get abbreviation by state that might not be there
state = states.get("Texas")

if not state:
    print("Sorry, no Texas")

#get a city with a default value
city = cities.get("TX", "Does not exist")
print(f"the city for the state Texas is: {city}")