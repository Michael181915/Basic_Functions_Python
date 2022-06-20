import time;
import math;

print("Добро пожаловать на демонстрационно-обучающую программу по изучению языка Python:\n\n\n");
print("1. Hello, World!");
print("2. Переменые");
print("3. Строки");
print("4. Hомера");
print("5. Циклы");
print("6. Массивы(1)");
print("7. Массивы(2)"); ##Доделать
print("8. Условные операторы if-elif-else"); ##Доделать
print("9. Словари(1)");
print("10. Словари(2)");
print("11. Ввод данных");
print("12. Функции(1)");
print("13. Функции(2)");
print("Введите число программы (ниже), которое означает номер программы \n");
print("Если хотите выйти из программы нажмите 0\n");

##while True:

x = int(input())
if(x == 1):
    print("Hello, World!");
    a1 = int(input("Введите первое число: "));
    a2 = int(input("Введите второе число: "));
    summ = a1 + a2;
    vus = a1 - a2;
    mult = a1 * a2;
    dev = a1 // a2;
    rest = a1 % a2;
    #str(a1) + "+" + str(a2) + "=" + 
    print("\n" + str(a1) + "+" + str(a2) + "=" + str(summ) + "\n");
    print(str(a1) + "-" + str(a2) + "=" + str(vus) + "\n");    
    print(str(a1) + "*" + str(a2) + "=" + str(mult) + "\n");
    print(str(a1) + ":" + str(a2) + "=" + str(dev) + "\n");
    #print(str(a1) + "+" + str(a2) + "=" + str(rest));
    print("Остаток деления числа " + str(a1) + " после деления числа " + str(a2) + " равен " + str(rest) + "\n");
    print("Выход из программы");
    exit();
    
elif(x == 2): 
    a = "Hello"
    print("Введите два числа:\n");
    a1 = int(input("Введите первое число: "));
    a2 = int(input("Введите второе число: "));
    if(a1 > a2):
        print("Число " + str(a1) + " больше, чем " + str(a2));

    elif(a1 < a2):
        print("Число " + str(a1) + " меньше, чем " + str(a2));
        
    else:
        print("Оба числа равны");
        
elif(x == 3):
    print("Введите любую строку: \n");
    mystring = str(input())
    print("Введите своё имя: \n");
    name = str(input());

    print("Ваше имя заглавными буквами: " + name.title());
    print("Ваше имя прописными буквами: " + name.lower());
    print("Ваше имя большими буквами: " + name.upper());

    print("\n\nДемонстрация использования символов после '\' (слеша)\n\n");
    print("Cписок:\n\tСтрока №1\n\tСтрока №2\n\tСтрока №3\n\t");

    print("Строк без пробела в конце:" + name.ratrip()); 

elif(x == 4):
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    num3 = int(input("Введите третье число: "))
    print("Сумма чисел равна: " + str(num1 + num2 + num3))
    print("Сумма увеличения третьего числа на 25 равна: " + str(num3 + 25));
    x1 = 6;
    x2 = 3;
    print("\nЧисла: " + str(x1*11111111111111111111) + " и " + str(x2*11111111111111111111));
    print("Сумма, разность, произведение, частное и остаток от деления равны:");
    print("\n\t" + str(x1 + x2) + "\n\t" + str(x1 - x2) + "\n\t" + str(x1 * x2) + "\n\t" + str(x1 / x2) + "\n\t" + str(x1 % x2));
    
    a = "     , duTCh .. ";
    print("");

    
        
