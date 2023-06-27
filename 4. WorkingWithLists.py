#Working with lists
print('#Working with lists')
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(magician)
 
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(f"{magician.title()}, that was a great trick!")
 print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

#Numerical lists#
print('Numerical lists\n')
for value in range(1, 5):
 print(value)
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2, 11, 3))
print(even_numbers)

#Exponents
squares = []
for value in range(1, 11):
 square = value ** 2
 squares.append(square)
print(squares)

#static list
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
#List Comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)

#Ejemplos
print('Ejemplos:')
example = [value**2 for value in range(1, 11)]
print(example)

# Working with Part of a List

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:5])

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:]) #imprime los ultimos 3

#Looping Through a Slic
players = ['carlos', 'martina', 'miguel', 'florencia', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
 print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# TUPLES
print('Working whith Tuples')

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
 print(dimension)

print('-------------')

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
