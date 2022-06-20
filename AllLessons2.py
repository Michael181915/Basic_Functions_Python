import math
import sys
import os
import json
import re

print("Добро пожаловать на демонстрационно-обучающую программу по изучению языка Python:\n\n\n");
print("1. Использование модулей");
print("2. Классы(1)");
print("3. Классы(2)");
print("4. Работа с файлами");
print("5. Перехват ошибок");
print("6. Использование JSON");
print("7. Аргументы коммандной строки");
print("8. Регулярные вырадения(1)");
print("9. Регулярные выражения(2)");
print("Введите число программы (ниже), которое означает номер программы \n");
print("Если хотите выйти из программы нажмите 0\n");

##while True:

x = int(input())
if(x == 1):

#print("\n1 или 2?");

#y = int(input())
#if(y == 1):
    def aaa():
        print("\nПервая ссылка на программу");

    def bbb():
        print("\nВторая ссылка на программу");

    def ccc():
        print("\nТретья ссылка на программу");

    def ddd():
        print("\nЧётвертая ссылка на программу");

    ddd()
    bbb()
    aaa()
    ddd()
    bbb()
    #print("Выход из программы");
    #exit();
    
elif(x == 2): 
    #a = int(input("Hello: "))
    print("\nГеографические данные\n\n")
    class Country():
        def __init__(self, name, total, population, currency, head):    
            self.name = name
            self.total = total        
            self.population = population
            self.currency = currency
            self.head = head
            self.year = 2020

        def country(self):
            print((self.name).title())
            print("В " + str(self.year) + " году размер территории составляет: " + str(self.total) + " человек.")
            print("Население государства составляет: " + str(self.population) + " тысяч км^2.")
            print("Денежной единицей является " + str(self.currency) + ".")
            print("Страной руководит " + self.head + ".")

        def plus_population(self):
            self.population += 10000

        def minus_population(self):  # name, total, population, currency, head):
            self.population -= 10000        
        
        def price_benzin(self, price):
            print("Цена на бензин составляет: " + str(price) + " " + self.currency + ".\n\n")

    '''life1 = Country("Панама", 78200, 4252620, "доллар США", "Лаурентино Кортиcо")
    life2 = Country("Мексика", 1972550, 128649565, "песо", "Андрес Мануэль Лопес Обрадор")
    life3 = Country("Коста-Рика", 510100, 5097988, "колон", "Карлос Альварадо Кесада")

    life1.country()
    life1.plus_population()
    life1.price_benzin(0.922)

    life2.country()
    life2.minus_population()
    life2.price_benzin(1.103)

    life3.country()
    life3.plus_population()
    life3.price_benzin(1.188)'''
        
elif(x == 3):
    #a = int(input("Hello: "))
    print("\nГеографические данные\n\n")
    class Country():
        def __init__(self, name, total, population, currency, head):    
            self.name = name
            self.total = total        
            self.population = population
            self.currency = currency
            self.head = head
            self.year = 2020

        def country(self):
            print((self.name).title())
            print("В " + str(self.year) + " году размер территории составляет: " + str(self.total) + " человек.")
            print("Население государства составляет: " + str(self.population) + " тысяч км^2.")
            print("Денежной единицей является " + str(self.currency) + ".")
            print("Страной руководит " + self.head + ".")
            print("\n\n")

        def plus_population(self):
            self.population += 10000

        def minus_population(self):  # name, total, population, currency, head):
            self.population -= 10000        
        
        def price_benzin(self, price):
            print("Цена на бензин составляет: " + str(price) + " " + self.currency + ".\n\n")

    class Capital(Country):
        def __init__(self, name, total, population, currency, head, namecap):
            super().__init__(name, total, population, currency, head)
            self.namecap = namecap
            self.aversalary = 2000

        def plus_salary(self): #, dsal):
            self.aversalary += 10;

        def capital(self):
            print((self.name).title())
            print("В " + str(self.year) + " году размер территории составляет: " + str(self.total) + " человек.")
            print("Население государства составляет: " + str(self.population) + " тысяч км^2.")
            print("Денежной единицей является " + str(self.currency) + ".")
            print("Страной руководит " + self.head + ".")
            print("Средняя зарплата в " + self.namecap + " столице: " + str(self.aversalary) + " долларов США.")
            print("\n\n")



elif(x == 4):
    
    inputfile1 = "D:/Программирование/Python/Python/19lesson_user.txt"
    outputfile2 = "D:/Программирование/Python/Python/Students_passwords.txt"
    password_tolookfor = "Александров"
    #password_tolookfor = "Александров" "АЛЕКСАНДРОВ"

    '''print("Введите полное название файла:")
    inputfile1 = input("Подсказка файл в виде расширения .txt: \n")
    password_tolookfor = input("Введите строку букв для поиска фамилии студента ЮрФака МГУ: \n")
    print("\n")
    outputfile2 = "D:/Программирование/Python/Python/Students_passwords.txt"'''
    
    myfile1 = open(inputfile1, mode = 'r', encoding = 'utf_8') #latin_1
    myfile2 = open(outputfile2, mode = 'w', encoding = 'utf_8')

    for i, line in enumerate(myfile1, 1):
        if password_tolookfor in line:
            print(str(i) + ". " + str(line.strip()).title())
            myfile2.write("Найден пароль: " + line + "\n")

    myfile1.close()
    myfile2.close()
    
