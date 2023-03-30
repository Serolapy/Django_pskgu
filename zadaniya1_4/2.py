string = input("Введите строку на русском языке: ")
flag = False #есть в строке заданный символ?
print("Строка без 3-го символа и без последнего: ", end = '')
for i in range(len(string)):
	if string[i] == 'с':
		flag = True
	if i != 2 and i != len(string) - 1: #не третий и не последний символ
		print(string[i], end = '')
print()

if flag:
	print("В строке есть символ \"с\"")
print("Длина строки", len(string))