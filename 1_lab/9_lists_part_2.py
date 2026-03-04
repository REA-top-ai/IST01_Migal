# Task 1
list1 = range(2, 20, 2)
list1_len = len(list1)
print(list1_len)

list2 = range(2, 20, 3)
list2_len = len(list2)
print(list2_len) #The lenght decreased.

#Task 2 
employees = ['Майкл', 'Дуайт', 'Джим', 'Пэм', 'Райан', 'Энди', 'Роберт']
index4 = employees[4]
print(len(employees))
# print(employees[8])

# Task 3
shopping_list = ['яйца', 'масло', 'молоко', 'огурцы', 'сок', 'хлопья']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(element5, last_element)

# Task 4
suitcase = ['рубашка', 'рубашка', 'брюки', 'брюки', 'пижамы', 'книги']
beginning = suitcase [0:2]
print(len(beginning))

beginning1 = suitcase[0:4]
print(len(beginning1))

middle = suitcase[(len(suitcase)//2-1):(len(suitcase)//2+1)]
print(middle)

#Task 5
suitcase = ['рубашка', 'футболка', 'носки', 'очки', 'пижама', 'книги']
start = suitcase[:3]

# Task 6
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Jake']
jake_votes = votes.count('Jake')
print(jake_votes)


# task 7
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace'
, '1600 Pennsylvania Ave', '10 Downing St.']
print(addresses)
addresses.sort()
print(addresses)

# Task 8
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games, games_sorted)

# Task 9 
inventory = ["двухспальная кровать", "двухспальная кровать", "изголовье", "двуспальная кровать", "двуспальная кровать", "комод", "комод", "стол", "стол", "тумбочка", "тумбочка", "королевская кровать", "двуспальная кровать", "две односпальные кровати", "две односпальные кровати", "простыни", "простыни", "подушка", "подушка"]

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("две односпальные кровати")
inventory.sort()
