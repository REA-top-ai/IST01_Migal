# task 2
max_val = 100
mean_val = 50
min_val = 10
std_val = 5

if max_val > mean_val + 5 * std_val or min_val < mean_val - 5 * std_val:
    print("В ваших данных имеются экстремальные значения и требуют предобработки")
elif max_val > mean_val + 3 * std_val or min_val < mean_val - 3 * std_val:
    print("В ваших данных имеются выбросы и требуют предобработки")
else:
    print("Ваши данные пригодны для анализа")

