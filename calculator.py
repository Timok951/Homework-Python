import math

operation = 0
number1 = 0
number2 = 0
read = ""

while True:
	try: 
		print("1-сложение\n2-вычитание\n3-умножение\n4-деление\n5-возведение в степень\n6-квадратный корень\n7-факториал\n8-синус\n9-косинус\n")
		read=input("введите номер операции ")
		operation = int(read)
		match operation:
			case 1: 
					read = input("введите первое число ")
					number1 = int(read)
					read = input("введите второе число ")
					number2 = int(read)	
					print(number1 + number2)
			case 2: 
					read = input("введите первое число ")
					number1 = int(read)
					read = input("введите второе число ")
					number2 = int(read)
					print(number1 - number2)
			case 3: 
					read = input("введите первое число ")
					number1 = int(read)
					read = input("введите второе число ")
					number2 = int(read)
					print(number1 * number2)
			case 4: 
					read = input("введите первое число ")
					number1 = int(read)
					print("введите число ")
					read = input("введите второе число ")
					number2 = int(read)
					print(number1 / number2)

			case 5: 
					read = input("введите первое число ")
					number1 = int(read)
					print("введите число ")
					read = input("введите степень ")




					num = number1
					i = 1
					while i != number2:
						number1 = number1 * num
						i = i + 1
					print (number1)
			case 6: 
					read = input("введите первое число ")
					number1 = int(read)
					print(math.sqrt(number1))

			case 7: 
					read = input("введите первое число ")
					number1 = int(read)
					print("введите число")

					print(math.factorial(number1))
			
			case 8: 
					read = input("введите первое число ")
					number1 = int(read)
					print("введите число")
					print(math.sin(number1))
			case 9: 
					read = input("введите первое число ")
					number1 = int(read)
					print(math.cos(number1))
	except:
			print("Error") 

	if (operation == 10):
		break 