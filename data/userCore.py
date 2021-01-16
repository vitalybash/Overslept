import csv

with open("data/UserSaves.csv", mode='r', encoding='utf8') as saves:
    listSaves = [save for save in csv.reader(saves,
                                             delimiter=';',
                                             quotechar='"')]

# Переменная выбранного профиля
profileSave = None
