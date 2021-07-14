num1 = int(input('Masukkan angka pertama : '))
num2 = int(input('Masukkan angka Kedua   :'))
op = input('Masukkan Jenis Operator : ')
if op == '+':
	print(num1+num2)
elif op == '-':
	print(num1-num2)
elif op == '*':
	print(num1*num2)
elif op == '/':
	print(num1/num2)
elif op == '%':
	print(num1%num2)
else:
	print('yang anda inputkan bukan operator')