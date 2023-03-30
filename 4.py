import math, random
while True:
	operation = input("Введите операцию из предложенных: +, -, *, /, exp, modul, random, faktorial, arсcos: ")

	if (operation == '+'):
		a = float(input("Сложение. Введите первое число: "))
		b = float(input("Введите второе число: "))
		print(f'{a} + {b} = {a+b}')
	elif (operation == '-'):
		a = float(input("Вычитание. Введите уменьшаемое: "))
		b = float(input("Введите вычитаемое: "))
		print(f'{a} - {b} = {a-b}')
	elif (operation == '*'):
		a = float(input("Умножение. Введите первое число: "))
		b = float(input("Введите второе число: "))
		print(f'{a} * {b} = {a*b}')
	elif (operation == '/'):
		a = float(input("Деление. Введите делимое: "))
		b = float(input("Введите делитель: "))
		if b == 0:
			print("Делитель не ноль!")
		else:
			print(f'{a} / {b} = {a/b}')
	elif (operation == 'exp'):
		a = float(input("Возведение в степень. Введите число: "))
		b = float(input("Введите степень: "))
		print(f'{a}^{b} = {a**b}')
	elif (operation == 'modul'):
		a = float(input("Модуль числа. Введите число: "))
		print(f'|{a}| = {abs(a)}')	
	elif (operation == 'random'):
		print(f'Рандомное число: {random.random()}')
	elif (operation == 'faktorial'):
		a = int(input("Факториал. Введите целое число: "))
		num = 1
		for i in range(a):
			num *= i+1
		print(f'{a}! = {num}')
	elif (operation == 'arccos'):
		x = int(input("Арккосинус. Введите число: "))
		print(f'arccos({x}) = {math.acos(x)}')
	else:
		print("Команду не понял")
