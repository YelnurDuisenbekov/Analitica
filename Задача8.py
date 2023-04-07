a = int(input("Введите кол-во строк - "))
b = int(input("Введите кол-во столбиков - "))
c = int(input("Введите кол-во долек - "))
d = int(a*b) 

if c<d :
    if c % a ==0 or c % b == 0 :
        print ("Да")
    else :
        print ("Нет")
else :
    print ("Невожно расчитать")
