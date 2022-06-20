import pygame
import pyodbc
import pygame.examples.cursors
import pygame.examples.stars
import random
import sys
import time

print("Добро пожаловать на демонстрационно-обучающую программу по изучению языка Python:\n\n\n");
print("1. PyGame. Начало и управление Картинкой.");
print("2. PyGame. Управление Картинкой.");
print("3. PyGame. Управление Картинкой при...");
print("4. PyGame. Анимация 'Снегопад'");
print("5. Конвертирование .py в .exe");
print("6. Работа с базами данных SQL Server");
print("7. Конвертирование .py в Linux bin");
print("8. PyCharm");
print("9. Работа с Интернетом (GET, POST, Download)");
print("10. Django (Первый проект)");
print("11. Django (Создание первого сайта)");
print("12. Django (Сооздание второго сайта из HTML)\n\n\n");
print("Введите число программы (ниже), которое означает номер программы \n");
print("Если хотите выйти из программы нажмите 0\n");

##while True:

x = int(input())
if(x == 1):
    print("Добро пожаловать на программу-представления :\n\n\n");
    print("1. PyGame. Начало и управление Картинкой.");
    print("2. PyGame. Анимация 'Снегопад'");
    print("3. Конвертирование .py в .exe");
    print("4. Работа с базами данных SQL Server");
    ch = int(input("Введите первое число: "));
    if(ch == 1):
        pygame.examples.cursors.main()
    elif(ch == 2):
        pygame.examples.stars.main()    
    elif(ch == 3):
        pygame.init()
        screen = pygame.display.set_mode((640, 480))

        while True:
            pygame.display.flip()
    #else:
    #    print("\n\nСписок городов\n");
    #print("Остаток деления числа " + str(a1) + "\n");
    #exit();
    
elif(x == 2): 

    MAX_X = 1400
    MAX_Y = 1000
    game_over = False
    bg_color = (0, 20, 0)
    #print("Hello");

    pygame.init()
    screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
    pygame.display.set_caption("Моя первая игра на консоли PyGame!")

    myimage = pygame.image.load("IMG.png").convert()
    myimage = pygame.transform.scale(myimage, (100, 100))
    #print(pygame.image.get_extended())

    x = 500
    y = 500

    move_right = False
    move_left = False
    move_up = False
    move_down = False


    while game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                if event.key == pygame.K_LEFT:
                    x -= 20
                if event.key == pygame.K_RIGHT:
                    x += 20
                if event.key == pygame.K_UP:
                    y -= 20
                if event.key == pygame.K_DOWN:
                    y += 20
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                
        screen.fill(bg_color)
        screen.blit(myimage, (x, y))
        pygame.display.flip()
        
elif(x == 3):
    MAX_X = 1400
    MAX_Y = 1000
    IMG_SIZE = 100
    game_over = False
    bg_color = (0, 20, 0)
    #print("Hello");

    pygame.init()
    screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN)
    pygame.display.set_caption("Моя первая игра на консоли PyGame!")

    myimage = pygame.image.load("IMG.png").convert()
    myimage = pygame.transform.scale(myimage, (IMG_SIZE, IMG_SIZE))
    #print(pygame.image.get_extended())

    x = 500
    y = 500

    move_right = False
    move_left = False
    move_up = False
    move_down = False


    while game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                if event.key == pygame.K_LEFT:
                    move_left = True
                if event.key == pygame.K_RIGHT:
                    move_right = True
                if event.key == pygame.K_UP:
                    move_up = True
                if event.key == pygame.K_DOWN:
                    move_down = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    game_over == False
                if event.key == pygame.K_LEFT:
                    move_left = False
                if event.key == pygame.K_RIGHT:
                    move_right = False
                if event.key == pygame.K_UP:
                    move_up = False
                if event.key == pygame.K_DOWN:
                    move_down = False

            if move_left == True:
                x -= 1
                if x < 0:
                    x = 0

            if move_right == True:
                x += 1
                if x > MAX_X - IMG_SIZE:
                    x = MAX_X - IMG_SIZE

            if move_up == True:
                y += 1
                if y > MAX_Y - IMG_SIZE:
                    y = MAX_Y - IMG_SIZE

            if move_down == True:
                y -= 1
                if y < 0:
                    y = 0
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                
        screen.fill(bg_color)
        screen.blit(myimage, (x, y))
        pygame.display.flip()

