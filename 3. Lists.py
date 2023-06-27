### LISTS ###

bicycles = ['trek', 'cannonaldale', 'redline', 'specialized']
print(bicycles)

print(bicycles[0])
print(bicycles[1].title())
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)
## Modifying conntens in a List

motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
motocycles[0] = 'ducati'
print(motocycles)
motocycles = ['honda', 'yamaha', 'suzuki']
## adding new element to the end of the list
motocycles.append('ducati')
print(motocycles)
print('***Adding new elements**')
motorcycles = [] #inicializando
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motocycles)
###Adding a new element in at list, choosing the idex
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

##Removing elements from a list
del motorcycles[0]
print(f'Removing elements from a list:\n{motorcycles}')

## Using poo() to remove
motorcycles = ['honda', 'yamaha', 'suzuki']
print(f'Using POP to remove {motorcycles}')
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

#Sorting a List Permanently with the sort() Method#
print('Sorting a List Permanently with the sort() Method')
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)
# Reverse
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

#Finding the Length of a List
print('Finding the Length of a List')
len(cars)








