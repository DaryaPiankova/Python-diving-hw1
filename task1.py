a=int(input('Длина 1-ой стороны: '))
b=int(input('Длина 2-ой стороны: '))
c=int(input('Длина 3-ей стороны: '))

while a <= 0 and b <= 0 and c <= 0:
    a=int(input('Введите положительное ненулевое значение! Длина 1-ой стороны: '))
    b=int(input('Длина 2-ой стороны: '))
    c=int(input('Длина 3-ей стороны: '))

if ((a + b > c) and (a + c > b) and b + c > a):
    if a == b and b == c:
        print ('треугольник равносторонний')
    elif(a != b and a != c and b != c):
        print ('треугольник разносторонний')
    elif ((a==b and  a != c) or (a==c and a != b) or (b == c and b!= a)):
        print ('треугольник равнобедренный')
else:
    print ('Такой треугольник не существует!')