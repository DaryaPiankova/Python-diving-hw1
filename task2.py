x=int(input('Введите число: '))
while (x<0 and x>100000):
    x=int(input('Число должно быть неотрицательным и не больше 100000! Введите число: '))
y=1
counter=0
while y<=x:
    if(x%y == 0):
        counter+=1
    y+=1
if counter>2:
    print('Число составное')
else:
    print('Число простое')
