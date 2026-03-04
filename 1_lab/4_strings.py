# task 1
favour_word = "Python"
print(favour_word)

# task 2
first_name = "Виталий"
last_name = "Красилов"
new_account = last_name[:5]
temp_password = last_name[2:6]

# task 3
def account_generator(first_name, last_name):
    return first_name[:3] + last_name[:3]

new_account = account_generator(first_name, last_name)

# task 4
def password_generator(first_name, last_name):
    return first_name[len(first_name)-3:] + last_name[len(last_name)-3:]

temp_password = password_generator(first_name, last_name)

# task 5
company_motto = "Мечты сбываются"
second_to_last = company_motto[-2]
final_word = company_motto[-4:]

# task 6
first_name = "Роб"
last_name = "Дейли"
fixed_first_name = "P" + first_name[1:]

# task 7
password = "theycallme\"crazy\"91"

# task 8
poem_title = "spring storm"
poem_author = "William Carlos Williams"
poem_title_fixed = poem_title.title()

