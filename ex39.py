# Define a dictionary mapping states to their abbreviations
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Define a dictionary mapping state abbreviations to cities
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

# Add additional cities to the dictionary
cities['NY'] = 'New York'
cities['OR'] = 'Portland'


print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])


print('-' * 10)
# Print the abbreviations for Michigan and Florida
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is:", states['Florida'])


print('-' * 10)
# Print the cities for Michigan and Florida using their state abbreviations
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])


print('-' * 10)
# Iterate through the states dictionary and print each state with its abbreviation
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")


print('-' * 10)
# Iterate through the cities dictionary and print each abbreviation with its city
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")


print('-' * 10)
# Iterate through the states dictionary and print each state with its abbreviation and corresponding city
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")


print('-' * 10)
# Try to get the abbreviation for Texas
state = states.get('Texas')

# Check if Texas is in the states dictionary
if not state:
    print("Sorry, no Texas.")

# Try to get the city for the abbreviation 'TX' with a default message if it doesn't exist
city = cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is: {city}")