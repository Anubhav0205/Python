Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

# creating a dictionary
country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}

# printing the dictionary
print(country_capitals)

# Valid dictionary

my_dict = {
  1: "Hello", 
  (1, 2): "Hello Hi", 
  3: [1, 2, 3]
}

print(my_dict)

# Invalid dictionary
# Error: using a list as a key is not allowed

# my_dict = {
#   1: "Hello", 
#   [1, 2]: "Hello Hi", 
# }

# print(my_dict)

country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}

# get dictionary's length
print(len(country_capitals))

country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London"
}

print(country_capitals["United States"]) 

print(country_capitals["England"])

country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Naples", 
  "England": "London"
}

# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"

print(country_capitals)

country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Naples" 
}

# add an item with "Germany" as key and "Berlin" as its value
country_capitals["Germany"] = "Berlin"

print(country_capitals)


country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Naples" 
}
print(country_capitals["United States"])

# delete item having "United States" key
del country_capitals["United States"]


print(country_capitals)

country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Naples" 
}

country_capitals.clear()

print(country_capitals)

# create a dictionary
marks = { 'Physics': 67, 'Chemistry': 72, 'Math': 89 }

element = marks.pop('Chemistry')

print('Popped Marks:', element)
print('Marks:', marks)


# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('apple')

print('The popped element is:', element)
print('The dictionary is:', sales)
# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

#element = sales.pop('guava')
element = sales.pop('guava',"The key is not present")

print(element)

scores = {
    'Physics': 67, 
    'Maths': 87,
    'History': 75
}

result = scores.get('Physics')


print(scores)
print(result)

marks = {'Physics':67, 'Maths':87}

print(marks.values())


my_list = {1: "Hello", "Hi": 25, "Howdy": 100}

print(1 in my_list) # True

# the not in operator checks whether key doesn't exist
print("Howdy" not in my_list) 

print("Hello" in my_list) 


country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Naples" 
}

# print dictionary keys one by one
for country in country_capitals:
    print(country)

print("----------")

# print dictionary values one by one
for country in country_capitals:
    capital = country_capitals[country]
    print(country,end="--")
    print(capital)