from random import randint

num = randint(0, 1000)
print(num)
counter=0

x=int(input('Угадайте число от 0 до 1000. У Вас 10 попыток. Введите число: '))
while(x!=num):
    if (counter == 9):
        print('К сожалению, Ваши попытки закончились!')
        break
    elif (x<num):
        counter+=1
        print('Осталось', 10-counter,'попыток.')
        x=int(input(f'Число меньше загаданного.  Введите число: '))
    elif(x>num):
        counter+=1
        print('Осталось', 10-counter,'попыток.')
        x=int(input('Число больше загаданного. Введите число: '))
if counter !=9:
    print('Молодцы, Вы угадали')
    
   

        


