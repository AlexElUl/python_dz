from package1 import p1

# Проверка задания №1
SUM1 = p1.Sum_sum
l1 = [1, 2, 3]
print(SUM1.Sum(l1))

SUM2 = p1.Sum_sum
l2 = [1, 2, -3]
print(SUM2.Sum(l2))

SUM3 = p1.Sum_sum
l3 = [1, 2, -3, 0.123, 19]
print(SUM2.Sum(l3))

# Проверка задания №2
STRING_1 = 'He never sleeps, He says that he will never die'
STRING_2 = 'Na nana na  na na, na nana na   Na'

count1 = p1.Count_words()
count2 = p1.Count_words()

print(count1.count(STRING_1), count2.count(STRING_2))

# Проверка задания №3
p=p1.Parsing(url_=f'https://www.muztorg.ru')
p.get_text()