elif(x == 5):
    print("Введите три числа для цикла:\n");
    t1 = int(input("Начало массива: "))
    t2 = int(input("Шаг массива: "))
    t3 = int(input("Конец массива: "))
    r = int(input("Вывод последовательных символов (0) или чисел (1): "))
    if(r == 0):
        ph = input("Введите строку для повтора: ")
        ph1 = input("Может быть еще одну строку? Если нет, то нажмите Enter.  ");
        print("\n\n")
        for x in range(t1, t3 + 1):
            print("\nВывод символов из цикла\n");
            print(ph);
            print(ph1);
    elif(r == 1):
        print("\nВывод чисел из цикла\n");
        for x in range(t1, t3 + 1, t2):
            print(x);

    print("\nА теперь посчитаем овец для сна (Цикл for)\n");

    o1 = int(input("Начальное число овец: "));
    o2 = int(input("Конечное число овец: "));
    print("\n\n");
    br = input("Хотите прервать цикл, если да, то ввесдите число, если нет, то нажмите 00: ");
    con = input("Хотите пропустить цикл, если нет, то нажмите 00: ");
    for x in range(o1, o2 + 1, 1):
        if(x == int(con)):
            print("Нет овечки!");
            continue;
        if(x == int(br)):
            print("--------------УСНУЛ!-------------");
            break;
        
        if (x == 1):
            print(str(x) + " овца");
        elif (x >= 2) and (x <= 4):
            print(str(x) + " овцы");    
        else:
            print(str(x) + " овец");

    ##else:
      ##  print("Введите другое число");
    print("\nА теперь посчитаем овец для сна (Цикл while)\n");
    x = o1;
    while True: 
        if (x == 1):
            print(str(x) + " овца");
        elif (x >= 2) and (x <= 4):
            print(str(x) + " овцы");    
        else:
            print(str(x) + " овец"); 
        x = x + 1;
        ##if(x == int(con)):
            ##print("Нет овечки!");
            ##continue;
        if(x == o2 + 1):
            print("--------------УСНУЛ!-------------");
            break; 
  
elif(x == 6):
    cities = ['Moscow', 'Minsk', 'kiev', 'Tbilisi', 'Erevan', 'baku', 'Perm'];

    def printcities():
        x = 0;
        while True:
            print("\t" + cities[x]);
            x = x + 1;
            if(x == len(cities)):
                break;
        print("\n\nКоличество городов: " + str(len(cities)) + "\n"); 
    
    def printcitiesCLS():
        x = 0;
        while True:
            print("\t" + cities[x].title() + "\t" + cities[x].upper() + "\t" + cities[x].lower());
            x = x + 1;
            if(x == len(cities)):
                break;
        print("\n\nКоличество городов: " + str(len(cities)) + "\n"); 
    
    def letter(numcity):
        #print("\n");
        if(numcity > 0):
            print(cities[numcity - 1]); 
        elif(numcity <= 0):
            print(cities[len(cities) + numcity - 1]);
    
    print("\n\nСписок городов\n");
    printcities();

    print("Список городов заглавными буквами, большими буквами и прописью\n");
    printcitiesCLS();

    numcity = int(input("Введите номер для определения названия города: "));
    letter(numcity);
    #print("\n");
    #if(numcity > 0):
    #    print(cities[numcity - 1]); 
    #elif(numcity <= 0):
    #    print(cities[len(cities) + numcity - 1]);



    print("\nХотите поменять город?\n")   
    numchange = int(input("Введите номер для замены названия города "));
    citychange = input("Введите название нового города: ");

    cities[numchange - 1] = citychange;
    printcities();    

    print("Вставка города в массив:\n")
    numchange1 = int(input("Введите номер для вставки города: "));
    citychange1 = input("Введите название название нового города: ");    

    cities.insert(numchange1, citychange1);
    printcities();

    print("Вставка города в последний элемент массива:\n");
    citychange2 = input("Введите название название нового города: ");
    cities.append(citychange2);
    printcities();    

    print("\nУдаление номера элемента города");
    numcity1 = int(input("Введите номер для определения названия города: "));
    
    #letter(numcity);    
    del cities[numcity1 - 1];
    printcities();

    print("\nУдаление название города");
    namecity1 = input("Введите название города: ");
        
    cities.remove(namecity1);
    printcities();

    print("\nУдаление последнего из предстваленных элементов городов");
    namecity1 = input("Введите номер для определения названия города: ");
        
    deleted_city = cities.pop()
    print("Удалённый элемент - это " + deleted_city);
    printcities();    
    
    print("\nСортировка городов");
    print("\nСортировка городов в порядке от A до Z");   
    cities.sort()
    printcities();
    
    print("\nСортировка городов в порядке от Z до A");   
    cities.sort(reverse = True)
    printcities();

    print("\nСортировка городов в порядке reverse");   
    cities.reverse()
    printcities();
        
