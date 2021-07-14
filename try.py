try:
	x = int(input('Masukkan sebuah angka : '))
	print(x)
except ValueError:
	print('terjadi sebuah kesalahan')
finally:
	print('try except selesai')