# task 1
def calc_age(current_year, birth_year):
    age = current_year - birth_year
    return age

my_age = calc_age(2049, 1993)
dads_age = calc_age(2049, 1953)
print(f"Мне {my_age} лет, а моему отцу {dads_age} лет")


# task 2
def repeat_stuff(stuff, num_repeats=10):
    return stuff * num_repeats

repeat_stuff("Row", 3)
lyrics = repeat_stuff("Row", 3) + " Your Boat."
song = repeat_stuff(lyrics)
print(song)