elif(x == 7):
    cars = ['MS', 'Lada', 'KIA', 'Toyota', 'Hyundai', 'Pegeuot', 'VW', 'Chery', 'UAZ', 'Porche'];

    def printcars():
        for car in cars:
            print("\t" + car);
        print("\n\nКоличество автомобилей: " + str(len(cars)) + "\n");
    
    def printcarsCLS():
        for x in cars:
            print("\t" + x.title() + "\t" + x.upper() + "\t" + x.lower());
        print("\n\nКоличество автомобилей: " + str(len(cars)) + "\n");
    
    def letter(numcars):
        #print("\n");
        if(numcars > 0):
            print(cars[numcars - 1]); 
        elif(numcars <= 0):
            print(cars[len(cars) + numcars - 1]);
    
    print("\n\nСписок автомоблей\n");
    printcars();

    print("Список городов заглавными буквами, большими буквами и прописью\n");
    printcarsCLS();

    t1 = int(input("Начало массива: "))
    t2 = int(input("Конец массива: "))
    mynumber_list = list(range(t1,t2 + 1))
    print(mynumber_list);

    #print("\n\nПроверка числа на наличие делителей\n");
    #numb = int(input("Введите число:"));
    #divv = [1];
    #for x in range(2, numb):
    #   if(numb % x == 0):
    #       divv.append(x);
    #   else: 
    #       continue;
    #
    #print("Список делителей числа " + numb);
    #for y in divv:
    #   print(y)
    #    
    #if(len(divv) == 2):
    #   print(numb + " - это простое число");   
    #else:
    #   print(numb + " - это cоставное число");
    #
    


    mult = int(input("Введите множитель: "));    
    
    for x in mynumber_list:
       x = x * mult;
       print(x);
    
    mynumber_list.sort(reverse = True);  # reverse();
    print("\n\n");
    print(mynumber_list);

    print("\n\nСамое большое число, самое маленькое число и сумма чисел\n");
    print("Самое большое число в массиве = " + str(max(mynumber_list)));
    print("Самое маленькое число в массиве = " + str(min(mynumber_list)));
    print("Сумма чисел в массиве = " + str(sum(mynumber_list)));    

    print("\nОтсечение элементов из массива\n");
    cut1 = int(input("Начальный элемент отсечения массива: "));
    cut2 = int(input("Конец элемент отсечения массива: "));

    mycars = cars[cut1:cut2];
    print("\nРезультат отсечения элементов из массива\n");
    print(mycars);

    mycars = cars[:]
    
    
elif(x == 8):
    def printcars(cars):
        x = 0;
        while True:
            print("\t" + cars[x]);
            x = x + 1;
            if(x == len(cars)):
                break;
        print("\n\nКоличество городов: " + str(len(cars)) + "\n");

    t = int(input("Введите число: "))
    if t == 100:
        print("Правильно, вы угадали число x = 100");
    else:
        print("Увы, это то не число, которое мы загадали");

    print("\n\nТарифы ЖКХ за электричество (многопиковая зона)\n");
    print("Время подключения электричества: ");   #6:00 9:00 12:00 18:00 22:00 2:00   #6:37 7:00
    hour1 = int(input("Часы: "));                 #       3   12     12   16    20  
    #minute1 = int(input("Минуты: "));            #            2     

    print("\nВремя продолжительности электричества: ");
    dhour = int(input("Часы: "));
    #dminute = int(input("Минуты: ")); 

    #print("\nВремя продолжительности электричества: ");
    #hour2 = int(input("Часы: "));
    #minute2 = int(input("Минуты: "));
    hourif = hour1 + dhour;
    #if(hourif >= 24):
    #    hour2 = hourif - 24;
    #else:
    #    hour2 = hourif;
    
    #if (hour1 > 7) and (hour1 <= 10) and (hour1 > 17) and (hour1 <= 21):
    if (hour1 > 7) and (hour1 <= 23):
        sumZKH = dhour * 4.54;
        print("\nСтоимость коммунальных услуг составляет: " + str(sumZKH) + " рублей\n");    #4,54

    #elif (hour1 > 10) and (hour1 <= 17) and (hour1 > 21) and (hour1 <= 23):
        #sumZKH = dhour * 4.12;
        #print("\nСтоимость коммунальных услуг составляет: " + str(sumZKH) + " рублей\n");    #4,12

    else:
        sumZKH = dhour * 1.46;
        print("\nСтоимость коммунальных услуг составляет: " + str(sumZKH) + " рублей\n");    #1,46
    
    all_cars = ['MS', 'Lada', 'KIA', 'Toyota', 'Hyundai', 'Pegeuot', 'VW', 'Chery', 'UAZ', 'Porche', 'Nissan', 'Honda', 'Ford', 'Fiat', 'Lifan'];    
    asian_cars = ['KIA', 'Toyota', 'Hyundai', 'Chery', 'Nissan', 'Honda', 'Lifan'];   
    
    printcars(all_cars);   

    chcar = input("Введите марку автомобиля: ");     
    if chcar in all_cars:
        print("Да, название автомобиля " + chcar + " есть в нашем списке\n\n");
    else: 
        print("Нет, название автомобиля " + chcar + " есть в нашем списке\n\n");

    print("\nПоиск автомобильных брендов по названию страны\n");
    for chcar in all_cars:
        if chcar in asian_cars:
            print("Да, " + chcar + " - это азиатский бренд автомобилей");
        #else: 
        #    print("Нет, " + chcar + " - это не азиатский бренд автомобилей");
    
    
    
    
