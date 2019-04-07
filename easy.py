# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
# import random
# lst = []
# ENDS = 10
# for _ in range(ENDS):
#     lst.append(random.randint(0,10))
# print(lst)
# lst_new = [i**2 for i in lst]
# print(lst_new)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
# lst1 = ['apple', 'peach', 'fruit1', 'fruit2', 'fruit3']
# lst2 = ['fruit1','fruit7', 'fruit10','apple']
# lst_res = list(set(lst1) & set(lst2))
# print(lst1)
# print(lst2)
# print(lst_res)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
import random
lst = []
ENDS = 20
for _ in range(ENDS):
    lst.append(random.randint(-100,100))
print(lst)
# lst_res = []
lst_res = [i for i in lst if i>0 and i % 3 ==0 and i % 4 != 0]
print(lst_res)