elif(x == 5):
    print("КЛАССИФИКАЦИЯ ОШИБОК\n");
    #filename = "233lesson_user.txt"

    filename = "The_Sovietc_Movies.txt"   

    #while True:
    try:
        print("Операция TRY")
        print("Процесс вывода данных из текстового файла ...")
        myfile = open(filename, mode = 'r', encoding = 'utf_8') #latin_1
    except Exception:
        print("Операция EXCEPT")
        print("Файл не найден")
        print(sys.exc_info())
        #print("Выберите другой файл!")
        #sys.exit()
        filename = input("Ввеите правильное полное название файла: ")
          #if(filename == 0):
            #break;
    #if(filename == 0):
        #break;
        #quit();
    else:
        print("Операция ELSE")
        print(myfile.read())
    finally:
        print("Операция FINALLY")
    #if(filename == 0):
            #break;
        
    print("-------------------------------------------------------------------------------\n");
    myfile1.close()
  
elif(x == 6):
    print("-----------------------------Советские кинорежиссёры--------------------------\n")

    filename = "Великие кинорежиссёры.txt"
    inputfile = "Великие кинорежиссёры.txt"
    myfile1 = open(filename, mode = 'w', encoding = 'utf-8') #koi8_r utf-8 latin_1

    director1 = {
        'DirectorName': "Oleg Tabakov",
        'ScoreMovies': 5,
        'Movies': ["Armchair", "Sailor 's silence", "Simplicity is enough for any wise man"]
        }  
    
    director2 = {
        'DirectorName': "Mark Zakharov",
        'ScoreMovies': 7,
        'Movies': ["12 chairs", "An ordinary miracle", "The same Munchausen"]#, "The formula of love"]
        }

    director3 = {
        'DirectorName': "Eldar Ryazanov",
        'ScoreMovies': 27, 
        'Movies': ["Irony of fate, or With a light steam!", "Hussar Ballad", "Train station for two"]#, "Office romance"] 
        }  

    director4 = {
        'DirectorName': "Alexander Gray",
        'ScoreMovies': 5,
        'Movies': ["Gentlemen good luck", "You to me, I to you", "Take care of the men!"]        
        }

    director5 = {
        'DirectorName': "Oleg Menshov",
        'ScoreMovies': 11,
        'Movies': ["Moscow does not believe in tears", "Shirley-myrly", "Chinese granny"]         
        }  
    
    myFavoriteDirectors = []
    myFavoriteDirectors.append(director1)
    myFavoriteDirectors.append(director5) 
    myFavoriteDirectors.append(director3)    

    print("Чтение файла\n");
    json.dump(myFavoriteDirectors, myfile1)
    myfile1.close()

    print("Запись файла\n");
    myfile2 = open(inputfile, mode = 'r', encoding = 'utf-8')
    json_data = json.load(myfile2)

    
    
    for user in json_data:
        print("Знаменитый советский кинорежиссёр " + str(user['DirectorName']) + " снимал " + str(user['ScoreMovies']) + " фильмов такие, как: ")
        print(str(user['Movies'][i]) + ", " + str(user['Movies'][1]) + ", " + str(user['Movies'][2]) + ".")
        print("-----------------------------------------------------------------------------------")

    #print();
    '''r = input("Записать файл или нет?\n")
    if(r == 'yes'):
        print("Запись файла\n");
        myfile1 = open(filename, mode = 'w', encoding = 'latin_1') #

        for line in myfile2:
            print(str(line.strip()).title() + "\n")
            #myfile2.write("Найден пароль: " + line + "\n")
        
        
    else:
        print("Чтение файла\n");
        myfile1 = open(filename, mode = 'r', encoding = 'latin_1') #
        json.dump(myFavoriteDirectors, myfile1)
        myfile1.close()'''



    
    #print("Записать файл или \n");
    
    #myfile2.close()    
    
    '''    director = []
    director[0] = {
        'DirectorName': "Олег Табаков",
        'ScoreMovies': 5,
        'Movies': ["Кресло", "Матросская тишина", "На всякого мудреца довольно простоты"]
        }  
    
    director[1] = {
        'DirectorName': "Марк Захаров",
        'ScoreMovies': 7,
        'Movies': ["12 стульев", "Обыкновенное чудо", "Тот самый Мюнхгаузен", "Формула любви"]
        }

    director[2] = {
        'DirectorName': "Эльдар Рязанов",
        'ScoreMovies': 27, 
        'Movies': ["Ирония судьбы, или С лёгким паром!", "Гусарская баллада", "Вокзал для двоих", "Служебный роман"] 
        }  

    director[3] = {
        'DirectorName': "Александр Серый",
        'ScoreMovies': 5,
        'Movies': ["Джентльмены удачи", "Ты — мне, я — тебе", "Берегите мужчин!"]        
        }

    director[4] = {
        'DirectorName': "Олег Меньшов",
        'ScoreMovies': 11,
        'Movies': ["Москва слезам не верит", "Ширли-мырли", "Китайская бабушка"]         
        }  
    
    myFavoriteDirectors = []
    for i in range(0, 4):
        myFavoriteDirectors.append(director[i])

    for j in range(0, 4):
        print(myFavoriteDirectors.append(director[i]))

   \d\D\w
    \W
    \s
    \S
    [0-9][3]
    [A-Z][a-z]
    '''
        