elif(x == 9):
     company = {
                'name':           'Останкино',     #name
                'yof_foundation': '1954',          #yof_foundation    
                'year':           2019,            #year
                'spetiality':     'мясная промышленность', #spetiality
                'production_volume(ths,tonn)': 182.5,           #production_volume(ths,tonn)
                'product_cost(mln,rubles)': 2921,            #product_cost(mln,rubles)
                'number_of_employees': 7000,            #number_of_employees              
     }

     #def printcompany():
     #   for comp in company.key() + company.values():
     #    print(comp + "\n")

     #print(company)

     print("\nОбъём произведённой продукции: " + str(company['production_volume(ths,tonn)']))
     print("\nСтоимость произведённой продукции: " + str(company['product_cost(mln,rubles)']))
     print("\nНазвание компании: " + str(company['name']))

     company['Budjet(mln,rubles)'] = 200000
     print(company)
     del company['year']
     print(company)

     productnew = int(input("\nВведите прибыль компании (production_volume(ths,tonn)): "));
     
     company['product_cost(mln,rubles)'] = productnew;
     company['spetiality'] = 'молочная промышленность'
     #if company['product_cost(mln,rubles)'] < 2000:
     #    company['number_of_employees'] = 5000
     print(company)
         
     if company['product_cost(mln,rubles)'] < 2000 + 1:
         company['number_of_employees'] = 5000
     print(company)
      
     print(company.keys())
     print(company.values())     
     
elif(x == 10):
     #t = int(input())
     company = {
                'name':           'Останкино',     #name
                'yof_foundation': '1954',          #yof_foundation    
                'year':           2019,            #year
                'spetiality':     'мясная промышленность', #spetiality
                'production_volume(ths,tonn)': 182.5,           #production_volume(ths,tonn)
                'product_cost(mln,rubles)': 2921,            #product_cost(mln,rubles)
                'number_of_employees': 7000,            #number_of_employees
                'awards': ['Орден трудового красного знамени', 'Орден Октябрьской Революции']
     }
         #print("Правильно, вы угадали число x = 100");

     all_companies = []

     for x in range(0, 10):
         all_companies.append(company)

     for comp in company.values():
         print(comp)

     for comp in all_companies:
         print(comp)

elif(x == 11):
    t = int(input())
    if t == 100:
        print("Правильно, вы угадали число x = 100");
    else:
        print("Увы, это то не число, которое мы загадали");