elif(x == 4):
    MAX_X = 1400
    MAX_Y = 1000
    MAX_SNOW = 100
    SNOW_SIZE = 100
    #SNOW_SIZE2 = 187

    class Snow():
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.speed = random.randint(1, 3)
            self.img_num = random.randint(1, 4)
            self.image_filename = "mon" + str(self.img_num) + ".jpg"
            #self.image_filename = "snow" + str(self.img_num) + ".png"
            self.image = pygame.image.load(self.image_filename).convert_alpha()
            self.image = pygame.transform.scale(self.image, (SNOW_SIZE, SNOW_SIZE))

        def move_snow(self):
            self.y = self.y + self.speed
            if self.y > MAX_Y:
                self.y = (0 - SNOW_SIZE)
            
            i = random.randint(1, 3)
            if i == 1:
                self.x += 1
                if self.x > MAX_X:
                    self.x = (0 - SNOW_SIZE)
            elif i == 2:
                self.x -= 1
                if self.x < (0 - SNOW_SIZE):
                    self.x = MAX_X

        def draw_snow(self):
            screen.blit(self.image, (self.x, self.y))


    def initialize_snow(max_snow, snowfall):
        for i in range(0, max_snow):
            xx = random.randint(0, MAX_X)
            yy = random.randint(0, MAX_Y)
            snowfall.append(Snow(xx, yy))
    
    def check_for_exit():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                sys.exit()
    
    
    pygame.init()
    screen = pygame.display.set_mode((MAX_X, MAX_Y))#, pygame.FULLSCREEN)
    bg_color = (0, 0, 0)
    snowfall = []
    
    initialize_snow(MAX_SNOW, snowfall)

    while True:
        screen.fill(bg_color)
        check_for_exit()
        for i in snowfall:
            i.move_snow()
            i.draw_snow()
        #time.sleep(0.020)
        pygame.display.flip()
        
    
    
#elif(x == 5):
    

elif(x == 6):
   mySQLServer = "MANOWAR\SQLEXPRESS"
   myDatabase = "northwind"

   #connection = pyodbc.connect('rDriver={Microsoft Driver (*.mdb, *.accdb)};DBQ = "D:\Программирование\Python\Python\AllLessons3.py"') 

   connection = pyodbc.connect('Driver={SQL Server};'
                               'DBQ =' + mySQLServer + ';'
                               'Database =' + myDatabase + ';') 


   cursor = connection.cursor()

   #mySQLQuery = {"""
   #                 SELECT phone.phoneModel, Count(company.companyCountry) AS [Count-companyCountry]
   #                 FROM phone INNER JOIN company ON phone.phoneModel = company.companyName
   #                 GROUP BY phone.phoneModel, company.companyCountry;
   #             """}

   #cursor.excute(mySQLQuery)
   
   cursor.excute("""SELECT phone.phoneModel, Count(company.companyCountry) FROM phone INNER JOIN company ON phone.phoneModel = company.companyName
                  GROUP BY phone.phoneModel, company.companyCountry;""") 
   
   results = cursor.fetchall()

   for row in results:
       phonemodel = row[0]
       companycountry = row[1]
    
       print(" " + str(phonemodel)+ " - " + str(companycountry) + ".") 
    
   connection.close() 
        
#elif(x == 7):
    
    
#elif(x == 8):
           
        
#elif(x == 9):
    

#elif(x == 10):
#    t = int(input())
#    if t == 100:
#        print("Правильно, вы угадали число x = 100");
#    else:
#        print("Увы, это то не число, которое мы загадали");


elif(x == 0):
    print("Выход из программы");
    exit();