elif(x == 7):

    print(sys.argv[1:])
    print(sys.argv[1])
    print(sys.argv[2])
    print(sys.argv[3])
    
    y = len(sys.argv)

    if y > 1:
        if sys.argv[1] == "/?":
            print("Помощь в ")
            print("Помощь в ")
        print("Помощь в " + str(sys.argv[1:]))
    else:
        print("Помощь в ")

    os.system("dir > test.txt")
    #os.mkdir("my dir")   #Одноразовое 
    sys.exit()

elif(x == 8):

    #def constanta():
    mytext = "Zhenya hhhhhhhhhhhhh 1995, Kolya - 1981: rrrrrrrr@outlook.com, " \
             "rrrr@outlook.com, Thedor ssssssssss, 1987, sdsfdssdfsfghg@yandex.ru, " \
             "rrrr@yandex.com, tiiida@rambler.ru, Python Python, Sergio %24 2000," \
             "Leonid 1970, tiiida@outlook.ru, rrrr@mail.com, 56 9#$" \
             "Oleg 1973, Rita 1999, weeeeeeeee@gmail.com, eeeeeeeeeeeeeeee@yandex.com" \
             "ppppppppppppp@mail.com, ppppppppppppp@yandex.ru, tutururifd@gmail.com" \
    
    #t = int(input("Введите число для совершения операции: \n")) #print("Введите число: \n"); 
    textlookfor1 = r"yandex"
    #allresults = re.findall(textlookfor, constanta())

    allresults1 = re.findall(textlookfor1, mytext)

    #print(allresults[0:2])

    print(mytext[0:100])
    
    print("Найдено " + str(len(allresults1)) + " совпадений:\n")
    for i in range(0, len(allresults1), 1):
        print(allresults1[i])
    print("-----------------------------------------------------------------------------------")    

    t = int(input("Введите число для нахождения 'слова' из данного количества : \n"))
    textlookfor2 = r"\w{" + str(t) + "}\s"
    allresults2 = re.findall(textlookfor2, mytext)
    
    print("Найдено " + str(len(allresults2)) + " совпадений:\n")
    for i in range(0, len(allresults2), 1):
        print(allresults2[i])
    print("-----------------------------------------------------------------------------------")
    
    textlookfor3 = r"[A-Z][a-z]+"
    allresults3 = re.findall(textlookfor3, mytext)
    
    print("Найдено " + str(len(allresults3)) + " совпадений:\n")
    for i in range(0, len(allresults3), 1):
        print(allresults3[i])
    print("-----------------------------------------------------------------------------------")    
    
    textlookfor4 = r"@\w+\."
    allresults4 = re.findall(textlookfor4, mytext)
    
    print("Найдено " + str(len(allresults4)) + " совпадений:\n")
    for i in range(0, len(allresults4), 1):
        print(allresults4[i])
    print("-----------------------------------------------------------------------------------")
    
    '''t = int(input())
    if t == 100:
        print("Правильно, вы угадали число x = 100");
    else:
        print("Увы, это то не число, которое мы загадали");'''        
        
elif(x == 9):
    '''t = int(input())'''
    
    input_filename="D:/Программирование/Python/Python/ValueToEuro.txt"
    reult_filename="D:/Программирование/Python/Python/ValueToEuro1.txt"
    
    inputfile = open(input_filename, mode='r', encoding='Latin-1')
    reultfile = open(reult_filename, mode='w', encoding='Latin-1')
    mytext = inputfile.read()

    '''lookfor = r"[\w.-]+"'''

    lookfor = r"0.00+[\w.-]"

    results = re.findall(lookfor, mytext)

    for item in results:
        print(item)
        reultfile.write(item + "\n")

    print("Всего обнаружено " + str(len(lookfor)) + " совпадений.")
    
elif(x == 0):
    print("Выход из программы");
    quit();