elif(x == 12):
    #print("\n")
    company = {
               'name':           'Останкино',     #name
               'yof_foundation': '1954',          #yof_foundation    
               'year':           2019,            #year
               'spetiality':     'мясная промышленность', #spetiality
               'production_volume(ths,tonn)': 182.5,           #production_volume(ths,tonn)
               'product_cost(mln,rubles)': 2921,            #product_cost(mln,rubles)
               'number_of_employees': 7000,            #number_of_employees
    }
    
    def printcompany():
       for comp in company:
           print(str(comp.title()) + ": " + str(company[comp]).title() + "\n")
    
    def printhello():
        print("Hello, World!")

    def printpr(prt):
        print("Hello, " + prt + "!")

    def logoriphm(a, b):
        s = math.log(b,a)
        return s

    def factorial(a1):
        answer = 1
        for i in range(1, a1 + 1):
            answer = answer * i
        return answer

    def fibbonachi(a1):
        fibb1 = fibb2 = 1
        print(fibb1, fibb2, end = " ")
        for i in range(2, a1):
            fibb1, fibb2 = fibb2, fibb1 + fibb2
            print(fibb2, end = " ")
        
    pr = input("Введите ваше имя: ");
    
    printcompany();
    print("------------------------------------");
    printhello();
    printpr(pr);
    print("------------------------------------");
    print("\nВведите два числа для вычсления логарифма по заданному основанию")
    b1 = int(input("Основание логарифма: "));
    b2 = int(input("Логарифм: "));
    x = logoriphm(b1, b2);
    print(x);
    print("------------------------------------");    
    print("\n")
    x1 = int(input("Введите число для вычисления факториала: "));
    for i in range(1, x1 + 1):
        print(str(i) + "!\t= " + str(factorial(i)))
    print("------------------------------------");    
    print("\n")
    x2 = int(input("Введите число для вычисления чисел Фибонначчи: "));
    fibbonachi(x2);
    print("\n")        
    print("------------------------------------");    
    print("\n")    
    
    

elif(x == 13):
    def create_password(site, name, telephone, e_mail, password):
        basse = {
            'site': site,
            'name': name,
            'telephone': telephone,            
            'e_mail': e_mail,
            'password': password
        }
        return basse

    def printbasse1(user):
       for bas in user:
           print(str(bas) + ": " + str(user[bas]) + "\n")

    def add_site(site, *persons):
        for person in persons:
            print("На сайте " + site + " вы можете найти имена следующих пользователей:" + person.title() + "\n")
    
    print("\n\n")
    '''
    d1 = input("Введите название сайта: ")
    d2 = input("Введите название логина: ")
    d3 = input("Введите название с: ")
    d4 = input("Введите название с: ")
    d5 = input("Введите название пароля: ")'''
    
    user0 = create_password("intuit.ru", "Mike", "+79858432204", "mike@mail.ru", "Jgd3@rdS")
    user1 = create_password("ozon.ru", "valera", "+79738432904", "valera@gmail.ru", "&hDHk57k")
    user2 = create_password("yandex.ru", "Rota", "+79858923253", "soldat@yandex.ru", "OU%gel512")
    print("\n")
    printbasse1(user0)
    printbasse1(user1)
    printbasse1(user2)
    print("------------------------------------");   
    print("\n")    
    
    add_site("intuit.ru", "andrei", "gennadiy", "leonid")
    add_site("ozon.ru", "gennadiy", "thedor")
    
    #bassegrand = dict()    
    
    #for i in bassegrand:
    #    printbasse()
    
    
    #printbasse()
    #printbasse()
    #printbasse()
    
    
    #t = int(input())
    #if t == 100:
    #    print("Правильно, вы угадали число x = 100");
    #else:
    #    print("Увы, это то не число, которое мы загадали");


    '''payments = [3541, 4275, 4404, 4463, 4358, 4310, 4427, 6836, 4366, 6426, 4774,
       5082, 5025, 6420, 4804, 6299, 4884, 6146, 5084, 6276, 5185, 5168,
       4933, 5451, 5032, 5228, 5379, 5226, 5090, 6960, 5447, 6190, 5189,
       6396, 5375, 5711, 5486, 5582, 5696, 5326, 5635, 5218, 5212, 5710,
       5726, 6933, 5463, 5657, 5742, 5199, 5325, 5217]

    print(payments[40:52])''' 

elif(x == 0):
    print("Выход из программы");
    quit();









