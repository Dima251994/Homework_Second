

import random #Імпорт модуля рандом
list_of_players = ["Бочков Віталій", #Створення списку
                   "Ломин АНдрій", 
                   "Скакунов Олег",
                   "Поролов Роман",
                   "Ломанова Ірина",
                   "Кукіна Оксана"
]
print("Переможець -", random.choice(list_of_players)) #Команда для виведдення переможця
print("Вітаємо!)")