# task 1
cake_list = ['торт', 1]

#task 2
household_chemicals =[['порошок', 1], ['средство для мытья посуды', 1], ['штука', 1]]

#task 3
names = ['Ben', 'Holly', 'Ann']
dogs_names = ['Sharik', 'Gab', 'Beethoven']
names_and_dogs_names = zip(names, dogs_names)
list_of_names_and_dog_names = list(names_and_dogs_names)
print(list_of_names_and_dog_names, '\n')

#task 4
orders = ['маргаритки', 'васильки']
print(orders)
orders.append('тюльпаны')
orders.append('розы')
print(orders, '\n')

#task 5
orders = ['маргаритка', 'лютик', 'львиный зев', 'гардения', 'лилия']
new_orders = orders + ['сирень', 'ирис']
print(new_orders, '\n')
broken_prices = [5, 3, 4, 5, 4] + [4]

#task 6
list1 = list(range(9))
list2 = list(range(7))

#task 7
list1 = list(range(5, 15, 3))
list2 = list(range(0, 40, 5))

# task 8
first_names = ['Эйнсли', 'Бен', 'Чани', 'Депак']
age = []
age.append(42)
all_ages = [32, 41, 29] + age
name_and_age = list(zip(first_names, all_ages))
ids = range(4)
