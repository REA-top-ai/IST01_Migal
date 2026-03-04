# Task 1
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']
sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']
for game in board_games:
    print(game)

# Task 2
for game in board_games:
    print(game)

# Task 3
for sport in sport_games:
    print(sport)

# Task 4
promise = "I will not chew gum in class"
for i in range(5):
    print(promise)

# Task 5
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]
for student in students_period_A:
    students_period_B.append(student)
    print(student)

# Task 6
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'
for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("У них есть собака, которую я хочу!")
        break

# Task 7
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for location in sales_data:
    for scoops in location:
        scoops_sold += scoops
print(scoops_sold)

# Task 8
single_digits = range(10)
squares = []
for digit in single_digits:
    print(digit)
    squares.append(digit ** 2)
print(squares)
cubes = [digit ** 3 for digit in single_digits]
print(cubes)
